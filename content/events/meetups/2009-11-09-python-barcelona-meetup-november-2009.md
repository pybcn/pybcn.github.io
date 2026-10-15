---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 11649508.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: Python Barcelona Meetup November 2009
date: 2009-11-09
year: 2009
venue: Parc de Recerca Biomèdica de Barcelona (PRBB)
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 8
meetup_url: https://www.meetup.com/python-barcelona/events/11649508/
group: PyBCN
# The talks this meetup announced, read from the description of event 11649508 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: introduction-to-deliverance
  title: Introduction to Deliverance
  speakers:
  - nate-aune
  type: talk
  description: Deliverance is a tool to theme HTML, applying a consistent style to applications and static files regardless of how they are implemented, and separating site-wide styling from application-level templating.
  links:
  - type: site
    url: https://deliverance.openplans.org
- id: easy-good-looking-documentation-an-introduction-to-sphinx
  title: 'Easy, good-looking documentation: an introduction to Sphinx'
  type: talk
  description: Sphinx is a tool that makes it easy to create intelligent and beautiful documentation, written by Georg Brandl and licensed under the BSD license.
  speakers:
  - carles-barrobes
---
