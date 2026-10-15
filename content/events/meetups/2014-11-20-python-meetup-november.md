---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 203263722.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup November"
date: 2014-11-20
year: 2014
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 60
meetup_url: "https://www.meetup.com/python-barcelona/events/203263722/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 203263722 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: conda-cross-platform-python-agnostic-binary-package-manager
    title: "Conda - Cross-platform, Python-agnostic binary package manager"
    speakers: [christine-doig]
    type: talk
    language: en
    duration_minutes: 20
    links:
      - type: site
        url: "https://conda.pydata.org"
  - id: putting-python-inside-postgresql
    title: "Putting Python inside PostgreSQL"
    speakers: [brian-sutherland]
    type: talk
    language: en
    duration_minutes: 20
    description: "Practical guide to writing triggers and stored procedures for PostgreSQL in Python."
  - id: inside-the-artificial-neural-network
    title: "Inside the Artificial Neural Network"
    speakers: [xavier-arrufat]
    type: talk
    language: en
    duration_minutes: 40
    description: "a visual and intuitive journey to understand how it stores knowledge and how it takes decisions."
---
