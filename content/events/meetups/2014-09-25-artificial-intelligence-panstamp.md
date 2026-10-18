---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 161059272.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Artificial Intelligence & Panstamp"
date: 2014-09-25
year: 2014
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 82
meetup_url: "https://www.meetup.com/python-barcelona/events/161059272/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 161059272 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: machine-learning
    title: "Machine learning"
    speakers: [xavier-arrufat]
    type: talk
    language: en
    duration_minutes: 20
  - id: heating-solution-using-panstamp-and-python
    title: "Heating solution using panstamp and python"
    speakers: [oriol-rius]
    type: talk
    language: en
    duration_minutes: 20
  - id: application-of-dynamical-systems-in-artificial-intelligence
    title: "Application of dynamical systems in artificial intelligence"
    speakers: [bac-ko]
    type: talk
    language: en
    duration_minutes: 20
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/515188039250092032"
  items:
    - file: 2014-09-25-artificial-intelligence-panstamp/01-python-and-machine-learning-by-xavier-arrufat-pybc.webp
      caption: "Python and Machine Learning, by Xavier Arrufat #pybcn"
      source: "https://x.com/PyBCN/status/515188039250092032"
      time: "19:16"
      talk: machine-learning
    - file: 2014-09-25-artificial-intelligence-panstamp/02-heating-solution-using-panstamp-and-python-by-orio.webp
      caption: "Heating solution using Panstamp and Python, by Oriol Rius @oriolrius #pybcn"
      source: "https://x.com/PyBCN/status/515198678844596224"
      time: "19:58"
      talk: heating-solution-using-panstamp-and-python
    - file: 2014-09-25-artificial-intelligence-panstamp/03-application-of-dynamical-systems-in-artificial-int.webp
      caption: "Application of dynamical systems in Artificial Inteligence, by Bac Ko #pybcn"
      source: "https://x.com/PyBCN/status/515208025507119105"
      time: "20:35"
---
