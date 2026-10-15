---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 288598387.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python for technical interviews. Tips & tricks"
date: 2022-09-28
year: 2022
venue: "Happy Scribe - Servicios de transcripcion"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 14
meetup_url: "https://www.meetup.com/pyladies-bcn/events/288598387/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 288598387 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: python-for-technical-interviews-tips-tricks
    title: "Python for technical interviews. Tips & tricks"
    speakers: [laura-perez-mayos]
    type: workshop
    language: en
    description: "Do you know how a hiring process for a Python-related job looks like? Have you ever wondered how to prepare for a technical interview? Or how to best deliver the solution to a technical test?\nThis is the right Meetup for you!\n\nIn this hands-on workshop, we will first detail what can we expect when interviewing for Python-related jobs, and we'll give tips and tricks on how to prepare technical interviews. Then, we'll work on how to solve and deliver a simple technical test: structure, styling, documentation and distribution."
---
