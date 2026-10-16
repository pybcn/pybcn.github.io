---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 256504042.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python November Meetup"
date: 2018-11-21
year: 2018
venue: "Travelperk"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 49
meetup_url: "https://www.meetup.com/python-barcelona/events/256504042/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 256504042 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: python-in-metal-additive-manufacturing-industrial-robotics
    title: "Python in metal additive manufacturing: Industrial Robotics"
    speakers: [horacio-canales]
    type: talk
    language: en
    duration_minutes: 30
    description: "Industrial robots are usually programmed using their own proprietary language depending on the manufacturer. As a result, the ecosystem around these languages and the code interchangeability between robots its limited. In this presentation, we will talk about how to overcome these limitations using Python and RoboDK for applications in the metal additive manufacturing industry. As well, we will talk about how Python is used for the development of new manufacturing processes where simulation, data analysis, machine learning and data visualisation play an important role."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=j0z7GJW0EMA"
  - id: time-series-regression-with-deep-neural-networks
    title: "Time-series regression with deep neural networks"
    speakers: [simone-totaro]
    type: talk
    language: en
    duration_minutes: 30
    description: "Recent progress in real-valued time-series crush the state-of-the-art of autoregressive models in many domains like neuroscience, stock markets and energy. I collected some of the most interesting models, like seq2seq, neural processes and GANs to make the research more accessible. During the talk we will walk trough to the challenges of real-valued time-series regression, the models that are currently used in state-of-the-art research and their novelties. Finally we will code a simple simple use case about price forecasting for cryptocurrencies."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=g2kggih_7-A"
---
