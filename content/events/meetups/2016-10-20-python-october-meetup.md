---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 234904410.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python October Meetup"
date: 2016-10-20
year: 2016
venue: "Skyscanner"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 63
meetup_url: "https://www.meetup.com/python-barcelona/events/234904410/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 234904410 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: how-to-avoid-sql-with-dataset-pandas-and-blaze
    title: "How to avoid SQL with dataset, pandas, and blaze"
    speakers: [gabriel-de-maeztu]
    type: talk
    duration_minutes: 25
    description: "For those of us that don't enjoy SQL but we are used to work with tables in pandas or blaze, dataset is a great library to work with SQL in a similar manner. A little introduction a neat tricks to avoid writing any SQL."
  - id: best-practices-for-a-python-project
    title: "Best practices for a Python project"
    speakers: [enrique-saez]
    type: talk
    duration_minutes: 20
    description: "During this talk I want to address best practices in terms of setting a new python project. I will go over how a project structure should look like, modules packages, pep8 and end up talking about testing (unit test, mock, nose, py.test) and how to distribute the project (wheels, egg, setup.py)"
  - id: tornado-an-asynchronous-web-framework-and-network-library
    title: "Tornado: An asynchronous web framework and network library"
    speakers: [jordi-soucheiron]
    type: talk
    duration_minutes: 25
    description: "Basic introduction to tornado."
---
