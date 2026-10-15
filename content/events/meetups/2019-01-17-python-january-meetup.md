---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 257959353.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python January Meetup"
date: 2019-01-17
year: 2019
venue: "21 buttons"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 44
meetup_url: "https://www.meetup.com/python-barcelona/events/257959353/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 257959353 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: django-gone-clean
    title: "Django gone clean"
    speakers: [jairo-vadillo]
    type: talk
    language: en
    duration_minutes: 30
    description: "At 21 Buttons we've evolved our backend from a monolithic, architecture-less django to a clean architecture, multi-serviced one. In this talk, I will explain the process we've been through, what we've learned and how the current codebase looks like."
  - id: machine-learning-and-time-series-analysis-for-brain-signals
    title: "Machine Learning and Time Series Analysis for Brain Signals"
    speakers: [andrea-insabato]
    type: talk
    language: en
    duration_minutes: 30
    description: "I will show in a tutorial style how to analyse brain activity recoded with fMRI. Time series analysis techniques will be employed to model the data and infer hidden variables. Machine learning will be used to understand the relation between brain activity and \"mental\" states (e.g. different cognitive states or pathological states)."
  - id: building-glovo-s-own-spatial-analytics-tool
    title: "Building Glovo's own spatial analytics tool"
    speakers: [aleksey-martynyuk]
    type: talk
    language: en
    duration_minutes: 30
    description: "There is a growing number of analytical applications offered by new firms and established software vendors. IT and Data departments have to decide between buying an external tool or developing one in-house. Either is costly. Glovo created a suitable analytical tool for leveraging the large amount of spatial data we collect using open-source tools, python libraries and frameworks. We were able to build a minimum viable product and a foundation for a spatial analytics framework without committing too much money or developer hours. This talk will take you through the process of designing and building the tool, and present the current architecture, with a demo."
---
