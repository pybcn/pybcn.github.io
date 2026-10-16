---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 262612448.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: PyLadies Summer Edition
date: 2019-07-16
year: 2019
venue: Marfeel
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 33
meetup_url: https://www.meetup.com/pyladies-bcn/events/262612448/
group: PyLadies BCN
# The talks this meetup announced, read from the description of event 262612448 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: one-day-as-a-data-scientist-with-python
  title: One day as a Data Scientist (with Python)
  speakers:
  - anisa-oshafi
  type: lightning
  description: Talk about what it is like being a data scientist, how to get started with it in Python and some lessons from personal experience.
- id: getting-involved-in-open-source-community-the-outreachy
  title: 'Getting involved in open source community: The Outreachy story'
  speakers:
  - lenka-segura
  type: lightning
  description: 'My fresh experience with Outreachy internship: a project supporting people underrepresented in tech'
- id: how-to-work-with-google-sheets-using-gspread-python-library
  title: How to work with Google Sheets using gspread python library
  speakers:
  - anna-fedotova
  type: lightning
  description: In this session I will walk you through the main functionality of gspread library and the use cases for its application to working with Google Sheets.
- id: having-fan-with-django-and-arduino
  title: Having FAN with Django and Arduino
  type: lightning
  description: Try to imagine. You are totally comfortable in your sofa, lights off, with your cat in your legs and after a while you realized that your fan is off. How to avoid breaking this Zen moment? IoT (internet of the things) is the solution. In this short talk you will see an example of how an small circuit and few lines of code can improve your day by day.
  speakers:
  - elisabeth-ortega-carrasco
- id: object-detection-using-deep-learning
  title: Object detection using Deep Learning
  speakers:
  - nohemi-veiga
  type: lightning
  description: Convolutional Neural Networks have been widely and successfully used for Image Classification. However, what happens when there are multiple objects that require localization and classification? This is a more challenging task since most of the time, multiple objects of different types, may be found on the image. Often, techniques developed for image classification with localization are used and demonstrated for object detection, and this kind of techniques have several applications including security, automated vehicle systems, retail and health.
---
