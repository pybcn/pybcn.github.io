---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 265681439.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Introduction to Programming with Python"
date: 2019-10-23
year: 2019
venue: "Carrer de Tànger, 122"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 26
meetup_url: "https://www.meetup.com/pyladies-bcn/events/265681439/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 265681439 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: introduction-to-programming-with-python
    title: "Introduction to Programming with Python"
    speakers: [natalia-padilla, laura-perez-mayos]
    type: workshop
    description: "In this workshop we will give an introduction to programming with Python. No previous programming knowledge is required. However, if you know how to program in another programming language, you can come and improve your skills in Python!"
---
