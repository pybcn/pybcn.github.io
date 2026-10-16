---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 266429413.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Introduction to Tackling networks in Python"
date: 2019-11-20
year: 2019
venue: "Holaluz"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 13
meetup_url: "https://www.meetup.com/pyladies-bcn/events/266429413/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 266429413 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: introduction-to-tackling-networks-in-python
    title: "Introduction to Tackling networks in Python"
    speakers: [carolina-fernandez]
    type: workshop
    description: "Wondering how to create, manage and test a virtual network in your local environment? Different Python-based solutions allow you to do so in an easy way. During the workshop we will be able to define a network and its behaviour via Python, then play with it! Come, learn and practice how to access to remote computers from wherever you are and manage this kind of networks!"
---
