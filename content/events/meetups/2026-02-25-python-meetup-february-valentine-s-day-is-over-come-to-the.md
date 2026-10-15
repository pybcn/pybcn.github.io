---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 313395411.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup February: Valentine's day is over, come to the meetup."
date: 2026-02-25
year: 2026
venue: "bsport Tasso office"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 51
meetup_url: "https://www.meetup.com/python-barcelona/events/313395411/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 313395411 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: faststream-a-modern-wrapper-for-publisher-consumer
    title: "Faststream: A Modern Wrapper for Publisher/Consumer Implementations"
    speakers: [felix-morillas-navas]
    type: talk
    language: en
    duration_minutes: 30
    description: "Design a structured project implementation with comprehensive tests and scalability features for a larger application using a simple wrapper pattern."
  - id: implementing-guidelines-and-good-practices-with-ai-and
    title: "Implementing guidelines and good practices with AI and semgrep"
    speakers: [adam-fourure]
    type: talk
    language: en
    duration_minutes: 30
    description: "Adam will present how to enforce good practices and guidelines in your development workflow via modern tooling.\nWe will explore three ways to do static analysis :\n- at code level via deterministic linters (notably via semgrep)\n- integrate your own custom business rules on top of the usual tools (ruff, mypy, etc.)\n- at review level via a fine-tuned AI code-reviewer (also integrated in modern IDE)"
---
