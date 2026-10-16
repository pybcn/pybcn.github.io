---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 259676160.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "March PyBCN Practice Sessions: Selenium for WebScraping workshop"
date: 2019-03-16
year: 2019
venue: "Punt Multimèdia La Casa del Mig"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 26
meetup_url: "https://www.meetup.com/python-barcelona/events/259676160/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 259676160 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: selenium-for-webscraping-workshop
    title: "Selenium for WebScraping workshop"
    type: workshop
    description: "Come to start the journey into web scraping using Selenium in Python. This workshop will take us into concepts like web scraping, automation, web api, html, http..."
---
