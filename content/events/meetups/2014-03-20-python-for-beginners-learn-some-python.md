---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 161424252.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python for beginners / Learn some python"
date: 2014-03-20
year: 2014
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 68
meetup_url: "https://www.meetup.com/python-barcelona/events/161424252/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 161424252 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: execution-model-and-other-must-know-s-for-python-newcomers
    title: "Execution model and other must-know's for Python newcomers"
    speakers: [pablo-enfedaque-vidal]
    type: talk
    duration_minutes: 40
  - id: the-zen-of-python
    title: "The Zen of Python"
    speakers: [david-arcos]
    type: lightning
    description: "It's simple, short and fun, and a good way to introduce the Python philosophy to beginners."
    links:
      - type: site
        url: "https://legacy.python.org/dev/peps/pep-0020/"
  - id: virtualenv-and-pip
    title: "Virtualenv and pip"
    speakers: [alex-maneu]
    type: lightning
    description: "A quick intro of setting up the virtualenv, activating it and installing/uninstalling packages. If it fits I would install two different versions of the same package in separate virtualenvs to illustrate why they are useful."
  - id: list-comprehensions
    title: "List comprehensions"
    speakers: [jordi-gomez-bao]
    type: lightning
  - id: metodos-magicos-en-python
    title: "Métodos mágicos en python"
    speakers: [nacho-gentile]
    type: lightning
    description: "Como sacar partido de los magic methods de python en un ejemplo simple."
  - id: python-2-vs-python-3
    title: "Python 2 vs. Python 3"
    speakers: [pablo-enfedaque-vidal]
    type: lightning
  - id: where-to-find-help-for-python
    title: "Where to find help for Python"
    speakers: [aleta-dunne]
    type: lightning
---
