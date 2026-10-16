---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 278997154.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Build your first webpage with Django"
date: 2021-06-29
year: 2021
# The export records this event as ONLINE, so it had no room.
venue: "Online"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 30
meetup_url: "https://www.meetup.com/pyladies-bcn/events/278997154/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 278997154 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: build-your-first-webpage-with-django
    title: "Build your first webpage with Django"
    speakers: [natalia-padilla]
    type: workshop
    language: en
    description: "In this online workshop we are going to build website with Django (https://www.djangoproject.com), a Python web framework, based on the Django Girls Tutorial (https://tutorial.djangogirls.org/en/)."
    links:
      - type: site
        url: "https://www.djangoproject.com"
      - type: site
        url: "https://tutorial.djangogirls.org/en/"
---
