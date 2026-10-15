---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 252810319.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python July Meetup"
date: 2018-07-19
year: 2018
venue: "Travelperk"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 58
meetup_url: "https://www.meetup.com/python-barcelona/events/252810319/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 252810319 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: practical-clean-code
    title: "Practical Clean Code"
    speakers: [israel-saeta-perez]
    type: talk
    language: en
    duration_minutes: 45
    description: "Dirty, obfuscated, messy code is one of the major causes of project delays, nasty bugs, developers suffering and general mankind doom. In this talk I will introduce some simple, subjective tricks based on experience to try to make our coding lives more enjoyable."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=64gY5bXuJPY"
  - id: building-nlp-models-with-python
    title: "Building NLP Models with Python"
    speakers: [gabriel-de-maeztu]
    type: talk
    language: en
    duration_minutes: 30
    description: "NLP, Natural Language Processing is a very powerful tool to extract value from large data repository. I'll make a short introduction to NLP and multiple techniques like named entity recognition, text classification, word embeddings. The other half of the talk I'll introduce Spacy a NLP library written in Cython and build a little model with it, showing all the steps, from getting some real world data to building and testing the model."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=prWA_rqKtVo"
---
