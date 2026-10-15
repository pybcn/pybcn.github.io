---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 117137012.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Agile development with Scrum and best practices for Python development"
date: 2013-05-29
year: 2013
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 55
meetup_url: "https://www.meetup.com/python-barcelona/events/117137012/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 117137012 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: introduction-to-agile-software-development-with-scrum
    title: "Introduction to agile software development with Scrum"
    speakers: [alex-ballarin]
    type: talk
  - id: development-work-flow-at-splendia
    title: "Development work-flow at Splendia"
    speakers: [christof-damian]
    type: talk
  - id: testing-and-continuous-integration
    title: "Testing and continuous integration"
    speakers: [thasso-griebel]
    type: talk
  - id: my-personal-python-best-practices
    title: "My personal Python Best practices"
    speakers: [pawe-piotr-przeradowski]
    type: talk
---
