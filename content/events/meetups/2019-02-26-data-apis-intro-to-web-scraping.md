---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 259151878.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: Data, APIs & intro to web scraping
date: 2019-02-26
year: 2019
venue: Codely at Spaces22@ coworking, Carrer Pallars 193.
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 24
meetup_url: https://www.meetup.com/pyladies-bcn/events/259151878/
group: PyLadies BCN
# The talks this meetup announced, read from the description of event 259151878 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: data-apis-intro-to-web-scraping
  title: Data, APIs & intro to web scraping
  type: workshop
  description: In this workshop we are going to continue discovering where to obtain data to work with and help us to answer questions using Python. In previous meetup we work with files provided by open data web pages and in this occasion we are going to use APIs and learn scraping basis to get information web pages that we can't obtain otherwise.
  speakers:
  - nuria-pujol-vilanova
---
