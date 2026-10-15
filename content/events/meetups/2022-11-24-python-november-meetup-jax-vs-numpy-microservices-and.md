---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 289785507.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python November Meetup: JAX vs Numpy & Microservices and distributed data"
date: 2022-11-24
year: 2022
venue: "CloudBlue"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 28
meetup_url: "https://www.meetup.com/python-barcelona/events/289785507/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 289785507 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: how-to-resolve-the-issue-with-the-inconsistency-of
    title: "How to resolve the issue with the inconsistency of distributed data in your Python project"
    speakers: [pavel-lonkin]
    type: talk
    language: en
    duration_minutes: 30
    description: "Often in the microservice architecture, you have to share the data between services. How do you resolve this problem in your product? I will share what approach we are using for our fancy Django services and also share the tip on how to do zero downtime continuous migration of data when you are in the process of splitting the monolith."
  - id: introducing-jax-a-faster-and-more-efficient-numpy
    title: "Introducing JAX: a faster and more efficient Numpy"
    speakers: [ferran-jimenez]
    type: talk
    language: en
    duration_minutes: 20
    description: "JAX is an Open Source Python library created by Google and already adopted by DeepMind. JAX supports automatic differentiation and employs XLA, resulting in faster numerical computing than Numpy."
---
