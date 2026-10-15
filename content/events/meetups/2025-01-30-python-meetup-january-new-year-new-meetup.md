---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 305663817.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup January: New Year, New Meetup."
date: 2025-01-30
year: 2025
venue: "TravelPerk"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 62
meetup_url: "https://www.meetup.com/python-barcelona/events/305663817/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 305663817 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: how-to-know-if-your-dog-is-annoying-your-neighbours-before
    title: "How to know if your dog is annoying your neighbours before they kill you - Implementing a Bark detector"
    speakers: [adrian-galera]
    type: talk
    language: en
    duration_minutes: 30
    description: "My dog has a little bit of separation anxiety, so when we leave him alone, he barks sometimes. We are training him to be home-alone, and we want to know if he barks or not when we are not home."
  - id: create-a-static-website-with-pelican
    title: "Create a static website with Pelican"
    speakers: [israel-saeta-perez]
    type: talk
    language: en
    duration_minutes: 30
    description: "Static site generators are awesome tools to build websites that are fast to develop, maintainable and easy to deploy in a secure and cheap environment. In this talk, we will learn how to create and deploy a basic static website using Pelican."
---
