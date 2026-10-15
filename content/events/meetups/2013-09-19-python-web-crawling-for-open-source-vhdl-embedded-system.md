---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 137913492.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python web crawling for open-source VHDL embedded system design"
date: 2013-09-19
year: 2013
# No venue: the export carries none for this event, and no other
# source gives it, so the page says nothing rather than a guess.
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 1
meetup_url: "https://www.meetup.com/python-barcelona/events/137913492/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 137913492 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: python-web-crawling-for-open-source-vhdl-embedded-system
    title: "Python web crawling for open-source VHDL embedded system design"
    type: talk
    description: "Open-source licensing of software allows people to get, modify and republish code. Opencores.org is a large (>3GB) databases of open-source VHDL code that has recently pass the 1000 project treshold offering a large number of sw tools for people interested in high-level embedded system code done in VHDL.\n\nIn this presentation I'd like to present a Python-based web crawling application that aims at taking advantage of opencores.org and offers a different kind of service for VHDL developers."
---
