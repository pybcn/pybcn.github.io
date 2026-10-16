---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 229156441.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: Python March Meetup
date: 2016-03-17
year: 2016
venue: Skyscanner
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 57
meetup_url: https://www.meetup.com/python-barcelona/events/229156441/
group: PyBCN
# The talks this meetup announced, read from the description of event 229156441 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: piggybacking-trello-for-automatic-student-assessment
  title: Piggybacking Trello for automatic student assessment
  speakers:
  - jordi-saludes
  type: talk
- id: computational-complexity-in-python
  title: Computational complexity in Python
  speakers:
  - jordi-soucheiron
  type: talk
  links:
  - type: video
    url: https://www.youtube.com/watch?v=Tppi9Fsiwp4
- id: sklearn-pandas-streamline-your-model-building-process
  title: 'sklearn-pandas: streamline your model building process'
  type: talk
  links:
  - type: video
    url: https://www.youtube.com/watch?v=3V1AEXT3PrI
  speakers:
  - israel-saeta-perez
---
