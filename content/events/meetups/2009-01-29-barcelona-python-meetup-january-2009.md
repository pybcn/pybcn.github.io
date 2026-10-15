---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 9520439.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Barcelona Python Meetup January 2009"
date: 2009-01-29
year: 2009
venue: "Campus Nord UPC"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 15
meetup_url: "https://www.meetup.com/python-barcelona/events/9520439/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 9520439 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: content-management-for-print-publications-with-python-and
    title: "Content management for print publications with Python and XML"
    speakers: [timo-stollenwerk]
    type: talk
    duration_minutes: 30
  - id: introduction-to-twisted
    title: "Introduction to Twisted"
    speakers: [esteve-fernandez]
    type: talk
    duration_minutes: 30
---
