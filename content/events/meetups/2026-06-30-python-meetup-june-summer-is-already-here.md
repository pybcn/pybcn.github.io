---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 315383583.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup June: Summer is already here!"
date: 2026-06-30
year: 2026
venue: "Cibernarium MediaTIC (Barcelona Activa)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 27
meetup_url: "https://www.meetup.com/python-barcelona/events/315383583/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 315383583 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: feedback-immediat-per-estudiants-de-programacio-powered-by
    title: "Feedback immediat per estudiants de programació: Powered by Python"
    speakers: [moises-gomez-giron]
    type: talk
    language: ca
    duration_minutes: 45
    description: "Presentació d'una eina per a l'ensenyament de la programació, creada per minimitzar el temps entre la resolució de l'exercici i la recepció de la retroacció. L'eina ha estat desenvolupada al llarg dels anys en paral·lel al seu ús a l'aula, sota pressió per terminis ajustats, canvis de temari i estudiants amb imaginació per trobar maneres enginyoses d'enganyar el sistema. El resultat és una història de compromisos i solucions creatives, des de prohibir funcionalitats concretes del llenguatge fins a l'ús exclusiu de tecnologies gratuïtes."
  - id: python-powered-cybersecurity-lab-caldera-elastic-stack-att
    title: "Python-powered Cybersecurity Lab: Caldera, Elastic Stack & ATT&CK simluation"
    speakers: [mauricio-volcanes]
    type: talk
    language: es
    duration_minutes: 45
    description: "En esta charla mostraremos un laboratorio completo de ciberseguridad compuesto por máquinas virtuales, Elastic Stack y el framework MITRE Caldera (Python). A través de una demostración guiada, analizaremos cómo simular técnicas del framework MITRE ATT&CK y cómo correlacionarlas en tiempo real con logs de sistemas Linux para detectar comportamiento malicioso."
---
