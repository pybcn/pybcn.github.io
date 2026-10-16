---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 311887940.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup November: LLMOps & Python Tooling with uv"
date: 2025-11-20
year: 2025
venue: "Dow Jones"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 86
meetup_url: "https://www.meetup.com/python-barcelona/events/311887940/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 311887940 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: llm-ops-tools-that-accelerate-your-llm-journey
    title: "LLM Ops: Tools that accelerate your LLM journey"
    speakers: [olga-garces, jordi-mas]
    type: talk
    language: en
    duration_minutes: 30
    description: "Large Language Models (LLMs) have moved from research to production at a rapid pace, but managing them effectively requires more than just model selection. Much like DevOps and MLOps, LLM Ops has emerged as a discipline focused on the end-to-end lifecycle of LLMs - from development and testing to deployment and monitoring.\nIn this talk, we will share practical insights and lessons learned from implementing LLM Ops in real environments. we'll highlight the challenges of complex workflow development, prompt evaluation, and system observability - and show the tools that helped us solve them like LangChain, PromptFoo or LangSmith.\nThis session will provide actionable guidance for anyone building with LLMs on how to accelerate their own LLM projects while avoiding common pitfalls."
  - id: a-new-era-in-python-tooling-with-uv-by-astral
    title: "A new Era in Python Tooling with uv (by Astral)"
    speakers: [marc-ramirez]
    type: talk
    language: en
    duration_minutes: 30
    description: "Python's packaging ecosystem has long been robust - but also fragmented and slow. Enter uv, Astral's next-generation Python tool designed to unify and accelerate everything from dependency management to virtual environments and builds.\nIn this session, we'll explore how uv reimagines the Python developer experience with lightning-fast performance.\nWe'll compare it with traditional tools, highlight its core features, and walk through real-world usage examples that show how uv can simplify your projects and speed up your day-to-day development."
---
