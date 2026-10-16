---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 310935234.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup September: Tornada a l'escola"
date: 2025-09-17
year: 2025
venue: "Auditori Cibernàrium - MEDIATIC"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 3
meetup_url: "https://www.meetup.com/python-barcelona/events/310935234/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 310935234 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: python-i-productivitat-com-sobreviure-a-la-vida-moderna
    title: "Python i productivitat: Com sobreviure a la vida moderna"
    speakers: [silvia-ampuero]
    type: talk
    language: ca
    duration_minutes: 45
    description: "En la xerrada descobriràs com Python et pot ajudar a automatitzar tasques quotidianes amb poques línies de codi. Es parlarà de llibreries com Pandas, Matplotlib o les que permeten integrar-te amb Telegram i reconeixement de veu, eines que et permetran passar de la idea a la realitat de manera ràpida i intuïtiva."
  - id: python-for-generation-z
    title: "Python for Generation Z"
    speakers: [nuria-pujol-vilanova]
    type: talk
    language: ca
    duration_minutes: 30
    description: "En aquesta xerrada descobriràs frameworks com FastAPI i llibreries com Streamlit, uv i Marimo, que permeten transformar idees en aplicacions reals, visuals i interactives de manera ràpida i intuïtiva. Aquestes eines, perfectament alineades amb el ritme i els interessos dels joves, fan que aprendre Python sigui un procés més motivador i adequat per al desenvolupament professional. Ideal per a qui vulgui conèixer com portar les seves idees a la realitat amb Python de manera eficaç, creativa i àgil."
---
