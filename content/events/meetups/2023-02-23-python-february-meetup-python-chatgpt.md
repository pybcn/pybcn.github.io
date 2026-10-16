---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 291610950.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: 'Python February Meetup: Python & ChatGPT'
date: 2023-02-23
year: 2023
venue: C/ dels Almogàvers, 160
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 56
meetup_url: https://www.meetup.com/python-barcelona/events/291610950/
group: PyBCN
# The talks this meetup announced, read from the description of event 291610950 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: python-and-chatgpt-chuckles-i-m-in-danger
  title: 'Python and ChatGPT: (chuckles) I''m in danger'
  type: talk
  language: en
  duration_minutes: 45
  description: Have you talked to the new kid in the building? I have, and a lot. Let me show you the capabilities of ChatGPT, and its limitations. Let us explore how to use it in a daily basis to enhance our Python programming experience from dummy scripts to create bots, to professional work using ChatGPT as your peer-programming colleague.
  speakers:
  - ismael-benito
---
