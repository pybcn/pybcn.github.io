---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 114969302.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python for Raspberry PI"
date: 2013-09-12
year: 2013
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 62
meetup_url: "https://www.meetup.com/python-barcelona/events/114969302/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 114969302 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: introduction-to-raspberry-pi
    title: "Introduction to Raspberry PI"
    speakers: [jordi-binefa]
    type: talk
    description: "Brief introduction: the hardware, available distributions, the community, projects, ..."
  - id: manipulating-the-raspberry-pi-gpio-pins-with-python
    title: "Manipulating the Raspberry PI GPIO pins with Python"
    speakers: [jordi-binefa]
    type: talk
    description: "Introduction to the GPIO expansion ports and the Python library RPi.GPIO with real in vivo example."
  - id: how-to-set-jass-just-another-surveillance-system-knowing
    title: "How to set JASS (Just Another Surveillance System) knowing few things of Python"
    type: talk
  - id: title
    title: "Title?"
    type: talk
  - id: cheap-video-surveillance-system-for-my-building
    title: "Cheap Video surveillance system for my building"
    speakers: [christian-perez-llamas]
    type: talk
  - id: home-energy-monitoring-system
    title: "Home energy monitoring system"
    speakers: [christian-perez-llamas]
    type: talk
---
