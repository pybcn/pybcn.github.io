---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 278238384.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyLadies BCN Workshop, May 2021"
date: 2021-05-25
year: 2021
# The export records this event as ONLINE, so it had no room.
venue: "Online"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 30
meetup_url: "https://www.meetup.com/pyladies-bcn/events/278238384/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 278238384 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: home-and-cleaning-automation-with-microcontrollers-and
    title: "Home and cleaning automation with Microcontrollers and CircuitPython"
    speakers: [maria-jose-molina]
    type: workshop
    language: [en, es]
    description: "For many years, people have been filling their home with devices that are based on Microcontrollers, like virtual assistants, smart fridges, washing machines, security systems, and many others that can be either programmable, or even replicated with a couple of boards and our Python knowledge.\n\nDuring this activity, we will start exploring CircuitPython without the need of a physical device, using a microcontroller emulator. If you are new to the microcontroller world, don't worry, we will have an introduction to the main concepts, so we have the base knowledge to start doing little experiments by ourselves.\n\nAfter the introduction, you will be able to start programming microcontrollers using the emulator, and later you will see a couple of real projects (with real devices!) that could easily be replicated by yourself: a movement-detector, a low-cost robot cleaner, and a plant watering and monitoring system."
    links:
      - type: github
        url: "https://github.com/mjmolina/pyladiesBCN_circuitpython_workshop/blob/master/installation.md"
      - type: github
        url: "https://github.com/mjmolina/pyladiesBCN_circuitpython_workshop/blob/master/using_simulator.md"
---
