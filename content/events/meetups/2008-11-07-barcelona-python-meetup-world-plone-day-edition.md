---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 9053205.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: Barcelona Python Meetup, World Plone Day Edition
date: 2008-11-07
year: 2008
venue: Campus Nord UPC
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 4
meetup_url: https://www.meetup.com/python-barcelona/events/9053205/
group: PyBCN
# The talks this meetup announced, read from the description of event 9053205 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: introduccio-a-plone-que-es-i-per-a-que-serveix
  title: Introducció a Plone, Què és i per a què serveix ?
  type: talk
  duration_minutes: 60
  speakers:
  - ramon-navarro-bosch
- id: plone-highlights-features-that-make-plone-a-killer
  title: Plone highlights, Features that make Plone a Killer Application
  speakers:
  - maik-roder
  type: talk
  duration_minutes: 30
- id: universitat-politecnica-de-catalunya-i-plone
  title: Universitat Politècnica de Catalunya i Plone
  type: talk
  duration_minutes: 60
---
