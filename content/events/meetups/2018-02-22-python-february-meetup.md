---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 247800240.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python February Meetup"
date: 2018-02-22
year: 2018
venue: "Worldsensing"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 43
meetup_url: "https://www.meetup.com/python-barcelona/events/247800240/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 247800240 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: using-python-for-everything-pyot
    title: "Using Python for everything (PyoT)"
    type: talk
    language: en
    duration_minutes: 30
    description: "How Worldsensing uses Python for their IoT chain: hardware design, embedded code, communication, software, infrastructure, and data analytics."
  - id: addressing-a-hard-graph-colouring-problem-in-python
    title: "Addressing a hard graph colouring problem in Python"
    speakers: [joan-vilaltella]
    type: talk
    language: en
    duration_minutes: 20
    description: "Graph edge colouring has many applications (scheduling, frequency assignment) but is widely believed to be computationally hard, even for graphs where each vertex has three neighbours (cubic graphs). In such difficult cases, heuristic algorithms are justified and may be empirically efficient in many specific instances. A simplified heuristic algorithm published by Fiol and Vilaltella in 2013 is reasonably fast on random graphs and also on many structured graphs. The Python language allows a clear and concise implementation of the algorithm."
  - id: do-we-need-a-serverless-framework-with-python-i-didn-t
    title: "Do we need a serverless framework? With Python, I didn't"
    speakers: [cristobal-garcia]
    type: talk
    language: en
    duration_minutes: 40
    description: "These days, a number of frameworks to deploy FaaS based services have appeared. The purpose of this talk is to demonstrate that it is perfectly possible (and even in some cases even advisable) to deploy a manageable application without adding the additional complexity and risks that opinionated dependencies add to our software systems."
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/966738901145661443"
  items:
    - file: 2018-02-22-python-february-meetup/03-about-to-start-today-s-meetup-pybcn.webp
      caption: "About to start today's meetup! #PyBCN"
      source: "https://x.com/PyBCN/status/966737392609656843"
      time: "19:12"
    - file: 2018-02-22-python-february-meetup/04-first-meetup-at-worldsensing-is-starting.webp
      caption: "First meetup at @Worldsensing is starting"
      source: "https://x.com/PyBCN/status/966738066948927488"
      time: "19:14"
    - file: 2018-02-22-python-february-meetup/01-using-python-for-everything-pyot-by-the-worldsensi.webp
      caption: "\"Using Python for everything (PyoT)\", by the @Worldsensing team #PyBCN"
      source: "https://x.com/PyBCN/status/966738901145661443"
      time: "19:18"
      talk: using-python-for-everything-pyot
    - file: 2018-02-22-python-february-meetup/05-no-no-no-problem.webp
      caption: "No ; No {} No Problem"
      source: "https://x.com/PyBCN/status/966739895090864134"
      time: "19:22"
    - file: 2018-02-22-python-february-meetup/02-addressing-a-hard-graph-colouring-problem-in-pytho.webp
      caption: "\"Addressing a hard graph colouring problem in Python\", by Joan Vilaltella (@joanvilaltella) #PyBCN"
      source: "https://x.com/PyBCN/status/966745972289212422"
      time: "19:46"
      talk: addressing-a-hard-graph-colouring-problem-in-python
    - file: 2018-02-22-python-february-meetup/06-do-we-need-a-serverless-framework-with-python-i-di.webp
      caption: "\"Do we need a serverless framework? With Python, I did not\", by Cristóbal García (@xtblg) #PyBCN"
      source: "https://x.com/PyBCN/status/966754057133215744"
      time: "20:18"
---
