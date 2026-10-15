---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 306008239.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup February: The Winter Meetup"
date: 2025-02-18
year: 2025
venue: "Oficinas de Glovo (Yellow Park)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 75
meetup_url: "https://www.meetup.com/python-barcelona/events/306008239/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 306008239 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: jupyter-notebook-based-report-engine
    title: "Jupyter Notebook based report engine"
    speakers: [xavier-orduna]
    type: talk
    language: en
    duration_minutes: 30
    description: "I will explain how to use Jinja2 and Jupyter Notebooks to give our customers a way to run code in a sandboxed environment (using k8s) to create any kind of HTML reports.\n\nSome topics covered:\n- Golang - Python communication\n- Starting kernel runners on K8S from Python\n- Communication with kernel runners\n- Image rendering\n- Self-contained HTML files\n- Disposable API keys"
  - id: leveraging-python-for-building-a-logistics-simulator
    title: "Leveraging Python for Building a Logistics Simulator"
    speakers: [manuel-bolivar]
    type: talk
    language: en
    duration_minutes: 30
    description: "Explore how Glovo leveraged the Python ecosystem to develop a digital twin of its logistics operations spanning 600+ cities in 22 countries. In this talk, we examine the integration of discrete-event simulation, optimization algorithms, and meta-heuristics to dynamically adjust and optimize operational parameters. Attendees will learn how these simulation techniques can drive operational improvements and gain practical insights from the lessons learned during development."
---
