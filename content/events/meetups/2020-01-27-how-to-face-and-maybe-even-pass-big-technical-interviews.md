---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 268068121.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyLadies BCN Workshop, January 2020"
date: 2020-01-27
year: 2020
venue: "C/ de Sardenya, 229"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 20
meetup_url: "https://www.meetup.com/pyladies-bcn/events/268068121/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 268068121 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: how-to-face-and-maybe-even-pass-big-technical-interviews
    title: "How to face (and maybe even pass) big technical interviews"
    speakers: [laura-perez-mayos]
    type: workshop
    description: "In this workshop we will give tips and tricks on how to prepare technical interviews, useful resources, and a practical part with example exercises"
---
