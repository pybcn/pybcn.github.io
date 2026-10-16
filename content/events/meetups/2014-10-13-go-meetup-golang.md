---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 204329322.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Go Meetup (#Golang)"
date: 2014-10-13
year: 2014
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 69
meetup_url: "https://www.meetup.com/python-barcelona/events/204329322/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 204329322 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: differences-and-common-aspects-of-go
    title: "Differences and common aspects of Go"
    speakers: [francesc-campoy]
    type: talk
    duration_minutes: 40
  - id: pythonjs-translator-to-compile-a-subset-of-python-to-go
    title: "PythonJS translator to compile a subset of Python to Go"
    speakers: [brett-hartshorn]
    type: talk
    duration_minutes: 20
---
