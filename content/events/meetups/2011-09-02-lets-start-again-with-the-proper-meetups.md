---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 27222151.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Lets start again with the proper meetups!"
date: 2011-09-02
year: 2011
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 22
meetup_url: "https://www.meetup.com/python-barcelona/events/27222151/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 27222151 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: launching-a-webstore-with-django-and-satchmo-a-personal
    title: "Launching a webstore with Django and Satchmo: A personal experience"
    speakers: [juan-ramon-gonzalez-vallinas]
    type: talk
  - id: wok-title-pending
    title: "Wok (Title pending)"
    speakers: [christian-perez-llamas]
    type: talk
  - id: viri-and-python-3-title-pending
    title: "Viri and Python 3 (Title pending)"
    speakers: [marc-garcia]
    type: talk
---
