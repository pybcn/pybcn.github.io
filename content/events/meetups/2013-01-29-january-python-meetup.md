---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 98380092.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "January Python Meetup"
date: 2013-01-29
year: 2013
venue: "Parc de Recerca Biomedica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 37
meetup_url: "https://www.meetup.com/python-barcelona/events/98380092/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 98380092 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: introducing-the-spanish-python-association
    title: "introducing the Spanish Python Association"
    speakers: [raul-cumplido]
    type: talk
  - id: tryton-a-framework-to-erp-applications
    title: "Tryton, a framework to ERP applications"
    speakers: [raimon-esteve]
    type: talk
  - id: python-packaging-the-gnu-way-with-pyconfigure
    title: "Python-packaging the GNU way with pyconfigure"
    speakers: [brandon-invergo]
    type: talk
---
