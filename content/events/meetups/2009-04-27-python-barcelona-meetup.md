---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 10191149.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Barcelona Meetup"
date: 2009-04-27
year: 2009
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 12
meetup_url: "https://www.meetup.com/python-barcelona/events/10191149/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 10191149 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: argparse-python-command-line-parser
    title: "argparse: Python command line parser"
    speakers: [timo-stollenwerk]
    type: talk
  - id: python-nose-a-unittest-based-testing-framework-for-python
    title: "python-nose: A unittest-based testing framework for python that makes writing and running tests easier"
    speakers: [timo-stollenwerk]
    type: talk
  - id: wxformbuilder-a-wysiwyg-gui-design-tool-for-wxwidgets
    title: "wxFormBuilder, a WYSIWYG GUI design tool for wxWidgets"
    speakers: [maarten-nieber]
    type: talk
  - id: some-examples-of-using-ipython-an-enhanced-interactive
    title: "Some examples of using iPython, an enhanced interactive Python shell"
    speakers: [jordi-molina]
    type: talk
  - id: code-review
    title: "Code review"
    type: workshop
    description: "Bring your code and we'll discuss it"
---
