---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 231531664.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: Python June Meetup
date: 2016-06-16
year: 2016
venue: Skyscanner
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 62
meetup_url: https://www.meetup.com/python-barcelona/events/231531664/
group: PyBCN
# The talks this meetup announced, read from the description of event 231531664 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: machine-learning-for-dummies-with-python
  title: Machine Learning for Dummies with Python
  speakers:
  - javier-arias-losada
  type: talk
  duration_minutes: 30
  description: 6 months ago I didn't know anything about Machine Learning, I want to share some very basic ideas and concepts about Machine Learning and some tools Python provides us for this interesting technology.
- id: geodjango-use-case-mapping-farmer-fields-all-over-spain-for
  title: 'GeoDjango Use Case: Mapping Farmer Fields all over Spain for Agroptima'
  speakers:
  - domenec-castillo
  - john-powell
  type: talk
  duration_minutes: 30
  description: A true story of success using GeoDjango with several map layers servers to map millions of farmer fields all over Spain for Agroptima.
---
