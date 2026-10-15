---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 316366469.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup September: Summer is ending!"
date: 2026-09-16
year: 2026
venue: "Dow Jones"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 72
meetup_url: "https://www.meetup.com/python-barcelona/events/316366469/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 316366469 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: nothing-has-beaten-our-14b-classifier
    title: "Nothing has beaten our 14b classifier"
    speakers: [marta-rodriguez]
    type: talk
    language: en
    duration_minutes: 35
    description: "A 14-billion-parameter classifier has been running in our production pipeline for almost a year, processing millions of documents a month. It's not out of attachment: we have tried to replace it with newer and better models, ones that on paper beat it on most benchmarks, and each time the replacement cost us more than it bought.\nIn this talk, I'll walk you through what happened each time we tried to upgrade, what we learned about the numbers we'd been trusting, and the bar a new model now has to clear before it gets near production. It's a low bar. Almost nothing clears it."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=r_upsuTDED4"
  - id: why-llms-can-t-make-your-code-simpler
    title: "Why LLMs Can't Make Your Code Simpler"
    speakers: [pol-alvarez-vecino]
    type: talk
    language: en
    duration_minutes: 35
    description: "LLMs tend to increase the complexity of a codebase very fast, especially if left unchecked. If you're fine with that creeping complexity, this talk may not be for you. But if you have tried to tame it, you'll have noticed how hard it is. Why is that? Why can't LLMs write simple code? Couldn't frontier labs just train models to minimize total LoC, or cyclomatic complexity?\nIn Programming as Theory Building (1985), Peter Naur argues that the real program is not the code but the understanding in your head. That is one of the key problems for LLMs: the information needed to simplify code was never in the code to begin with. As a working example, I'll show how this mindset let us at Answer.AI cut our Stripe billing system down to ~300 lines of Python - and why this solution might also be good for you (or not!)."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=LwchtmM-d-s"
---
