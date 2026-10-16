---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 222342448.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python May Meetup"
date: 2015-05-21
year: 2015
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 63
meetup_url: "https://www.meetup.com/python-barcelona/events/222342448/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 222342448 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: python-decorators
    title: "Python Decorators"
    speakers: [guillermo-blasco-jimenez]
    type: talk
    duration_minutes: 40
  - id: python-for-data-analysis
    title: "Python for Data Analysis"
    speakers: [juan-gonzales-vallinas]
    type: talk
    duration_minutes: 40
  - id: machine-learning-with-scikit-learn
    title: "Machine Learning with scikit-learn"
    speakers: [christopher-bonnett]
    type: talk
    duration_minutes: 30
---
