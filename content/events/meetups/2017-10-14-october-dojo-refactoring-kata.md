---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 243106353.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "October Dojo: Refactoring Kata"
date: 2017-10-14
year: 2017
venue: "Punt Multimèdia Espanya Industrial"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 11
meetup_url: "https://www.meetup.com/python-barcelona/events/243106353/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 243106353 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: refactoring-kata
    title: "Refactoring Kata"
    type: workshop
    description: "We will work on a refactoring kata based on python 3.5 and pytest.\n\nBasically, this exercise will consist in:\n\n• Add tests to legacy code.\n\n• Refactor it to be clearer, with some limitations on what can be changed.\n\n• Add new features using TDD."
---
