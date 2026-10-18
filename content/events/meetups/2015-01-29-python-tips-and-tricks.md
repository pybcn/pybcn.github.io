---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 219714569.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyLadies BCN Workshop, January 2015"
date: 2015-01-29
year: 2015
venue: "UPF, Campus de la Comunicación - Poblenou"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 18
meetup_url: "https://www.meetup.com/pyladies-bcn/events/219714569/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 219714569 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: python-tips-and-tricks
    title: "Python Tips and Tricks"
    type: talk
    description: "In this session we are going to learn and practice some tips and trick to use idiomatic Python to take better advantage of Python's best features and use it in future projects."
---
