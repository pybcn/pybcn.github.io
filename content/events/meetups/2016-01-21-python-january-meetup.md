---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 228054096.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python January Meetup"
date: 2016-01-21
year: 2016
venue: "Skyscanner"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 60
meetup_url: "https://www.meetup.com/python-barcelona/events/228054096/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 228054096 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: recommender-systems-in-python
    title: "Recommender Systems in Python"
    speakers: [biel-aparicio-terrasa, david-arazo-marin]
    type: talk
  - id: a-journey-to-using-an-encryption-standard-in-python
    title: "A journey to using an encryption standard in python"
    speakers: [daniel-moreno-medina]
    type: talk
  - id: tracking-django-errors-with-rollbar
    title: "Tracking Django errors with rollbar"
    speakers: [antonio-barcia-garcia]
    type: talk
---
