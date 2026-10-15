---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 267705825.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "January PyBCN Practice Sessions: Dealing with legacy code"
date: 2020-01-11
year: 2020
venue: "Punt Multimèdia La Casa del Mig"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 24
meetup_url: "https://www.meetup.com/python-barcelona/events/267705825/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 267705825 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: dealing-with-legacy-code
    title: "Dealing with legacy code"
    type: workshop
    description: "In this session we'll see how to deal with legacy code, improve it and get ready to add new features with ease, using tests, coverage, golden master, ."
---
