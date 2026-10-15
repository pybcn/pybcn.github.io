---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 203249502.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python December Meetup"
date: 2014-12-18
year: 2014
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 71
meetup_url: "https://www.meetup.com/python-barcelona/events/203249502/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 203249502 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: python-tips-tricks-and-dark-magic
    title: "Python tips, tricks and dark magic"
    speakers: [jordi-soucheiron]
    type: talk
  - id: buildbot-the-continuous-integration-python-framework
    title: "Buildbot: The Continuous Integration Python framework"
    speakers: [carles-san-agustin]
    type: talk
    links:
      - type: site
        url: "https://buildbot.net"
  - id: unit-test-based-programming
    title: "Unit-Test-Based Programming"
    speakers: [miguel-lechon]
    type: talk
---
