---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 64046582.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Barcelona Python Meetup June 2012"
date: 2012-06-11
year: 2012
venue: "Parc de Recerca Biomedica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 28
meetup_url: "https://www.meetup.com/python-barcelona/events/64046582/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 64046582 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: porting-to-python-3
    title: "Porting to Python 3"
    speakers: [lennart-regebro]
    type: talk
    duration_minutes: 40
    description: "A look at the strategies for porting to Python 3, and a quick look of the most common problems.\n\nThe status of Python 3 When should you port? Choosing a strategy for porting Preparing for the port Running 2to3 Common Problems Supporting Python 2 without 2to3 A quick look at C Extensions"
  - id: amazon-webservices
    title: "Amazon webservices"
    speakers: [zoltan-toth-czifra]
    type: talk
    duration_minutes: 40
    description: "Introduction of several services EC2 S3 CloudFront SES SQS RDS ElastiCache Price calculations for an average web project"
---
