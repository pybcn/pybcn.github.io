---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 265144277.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyLadies BCN Workshop, September 2019"
date: 2019-09-30
year: 2019
venue: TravelPerk
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 25
meetup_url: https://www.meetup.com/pyladies-bcn/events/265144277/
group: PyLadies BCN
# The talks this meetup announced, read from the description of event 265144277 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: introduction-to-relational-databases-with-sql-and-python
  title: Introduction to Relational Databases with SQL and Python
  type: workshop
  description: This workshop is an introduction to Relational Databases and how to manage them (create, store data, extract data, etc.) using SQL and Python. In the session we are going to learn by some examples and some hands-on exercices.
  speakers:
  - nuria-pujol-vilanova
---
