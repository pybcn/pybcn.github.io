---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 103676402.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: Python Web Frameworks
date: 2013-03-21
year: 2013
venue: Parc de Recerca Biomedica de Barcelona (PRBB)
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 62
meetup_url: https://www.meetup.com/python-barcelona/events/103676402/
group: PyBCN
# The talks this meetup announced, read from the description of event 103676402 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: introduction-to-django-or-rest-with-tastypie-in
  title: Introduction to Django or REST with Tastypie in
  speakers:
  - colin-kingswood
  type: talk
  duration_minutes: 15
- id: django-best-practices
  title: Django - Best practices
  speakers:
  - david-arcos
  type: talk
  duration_minutes: 15
- id: plone
  title: Plone
  type: talk
  duration_minutes: 15
  speakers:
  - ramon-navarro-bosch
- id: pyramid
  title: Pyramid
  speakers:
  - victor-fernandez-de-alba
  type: talk
  duration_minutes: 15
- id: flask
  title: Flask
  speakers:
  - areski-belaid
  type: talk
  duration_minutes: 15
- id: offline-websites-appcache-and-filesystem-api
  title: Offline websites (appcache and filesystem api)
  speakers:
  - marc-garcia
  type: talk
  duration_minutes: 15
- id: nodejs
  title: NodeJs
  speakers:
  - guillem-serra
  type: talk
  duration_minutes: 15
- id: interactive-session-brainstorming
  title: Interactive Session / brainstorming
  speakers:
  - grzegorz-swierad
  type: workshop
  duration_minutes: 15
---
