---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 241181460.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "July Dojo: Getting started with Flask"
date: 2017-07-08
year: 2017
venue: "Punt Multimèdia Espanya Industrial"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 17
meetup_url: "https://www.meetup.com/python-barcelona/events/241181460/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 241181460 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: getting-started-with-flask
    title: "Getting started with Flask"
    type: workshop
    description: "Flask is a great lightweight web framework ideal to build fast and reliable web services and much more. After a short introduction to microservices, API, RESTful and Flask, we will use Flask to solve some practical exercises."
---
