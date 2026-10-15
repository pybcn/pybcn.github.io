---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 228635375.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Django 2: Views & templates"
date: 2016-03-01
year: 2016
venue: "UPF, Campus de la Comunicación - Poblenou"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 11
meetup_url: "https://www.meetup.com/pyladies-bcn/events/228635375/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 228635375 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: django-2-views-templates
    title: "Django 2: Views & templates"
    type: workshop
    description: "After learning how Django Models work, we'll learn how views and templates work."
---
