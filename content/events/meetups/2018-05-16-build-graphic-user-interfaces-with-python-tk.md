---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 250573208.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyLadies BCN Workshop, May 2018"
date: 2018-05-16
year: 2018
venue: "Punt Multimedia"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 18
meetup_url: "https://www.meetup.com/pyladies-bcn/events/250573208/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 250573208 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: build-graphic-user-interfaces-with-python-tk
    title: "Build Graphic User Interfaces with Python Tk"
    type: workshop
    description: "Tk is a user interface toolkit that makes it easy to build desktop graphical user interfaces. Tk is cross-platform, meaning that the same code can be run on Windows, Mac OS X, or Linux. In this workshop, we are going to use Tkinter, the Tk interface for Python. You will build your first Graphic User Interface with a fews windows and some interaction between them."
---
