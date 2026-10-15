---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 248905473.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "March Dojo: Coins kata"
date: 2018-03-24
year: 2018
venue: "Punt Multimèdia Espanya Industrial"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 13
meetup_url: "https://www.meetup.com/python-barcelona/events/248905473/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 248905473 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: coins-kata
    title: "Coins kata"
    type: workshop
    description: "We will take the Coins Kata, but this time we will use pytest. During the session we will work following TDD and Pair programming, in time-boxed iterations. This kata is very good to practice TDD and see how code and tests evolve."
---
