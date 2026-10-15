---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 293018629.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python April Meetup: Python Packaging 101"
date: 2023-04-27
year: 2023
venue: "Ironhack Barcelona Tech bootcamps"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 57
meetup_url: "https://www.meetup.com/python-barcelona/events/293018629/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 293018629 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: python-packaging-101
    title: "Python packaging 101"
    speakers: [ferran-jovell]
    type: talk
    language: en
    duration_minutes: 45
    description: "Have you ever wondered how does the pip install? Would you like to know how to create your very own python package? This talk will go through on all the necessary steps to get started on creating python packages and uploading them to the Python Packaging Index (PyPI)."
---
