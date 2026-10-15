---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 236196808.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: Python December Meetup
date: 2016-12-22
year: 2016
venue: Skyscanner
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 54
meetup_url: https://www.meetup.com/python-barcelona/events/236196808/
group: PyBCN
# The talks this meetup announced, read from the description of event 236196808 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: clean-code-in-python
  title: Clean code in Python
  speakers:
  - mariano-anaya
  type: talk
  language: en
  duration_minutes: 30
  description: Introduction to the clean code principles tailored for Python projects. The goal is to achieve better code quality and a more maintainable code base. Python has a nature of being clear, and easy to follow, so let's take advantage of it in our own code, in order to enforce the principle "readability counts" by writing pythonic code. This talk introduces general concepts of code quality for Python developers, analyzing technical debt, with examples on how to achieve a more legible, maintainable and clean code base, by refactoring, writing unit tests and having good coding guidelines for the project. If you are giving your first steps with Python, you will gain insight on best practices for writing good software from the start. If you are a experienced developer, the ideas should work as food for thought, helping with recommendations for code reviews, best practices, etc.
- id: neither-conda-pip-virtualenv-long-live-to-buildout
  title: Neither conda, pip, virtualenv ... long live to buildout!
  type: talk
  language: en
  duration_minutes: 30
  description: Buildout is a system to manage development/production, its centric on replication of a Python application assembly, configuration and deployment. Designed to be development friendly has an addon API with hundreds of recipes on top to build most generic python software and easy interface to create your own.
  speakers:
  - ramon-navarro-bosch
- id: asynchronous-caching-with-aiocache
  title: Asynchronous caching with aiocache
  speakers:
  - manuel-miranda
  type: talk
  language: en
  duration_minutes: 30
  description: asyncio is the default standard for asynchronous programming in Python. Although it has been around for a while, the ecosystem around it is still quite new and under development. One of the needs I had and wasn't resolved yet was the existence of an easy caching package for asynchronous frameworks like aiohttp and sanic. This is the reason why I started https://github.com/argaen/aiocache . Come and learn all its possibilities and use cases :)
  links:
  - type: github
    url: https://github.com/argaen/aiocache
---
