---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 259895251.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Multiprocessing versus threading in a single workstation in Python 2.x"
date: 2019-03-26
year: 2019
venue: "Universitat de Barcelona"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 21
meetup_url: "https://www.meetup.com/pyladies-bcn/events/259895251/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 259895251 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: multiprocessing-versus-threading-in-a-single-workstation-in
    title: "Multiprocessing versus threading in a single workstation in Python 2.x"
    type: workshop
    language: en
    description: "In this session, we will discuss parallelization strategies. We will first cover typical computational problems that can be optimised through parallelization. Then we will cover general concepts and the important aspects to consider when designing your parallelization. In particular, we will look at parallelization in Python 2.x. and in a single machine using either processes or threads."
---
