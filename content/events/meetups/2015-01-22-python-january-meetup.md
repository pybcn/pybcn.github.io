---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 203258202.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python January Meetup"
date: 2015-01-22
year: 2015
venue: "itnig"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 63
meetup_url: "https://www.meetup.com/python-barcelona/events/203258202/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 203258202 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: an-introduction-to-sqlalchemy-and-orm-in-python
    title: "An introduction to SQLAlchemy and ORM in Python"
    speakers: [oriol-andres]
    type: talk
    duration_minutes: 20
  - id: how-to-open-a-bar-in-python
    title: "How to open a bar in Python"
    speakers: [edward-van-kuik]
    type: talk
    duration_minutes: 20
  - id: continuous-integration-on-a-large-open-source-software
    title: "Continuous Integration on a large open source software: Plone & Plone 5 is here!"
    speakers: [ramon-navarro-bosch]
    type: talk
    duration_minutes: 40
---
