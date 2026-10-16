---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 270692295.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyBCN Online: Impact of the COVID-19 pandemic in the IT labor market"
date: 2020-05-20
year: 2020
# The export records this event as ONLINE, so it had no room.
venue: "Online"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 120
meetup_url: "https://www.meetup.com/python-barcelona/events/270692295/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 270692295 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: impact-of-the-covid-19-pandemic-in-the-it-labor-market
    title: "Impact of the COVID-19 pandemic in the IT labor market"
    speakers: [dani-martos]
    type: talk
    language: en
    description: "Dani Martos, Recruitment Manager at Travelperk and member of PyBCN, will share with us some insights about the present and future changes in the labour due the Covid-19 pandemic."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=UhNQRmAUJj0"
---
