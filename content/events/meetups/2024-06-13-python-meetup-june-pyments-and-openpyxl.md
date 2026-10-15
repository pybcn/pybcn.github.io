---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 301297291.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: 'Python Meetup June: Pyments and OpenPyXL'
date: 2024-06-13
year: 2024
venue: Gartner - Center of Excellence
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 69
meetup_url: https://www.meetup.com/python-barcelona/events/301297291/
group: PyBCN
# The talks this meetup announced, read from the description of event 301297291 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: pyments-how-to-design-payment-applications-in-python
  title: 'Pyments: How To Design Payment Applications In Python'
  type: talk
  language: en
  duration_minutes: 30
  description: '"Payments are a massive part of how the world works. But most engineers know very little about it. That''s sad, because, as more and more of business happens online, there''s an increasing demand for payment applications that are scalable, and maintainable. Besides, Python is a great programming language to build payment applications! It is very interoperable, has a thriving open source community, and even non-engineers can contribute significantly to software built with it. In payments, readability counts, too!

    In this talk, we''re going to dive deep into how to build money software effectively. You''ll learn why Python and payments are a match made in heaven, and how to leverage the language to build your own payment applications, in-house, fast, and effectively. That way, you''ll cut some intermediaries in the process, saving your company a lot of money. It is no wonder why software engineers that can build payment applications are in high demand, they can point to their code and say "that prints money"."'
  speakers:
  - alvaro-duran-barata
- id: mastering-excel-automation-with-openpyxl
  title: Mastering Excel Automation with OpenPYXL
  speakers:
  - jordi-bosch
  type: talk
  language: es
  duration_minutes: 30
  description: 'Tired about complex VBA macros and functions? Join the Excel revolution as we see how OpenPYXL Python library changes how we work with spreadsheets. We''ll discover how to handle data with a touch of Python magic.

    By the end, you''ll be an Excel expert, easily automating tasks and managing complex data with a few clicks. Get ready to improve your data skills!'
---
