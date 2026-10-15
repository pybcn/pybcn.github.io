---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 243106357.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "November Dojo: Guilded Rose Kata (Cont'd)"
date: 2017-11-25
year: 2017
venue: "Punt Multimèdia Espanya Industrial"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 4
meetup_url: "https://www.meetup.com/python-barcelona/events/243106357/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 243106357 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: guilded-rose-kata-cont-d
    title: "Guilded Rose Kata (Cont'd)"
    type: workshop
    description: "Since we could not finish the analysis of the Guilded Rose Kata last month, this edition, we'll take this again. We'll start doing a quick review of what was done in last meetup, and we'll see how to continue with the Refactoring."
---
