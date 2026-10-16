---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 38412652.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Agile Collaboration Workshop"
date: 2011-11-02
year: 2011
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 18
meetup_url: "https://www.meetup.com/python-barcelona/events/38412652/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 38412652 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: agile-collaboration-workshop
    title: "Agile Collaboration Workshop"
    type: workshop
    description: "I will facilitate some games/exercises (amount will depend on time limits) through which we will work as teams and learn different collaboration patterns and anti-patterns. The idea is to get hands-on practice on some of the key agile software development practices that are meant to achieve high-performing teams. Disclaimer: There will be no programming."
---
