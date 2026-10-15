---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 268290923.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python February Meetup"
date: 2020-02-20
year: 2020
venue: "Holaluz"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 28
meetup_url: "https://www.meetup.com/python-barcelona/events/268290923/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 268290923 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: automatically-intercepting-debugging-all-python-http-s
    title: "Automatically intercepting & debugging all Python HTTP(S)"
    speakers: [tim-perry]
    type: talk
    language: en
    duration_minutes: 30
    description: "HTTP Toolkit is an open-source HTTP(S) debugging tool that can completely automatically capture and/or rewrite all HTTP(S) traffic from your Python code, for debugging & testing. That sounds a lot like magic. In this talk, we'll look at how it really works: how HTTP Toolkit can automatically man-in-the-middle all your requests, with no admin permissions or code changes necessary. We'll learn a bit about how HTTP interception works, see why this is useful, and then explore how HTTP Toolkit injects into the Python's own internals to make this happen."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=1R3WiyJhpQs"
      - type: site
        url: "https://httptoolkit.tech/"
  - id: migracode-creating-a-migrant-tech-community
    title: "Migracode: Creating a Migrant-Tech Community"
    speakers: [vincent-van-grondelle]
    type: talk
    language: en
    duration_minutes: 30
    description: "We are currently running Migracode: the first code school for refugees and migrants in Barcelona. Through free tech education we offer vulnerable groups to become Junior Web Developers, and we also help them connect to tech companies throughout Catalunya and Spain, and possibly throughout Europe. We would love to present our project in the Python Community and find potential partners, volunteers and other opportunities. We also have a lot to offer regarding Corporate Social Responsibility and our talk also includes this part."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=QmqrBAKSB6s"
---
