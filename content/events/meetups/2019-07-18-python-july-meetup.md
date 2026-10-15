---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 262963199.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python July Meetup"
date: 2019-07-18
year: 2019
venue: "Verse"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 45
meetup_url: "https://www.meetup.com/python-barcelona/events/262963199/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 262963199 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: ml-against-fraud-catching-bad-guys-with-python
    title: "ML Against Fraud: Catching Bad Guys with Python"
    speakers: [gabriel-oliveira-barra]
    type: talk
    language: en
    description: "We will show you the importance of detecting and preventing fraud before it takes place and how Machine Learning-based solutions can help with such issues. We will introduce you to the process of detection of anomalies in users' behaviour in Verse and demonstrate why Python is a great tool for achieving this."
  - id: python-on-ucontrollers
    title: "Python on uControllers"
    speakers: [juan-biondi]
    type: talk
    language: en
    description: "Python language has made programming more accessible but It was designed to run on machines with plenty of resources. Is there anything that works flawlessly on embedded systems to implement quick prototypes? Yes, that were MicroPython comes in."
---
