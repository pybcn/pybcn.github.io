---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 223493950.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python July Meetup"
date: 2015-07-16
year: 2015
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 65
meetup_url: "https://www.meetup.com/python-barcelona/events/223493950/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 223493950 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: cliquet-a-toolkit-to-build-http-microservices
    title: "Cliquet, a toolkit to build HTTP microservices"
    speakers: [mathieu-leplatre]
    type: talk
    language: en
    duration_minutes: 30
  - id: include-python-h
    title: "#include < Python.h >"
    speakers: [gustavo-chain]
    type: talk
    language: es
    duration_minutes: 30
  - id: factories-mocks-spies-and-other-tester-s-little-helpers
    title: "Factories, mocks, spies and other tester's little helpers."
    speakers: [carles-barrobes]
    type: talk
    language: en
    duration_minutes: 30
    description: "Part of the challenge of writing test suites is dealing with the dependencies of the code you are testing - both data and external code. We will take a look at some of the tools you can use, and contexts where they are appropriate."
---
