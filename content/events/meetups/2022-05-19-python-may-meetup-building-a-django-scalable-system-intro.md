---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 285859785.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: 'Python May Meetup: Building a Django scalable system & Intro to PyScript'
date: 2022-05-19
year: 2022
venue: Mundimoto
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 53
meetup_url: https://www.meetup.com/python-barcelona/events/285859785/
group: PyBCN
# The talks this meetup announced, read from the description of event 285859785 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: from-zero-to-hero-building-a-scalable-system-from-scratch
  title: 'From zero to hero: building a scalable system from scratch using Django'
  speakers:
  - samuel-parra
  type: talk
  language: en
  duration_minutes: 30
  description: 'Mundimoto is the intersection between two models: modern startups and traditional companies. It has grown 25x its operations in the last year, taking an undisputed lead in the used motorbike industry in Europe. We''re not going to stop here; we''re expanding our factories internationally, this April we already opened Milan (Italy), we''re planning eight more countries in Europe, and we want to have a part in the future of mobility, doing way more than buying and selling motorbikes. To support all these challenges, we know software and talent are essential. We have a diverse team coming from Facebook, Snapchat, Glovo, Skyscanner, Typeform, Wallapop and many others. Our use cases are unique, and we see the company''s future depends on having software built specifically for us and by us. With so many moving pieces, the only way to achieve our goals is with high-quality software, data science being at the core of the system decisions, and clever UI/UX designs to support our use cases. In this talk we are going to speak about an essential part of our architecture that is how we design, test and deploy our services into production.'
- id: introduction-to-pyscript
  title: Introduction to PyScript
  speakers:
  - david-arcos
  type: talk
  language: en
  duration_minutes: 30
  description: PyScript was just announced at the PyCon 2022! This new framework allows users to create rich Python applications in the browser using HTML's interface. PyScript aims to give users a first-class programming language that has consistent styling rules, is more expressive, and is easier to learn. Let's see how it works!
---
