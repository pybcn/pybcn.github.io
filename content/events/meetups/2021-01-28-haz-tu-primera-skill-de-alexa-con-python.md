---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 275867843.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Haz tu primera skill de Alexa con Python"
date: 2021-01-28
year: 2021
# The export records this event as ONLINE, so it had no room.
venue: "Online"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 36
meetup_url: "https://www.meetup.com/pyladies-bcn/events/275867843/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 275867843 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: haz-tu-primera-skill-de-alexa-con-python
    title: "Haz tu primera skill de Alexa con Python"
    speakers: [elisabeth-ortega-carrasco, clara-jimenez-recio]
    type: workshop
    description: "Elisabeth Ortega-Carrasco, Field Applications Scientist / Product Owner en Lead Molecular Design, SL, nos enseñará a crear nuestra primera Skill con Python. Además, contamos con Clara Jiménez Recio, FullStack JavaScript Developer en Gamelearn, que en diciembre nos contó más sobre cómo crear una Alexa Skill.\n\nEn esta charla, que se realiza conjuntamente entre las asociaciones de PyLadiesBCN y Women In Voice Spain, os explicaremos en qué consisten las skills de Alexa, cuales son sus partes y desarrollaremos juntas una skill muy sencilla usando Python. Para asistir al evento y crear tu propia skill de Alexa, solo necesitas tener una cuenta de Amazon, ya que todo el desarrollo se realizará dentro de su misma interfaz web. Para poder sacarle el máximo partido a este evento, recomendados asistir a este evento on-line desde un ordenador en el que ver bien la pantalla (en el móvil no podrás sacarle el máximo partido)."
---
