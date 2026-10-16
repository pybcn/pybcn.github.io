---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 249666487.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python April Meetup"
date: 2018-04-19
year: 2018
venue: "Skyscanner"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 57
meetup_url: "https://www.meetup.com/python-barcelona/events/249666487/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 249666487 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: ttn-3-python
    title: "TTN <3 Python"
    speakers: [xose-perez]
    type: talk
    duration_minutes: 45
    description: "Des de TTNCat estem treballant per impulsar una xarxa de telemetria oberta, lliure i neutral. Volem donar a conèixer la tecnologia LoRa/LoRaWan amb la intenció de generar casos d'ús a la ciutat. És part d'un pilot que també inclou el desplegament de 15 gateways TTN a Barcelona i la realització de 2 hackatons. Existeixen solucions comercials i DIY que permeten programar dispositius IoT amb MicroPython i connectar-los a la xarxa TTN. La intenció de la xerrada serà explicar una mica què és TTN/LoRa/LoRaWan, veure algun exemple, algun hardware i convidar qui vulgui a unir-se a la comunitat."
  - id: high-altitude-python
    title: "High Altitude Python"
    speakers: [juampe-lopez]
    type: talk
    language: en
    duration_minutes: 30
    description: "We visited the stratosphere with a big helium-filled balloon and a long string of capsules that were ready to do some citizen science. The Koroliov 2 capsule featured a Raspberry Pi Zero running Linux and some sweet Python scripts that made the job easier."
---
