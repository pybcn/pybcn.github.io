---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 308161751.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup June: Almost summer and already sweating"
date: 2025-06-11
year: 2025
venue: "Codurance"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 58
meetup_url: "https://www.meetup.com/python-barcelona/events/308161751/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 308161751 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: ai-is-the-new-ui-building-interactive-genui-with-fasthtml
    title: "AI is the new UI: Building Interactive GenUI with FastHTML"
    speakers: [pol-alvarez-vecino]
    type: talk
    language: en
    duration_minutes: 30
    description: "Today's AI applications are predominantly text-based and feel clunky compared to traditional UIs. This talk demonstrates how to build truly interactive Generative UI (genUI) applications using Python, FastHTML, and Answer.ai libraries. I'll showcase how to transition from basic text-based chat into rich interactive experiences with buttons and visual elements - all in less than 150 lines of code. Through live demos of weather cards, an interactive mindfulness app, and a HAL 9000 simulator, you'll learn how the hypermedia approach eliminates \"contract coupling\" between frontend and backend, enabling LLMs to generate truly dynamic interfaces that users can interact with directly."
  - id: license-to-think-build-your-own-ai-agent-with-python-and
    title: "License to Think: Build Your Own AI Agent with Python and PydanticAI"
    speakers: [javier-martinez-alcantara]
    type: talk
    language: en
    duration_minutes: 30
    description: "What if your next secret agent wasn't human... but artificial?\nIn this 30-minute crash course, you'll learn how to build structured, tool-using AI agents with PydanticAI - the sleek new framework for LLM-powered applications. Perfect for devs, data enthusiasts, and Python spies in training"
---
