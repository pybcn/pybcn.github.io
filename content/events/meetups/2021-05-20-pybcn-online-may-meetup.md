---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 277934582.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: 'PyBCN Online: May Meetup'
date: 2021-05-20
year: 2021
# The export records this event as ONLINE, so it had no room.
venue: Online
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 67
meetup_url: https://www.meetup.com/python-barcelona/events/277934582/
group: PyBCN
# The talks this meetup announced, read from the description of event 277934582 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: adding-structure-to-a-sea-of-chaos-a-principled-approach-to
  title: 'Adding structure to a sea of chaos: a principled approach to authorization using Python + SQLAlchemy'
  speakers:
  - sam-scott
  type: talk
  language: en
  description: Authorization is an unstructured problem. Writing code to decide who can do what in your app can cover a broad set of cases. The most structure that typically gets applied to this problem area is a set of if statements and roles, but in reality, there are a lot more patterns and structure that we can apply. oso is an open source system for building authorization into applications. It's a bit like SQLAlchemy in that it provides a structured approached to authorization, much like SQLAlchemy does for data modeling and access. In this talk, we'll provide a mental model for authorization and show how to apply it using oso, Python and SQLAlchemy.
  links:
  - type: site
    url: https://www.osohq.com/
  - type: site
    url: https://docs.osohq.com/
---
