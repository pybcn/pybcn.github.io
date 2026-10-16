---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 300940146.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup May: Computer vision and A/B Testing"
date: 2024-05-23
year: 2024
venue: "Aticco Bogatell - Coworking en Poblenou"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 82
meetup_url: "https://www.meetup.com/python-barcelona/events/300940146/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 300940146 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: using-opencv-in-ai-practical-image-processing-in-python
    title: "Using OpenCV in AI: Practical Image Processing in Python"
    speakers: [paula-oses]
    type: talk
    language: en
    duration_minutes: 30
    description: "This talk focuses on the practical use of OpenCV in the field of artificial intelligence, particularly for Python users. The session will cover the essentials of OpenCV, including basic image operations and advanced preprocessing techniques vital for preparing data for AI models. As an AI Engineer I have used the OpenCV library since my years at university, I have prepared lots of datasets for AI models using this library as well as explored its capabilities in terms of Computer Vision models."
  - id: cluster-experiments-a-simulation-library-to-design-ab-tests
    title: "cluster-experiments, a simulation library to design AB tests"
    speakers: [david-masip]
    type: talk
    language: en
    duration_minutes: 45
    description: "Cluster-experiments is an open-source library that is used at Glovo to design AB tests (assess experiment length, AA tests, etc). We use a simulation approach which can accommodate different types of tests, being more general than what more popular libraries provide."
---
