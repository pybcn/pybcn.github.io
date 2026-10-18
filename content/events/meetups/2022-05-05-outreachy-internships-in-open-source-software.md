---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 285515902.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyLadies BCN Workshop, May 2022"
date: 2022-05-05
year: 2022
venue: "Canòdrom - Ateneu d'Innovació Digital i Democràtica"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 9
meetup_url: "https://www.meetup.com/pyladies-bcn/events/285515902/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 285515902 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: outreachy-internships-in-open-source-software
    title: "Outreachy: internships in open source software"
    speakers: [lauryn-menard]
    type: talk
    language: en
    description: "Have you ever wanted to develop your Python skills beyond a personal project? Are you a non-traditional student looking to get real world experience in programming or looking to make a career transition to programming later in life? Do you like the idea of open source software, but don't know how to become involved in a project?\n\nAbout a year ago, I could answer yes to all of those questions and so I set out to find some answers.\n\nIn this talk, I'll share how I found out about Outreachy, a program that provides internships in open source and open science to people subject to systemic bias and impacted by under-representation in the technical industry where they are living.\n\nI'll share about my experience applying, being accepted and working as an intern for Zulip, a 100% open source chat program for distributed teams.\n\nFinally, we'll research together (so bring your laptop) some of the organizations and projects connected to Outreachy where you could leverage your Python skills to become an active contributor or possibly a paid intern through Outreachy."
---
