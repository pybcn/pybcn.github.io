---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 288792556.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyLadies BCN Workshop, October 2022"
date: 2022-10-05
year: 2022
venue: Canòdrom - Ateneu d'Innovació Digital i Democràtica
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 9
meetup_url: https://www.meetup.com/pyladies-bcn/events/288792556/
group: PyLadies BCN
# The talks this meetup announced, read from the description of event 288792556 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: first-steps-to-open-source-with-hacktoberfest-2022
  title: First steps to open source with Hacktoberfest 2022
  type: workshop
  language: en
  description: 'Hacktoberfest is annual event that encourages people to contribute to open source throughout october.


    In this hands-on workshop, we will learn how to contribute to open source projects within the Hacktoberfest event. Bring your own laptop and we will learn the basics of git, how to submit a pull request and how to participate to Hacktoberfest 2022.'
  speakers:
  - elisabeth-ortega-carrasco
---
