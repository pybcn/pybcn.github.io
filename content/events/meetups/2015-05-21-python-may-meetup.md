---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 222342448.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python May Meetup"
date: 2015-05-21
year: 2015
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 63
meetup_url: "https://www.meetup.com/python-barcelona/events/222342448/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 222342448 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: python-decorators
    title: "Python Decorators"
    speakers: [guillermo-blasco-jimenez]
    type: talk
    duration_minutes: 40
  - id: python-for-data-analysis
    title: "Python for Data Analysis"
    speakers: [juan-ramon-gonzalez-vallinas]
    type: talk
    duration_minutes: 40
  - id: machine-learning-with-scikit-learn
    title: "Machine Learning with scikit-learn"
    speakers: [christopher-bonnett]
    type: talk
    duration_minutes: 30
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/601436263019782144"
  items:
    - file: 2015-05-21-python-may-meetup/04-empezando-el-barcelona-python-meetup-de-mayo-pybcn.webp
      caption: "Empezando el Barcelona Python Meetup de Mayo #pybcn"
      source: "https://x.com/PyBCN/status/601435871280177152"
      time: "19:14"
    - file: 2015-05-21-python-may-meetup/01-python-decorators-by-guillermo-blasco-theblackboxi.webp
      caption: "Python Decorators, by Guillermo Blasco (@theblackboxio) #pybcn"
      source: "https://x.com/PyBCN/status/601436263019782144"
      time: "19:15"
      talk: python-decorators
    - file: 2015-05-21-python-may-meetup/02-python-for-data-analysis-by-juan-gonzales-vallinas.webp
      caption: "Python for Data Analysis, by Juan Gonzales-Vallinas #pybcn"
      source: "https://x.com/PyBCN/status/601447469210214401"
      time: "20:00"
      talk: python-for-data-analysis
    - file: 2015-05-21-python-may-meetup/03-machine-learning-with-scikit-learn-by-christopher.webp
      caption: "Machine Learning with scikit-learn, by Christopher Bonnett (@cbonnett) #pybcn"
      source: "https://x.com/PyBCN/status/601453857508438016"
      time: "20:25"
      talk: machine-learning-with-scikit-learn
---
