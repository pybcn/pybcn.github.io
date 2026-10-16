---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 231092415.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: Python May Meetup
date: 2016-05-19
year: 2016
venue: MediaTIC Building
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 37
meetup_url: https://www.meetup.com/python-barcelona/events/231092415/
group: PyBCN
# The talks this meetup announced, read from the description of event 231092415 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: plone-5
  title: Plone 5
  speakers:
  - eric-steele
  type: talk
  language: en
  description: In October, The Plone community released Plone 5.0. I'll give a short overview of Plone 5's features and discuss what "hackability" means to us and how we're working to bring it back to Plone.
- id: how-containers-helped-a-saas-startup-be-developed-and-go
  title: How containers helped a SaaS startup be developed and go live
  type: talk
  language: en
  description: We at Intranetum as an startup decided to push for a complex SaaS solution that can scale on a machine learning product in November 2015. At that time we had 3 months to be able to have a working first implementation that could be used in production. An architecture with more than 30 components and the need to scale fast needed to design how we were going to develop / deploy and scale. Based on DevOps ideas we decided to push for a Docker + Kubernettes + Jenkins for development/testing/staging/production autodeployment. I'm going to explain how we used this tools to achieve our objective and our conclusions for the future.
  speakers:
  - ramon-navarro-bosch
- id: pyramid-a-good-alternative-to-flask-and-django
  title: Pyramid, a good alternative to Flask and Django
  speakers:
  - nathan-van-gheem
  type: talk
  language: en
  description: Learn about the Pyramid Python web framework and what use cases it is useful with. Attendees will learn differences between Pyramid and other popular Python frameworks and what sets Pyramid apart.
---
