---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 258333212.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: Data & interactive plots
date: 2019-01-29
year: 2019
venue: Kiwi.com
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 25
meetup_url: https://www.meetup.com/pyladies-bcn/events/258333212/
group: PyLadies BCN
# The talks this meetup announced, read from the description of event 258333212 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: data-interactive-plots
  title: Data & interactive plots
  type: workshop
  description: In this sessions we will learn and practice how to get data from different sources (files, open data, APIs, etc.), work with different data formats and plot this information into interactive plots and maps.
  speakers:
  - nuria-pujol-vilanova
---
