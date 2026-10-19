---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 311516500.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Global Day of Coderetreat - November 8th!"
date: 2025-11-08
year: 2025
venue: "Codurance"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
# No attendance: yesCount is zero on this record.
meetup_url: "https://www.meetup.com/python-barcelona/events/311516500/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 311516500 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: let-s-code-the-game-of-life
    title: "Let's Code the Game of Life!"
    type: workshop
    description: "We'll be using Python to explore and implement Conway's Game of Life Kata.\n\nWhat you'll need:\n- A code editor / IDE\n- Git for version control\n- An empty project with a failing test (we'll fix that together!)"
---
