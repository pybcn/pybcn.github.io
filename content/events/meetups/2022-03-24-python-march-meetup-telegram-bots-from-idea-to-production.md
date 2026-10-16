---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 284385893.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python March Meetup: Telegram bots - From idea to production"
date: 2022-03-24
year: 2022
venue: "Aticco Verdaguer - El teu coworking a Gràcia"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 69
meetup_url: "https://www.meetup.com/python-barcelona/events/284385893/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 284385893 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: telegram-bots-from-idea-to-production
    title: "Telegram bots - From idea to production"
    speakers: [ferran-jovell]
    type: talk
    language: en
    duration_minutes: 45
    description: "Creating and deploying telegram bots is easy with the Python Telegram Bot Library and Heroku! In this talk, we'll take a look at all the components and how you can quickly get up and running with your own Telegram bot."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=pOg3IbFEnlw"
---
