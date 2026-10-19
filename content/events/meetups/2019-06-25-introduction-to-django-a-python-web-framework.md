---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 262411770.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyLadies BCN Workshop, June 2019"
date: 2019-06-25
year: 2019
venue: "Verse"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 29
meetup_url: "https://www.meetup.com/pyladies-bcn/events/262411770/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 262411770 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: introduction-to-django-a-python-web-framework
    title: "Introduction to Django, a python web framework"
    speakers: [natalia-padilla]
    type: workshop
    language: en
    description: "In this workshop we are going to discover Django, a framework to build websites with python. We will offer an introduction about Django based on the Django Girls Tutorial followed by some hands-on exercises."
    links:
      - type: site
        url: "https://www.djangoproject.com"
      - type: site
        url: "https://tutorial.djangogirls.org/en/"
---
