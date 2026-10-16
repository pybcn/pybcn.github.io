---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 226653236.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python November Meetup"
date: 2015-11-26
year: 2015
venue: "Skyscanner"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 49
meetup_url: "https://www.meetup.com/python-barcelona/events/226653236/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 226653236 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: theano-high-performance-computing-using-gpus-in-python
    title: "Theano: High performance computing using GPUs in Python"
    speakers: [amir-hossein-bakhtiary-davijani]
    type: talk
  - id: using-telegram-as-an-interface-for-an-led-wall
    title: "Using Telegram as an interface for an LED wall"
    speakers: [xavier-orduna]
    type: talk
  - id: python-descriptors-in-detail
    title: "Python descriptors in detail"
    speakers: [pablo-enfedaque-vidal]
    type: talk
---
