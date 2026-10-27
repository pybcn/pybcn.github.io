/* The site search, on /search/ and on the 404 page.
 *
 * Reads the query and the filters from the form and from the address the
 * page was opened with, loads the Pagefind engine the build wrote under
 * /pagefind/ (bin/search, after Hugo), and draws the first 30 results.
 * The engine downloads the index in pieces as it needs them: the
 * alphabetical chunk the typed word falls in, one fragment per result
 * drawn, never the whole index.
 *
 * Every result is drawn with textContent and never innerHTML. A talk
 * description can carry raw HTML (unsafe=true in config.toml), and the
 * excerpt Pagefind returns is parsed in an inert document so that only its
 * text and its mark elements reach the page.
 *
 * A photo caption is indexed as part of the page of its event, at the
 * figure that holds it (partials/photo_gallery.html). Pagefind records one
 * result per page, so a caption is not a result of its own, but the
 * fragment of a page records where each figure starts in its text and
 * where each matched word is. A match inside a caption is drawn here as a
 * Photo result that links to the figure; a match in the record of the day
 * is drawn as the Event result.
 *
 * The dev server (bin/serve) has no index: the import fails, the page says
 * so, and nothing is thrown.
 */
(function () {
  "use strict";

  var form = document.getElementById("search_form");
  if (!form) {
    return;
  }
  var field = form.elements.q;
  var kindSelect = form.elements.kind;
  var yearSelect = form.elements.year;
  var langSelect = form.elements.lang;
  var newest = form.elements.newest;
  var status = document.getElementById("search_status");
  var list = document.getElementById("search_results");
  var LIMIT = 30;
  var LABELS = { talk: "Talk", event: "Event", person: "Person", photo: "Photo" };
  var onNotFound = form.hasAttribute("data-path-query");
  var pagefind = null;

  function setStatus(text) {
    status.textContent = text;
  }

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) {
      node.className = className;
    }
    if (text !== undefined) {
      node.textContent = text;
    }
    return node;
  }

  /* The form from the address: a GET form does not refill itself on a
     static page. On the 404 page the words of the missing address are the
     query, less the section names and anything shorter than three
     characters, which are the numbers of a date and the noise of a slug. */
  var params = new URLSearchParams(location.search);
  if (params.has("q")) {
    field.value = params.get("q");
  } else if (onNotFound) {
    field.value = decodeURIComponent(location.pathname)
      .replace(/\.html?$/, "")
      .split(/[\/._\-+\s]+/)
      .filter(function (word) {
        return word.length > 2 && !/^(talks|events|people|meetups|index)$/.test(word);
      })
      .join(" ");
  }
  kindSelect.value = params.get("kind") || "";
  newest.checked = params.has("newest");

  function rememberAddress(term) {
    if (onNotFound) {
      return;
    }
    var next = new URLSearchParams();
    if (term) {
      next.set("q", term);
    }
    [kindSelect, yearSelect, langSelect].forEach(function (select) {
      if (select.value) {
        next.set(select.name, select.value);
      }
    });
    if (newest.checked) {
      next.set("newest", "1");
    }
    var query = next.toString();
    history.replaceState(null, "", location.pathname + (query ? "?" + query : ""));
  }

  function options() {
    var wanted = { filters: {} };
    var kind = kindSelect.value;
    if (kind === "photo") {
      wanted.filters.kind = "event";
    } else if (kind) {
      wanted.filters.kind = kind;
    }
    if (yearSelect.value) {
      wanted.filters.year = yearSelect.value;
    }
    if (langSelect.value) {
      wanted.filters.lang = langSelect.value;
    }
    if (newest.checked) {
      wanted.sort = { date: "desc" };
    }
    return wanted;
  }

  /* The year and language selectors take their values from the index, so a
     year with no page is not offered. The value the address asked for is
     kept once the options exist. */
  function fillSelect(select, values, compare) {
    var wanted = params.get(select.name) || "";
    Object.keys(values).sort(compare).forEach(function (value) {
      var option = el("option", "", value);
      option.value = value;
      select.appendChild(option);
    });
    select.value = wanted;
    if (select.value !== wanted) {
      select.value = "";
    }
  }

  /* One page, one or more results. A page with figure anchors is an event
     page with a gallery: a matched word at or after the position of a
     figure, and before the next, is inside that caption. */
  function hits(page) {
    var meta = page.meta || {};
    var figures = (page.anchors || []).filter(function (anchor) {
      return anchor.element === "figure";
    }).sort(function (a, b) {
      return a.location - b.location;
    });
    var whole = { kind: meta.kind, url: page.url, title: meta.title, meta: meta, excerpt: page.excerpt };
    if (meta.kind !== "event" || figures.length === 0) {
      return [whole];
    }
    var words = (page.content || "").split(/\s+/);
    var results = [];
    var drawn = {};
    var inRecord = false;
    (page.locations || []).forEach(function (location) {
      var index = -1;
      figures.forEach(function (figure, i) {
        if (figure.location <= location) {
          index = i;
        }
      });
      if (index < 0) {
        inRecord = true;
        return;
      }
      var figure = figures[index];
      if (drawn[figure.id]) {
        return;
      }
      drawn[figure.id] = true;
      var end = index + 1 < figures.length ? figures[index + 1].location : words.length;
      var caption = words.slice(figure.location, end).join(" ").replace(/\.\s*$/, "");
      results.push({ kind: "photo", url: page.url + "#" + figure.id, title: caption, meta: meta, excerpt: "" });
    });
    if (inRecord || results.length === 0) {
      results.unshift(whole);
    }
    return results;
  }

  /* The excerpt comes as HTML with mark elements around the matched words.
     It is parsed in an inert document and rebuilt as text nodes and marks,
     so nothing else in it can reach the page. */
  function excerptNodes(html) {
    var doc = new DOMParser().parseFromString(html, "text/html");
    var nodes = [];
    Array.prototype.forEach.call(doc.body.childNodes, function (node) {
      if (node.nodeName === "MARK") {
        nodes.push(el("mark", "", node.textContent));
      } else {
        nodes.push(document.createTextNode(node.textContent));
      }
    });
    return nodes;
  }

  function draw(hit) {
    var item = el("li", "search_result search_result_" + hit.kind);
    var title = el("p", "search_result_title");
    title.appendChild(el("span", "search_result_kind", LABELS[hit.kind] || hit.kind || "Page"));
    var link = el("a", "", hit.title || hit.url);
    link.href = hit.url;
    title.appendChild(link);
    item.appendChild(title);
    var meta = hit.meta;
    var facts = [];
    if (hit.kind === "talk") {
      if (meta.speakers) { facts.push("by " + meta.speakers); }
      if (meta.event) { facts.push(meta.event); }
      if (meta.date) { facts.push(meta.date); }
      if (meta.lang) { facts.push(meta.lang); }
    } else if (hit.kind === "event") {
      if (meta.date) { facts.push(meta.date); }
      if (meta.venue) { facts.push(meta.venue); }
    } else if (hit.kind === "photo") {
      facts.push("in the gallery of " + meta.title);
      if (meta.date) { facts.push(meta.date); }
    } else if (hit.kind === "person") {
      if (meta.roles) { facts.push(meta.roles); }
    }
    if (facts.length) {
      item.appendChild(el("p", "search_result_meta", facts.join(", ")));
    }
    if (hit.excerpt) {
      var excerpt = el("p", "search_result_excerpt");
      excerptNodes(hit.excerpt).forEach(function (node) {
        excerpt.appendChild(node);
      });
      item.appendChild(excerpt);
    }
    return item;
  }

  function show(items) {
    list.replaceChildren();
    items.forEach(function (hit) {
      list.appendChild(draw(hit));
    });
  }

  function run(now) {
    var term = field.value.trim();
    rememberAddress(term);
    if (!term) {
      show([]);
      setStatus("Type a word: a technology, a name, a venue, a year.");
      return;
    }
    var wanted = options();
    var search = now ? pagefind.search(term, wanted) : pagefind.debouncedSearch(term, wanted);
    search.then(function (found) {
      if (found === null) {
        return; /* a later keystroke replaced this search */
      }
      var pages = found.results.slice(0, LIMIT);
      return Promise.all(pages.map(function (result) {
        return result.data();
      })).then(function (data) {
        var items = [];
        data.forEach(function (page) {
          items = items.concat(hits(page));
        });
        if (kindSelect.value === "photo") {
          items = items.filter(function (hit) {
            return hit.kind === "photo";
          });
        }
        show(items);
        var total = found.results.length;
        if (total === 0) {
          setStatus("Nothing matches “" + term + "”.");
        } else if (total > LIMIT) {
          setStatus(total + " pages match “" + term + "”. The first " + LIMIT + " are shown: add a word to narrow them.");
        } else {
          setStatus(total + (total === 1 ? " page matches “" : " pages match “") + term + "”.");
        }
      });
    });
  }

  function start(engine) {
    pagefind = engine;
    return pagefind.filters().then(function (filters) {
      fillSelect(yearSelect, filters.year || {}, function (a, b) {
        return b.localeCompare(a);
      });
      fillSelect(langSelect, filters.lang || {}, function (a, b) {
        return a.localeCompare(b);
      });
      field.addEventListener("focus", function () {
        pagefind.preload(field.value);
      });
      field.addEventListener("input", function () {
        run(false);
      });
      [kindSelect, yearSelect, langSelect, newest].forEach(function (control) {
        control.addEventListener("change", function () {
          run(true);
        });
      });
      form.addEventListener("submit", function (event) {
        event.preventDefault();
        run(true);
      });
      run(true);
      if (!onNotFound) {
        field.focus();
      }
    });
  }

  import("/pagefind/pagefind.js").then(start, function () {
    setStatus("Search is not available on the dev server: the index is built after Hugo, by bin/search, and is on pybcn.org. Every talk is listed on /talks/ and every person on /people/.");
  });
})();
