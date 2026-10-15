---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 294322691.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: 'Python June Meetup: Data Science learning path & Collaboration in Data Teams'
date: 2023-06-28
year: 2023
venue: Le Wagon Barcelona
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 36
meetup_url: https://www.meetup.com/python-barcelona/events/294322691/
group: PyBCN
# The talks this meetup announced, read from the description of event 294322691 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: from-data-science-bootcamp-student-to-freelancer
  title: From Data Science Bootcamp student to Freelancer
  speakers:
  - nikita-polovinkin
  type: talk
  language: en
  duration_minutes: 30
  description: Sharing valuable experience of attending a Data Science Bootcamp and applying the skills acquired to start a career in the tech sector as a Data Scientist freelancer, working for companies from different sectors, providing valuable insights in their business and provide automation
- id: collaboration-between-data-scientists-and-data-engineers
  title: Collaboration between Data Scientists and Data Engineers - Raise team's performance through Merge Requests
  type: talk
  language: en
  duration_minutes: 40
  description: Sometimes Data Scientists that are not computer engineers and come from different backgrounds, write Machine Learning models and to deploy them to production Data Engineers have to do some refactoring. In this talk we will see how we can improve the workflow and have Data Scientists writing production code through Merge Requests.
  speakers:
  - josep-martinez-vila
  - juan-prida
---
