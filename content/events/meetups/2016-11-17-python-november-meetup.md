---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 235058828.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: Python November Meetup
date: 2016-11-17
year: 2016
venue: Skyscanner
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 56
meetup_url: https://www.meetup.com/python-barcelona/events/235058828/
group: PyBCN
# The talks this meetup announced, read from the description of event 235058828 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: ajuntament-de-barcelona-inicia-el-desarrollo-de-sus-sistema
  title: Ajuntament de Barcelona inicia el desarrollo de sus sistema core-business en Python/Django
  speakers:
  - xavi-roca
  - montse-comaposada
  type: talk
  language: es
  duration_minutes: 30
  description: Ajuntament de Barcelona, bajo la dirección estratégica de la Comisionada de Tecnología e Innovación Digital, Francesca Bria, está desarrollando un plan de transformación digital orientado a cambiar el modo en que se ofrecen los servicios municipales. El plan, bautizado como AGILE DIGITAL TRANSFORMATION, incorpora entre sus ejes de trabajo un grupo de OPEN TECHNOLOGIES. Las iniciativas del plan relacionadas con código abierto y plataformas abiertas son muchas, y algunas de ellas vienen a consolidar proyectos realizados ya en Python/Django. El objetivo de la presentación es dar a conocer los proyectos ya realizados en Python, los últimos licitados, y los que próximamente se van a licitar. En resumen, queremos poner en conocimiento de la comunidad Python este giro de las TIC en el gobierno de la ciudad, y posicionarnos como un miembro activo dentro de ella.
- id: introduction-to-conda
  title: Introduction to Conda
  speakers:
  - ignasi-fosch
  type: talk
  language: en
  duration_minutes: 30
  description: This is a fairly overview and introduction to conda, the package and environment manager. This will depict what it is, its setup, how to create environments, and installing, building, and sharing packages; all these with a simple live session on Linux.
- id: plone-server-rest-api-async-framework-for-cms
  title: plone.server - REST API async framework for CMS
  type: talk
  language: en
  duration_minutes: 30
  description: On the Plone Community we have different efforts for 2020. One of them is switching from actual Zope Stack to a different backend that holds content in a ZODB, with modern technologies and python 3. Plone.server is an experiemental Framework to build Content based REST API services based on a asyncio loop and a object database called ZODB.
  speakers:
  - ramon-navarro-bosch
---
