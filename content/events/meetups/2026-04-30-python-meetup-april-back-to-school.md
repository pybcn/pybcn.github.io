---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 314072460.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup April: back to school!"
date: 2026-04-30
year: 2026
venue: "Facultat de Matemàtiques/ Faculty of Mathematics"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 53
meetup_url: "https://www.meetup.com/python-barcelona/events/314072460/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 314072460 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: spec-driven-development-is-it-a-silver-bullet
    title: "Spec Driven Development. Is it a silver bullet?"
    speakers: [sergei-martynov]
    type: talk
    language: en
    duration_minutes: 30
    description: "I would like to talk about spec driven development in case of modern development with AI agents. What is it, how to use it and how I use it in my team on real tasks. With a live demo based on speckit."
  - id: understanding-the-anatomy-of-arrow-and-parquet
    title: "Understanding the Anatomy of Arrow and Parquet"
    speakers: [raul-cumplido]
    type: talk
    language: en
    duration_minutes: 30
    description: "Apache Arrow and Apache Parquet are the de-facto standards for in-memory and file formats for columnar data. We use them on our data workflows daily, sometimes even without noticing. This talk will demystify these formats by going over the specifications and showing some real world examples of how the data actually looks on our systems."
---
