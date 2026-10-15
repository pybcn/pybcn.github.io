---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 264597651.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python September Meetup"
date: 2019-09-19
year: 2019
venue: "BitPhy"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 48
meetup_url: "https://www.meetup.com/python-barcelona/events/264597651/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 264597651 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: data-quality-and-how-we-are-trying-to-break-the-80-20
    title: "Data Quality and how we are trying to break the 80/20 cleaning rule"
    speakers: [ana-dorofei]
    type: talk
    language: en
    duration_minutes: 30
    description: "We have all heard data scientists spend only about 20% of their precious time developing algorithms and building machine learning models. Let's look a bit into the less sexy aspect of Data Science which takes 80% of our time - cleaning and organizing the data - and a couple of ideas towards automating it with Python."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=b8s8a71AYd8"
  - id: python-for-the-management-of-iot-platforms-at-worldsensing
    title: "Python for the management of IoT platforms at Worldsensing"
    speakers: [toni-martinez-del-hoyo]
    type: talk
    language: en
    duration_minutes: 30
    description: "Overview on the tech stack and architecture at the Innovation department of Worldsensing to bridge the gap between our IoT sensors and our data monitoring application."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=JzX9WAv7PVM"
---
