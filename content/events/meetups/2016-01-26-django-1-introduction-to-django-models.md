---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 228207730.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Django 1: Introduction to Django Models"
date: 2016-01-26
year: 2016
venue: "UPF, Campus de la Comunicación - Poblenou"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 6
meetup_url: "https://www.meetup.com/pyladies-bcn/events/228207730/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 228207730 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: django-1-introduction-to-django-models
    title: "Django 1: Introduction to Django Models"
    type: workshop
    description: "We are going to learn about models. A model is where all the information is stored. We are going to learn how to use them for our profit to build any application. How to organize it and how to retrieve it after."
---
