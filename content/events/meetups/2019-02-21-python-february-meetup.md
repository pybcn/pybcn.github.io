---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 258998028.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python February Meetup"
date: 2019-02-21
year: 2019
venue: "Skyscanner"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 61
meetup_url: "https://www.meetup.com/python-barcelona/events/258998028/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 258998028 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: repository-templates-with-cookiecutter
    title: "Repository templates with Cookiecutter"
    speakers: [hector-canto]
    type: talk
    language: es
    duration_minutes: 30
    description: "\"Starting a new project is always cumbersome, specially if you collaborate with others: you have to follow standards and agreements, there are some mandatory files, deploy artifacts and requirements that should be in a certain place etc. We will see how to create a repository template, talk about some standards you may follow and how to use Cookiecutter to initialize your project in a few seconds. We will also comment some CLI tools to help you maintain your repository up to date, with a special focus on how to easily handle environment variables.\""
  - id: recursive-generators
    title: "Recursive generators"
    speakers: [joan-vilaltella]
    type: talk
    language: en
    duration_minutes: 30
    description: "\"Recursive calls and generators are two well-known programming concepts. They can be easily combined in Python, with interesting results. The generator version of a tail-recursive function is good in terms of memory use, with a possible (usually acceptable) drawback in terms of speed.\""
  - id: pipenv-nuevo-sistema-de-gestion-de-dependencias-de-paquetes
    title: "Pipenv: nuevo sistema de gestión de dependencias de paquetes para Python"
    speakers: [andreu-vallbona-plazas]
    type: talk
    language: es
    duration_minutes: 30
    description: "\"Pipenv, creado por Kenneth Reitz hace poco más de un año, se ha convertido en el recurso oficial recomendado por Python para administrar dependencias de paquetes. Pero todavía hay confusión sobre qué problemas resuelve y cómo es más útil que el flujo de trabajo estándar usando pip y un archivo requirements.txt. En esta charla se intentará explicar la solución a dichos problemas.\""
---
