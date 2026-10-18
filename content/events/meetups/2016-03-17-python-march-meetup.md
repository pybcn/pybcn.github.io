---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 229156441.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: Python March Meetup
date: 2016-03-17
year: 2016
venue: Skyscanner
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 57
meetup_url: https://www.meetup.com/python-barcelona/events/229156441/
group: PyBCN
# The talks this meetup announced, read from the description of event 229156441 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: piggybacking-trello-for-automatic-student-assessment
  title: Piggybacking Trello for automatic student assessment
  speakers:
  - jordi-saludes
  type: talk
- id: computational-complexity-in-python
  title: Computational complexity in Python
  speakers:
  - jordi-soucheiron
  type: talk
  links:
  - type: video
    url: https://www.youtube.com/watch?v=Tppi9Fsiwp4
- id: sklearn-pandas-streamline-your-model-building-process
  title: 'sklearn-pandas: streamline your model building process'
  type: talk
  links:
  - type: video
    url: https://www.youtube.com/watch?v=3V1AEXT3PrI
  speakers:
  - israel-saeta-perez
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/710528772924153856"
  items:
    - file: 2016-03-17-python-march-meetup/01-piggybacking-trello-for-automatic-student-assessme.webp
      caption: "Piggybacking Trello for automatic student assessment, by Jordi Saludes (@jsaludes) #pybcn"
      source: "https://x.com/PyBCN/status/710528772924153856"
      time: "19:10"
      talk: piggybacking-trello-for-automatic-student-assessment
    - file: 2016-03-17-python-march-meetup/02-computational-complexity-in-python-by-jordi-souche.webp
      caption: "Computational complexity in Python, by Jordi Soucheiron (@jordixou) #pybcn"
      source: "https://x.com/PyBCN/status/710536419798859776"
      time: "19:40"
      talk: computational-complexity-in-python
    - file: 2016-03-17-python-march-meetup/03-sklearn-pandas-streamline-your-model-building-proc.webp
      caption: "sklearn-pandas: streamline your model building process, by Israel Saeta (@dukebody) #pybcn"
      source: "https://x.com/PyBCN/status/710548634962632706"
      time: "20:29"
      talk: sklearn-pandas-streamline-your-model-building-process
    - file: 2016-03-17-python-march-meetup/04-photo.webp
      caption: "A slide of the talk: the scikit-learn logo, a broken heart, and a panda, with the note \"improved in sklearn>=0.16!\""
      source: "https://x.com/PyBCN/status/710550278043508737"
      time: "20:36"
---
