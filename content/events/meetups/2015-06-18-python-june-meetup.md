---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 223101140.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python June Meetup"
date: 2015-06-18
year: 2015
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 56
meetup_url: "https://www.meetup.com/python-barcelona/events/223101140/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 223101140 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: an-introduction-to-the-flask-web-framework-and-a-recipe-for
    title: "An introduction to the Flask Web framework and a recipe for the Google's App Engine"
    speakers: [gabriel-de-maeztu]
    type: talk
  - id: real-time-kpi-metrics-with-django-and-statsd
    title: "Real-time KPI metrics with Django and Statsd"
    speakers: [israel-saeta-perez]
    type: talk
    duration_minutes: 20
  - id: python-and-cancer-genomics
    title: "Python and Cancer Genomics"
    speakers: [loris-mularoni]
    type: talk
    duration_minutes: 20
---
