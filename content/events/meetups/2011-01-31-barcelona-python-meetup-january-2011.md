---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 16005963.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Barcelona Python Meetup January 2011"
date: 2011-01-31
year: 2011
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 31
meetup_url: "https://www.meetup.com/python-barcelona/events/16005963/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 16005963 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: programming-efficient-sites-in-google-app-engine
    title: "Programming efficient sites in Google App Engine"
    speakers: [marc-garcia]
    type: talk
  - id: connecting-your-python-app-to-openerp-through-ooop
    title: "Connecting your Python App to OpenERP through OOOP"
    speakers: [raimon-esteve]
    type: talk
  - id: desktopcouch-blurring-the-cloud-and-the-desktop
    title: "Desktopcouch, blurring the cloud and the desktop"
    speakers: [manuel-de-la-pena]
    type: talk
  - id: the-basics-and-customization-of-the-satchmo-project-remarks
    title: "The basics and customization of the Satchmo project: Remarks and Personal Experience"
    speakers: [juan-ramon-gonzalez-vallinas]
    type: talk
---
