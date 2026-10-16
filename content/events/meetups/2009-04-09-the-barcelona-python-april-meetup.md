---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 10025844.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "The Barcelona Python April Meetup"
date: 2009-04-09
year: 2009
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 10
meetup_url: "https://www.meetup.com/python-barcelona/events/10025844/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 10025844 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: report-from-pycon-2009-chicago
    title: "Report from Pycon 2009 Chicago"
    speakers: [maik-roder]
    type: talk
    duration_minutes: 10
  - id: csnake-a-python-wrapper-around-the-cmake-configuration-tool
    title: "CSnake, a Python wrapper around the CMake configuration tool"
    speakers: [maarten-nieber]
    type: talk
    duration_minutes: 20
  - id: wxformbuilder-a-wysiwyg-gui-design-tool-for-wxwidgets
    title: "wxFormBuilder, a WYSIWYG GUI design tool for wxWidgets"
    speakers: [maarten-nieber]
    type: talk
    duration_minutes: 10
---
