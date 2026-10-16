---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 266430123.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python November Meetup"
date: 2019-11-21
year: 2019
venue: "ColorSensing"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 66
meetup_url: "https://www.meetup.com/python-barcelona/events/266430123/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 266430123 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: avoid-food-waste-with-qr-codes-and-computer-vision
    title: "Avoid food waste with QR codes and computer vision"
    speakers: [ismael-benito]
    type: talk
    language: en
    duration_minutes: 30
    description: "At ColorSensing, a spin-off from University of Barcelona, we are developing both a general SaaS solution to digitalize colorimetric sensors and also a specific solution with colorimetric gas sensors to study the behaviour of food modified athmosphere packaging (MAP). We aim to impact the value chain in the food market with real traceability of the sealed food packages."
  - id: machine-learning-with-electronic-health-record-ehr-systems
    title: "Machine Learning with Electronic Health Record (EHR) Systems"
    speakers: [gabriel-de-maeztu]
    type: talk
    language: en
    duration_minutes: 45
    description: "EHR systems can have data from a variety of different sources including billing data, patient demographics, medical history, lab results, sensor data, prescriptions, clinical notes, medical images, etc. I will cover a couple of ML models that use this kind of data to cover different use cases and i'll talk about the multiple bias that the data might have."
---
