---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 303407709.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup September: AI Goes Back To School"
date: 2024-09-26
year: 2024
venue: "Codurance"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 55
meetup_url: "https://www.meetup.com/python-barcelona/events/303407709/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 303407709 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: from-text-to-actions-llms-as-the-new-software-consumers
    title: "From text to actions: LLMs as the new software consumers"
    speakers: [pol-alvarez-vecino]
    type: talk
    language: en
    duration_minutes: 30
    description: "QA bots, copilots, workflow automation - LLMs are evolving to control our software through natural language. The endgame is APIs. LLMs that can convert user intents directly into HTTP requests, like Talk2Apis does today, will have the flexibility to access any service. This creates a machine-first software economy with big implications for developers. Python examples included."
  - id: ragtime-an-approach-to-retrieval-augmented-generation
    title: "Ragtime: An Approach to Retrieval-Augmented Generation"
    speakers: [javier-martinez-alcantara]
    type: talk
    language: en
    duration_minutes: 30
    description: "In this session, we'll explore a pattern that has sparked significant interest in the world of natural language models (LLMs): Retrieval-Augmented Generation (RAG). We'll walk through a practical implementation, dive into its details, and share insights based on our experiences working with these methods. Whether you're a beginner or an expert, we encourage you to join-what matters most is your interest in LLMs, machine learning, and engineering, and how to leverage these technologies to bring value to your company or organization."
---
