---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 286415255.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyLadies BCN Workshop, June 2022"
date: 2022-06-17
year: 2022
venue: Mundimoto
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 22
meetup_url: https://www.meetup.com/pyladies-bcn/events/286415255/
group: PyLadies BCN
# The talks this meetup announced, read from the description of event 286415255 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: quantum-computing-for-everyone-with-qiskit
  title: Quantum computing for everyone with Qiskit
  type: talk
  language:
  - en
  - ca
  description: 'To the general public, quantum computing sounds like a science fiction topic or something that exists only in few laboratories around the world in a very preliminar state, far yet to be useful for society.


    But, what if I tell you that you can take a 10 years old laptop and execute a quantum computing algorithm? in this session I''ll explain you how this technology looks like and what is the current status. At the end we will play together with Qiskit, a python library made by IBM to work with quantum computers.'
  links:
  - type: site
    url: https://qiskit.org/
  speakers:
  - elisabeth-ortega-carrasco
---
