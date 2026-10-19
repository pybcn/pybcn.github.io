---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 299261127.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: 'Python Meetup March: Rustacean Python Skills'
date: 2024-03-21
year: 2024
venue: Codurance
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 64
meetup_url: https://www.meetup.com/python-barcelona/events/299261127/
group: PyBCN
# The talks this meetup announced, read from the description of event 299261127 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: python-and-rust
  title: Python and Rust
  speakers:
  - dirk-ludtke
  type: talk
  language: en
  duration_minutes: 30
  description: As a passionate Python developer who has recently started to learn Rust, I would like to share my experiences how these two programming languages complement each other and how one can use both of them to optimize the own projects.
- id: hands-on-polars-an-alternative-to-data-frames-leveraging-in
  title: Hands on Polars 🐻‍❄️, an alternative to data frames leveraging in Rust
  type: talk
  language: en
  duration_minutes: 30
  description: 'Data frames are daily bread and butter in data science. Most of us use Pandas 🐼 data frames as the main tool when performing our analysis.


    In this session we are going to introduce Polars a relatively new library written in Rust that could be handy in our toolbox. We will compare its performance, put our hands on it and try to find which is the best way to replace analysis done with Pandas with Polars. All of it with a pinch of Rust.'
  speakers:
  - javier-martinez-alcantara
---
