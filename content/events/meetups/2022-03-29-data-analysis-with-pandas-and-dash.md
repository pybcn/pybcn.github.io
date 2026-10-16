---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 284775376.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: Data Analysis with Pandas and Dash
date: 2022-03-29
year: 2022
venue: Canòdrom - Ateneu d'Innovació Digital i Democràtica
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 20
meetup_url: https://www.meetup.com/pyladies-bcn/events/284775376/
group: PyLadies BCN
# The talks this meetup announced, read from the description of event 284775376 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: data-analysis-with-pandas-and-dash
  title: Data Analysis with Pandas and Dash
  type: workshop
  language:
  - en
  - es
  description: 'This workshop is a hands-on introduction to data analysis with two libraries: Pandas and Dash. We are going to learn how to analyze and visualize real-world data in an understanding and attractive way. We will follow some examples and do hands-on exercises.'
  speakers:
  - nuria-pujol-vilanova
---
