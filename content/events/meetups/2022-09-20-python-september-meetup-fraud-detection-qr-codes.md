---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 288431501.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: 'Python September Meetup: Fraud Detection & QR Codes'
date: 2022-09-20
year: 2022
venue: Diagonal 123
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 46
meetup_url: https://www.meetup.com/python-barcelona/events/288431501/
group: PyBCN
# The talks this meetup announced, read from the description of event 288431501 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: crunching-data-to-catch-fraud
  title: Crunching data to catch fraud
  speakers:
  - rivo-laks
  type: talk
  language: en
  duration_minutes: 30
  description: 'Veriff''s fraud team detects and blocks fraud by looking for patterns in the millions of incoming verifications.To be able to make good decisions in a fraction of a second, we need fast access to lots of data. Our automatic solutions can recognize known patterns of fraud, but we also need to manually add new rules on the fly when we recognise new attacks.

    In this talk I''ll show how we built a solution for quickly accessing that data at scale and running analytical queries on it. The result powers both our real-time decision making, as well as the tools for manually finding the patterns and blocking them.'
- id: qr-codes-let-us-make-some-gifs
  title: 'QR Codes: let us make some GIFs'
  type: talk
  language: en
  duration_minutes: 30
  description: 'QR Codes are (finally) everywhere. QR Codes were popular in Asia way before Europe, but the pandemic crisis has increased the presence of QR Codes in our daily life.

    However, QR Code can be aesthetically boring. Let us explore some cool libraries in Python to create more dynamic QR Codes, also, let us understand a bit how QR Codes work and how these fancy solutions still are compatible with smartphone QR Code readers.'
  speakers:
  - ismael-benito
---
