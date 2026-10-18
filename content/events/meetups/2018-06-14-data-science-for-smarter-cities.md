---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 251511806.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyLadies BCN Workshop, June 2018"
date: 2018-06-14
year: 2018
venue: "Worldsensing"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 17
meetup_url: "https://www.meetup.com/pyladies-bcn/events/251511806/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 251511806 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: data-science-for-smarter-cities
    title: "Data science for smarter cities"
    speakers: [jamie-arjona]
    type: workshop
    language: es
    description: "\"We're entering in the megacities era. Nowadays half of the population lives in urban areas, and this proportion is expected to increase to two thirds by 2050. This new situation brings lots of new opportunities but also many challenges. Cities are already struggling to reduce commuting time, improve citizen satisfaction and optimize resources. In order to achieve these goals, gathering information about the city state is key. This workshop will explore smart cities data to get insights of how the parking behavior evolves in a European city. Using data from Worldsensing sensors we will be able to visualize and analyze the parking occupation in order to make a diagnose and improve the time spent in parking by citizens.\""
---
