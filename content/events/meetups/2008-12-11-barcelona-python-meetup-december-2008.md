---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 9217150.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Barcelona Python Meetup December 2008"
date: 2008-12-11
year: 2008
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 21
meetup_url: "https://www.meetup.com/python-barcelona/events/9217150/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 9217150 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: biopython-doctests-and-build-automation
    title: "BioPython, DocTests and build automation"
    speakers: [giovanni-dall-olio]
    type: talk
    duration_minutes: 30
  - id: a-philosophical-view-of-programming
    title: "A philosophical view of programming"
    type: talk
    duration_minutes: 30
---
