---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 260694069.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyLadies BCN Workshop, April 2019"
date: 2019-04-25
year: 2019
venue: "Holaluz"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 25
meetup_url: "https://www.meetup.com/pyladies-bcn/events/260694069/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 260694069 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: python-nlp-introduction-to-spacy-with-jupyter-notebooks
    title: "Python & NLP. Introduction to spaCy with Jupyter notebooks"
    speakers: [laura-perez-mayos]
    type: workshop
    language: en
    description: "In this workshop we are going to discover spaCy, an Industrial-Strength Natural Language Processing library in Python. We will offer an overview of basic NLP, a (brief) introduction to Jupyter Notebooks and an introduction to spaCy through examples, followed by some hands-on exercises."
    links:
      - type: github
        url: "https://github.com/pyladies-bcn/spacy-workshop"
---
