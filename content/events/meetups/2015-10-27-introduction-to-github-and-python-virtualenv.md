---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 226180722.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: Introduction to Github and python virtualenv
date: 2015-10-27
year: 2015
venue: UPF, Campus de la Comunicación - Poblenou
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 19
meetup_url: https://www.meetup.com/pyladies-bcn/events/226180722/
group: PyLadies BCN
# The talks this meetup announced, read from the description of event 226180722 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: introductory-session-to-github
  title: Introductory session to GitHub
  speakers:
  - joana-figueira
  type: talk
  duration_minutes: 10
  description: We start this session with a 10min talk on the main features of GitHub (what it is, why and how to use it).
- id: virtualenv-if-you-don-t-love-it-is-probably-because-you-don
  title: virtualenv, if you don't love it is probably because you don't know about it
  type: workshop
  duration_minutes: 10
  description: I will introduce you in the what's, why's and how's about virtualenv.
  speakers:
  - elisabeth-ortega-carrasco
---
