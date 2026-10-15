---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 11580758.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "The Barcelona Python October Meetup - Part 2"
date: 2009-10-16
year: 2009
venue: "Vertex VS206A"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 12
meetup_url: "https://www.meetup.com/python-barcelona/events/11580758/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 11580758 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: how-to-create-web-application-very-fast-and-efficiently
    title: "How to create web application very fast and efficiently using Django."
    speakers: [juan-ramon-gonzalez-vallinas]
    type: talk
    description: "Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design"
    links:
      - type: site
        url: "https://www.djangoproject.com"
  - id: grok-1-0
    title: "Grok 1.0"
    speakers: [jan-jaap-driessen]
    type: talk
    description: "Grok is a web application framework for Python developers with an emphasis on agile development."
    links:
      - type: site
        url: "https://grok.zope.org"
---
