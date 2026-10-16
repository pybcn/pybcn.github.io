---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 285765821.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Code Katas - TDD first steps"
date: 2022-05-26
year: 2022
venue: "TravelPerk 4ª Planta"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 24
meetup_url: "https://www.meetup.com/python-barcelona/events/285765821/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 285765821 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: python-code-katas-tdd-first-steps
    title: "Python Code Katas - TDD first steps"
    type: workshop
    description: "ESPAÑOL\n\n¡Vuelven las sesiones prácticas!\n\nEn este taller practicaremos nociones básicas de Test Driven Development con Python con un ejercicio (kata) sencillo, al que iremos añadiendo complejidad a medida que avance la sesión.\n\n¿Aún no sabes cómo escribir tests? ¡No te preocupes! Comenzaremos con una pequeña introducción al testing en Python con pytest, y a continuación presentaremos el problema a resolver, creando grupos de dos o tres personas con diferentes niveles, para que todo el mundo pueda aprender.\n\nRequisitos:\n\n* Conocimientos básicos de programación en algún lenguaje orientado a objetos\n* Ven con tu portátil con Python 3 instalado\n\nHabrá pica-pica y bebidas durante toda la sesión.\n\nENGLISH\n\nPractice sessions are back!\n\nIn this workshop we will practice Test Driven Development in Python with a simple exercise (kata), that will increase in difficulty over the course of the session.\n\nYou don't know how to write tests yet? Don't worry! We will start with a short introduction about how to do testing in Python using pytest, present the problem to be solved, and then work on it in groups of 2 or 3 people, trying to mix up people with different levels so we all can learn.\n\nRequisites:\n\n* Basic knowledge of an object-oriented programming language\n* Come with your laptop with Python 3 installed\n\nSnacks and drinks will be available during the whole session."
---
