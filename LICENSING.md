# Licensing

This repository holds the source of [pybcn.org](https://pybcn.org/), the site
of the Associació Python Barcelona (PyBCN). It holds three kinds of thing, and
one licence does not fit all of them: the code of the site, the text of the
site, and material that the association publishes but does not own. This file
says which licence covers which path, and which paths no licence covers at all.

GitHub reads the licence of a repository from the `LICENSE` file alone, and a
second licence in that file stops the detection. So `LICENSE` holds the MIT
License text and nothing else, and everything else about licensing is here.

## Code: MIT License

The MIT License in [`LICENSE`](LICENSE) covers the code that builds and runs
the site:

- `layouts/`: the Hugo templates and shortcodes of the site.
- `themes/pybcn_theme/`: the theme. Its templates and partials (`layouts/`),
  its stylesheets (`assets/scss/`), the scripts written for this site
  (`assets/js/`, except `cookieconsent.min.js`, which is a third-party
  library, see below), its `archetypes/`, `theme.toml`, and `README.md`. The
  images and the vendored libraries under the theme are listed under
  [Not licensed](#not-licensed).
- `assets/xsl/`: the stylesheets that show the sitemap and the feed as a page.
- `bin/`: the build, check, and maintenance scripts.
- `.github/`: the workflows, the code owners, and the Dependabot configuration.
- `config.toml`, `data/`, `archetypes/`, and the other configuration files at
  the root (`.gitignore`, `.hugo-version`, `CNAME`).

The copyright line in `LICENSE` names the association and the contributors,
and runs from 2013, the year of the first commit. The theme began as a copy of
the `hugo-theme-bootstrap4-blog` theme, which is also under the MIT License;
its notice stays in `themes/pybcn_theme/LICENSE.txt` and covers what remains
of it.

## Content: CC BY-SA 4.0

The text of the site is licensed under the Creative Commons
Attribution-ShareAlike 4.0 International licence (CC BY-SA 4.0):

- `content/`, except `content/people/`, see [Person pages](#person-pages).
- `README.md` and `CONTRIBUTING.md`.
- `static/humans.txt`.

Deed: <https://creativecommons.org/licenses/by-sa/4.0/>

Legal code: <https://creativecommons.org/licenses/by-sa/4.0/legalcode>

Attribute the text to "Python Barcelona (PyBCN), https://pybcn.org/". The
licence requires attribution, a link to the licence, a note of any change, and
the same licence on any adaptation.

The full legal code is not copied here. Creative Commons keeps the canonical
text at the URL above and says a link to it is enough, and a copy in this
repository would be a second licence text at the root, which is what confuses
the detection described above.

## Not licensed

The paths below are published on the site but are not covered by either
licence, because the rights in them are not the association's to give. A
licence that promised more than that would tell people they may do things they
may not.

### Photographs of people

`themes/pybcn_theme/assets/images/people/` holds one photograph per person on
the site, and `themes/pybcn_theme/assets/images/photos/` holds photographs
taken at PyBCN events.

The people on this site sent their own photograph for publication on it.
Anyone who did not want one did not send one, and the site shows a silhouette
instead. The association publishes those photographs with the permission of
the people in them, given for that purpose. That permission is not a licence
for anyone else to reuse a photograph, for two reasons:

- The copyright in a photograph belongs to whoever took it. Giving PyBCN a
  copy to publish does not transfer that copyright, so PyBCN has nothing to
  sub-license.
- Consent to appear on this site is narrower than a CC BY-SA grant, which
  would let a stranger reuse and adapt the image, commercially, for ever.
  Under Spanish law (Ley Orgánica 1/1982) the right to one's own image is a
  personality right and the consent is revocable, so it cannot become a
  perpetual and irrevocable licence, which is what CC BY-SA is.

So the photographs are not licensed. They are published with the permission
of the people in them, and that permission can be withdrawn. The event
photographs are the same case: the photographer keeps the copyright, and the
people in them keep their image rights.

### Person pages

`content/people/` holds one page per person. Each person wrote their own text
and sent it for publication here, so the same reasoning applies: the
association publishes the text, it does not own it, and it cannot license it.

There is a second reason, specific to these pages. A person can ask the
association to erase their page, and the GDPR (Article 17.2) then obliges the
association to take reasonable steps to tell anyone else holding a copy that
erasure was requested. A licence that invites lawful copies of a person's
entry multiplies the copies the association would have to chase, and works
against the erasure it has to be able to deliver.

### Sponsor logos

`themes/pybcn_theme/assets/images/sponsors/` holds the logos of the sponsors.
Each logo is the trade mark of its owner, shown here to acknowledge its
support of PyBCN, with that owner's permission. A trade mark is not the
association's to license, and CC BY-SA 4.0 does not license trade marks in any
case (section 2(b)(2) of the legal code).

### The association's own marks

The PyBCN logo and its variants (`themes/pybcn_theme/assets/images/logo.png`,
`themes/pybcn_theme/assets/images/favicon.png`, `static/favicon.ico`,
`static/favicon.png`, and the files under `static/images/backgrounds/`)
identify the association. They are not covered by the content licence: use
them to refer to PyBCN, not to suggest that PyBCN endorses something it has
not seen. The PyLadies name and logo in that same folder are not the
association's.

### Third-party libraries

Each of these keeps its own licence, and the notice inside each file stays
with it:

- `themes/pybcn_theme/assets/vendor/`: jQuery 3.3.1 (MIT), jQuery Easing
  1.4.1 (BSD), Bootstrap 4.0.0 (MIT), and Font Awesome Free 5.8.2 (icons
  CC BY 4.0, fonts SIL OFL 1.1, code MIT).
- `themes/pybcn_theme/static/vendor/font-awesome/webfonts/`: the Font Awesome
  fonts (SIL OFL 1.1).
- `themes/pybcn_theme/assets/css/bootstrap.min.css`: Bootstrap 4.0.0 (MIT).
- `themes/pybcn_theme/assets/css/cookieconsent.min.css` and
  `themes/pybcn_theme/assets/js/cookieconsent.min.js`: the Cookie Consent
  library by Osano (MIT).
- `themes/pybcn_theme/assets/images/anon_member.png`: the Font Awesome `user`
  icon as a PNG (CC BY 4.0).

### Archived sites

`static/archives/` holds copies of two sites as they were published, made
with `bin/archive`: `pybcn.org/`, the previous site of the association, and
`hacktoberfestbarcelona.com/`, the site of Hacktoberfest BCN 2018. They are
kept as a record and are not maintained. Each carries its own photographs,
logos, fonts, and libraries, so nothing under `static/archives/` is licensed by
this repository.

### Code of conduct

`CODE_OF_CONDUCT.md` was adapted from the
[PyLadies code of conduct](https://www.pyladies.com/CodeOfConduct/) and is
licensed under
[CC BY-SA 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/), as
the file itself says. The ShareAlike clause of that licence requires an
adaptation to stay under CC BY-SA 3.0 or a later version of it, so that file
cannot go under the MIT License, and it is not relicensed with the rest of
the content. It keeps the notice it carries.
