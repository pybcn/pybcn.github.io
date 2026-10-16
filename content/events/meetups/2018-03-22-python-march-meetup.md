---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 248832261.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python March Meetup"
date: 2018-03-22
year: 2018
venue: "Travelperk"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 33
meetup_url: "https://www.meetup.com/python-barcelona/events/248832261/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 248832261 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: wikipedia-and-wikidata-with-python
    title: "Wikipedia and Wikidata with Python"
    speakers: [toni-hermoso]
    type: talk
    language: en
    duration_minutes: 30
    description: "In this short talk we would introduce some popular and convenient approaches for interacting with Wikipedia and Wikidata by using Python. We would learn how to query the available API and SPARQL endpoints, create simple bots and import data."
  - id: to-cli-or-not-to-cli-that-is-the-question
    title: "To CLI or not to CLI, that is the question"
    speakers: [eduardo-bellido]
    type: talk
    language: es
    duration_minutes: 40
    description: "El uso de terminal y herramientas CLI es un mundo a veces desconocido y/o temido por algunos por tener una curva de aprendizaje más pronunciada que las herramientas gráficas, GUI. En esta charla se intentará explicar las ventajas de dominar el uso del terminal y del shell para ser más productivo."
---
