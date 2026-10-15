---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 159792902.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Web Frameworks"
date: 2014-02-20
year: 2014
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 78
meetup_url: "https://www.meetup.com/python-barcelona/events/159792902/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 159792902 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: pyramid-python-webframework
    title: "Pyramid Python WebFramework"
    speakers: [ramon-navarro-bosch]
    type: talk
  - id: simple-webapps-with-nginx-uwsgi-emperor-bottle
    title: "Simple webapps with nginx + uWSGI emperor + Bottle"
    speakers: [jordi-soucheiron]
    type: talk
  - id: rapid-web-development-with-web2py
    title: "Rapid web development with Web2py"
    speakers: [giorgio-zoppi]
    type: talk
  - id: pybcn-org-website-powered-by-nikola
    title: "Pybcn.org website powered by Nikola"
    speakers: [areski-belaid]
    type: talk
---
