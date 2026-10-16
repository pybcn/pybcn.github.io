---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 255574057.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python October Meetup"
date: 2018-10-24
year: 2018
venue: "Kiwi.com"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 56
meetup_url: "https://www.meetup.com/python-barcelona/events/255574057/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 255574057 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: using-votes-to-combine-rankings
    title: "Using votes to combine rankings"
    speakers: [ferran-muinos]
    type: talk
    language: en
    duration_minutes: 30
    description: "How to best combine the outcome of several ranked data into a single, meaningful consensus ranking is a recurrent problem in scientific data analysis. Particularly, in genome data analysis we are often bound to merge ranked data arising from separate statistical analyses. Traditional blending strategies applied in the field rely on techniques to combine statistical significance, but this approach on its own has been associated with a number of caveats. I hereto present a voting-based heuristics implemented in Python which leverages both Schulze's voting algorithm and optimization techniques to combine rankings upon credibility scores inferred from prior knowledge. This rationale can be used alongside state-of-the-art methods to systematically incorporate prior knowledge, thereby leading to more interpretable outcomes. The scope of the method is quite general and may be of use in other data analysis contexts."
  - id: async-makes-me-hmmm-thinking-face
    title: "Async makes me hmmm :thinking_face:"
    speakers: [lukas-kubis]
    type: talk
    language: en
    duration_minutes: 30
    description: "The introduction of async/await syntax to python couple of years ago spiked interest in many people, only to leave most of them confused and terrified. It's getting even worse as async quickly expands and the whole language is effectively splitting into two. Let's discuss why it's happening, who is it for and how can we reason about the existence of this mysterious code."
  - id: coding-together-different-ways-to-do-so-for-data-enthusiasts
    title: "Coding together, different ways to do so for Data Enthusiasts"
    speakers: [dimitri-herrero]
    type: talk
    language: es
    duration_minutes: 30
    description: "En esta charla me gustaría repasar y comparar las herramientas que hay ahora para explorar datos y entrenar modelos de machine learning. Si eres un data scientist o enthusiast, seguramente estás usando Jupyter Notebooks para explorar datos. Sin embargo a la hora de trabajar en equipo tenemos varias herramientas como Google Colaboratory, Google Datalab, Amazon SageMaker, etc. que podrían adaptarse mejor para el uso de un equipo."
---
