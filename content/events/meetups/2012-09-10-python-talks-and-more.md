---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 78173542.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Talks and more"
date: 2012-09-10
year: 2012
venue: "Parc de Recerca Biomedica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 21
meetup_url: "https://www.meetup.com/python-barcelona/events/78173542/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 78173542 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: report-from-froscon
    title: "Report from FrOSCon"
    speakers: [maik-roder]
    type: talk
    links:
      - type: site
        url: "https://www.froscon.de/"
  - id: tools-for-python-package-development
    title: "Tools for Python package development"
    speakers: [maik-roder]
    type: talk
  - id: reality-check-your-software-with-vagrant
    title: "Reality-check your software with Vagrant"
    speakers: [maik-roder]
    type: talk
    links:
      - type: site
        url: "https://vagrantup.com/"
---
