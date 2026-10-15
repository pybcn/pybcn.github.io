---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 286896069.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyLadies Summer Edition"
date: 2022-07-07
year: 2022
venue: "Canòdrom - Ateneu d'Innovació Digital i Democràtica"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 21
meetup_url: "https://www.meetup.com/pyladies-bcn/events/286896069/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 286896069 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: my-first-gui-with-python
    title: "My first GUI with Python"
    speakers: [kimberly-aliaga]
    type: lightning
    description: "Introduction to GUI development using contact agenda as an example. Intro to Tkinter elements, where to use it, real life use examples and alternatives."
  - id: outreachy-interships-in-open-source-software
    title: "Outreachy: Interships in open source software"
    speakers: [lauryn-menard]
    type: lightning
    description: "Have you ever wanted to develop your Python skills beyond a personal project? Are you a non-traditional student looking to make a career transition to programming later in life? Do you like the idea of open source software, but don't know how to become involved in a project?\nAbout a year ago, I could answer yes to all of those questions and so I set out to find some answers."
  - id: el-mundo-del-data-es-para-todos-y-necesita-de-todos
    title: "El mundo del Data es para todos (y necesita de todos)"
    speakers: [afra-llado]
    type: lightning
    description: "El objetivo es explicar, con experiencias, la variedad de oportunidades y perfiles que hay en el sector del Data en la actualidad, a parte de los puramente informáticos o matemáticos. Además, de los diferentes productos y finalidades, se necesitan variedad de conocimientos."
  - id: biohacking-con-python-ingenieria-genetica-al-alcance-de
    title: "Biohacking con Python: ingeniería genética al alcance de cualquiera"
    speakers: [marina-moro-lopez]
    type: lightning
    description: "Introducción al biohacking seguida por una mini clase con un caso práctico que consistirá en editar nuestro propio ADN con CRISPR (una herramienta de corte y empalme biológico) y un script de Python (que diseñará las secuencias genéticas necesarias para el experimento) para biohackearnos ciertos genes y conseguir que seamos fluorescentes, tengamos el pelo azul y seamos calvas. Todo esto nos servirá para ver el tremendo potencial de la sinergia entre la ingeniería genética y Python, no sólo en ejemplos cómicos como los ya mencionados, sino también en el ámbito sanitario como tratamiento de enfermedades."
---
