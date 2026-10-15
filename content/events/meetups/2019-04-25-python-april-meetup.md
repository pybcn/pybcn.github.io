---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 260642585.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python April Meetup"
date: 2019-04-25
year: 2019
venue: "TravelPerk"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 41
meetup_url: "https://www.meetup.com/python-barcelona/events/260642585/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 260642585 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: building-a-validation-scheme-for-a-rest-api-using-voluptuous
    title: "Building a validation scheme for a REST API using voluptuous"
    speakers: [alberto-camara]
    type: talk
    language: en
    duration_minutes: 30
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=CCxse-fiAr4"
  - id: does-django-scale-introduccion-a-la-escalabilidad
    title: "Does Django scale? Introducción a la escalabilidad"
    speakers: [david-arcos]
    type: talk
    language: es
    duration_minutes: 30
    description: "\"Vamos a repasar el concepto de escalabilidad, y cómo conseguirla en nuestra aplicación web. Pondremos de ejemplo el framework Django.\""
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=S1fZAascs04"
---
