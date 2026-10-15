---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 286466251.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Code Katas - June"
date: 2022-06-28
year: 2022
venue: "Holaluz"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 24
meetup_url: "https://www.meetup.com/python-barcelona/events/286466251/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 286466251 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: python-code-katas-june
    title: "Python Code Katas - June"
    type: workshop
    description: "ESPAÑOL\n\n¡Vuelven las sesiones prácticas!\n\nEn esta sesión continuaremos con la práctica de Test Driven Development, con un ejercicio de nivel algo superior al de la primera sesión, al que iremos añadiendo complejidad poco a poco.\n\nRequisitos:\n\n* Conocimientos básicos de programación en algún lenguaje orientado a objetos\n* Ven con tu portátil con Python 3 instalado\n\nHabrá pica-pica y bebidas durante toda la sesión.\n\nENGLISH\n\nPractice sessions are back!\n\nWe will continue practicing Test Driven Development in Python. The exercise will be slightly more complex than the one in the first session, and it will increase difficulty over time.\n\nRequisites:\n\n* Basic knowledge of an object-oriented programming language\n* Come with your laptop with Python 3 installed\n\nSnacks and drinks will be available during the whole session."
---
