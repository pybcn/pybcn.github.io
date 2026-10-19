---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 255576739.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyLadies BCN Workshop, October 2018"
date: 2018-10-23
year: 2018
venue: "Travelperk"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 15
meetup_url: "https://www.meetup.com/pyladies-bcn/events/255576739/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 255576739 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: introduccion-a-the-things-network
    title: "Introducción a The Things Network"
    speakers: [nuria-vega, xose-perez]
    type: workshop
    description: "El taller estará dividido en tres partes principales: presentación de la comunidad TTN en Barcelona y el piloto que están llevando a cabo; introducción a LoRa, LoRaWan y la red The Things Network; y un hands on sobre cómo crear sensores DIY con MicroPython connectados a TTN."
---
