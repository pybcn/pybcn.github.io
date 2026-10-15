---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 250585106.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Guillotina - asyncio based data framework with REST API and websockets"
date: 2018-05-11
year: 2018
venue: "Onna HQ"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 17
meetup_url: "https://www.meetup.com/python-barcelona/events/250585106/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 250585106 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: guillotina-asyncio-based-data-framework-with-rest-api-and
    title: "Guillotina - asyncio based data framework with REST API and websockets"
    type: talk
    description: "Learn about Guillotina, the Asyncio REST Resource API. We'll talk about the features and capabilities of Guillotina and then give a live demonstration. If you want to follow alone, have a working Python 3.6 and docker installed on your laptops."
    links:
      - type: site
        url: "https://guillotina.readthedocs.io/en/latest/"
---
