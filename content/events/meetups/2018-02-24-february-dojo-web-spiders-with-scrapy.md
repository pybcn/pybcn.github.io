---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 247703047.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "February Dojo: Web spiders with Scrapy"
date: 2018-02-24
year: 2018
venue: "Punt Multimèdia Espanya Industrial"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 19
meetup_url: "https://www.meetup.com/python-barcelona/events/247703047/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 247703047 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: web-spiders-with-scrapy
    title: "Web spiders with Scrapy"
    type: workshop
    description: "We will explain the Scrapy architecture and show an example of a simple web spider. Then, you will have a chance to write several web spiders to compare prices from different e-commerce sites. You will work in pairs and we will be by your side to help you learn."
---
