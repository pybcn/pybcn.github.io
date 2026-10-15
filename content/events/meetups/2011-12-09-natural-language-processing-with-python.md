---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 41288182.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Natural Language Processing with Python"
date: 2011-12-09
year: 2011
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 17
meetup_url: "https://www.meetup.com/python-barcelona/events/41288182/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 41288182 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: natural-language-processing-with-python
    title: "Natural Language Processing with Python"
    speakers: [luciano-guasco]
    type: talk
    description: "Luciano Guasco is going to give an introduction to Natural Language Processing in Python.\n\nOutline:\n\n* What does NLP mean from a practical perspective?\n\n-Intro\n\n-Basic tasks: Tokenization, Stemming, POS Tagging, Synonyms.\n\n-Examples\n\n-Open Problems\n\n* Why Python to process language?\n\n-Personal experience of migration\n\n-Fast review of Python operations\n\n-NLTK, a NLP Swiss Army knife : Using the library for Tokenization, Stemming, POS Tagging, Synonyms, Grammar Parsing.\n\n-Extending text processing: Some Datamining & Machine Learning concepts, and how to use them with language and text\n\n* Let's Code: Some basic and advanced examples!"
    links:
      - type: site
        url: "https://www.nltk.org/"
---
