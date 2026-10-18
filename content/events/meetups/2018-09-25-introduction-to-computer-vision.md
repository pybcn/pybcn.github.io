---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 254762352.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyLadies BCN Workshop, September 2018"
date: 2018-09-25
year: 2018
venue: Kiwi.com
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 24
meetup_url: https://www.meetup.com/pyladies-bcn/events/254762352/
group: PyLadies BCN
# The talks this meetup announced, read from the description of event 254762352 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: introduction-to-computer-vision
  title: Introduction to Computer Vision
  type: workshop
  description: You will learn and experiment with computer vision Python libraries capabilities. We will see the basics of computer vision and all you need to know to work and extract information from images. We will try and learn different Python libraries and see some daily life examples.
  speakers:
  - nuria-pujol-vilanova
---
