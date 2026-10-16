---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 281418180.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "How we built our experimentation framework with Python"
date: 2021-10-26
year: 2021
# The export records this event as ONLINE, so it had no room.
venue: "Online"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 56
meetup_url: "https://www.meetup.com/pyladies-bcn/events/281418180/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 281418180 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: how-we-built-our-experimentation-framework-with-python
    title: "How we built our experimentation framework with Python"
    speakers: [shyamala-gopalakrishnan, liss-mansurova]
    type: talk
    language: en
    description: "Preply is a global language learning marketplace, connecting tutors with millions of learners from all over the world. Since the company launched in 2012, Preply has been driven by the mission to shape the future of effective learning through human tutoring. The company uses a machine learning algorithm to increase matching efficiency between learners and tutors on a variety of parameters such as price, availability, country of birth, other languages spoken, learning objectives and more. From there, the student can select their preferred tutor considering their introduction video, methodology description and reviews from other learners.\n\nIn Preply we have a strong experimentation culture and in this talk we would explain how we created our experimentation framework, step by step and with production code examples. We will show the tools we use, the metrics we check and how our value chain is, from research, design, implementation to measuring. You will learn something that you probably haven't seen before!"
---
