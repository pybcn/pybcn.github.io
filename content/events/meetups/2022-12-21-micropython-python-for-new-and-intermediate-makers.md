---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 290318025.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyLadies BCN Workshop, December 2022"
date: 2022-12-21
year: 2022
venue: Canòdrom - Ateneu d'Innovació Digital i Democràtica
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 17
meetup_url: https://www.meetup.com/pyladies-bcn/events/290318025/
group: PyLadies BCN
# The talks this meetup announced, read from the description of event 290318025 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: micropython-python-for-new-and-intermediate-makers
  title: 'Micropython: Python for new and intermediate makers'
  type: workshop
  language:
  - en
  - es
  description: 'This workshop is a hands-on introduction to Micropython and electronics.


    This is the perfect opportunity learn how to use simple programmable boards for those who want to start developing their own projects without any prior knowledge of electronics or just having fun with different sensors while learning something new. Don''t miss it out!!'
  speakers:
  - nuria-pujol-vilanova
---
