---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 258198547.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "January PyBCN Practice Sessions: Concurrency workshop"
date: 2019-01-26
year: 2019
venue: "Punt Multimèdia La Casa del Mig"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 18
meetup_url: "https://www.meetup.com/python-barcelona/events/258198547/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 258198547 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: concurrency-workshop
    title: "Concurrency workshop"
    type: workshop
    description: "Come to start the journey into concurrency in Python. This workshop will take us into concepts like concurrency, parallelism, and CPU and IO bound processes. If the workshop goals are acquired in less time than expected, some more details on concurrency might be included."
---
