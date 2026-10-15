---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 261405719.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: Python May Meetup
date: 2019-05-16
year: 2019
venue: gaa9
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 44
meetup_url: https://www.meetup.com/python-barcelona/events/261405719/
group: PyBCN
# The talks this meetup announced, read from the description of event 261405719 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: chatops-101-with-python-and-opsdroid
  title: Chatops 101 with Python and Opsdroid
  type: talk
  language: es
  duration_minutes: 30
  description: We will see how easy it is to have a bot running with some basic skills and connected to different services (Slack, Telegram, Github...). Also, we will see how to write our custom skills and adapt the bot to our necessities.
  speakers:
  - angel-fernandez-ibanez
  links:
  - type: video
    url: "https://www.youtube.com/watch?v=04ZPyA_lE8Y"
- id: damegender-gender-detection-tool-experiments-with-nltk-and
  title: 'Damegender: gender detection tool experiments with NLTK and Scikit'
  speakers:
  - david-arroyo-menendez
  type: talk
  language: es
  duration_minutes: 45
  description: Se abordarán las problemáticas de NLP (feeling analysis, clasificación de documentos, identificación de género, similitud de frases, resumen de textos, ...) mediante ejemplos prácticos de NLTK. Seguidamente, se introducirá la estadísitica y el machine learning con Scikit. Finalmente, se expone damegender un detector de género scrito en Python utilizando estas tecnologías como ejemplo práctico de aplicación.
  links:
  - type: video
    url: https://www.youtube.com/watch?v=dvN0lMgQ9Pc
  - type: github
    url: https://github.com/davidam/damegender
- id: mocking-and-patching-pitfalls
  title: Mocking and Patching Pitfalls
  speakers:
  - edwin-jung
  type: talk
  language: en
  duration_minutes: 30
  description: Mocking and patching are powerful techniques for testing, but they can be easily abused, with negative effects on code quality, maintenance, and application architecture. These pain-points can be hard to verbalize, and consequently hard to address. If your unit tests are a PITA, but you cannot explain why, this talk may be for you. Mocking as a technique has deep roots within OOD and TDD, going back 20+ years, but many Python developers know mocks and patches merely as a technique to isolate code under test. In the absence of knowledge around OOD and TDD, best practices around mocking are completely unknown, misunderstood, or ignored. Developers who use mocks and patches without doing TDD or OOD are susceptible to falling into many well-understood and documented traps. This talk will draw a historical connection between the way mocks are taught today, and their origins in TDD, OOD, and Java. It will also demonstrate some pitfalls, and provide some guidance and alternatives to mocking and patching (e.g., dependency injection, test doubles, functional style).
  links:
  - type: video
    url: https://www.youtube.com/watch?v=qqse-zvnNn0
---
