---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 220028399.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python February Meetup"
date: 2015-02-19
year: 2015
venue: "Parc de Recerca Biomedica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 72
meetup_url: "https://www.meetup.com/python-barcelona/events/220028399/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 220028399 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: high-performance-python
    title: "High Performance Python"
    speakers: [marc-garcia]
    type: talk
    duration_minutes: 40
  - id: zipline-a-powerful-algorithmic-trading-simulator
    title: "Zipline, a powerful algorithmic trading simulator"
    speakers: [jesus-corrius]
    type: lightning
  - id: issue-certificates-with-python-to-build-a-trust-relationship
    title: "Issue certificates with Python to build a trust relationship"
    speakers: [pau-freixes]
    type: lightning
  - id: natural-language-processing-with-python-and-nltk
    title: "Natural Language Processing with Python and NLTK"
    type: talk
    duration_minutes: 20
---
