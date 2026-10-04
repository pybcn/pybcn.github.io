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
---

This page renders the canary sponsor and the canary person through the real
sponsor and people grids, so that `bin/check-rendered` can confirm on every
build that both names reach the page as text and not as markup. All three
files are drafts: Hugo builds them only with `-D`, which the pull request
workflow passes and the deploy workflow does not, so no visitor sees them.
