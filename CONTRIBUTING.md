# Contributing to the PyBCN site

This repository holds the source of [pybcn.org](https://pybcn.org/), the site
of the Python Barcelona association, built with [Hugo](https://gohugo.io). A
change goes through a pull request against the `edition` branch, and this
guide says how. The [README](README.md) documents the site itself: the content
fields, the layouts, and what each check looks for.

## Code of conduct

The PyBCN [Code of Conduct](CODE_OF_CONDUCT.md) applies to every contribution:
a pull request, an issue, a review, and the discussion around them. It is the
same text the site publishes at
[pybcn.org/pybcn_association/coc/](https://pybcn.org/pybcn_association/coc/),
which renders that file.

## Licence

The code of the site is under the [MIT License](LICENSE) and the content is
under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
[LICENSING.md](LICENSING.md) says which paths each one covers, and which paths
are not licensed at all: the photographs of people, the person pages, the
sponsor logos, the association's own logos, the third-party libraries, and the
archived sites.

A pull request is a contribution under those terms. A change to a template, a
script, or a stylesheet is offered under the MIT License, and a change to the
text of a page is offered under CC BY-SA 4.0. Your own page under
`content/people/` and your photo are different: you keep every right in them,
and you give PyBCN permission to publish them on this site, which you can
withdraw.

## Which branch

Open the pull request against `edition`. It is the default branch and it holds
the source. `master` holds the built site: the `github-pages` workflow writes
it on every merge to `edition` and replaces its history each time, so nothing
is edited there, and a change made on `master` is lost on the next deploy.

## Add content without writing code

Most changes to this site are content: a person, a sponsor, an event. Each one
is a Markdown file with a front matter, and the README documents the fields.
Edit the file on GitHub, or clone the repository and follow the steps below.

- **A person** (an organizer, a speaker, a mentor): run
  `bin/hugo new people/my-name.md`, or copy a file under `content/people/`, and
  fill the fields listed in [Person fields](README.md#person-fields). Leave out
  any field the person does not have. The photo goes under
  `themes/pybcn_theme/assets/images/people/` and has to be square, see
  [Person photos](README.md#person-photos).
- **A sponsor**: run `bin/hugo new sponsors/my-sponsor.md` and fill the four
  fields listed in [How to add a new sponsor](README.md#how-to-add-a-new-sponsor).
  The logo goes under `themes/pybcn_theme/assets/images/sponsors/`. Then list
  the sponsor on the sponsors page, or on the event, that shows it.
- **An event**: copy the previous edition under `content/events/`, for example
  `content/events/pyday_bcn/pyday_bcn_2025.md`, and edit it. The sections, the
  agenda and the people grids are described in
  [Event page](README.md#event-page). An event lists its people and sponsors by
  their `id`, so add those files first.

`bin/check-content` reads every person, sponsor and event file. The pull
request fails when a field is empty, an `id` does not match the file name, a
declared photo is missing, or an event names a person or a sponsor that does
not exist. Run it locally, step 5 below, to see what it would say.

To report a problem with the site, open an issue and give the URL of the page.

## Make the change

Nothing is pushed to `edition` directly.

1. Clone the repository. `git clone --single-branch --branch edition` is enough
   and skips the built site, which lives on its own branch.
2. Run `bin/install`. It downloads the pinned Hugo binary into `bin/hugo` and
   verifies its checksum. You do not need Python, Go, or npm for this step.
3. Run `bin/serve` to see the site at `http://localhost:1313` while you work.
4. Make the change.
5. Run the three checks locally, so you find what the pull request would find:

   ```
   pip install pyyaml pillow
   bin/check-content
   bin/check-html-safety
   bin/hugo --minify -D -d public && bin/check-rendered
   ```

   Pillow is only needed for the black and white photo check. Without it the
   rest still runs and the check says it was skipped, so a missing Pillow
   never fails a build for the wrong reason.

6. Open the pull request against `edition`.

## What the pull request goes through

The `pr-checks` workflow runs the same checks on your branch, plus a build and
a link check. **All of them have to pass**, and one approving review is needed
before the pull request can be merged.

What each check is for:

| Check | Fails when |
|---|---|
| Build the site | Hugo cannot build, or emits a warning |
| `bin/check-content` | Front matter does not parse, a person `id` does not match its filename, an id is duplicated, a declared photo is missing, an event references a person or sponsor that does not exist, a social URL has the wrong shape, or a field is empty. It warns, without failing, about a photo that is too small or has no colour |
| `bin/check-html-safety` | Content carries raw HTML that turns a content change into script execution, a redirect, a credential prompt, or a page overlay. See [Content safety check](README.md#content-safety-check) |
| `bin/check-rendered` | The built pages carry that same markup, which catches a template that produces it even when no content file does, or they link to anything over `http`. See [Rendered page check](README.md#rendered-page-check) |
| Check the links | Reported, never blocking, because external sites rate-limit |

A merge to `edition` deploys the site. The `github-pages` workflow builds it and
publishes the result, so a change is live within a few minutes of the merge.

## Review by the web team

`.github/CODEOWNERS` lists the paths where a change reaches every page of the
site, or reaches money, or reaches the deploy: `.github/`, `bin/`,
`config.toml`, `layouts/`, `static/`, `themes/`, `CNAME`, the association
pages under `content/pybcn_association/`, `CODE_OF_CONDUCT.md`, and the
sponsor and event files under `content/sponsors/` and `content/events/`.

A pull request that touches one of those paths requests a review from
`@pybcn/web` automatically, and the branch protection on `edition` requires
it, so the pull request waits until a member of that team approves it. A
person's file under `content/people/` is not on the list on purpose: a speaker
edits their own page and needs no organizer for that, only the one approving
review every pull request needs.
