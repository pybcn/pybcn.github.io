---
title: Canary
description: "Fixture page for bin/check-rendered"
layout: event
draft: true
sponsor_levels:
  - sponsors_per_line: 4
    sponsors:
      - canary
people_sections:
  - title: Canary
    id: canary_people
    levels:
      - people_per_line: 4
        people:
          - canary
photos:
  thread: "https://x.com/PyBCN/status/1"
  items:
    - file: pyday/group_photo.jpeg
      caption: 'Canary caption "><a href="//canary.invalid/caption">canary</a><span x="'
      source: "https://x.com/PyBCN/status/1"
---

This page renders the canary sponsor and the canary person through the real
sponsor and people grids, and the canary caption through the real photo
gallery, so that `bin/check-rendered` can confirm on every build that all
three names reach the page as text and not as markup. All three files are
drafts: Hugo builds them only with `-D`, which the pull request workflow
passes and the deploy workflow does not, so no visitor sees them.

The caption is the one field of the site that reaches a template through
`safeHTML`: `partials/caption_links.html` escapes it and then makes the
mentions, the hashtags, and the URLs of the post into links. So the canary
caption carries markup and no `https://` URL. A URL in a caption becomes a
link by design, which is what the partial is for, and a canary that held one
could not tell that apart from an escape that failed. A protocol relative
address answers the same question without that: `//canary.invalid/caption`
reaches the canary host if a template ever prints the caption as markup, and
the partial leaves it alone.
