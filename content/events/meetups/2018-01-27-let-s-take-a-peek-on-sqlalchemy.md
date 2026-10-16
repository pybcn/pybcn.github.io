---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 246992032.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Let's take a peek on SQLAlchemy"
date: 2018-01-27
year: 2018
venue: "Punt Multimèdia Espanya Industrial"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 12
meetup_url: "https://www.meetup.com/python-barcelona/events/246992032/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 246992032 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: let-s-take-a-peek-on-sqlalchemy
    title: "Let's take a peek on SQLAlchemy"
    type: workshop
    language: es
    description: "In this session we will take our first steps with SQLAlchemy, highlighting most relevant features. As a summary, we will provide you with an example database on which we will create a simple command line application to add, manage, and query its records. Then, you will work on create a similar application with SQLAlchemy."
---
