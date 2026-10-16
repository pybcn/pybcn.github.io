# AGENTS.md

Guidance for AI coding agents working on pybcn.org, the website of Associació
Python Barcelona.

Read [CONTRIBUTING.md](CONTRIBUTING.md) as well. This file covers only what an
agent gets wrong that a human would not, and what this repository does
differently from a default Hugo site.

## Build and run

```sh
bin/install     # downloads the pinned Hugo binary, verifies its SHA256
bin/serve       # dev server, Hugo's default :1313
bin/build       # writes to docs/
bin/hugo --quiet -d /tmp/out     # the binary directly
```

**The Hugo binary lives at `bin/hugo` and is gitignored.** `bin/helpers` prefers
it over anything on `$PATH`, and checks the version from `.hugo-version`.

**Do not `pip install hugo`.** That PyPI package now requires a Go toolchain and
fails. `bin/install` fetches the official release binary instead.

A clean build produces **109 HTML pages**: 53 Hugo-generated and 56 copied
from `static/archives/`. Recount rather than trusting this line: the number
moves with the content. It was 317 until #202 stopped publishing the 206
person and sponsor pages that nothing linked to, which is how quickly a
figure like this goes stale.

## Traps that have already cost time

**TOML key placement.** `config.toml` ends with nested `[params.social_items...]`
tables. A key appended at the end of the file lands **inside the last table** and
silently does nothing. Put top-level keys near `theme =`, and verify by building
and checking the output, not by reading the file.

**`merge.ff = only`.** Any local merge needs `--no-ff`. A failed merge here reports
"Not possible to fast-forward", which is not a conflict.

**The archive imports run in one order and only once.** `bin/import-meetups`,
then `bin/import-talks`, then `bin/import-videos`. `bin/import-talks` replaces
the whole `talks` block of a page and everything after it in the front matter,
so running it after the others throws away what they added: a re-run over
`content/events/meetups/` deletes every video link of the talks and every
`session_videos` block, and puts the speaker credits a human resolved by hand
back in `speaker_names`. Its docstring has the detail, with the figures of the
day it was measured. Count what is at stake today with:

```sh
grep -h 'type: video' content/events/meetups/*.md | wc -l
grep -l '^session_videos:' content/events/meetups/*.md | wc -l
```

Re-run any import with `--dry-run` first, and with `--out` pointing at a copy,
never at `content/`.

**The `bin/import-*` scripts are one-time archaeology, not maintenance.** They
read an export, the pybcn-archive, that is not in this repository, so that a
published fact can be traced to a source. They ran once, in the order above,
and that is the whole of their job. Adding an event, a talk, or a video means
writing the front matter by hand, as `CONTRIBUTING.md` describes, never
re-running an importer against `content/`, which is the destructive thing the
paragraph above measures. The export is not part of maintaining this site, and
a correction to a published page goes in the page.

**`unsafe=true` in `[markup.goldmark.renderer]`.** Raw HTML in front matter
and page bodies renders unescaped. Two content files still carry it,
`content/events/pyday_bcn/pyday_bcn_2018.md` and `pyday_bcn_2019.md`, which
are pre-Hugo programmes pasted in as tables. So **assume any content field
can inject HTML**, and never add a field that reaches a template through
`safeHTML`. `bin/check-html-safety` rejects dangerous markup in content and
`bin/check-rendered` checks the built pages; both run on every pull request.

**`resources/_gen/` and `docs/` are build output and are gitignored.** They
used to be tracked, so a build dirtied the tree and a pull request carried
hundreds of regenerated files. If `git status` shows either of them, you are
on a branch from before that change.

**`master` is not a source branch.** It is the built site, force-pushed as an
orphan commit by the deploy workflow. The default branch is **`edition`**.

**Images in `static/` cannot be processed by Hugo.** They must be under `assets/`
for `resources.Get` and `.Resize` to work. This is why the site once shipped 8.97
MB of photographs on a single page.

## Rules that are not style preferences

These come from decisions with reasons behind them. Breaking them creates a
problem somebody else has to find.

**Never store a role that can be computed.** `speaker` and `host` are derived from
the talk and meetup records. Writing them into a person's front matter guarantees
they will eventually contradict the data.

**A programme is two lists, not one.** An event page carries `agenda` (the grid:
`start`, `track_length`, `room`, and either a `talk` id or its own `label` and
`type`), `talks` (the content: `title`, `speaker`, `description`, `language`,
`topic`, `duration_minutes`, `links`), and `rooms` (`id` and `name`). They are
separate because one talk can take several slots, and because a photo of the
gallery links to a talk by id, which a row of a grid cannot give it. The colour
of a block and the end of a slot are computed, not stored: see
`partials/agenda_entry.html`. **A time is always a quoted string.** YAML 1.1
reads an unquoted `9:00` as the integer 540, sexagesimal, so Hugo renders it
right and every Python checker reads a number.

**`language` takes `en`, `es` or `ca`,** or a list of them for a session given in
two. It was free text and carried seven spellings of those three languages,
which is how one page printed both `Catalan` and `Català`. **A list is written
in that order, `en`, `es`, `ca`.** The archive held `[en, es]` once and
`[es, en]` three times for the same pair, and the page printed "English /
Spanish" and "Spanish / English", because `partials/agenda_entry.html` prints
the codes in the order the list gives them. `bin/check-content` rejects any
other order.

**A person attribution requires human verification.** Talk records carry
`source` and `confidence`. **Only a human-verified record may create a person page
or link a speaker name.** A record with `confidence: medium` or `low` renders the
talk with an "unconfirmed" marker and leaves the speaker name as plain text.

This is not a style rule. Publishing an unverified claim about a named person
fails the accuracy principle of the GDPR, and the confidence field then documents
that we knew.

**Never merge two people on a first-name match.** The existing ids include bare
first names (`david`, `alberto`, `jordi`, `ricardo`) that already collide with
fuller names on the site. When in doubt, leave both and flag it.

**Do not promote hosting to a role.** Meetup's `eventHosts` field is a tool
attribute, not a title. Hosting one meetup is not being an organizer.

**RSVPs are not attendance.** `rsvps.attendedCount` is zero on 282 of the 285
events of the export, so the only figure available is who said yes on Meetup.
Render it as registrations. The figure was 205 of 207 while only the
`python-barcelona` group was read; the import reads `pyladies-bcn` as well.

**No personal data beyond what is already published.** Never render email
addresses, phone numbers, or social handles extracted from old event
descriptions, even though they are present in the source data. Never derive a
person's attributes from the event they spoke at.

**Person ids** are `firstname-surname`, kebab-case, accents stripped. A rename
carries an `aliases` entry **and** updates every reference in `content/events/` in
the same commit. Skipping the second half silently drops the person from those
pages, and that bug has been live on this site.

## Commits

**No AI attribution.** No `Co-Authored-By` trailer, no generated-with footer, no
model byline. Commits read as authored by the person who made them.

**Never use the em dash character (U+2014).** Use a comma, a colon, parentheses, or
restructure.

Write in plain, factual English. Say what changed, why, and what you verified.
**If part of the work is unfinished, say so in the commit message**, with what
blocks it. A commit that claims more than it did is worse than one that admits a
gap.

## Verify, do not assert

This repository has a history of changes that looked right and were not. The
build succeeding proves very little: a missing sponsor page, a person id that does
not match its filename, and a broken image URL all build cleanly.

So:

- Build and grep **the generated HTML**, not the templates.
- Give before and after numbers for anything you claim to have fixed.
- When you cannot verify something without a browser or a screen reader, **say
  that** rather than asserting it works.

Two checkers exist and both are cheap to run:

```sh
bin/check-content       # front matter, ids, cross-references (needs pyyaml)
bin/check-html-safety   # dangerous raw HTML in content
```

## Things you cannot do

**Do not push, open pull requests, or comment on GitHub.** Leave your work as a
local branch. Opening it is a human decision, taken per item.

**Do not change DNS, repository settings, or anything outside the working tree.**

**Do not install software.** If a task genuinely needs a tool that is absent, say
so and stop, rather than working around it with something that produces a
plausible but different result.

## Where things are

| Path | What |
|---|---|
| `content/people/` | One markdown file per person, keyed by `id` |
| `content/events/` | PyDay BCN, PyDataBCN, and other events, with their agendas in front matter |
| `content/sponsors/` | One file per sponsor |
| `themes/pybcn_theme/` | The theme, **vendored in-tree**, not a submodule |
| `themes/pybcn_theme/layouts/partials/` | Most of the interesting template logic |
| `static/archives/` | Verbatim mirrors of pre-Hugo sites, copied unprocessed |
| `data/` | Tables the templates read: `roles.yaml` maps a heading to a role, `role_emoji.yaml` a role to a glyph |
| `bin/` | Setup and build scripts, the checks, `bin/list-channel` (names a channel video the inventory lacks; needs `yt-dlp` and the network), the one-time `bin/import-*` scripts, plus the gitignored Hugo binary |
| `.hugo-version` | The pinned Hugo version, single source of truth |

The checks, which are what a pull request has to pass:

| Script | What it rejects |
|---|---|
| `bin/check-content` | A broken reference, a photo that is not square, a source far larger than the build asks for, a field that no longer exists, an `end_date` that is not a date or not later than `date` |
| `bin/check-html-safety` | Dangerous raw HTML in content, with an allowlist for the legitimate embeds |
| `bin/check-rendered` | The same, on the built pages, plus any `http://` URL. Run it against a directory you built, never against `public/` while a dev server is writing there |

The join between a person and an event is `where $pages ".Params.id" "eq" $person`
in `partials/people-grid.html`. That pattern is how everything cross-references,
and it fails silently when an id does not match.
