---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 60985302.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Joining the Webcat April meeting"
date: 2012-04-19
year: 2012
venue: "Un lugar de gracia"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 5
meetup_url: "https://www.meetup.com/python-barcelona/events/60985302/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 60985302 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: desarrollo-front-end-para-entornos-agile
    title: "Desarrollo front-end para entornos Agile"
    speakers: [victor-gonzalez]
    type: talk
  - id: it-s-already-the-plone-era
    title: "It's already the Plone era!"
    speakers: [ramon-navarro-bosch]
    type: talk
  - id: metodologia-de-valoracion-de-ideas-de-negocio-en-la-web
    title: "Metodologia de valoración de ideas de negocio en la web"
    speakers: [bernat-farrero]
    type: talk
  - id: web-building-blocks-privacy-principles
    title: "Web building blocks / privacy principles"
    speakers: [alina-mierlus]
    type: talk
---
