---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 237576580.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python February Meetup"
date: 2017-02-16
year: 2017
venue: "Travelperk"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 50
meetup_url: "https://www.meetup.com/python-barcelona/events/237576580/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 237576580 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: python-cryptography-101
    title: "Python Cryptography 101"
    speakers: [giorgio-zoppi]
    type: talk
    language: en
    duration_minutes: 15
    description: "This 15 minutes talk will give you hints and overview on about applying cryptography in your projects"
  - id: modern-web-development-with-graphql
    title: "Modern web development with GraphQL"
    speakers: [israel-saeta-perez]
    type: talk
    language: en
    duration_minutes: 45
    description: "GraphQL is a query language for APIs developed by Facebook that overcomes many limitations of REST to make web app development more flexible and powerful. In this talk we will introduce its main features and show how to create an example GraphQL app with Graphene and Django."
---
