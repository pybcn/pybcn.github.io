---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 249381363.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyLadies BCN Workshop, April 2018"
date: 2018-04-10
year: 2018
venue: "espai30"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 19
meetup_url: "https://www.meetup.com/pyladies-bcn/events/249381363/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 249381363 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: very-first-hands-on-arduino-and-its-connection-to-python
    title: "Very first hands on Arduino and its connection to Python through PySerial"
    type: workshop
    description: "The number of libraries available for Python is so big that anyone can't guess how many things one can do using our lovely programming language without typing \"How to do that fancy thing with Python\". In this workshop we will show you one of these \"fancy things\": the interaction between Python and Arduino through PySerial library. The number of applications of such interaction is only limited by our creativity! In this workshop we will focus in the use of RGB LEDs, changing its color and its shine using Python code."
---
