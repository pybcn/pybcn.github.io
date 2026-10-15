---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 222132038.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Testing & Test-driven development (TDD) in Python"
date: 2015-05-14
year: 2015
venue: "UPF, Campus de la Comunicación - Poblenou"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 15
meetup_url: "https://www.meetup.com/pyladies-bcn/events/222132038/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 222132038 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: testing-test-driven-development-tdd-in-python
    title: "Testing & Test-driven development (TDD) in Python"
    type: workshop
    description: "This session is an Introductory session about testing focused on unit testing (unittest and pytest)."
---
