---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 243743998.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Kiwi.com Python Meetup"
date: 2017-10-26
year: 2017
venue: "Pasaje Montoya"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 167
meetup_url: "https://www.meetup.com/python-barcelona/events/243743998/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 243743998 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: introduction-to-dronekit-creating-apps-for-uavs-with-python
    title: "Introduction to DroneKit: creating apps for UAVs with Python"
    speakers: [dimitri-herrero]
    type: talk
    description: "In this session we'll have a quick review of the evolution of open-source software in the UAV industry: ArduPilot and MAVLink. Then, we'll go through the basics of DroneKit-Python API and have a short flight simulation demo."
  - id: python-memory-management
    title: "Python Memory Management"
    speakers: [robert-kuska]
    type: talk
    description: "In this talk we are going to dive into the memory management of Python to explore its nooks and crannies. How deep does the rabbit hole go?"
  - id: secret-art-of-code-reviews
    title: "Secret art of code reviews"
    speakers: [petr-joachim]
    type: talk
    description: "In this session Petr will show you how to dig into code reviews on practical examples with explanations. How to approach them, what to look for and, finally, how to return feedback to the programmer who wrote the code? All of those questions will be covered."
---
