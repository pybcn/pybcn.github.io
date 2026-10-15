---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 275699716.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyBCN Online: January Meetup"
date: 2021-01-21
year: 2021
# The export records this event as ONLINE, so it had no room.
venue: "Online"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 116
meetup_url: "https://www.meetup.com/python-barcelona/events/275699716/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 275699716 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: architecture-decision-records-documenta-tu-arquitectura
    title: "Architecture Decision Records: documenta tu arquitectura, explica tus decisiones"
    speakers: [hector-canto]
    type: talk
    language: es
    description: "Una de los aspectos peor documentados de un proyecto de Software es la evolución de la arquitectura. Los ADR os ayudarán a hacer una foto de vuestras decisiones como desarrollador y arquitecto de software, reflexionar sobre tus motiviciones para optar por ciertas soluciones y poner por escrito tus expectativas y riesgos asumidos.\n\nEn esta charla veremos qué es un ADR, por qué hacerlo, cuando hacerlo y cómo empezar."
---
