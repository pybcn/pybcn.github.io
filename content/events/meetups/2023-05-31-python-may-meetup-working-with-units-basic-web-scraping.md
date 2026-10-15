---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 293692260.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: 'Python May Meetup: Working with units & Basic Web Scraping'
date: 2023-05-31
year: 2023
venue: Gran Via de les Corts Catalanes, 613
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 42
meetup_url: https://www.meetup.com/python-barcelona/events/293692260/
group: PyBCN
# The talks this meetup announced, read from the description of event 293692260 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: working-in-units-how-to-decouple-the-database-and-domain
  title: 'Working in Units: How to Decouple the Database and Domain Layers in Python'
  type: talk
  language: en
  duration_minutes: 30
  description: A crucial element of architecting a software application for scale is the collaboration of domain experts and developers. For that to happen, the application must separate the domain layer- where elements that represent the real world reside-from the infrastructure layer-where these elements are translated into precise software processes.Within the Fintech team at Kiwi.com, we are rearchitecting a critical service to accept more payment providers. As part of this refactor, we are adopting the Unit of Work pattern to disentangle domain entities from the database processes that represent them. This way, domain experts can share their knowledge with developers more easily, and developers can find opportunities for optimization without the involvement of domain experts in the process.Attendees will gain a solid understanding of how to implement the UoW pattern in their Python applications, how it fits into the broader context of DDD, and how to prepare their code for future growth.
  speakers:
  - alvaro-duran-barata
- id: basic-web-scraping-with-beautiful-soup
  title: Basic web scraping with Beautiful Soup
  speakers:
  - noe-casas
  type: talk
  language: en
  description: Web scraping consists of different techniques to extract information from web pages. Beautiful Soup is one of the most popular web scraping Python frameworks. In this talk we will be having a practical live coding session, creating a web scraper to collect information from a web site.
---
