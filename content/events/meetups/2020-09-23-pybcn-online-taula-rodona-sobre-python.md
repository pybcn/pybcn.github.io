---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 273389765.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyBCN Online: Taula Rodona sobre Python"
date: 2020-09-23
year: 2020
# The export records this event as ONLINE, so it had no room.
venue: "Online"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 48
meetup_url: "https://www.meetup.com/python-barcelona/events/273389765/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 273389765 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: taula-rodona-sobre-python-python-round-table
    title: "Taula Rodona sobre Python (Python Round Table)"
    speakers: [ruben-berenguel, alberto-camara, david-arcos, julio-martinez]
    type: panel
    language: ca
    description: "We kickstart the new season of PyBCN with a virtual round table where we will talk about Python, the pandemic situation and its impact on the developer labour market and remote events."
---
