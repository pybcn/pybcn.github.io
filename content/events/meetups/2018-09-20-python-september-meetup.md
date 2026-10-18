---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 254683829.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python September Meetup"
date: 2018-09-20
year: 2018
venue: "Skyscanner"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 69
meetup_url: "https://www.meetup.com/python-barcelona/events/254683829/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 254683829 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: deep-learning-for-time-series
    title: "Deep learning for time series"
    speakers: [alexander-honchar]
    type: talk
    language: en
    duration_minutes: 60
    description: "10 years ago software was eating the world, today AI is eating the software. Machine learning is developing extremely quickly, especially such fields as computer vision, natural language processing, business oriented fields as recommendation systems and many others. In shadow of hyped areas like computer vision and NLP we can forget about another important source of data - signals, or time series. In this talk I want to review the world of applications of time series analysis (since application areas are not very known to the broad audience), discuss previous approaches (let's call it \"pre-deep-learning era\") and share my experience in using deep neural networks in bio signal analysis and financial forecasting. Apart of best practices I'll show some important research paths that potentially can solve any time series related problems in the future."
  - id: microservices-at-scale
    title: "Microservices at scale"
    speakers: [jordi-soucheiron]
    type: talk
    language: en
    duration_minutes: 30
    description: "In Skyscanner we operate hundreds of services and perform thousands of deploys a day. In this talk I'll try to cover what have we put in place to empower our team so we can focus on solving traveler problems."
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/1042824805202972672"
  items:
    - file: 2018-09-20-python-september-meetup/04-full-venue-at-today-s-meetup-thanks-skyscanner-for.webp
      caption: "Full venue at today's Meetup. Thanks Skyscanner for hosting us! #pybcn"
      source: "https://x.com/PyBCN/status/1042824484896616448"
      time: "19:15"
    - file: 2018-09-20-python-september-meetup/01-deep-learning-for-time-series-by-alexander-honchar.webp
      caption: "Deep learning for time series, by Alexander Honchar (@alexrachnog) #pybcn"
      source: "https://x.com/PyBCN/status/1042824805202972672"
      time: "19:16"
      talk: deep-learning-for-time-series
    - file: 2018-09-20-python-september-meetup/02-classical-approaches.webp
      caption: "Classical approaches..."
      source: "https://x.com/PyBCN/status/1042827545819930624"
      time: "19:27"
    - file: 2018-09-20-python-september-meetup/03-microservices-at-scale-by-jordi-soucheiron-jordixo.webp
      caption: "Microservices at scale, by Jordi Soucheiron (@jordixou) #pybcn Slides: https://docs.google.com/presentation/d/1rtTkhtdzJflTTZYJaJ_zJ3u56T8nVBNLTpA9wL8tVm4/edit"
      source: "https://x.com/PyBCN/status/1042842561164062721"
      time: "20:26"
      talk: microservices-at-scale
---
