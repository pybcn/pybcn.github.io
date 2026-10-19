---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 240703824.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python June Meetup"
date: 2017-06-15
year: 2017
venue: "Tiendeo"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 62
meetup_url: "https://www.meetup.com/python-barcelona/events/240703824/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 240703824 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: tiendeo-high-level-reporting-with-office-libraries-and
    title: "Tiendeo: high level reporting with office libraries and python"
    speakers: [antonio-escartin]
    type: talk
    language: en
    duration_minutes: 25
    description: "Brief introduction about who is tiendeo and how we use python for automation of high level reports generation, using office tools by libraries such as python-pptx and openpyxl."
  - id: deep-learning-for-signal-processing
    title: "Deep Learning for Signal Processing"
    speakers: [marius-miron]
    type: talk
    language: en
    duration_minutes: 25
    description: "Deep learning is a powerful technique for tasks as classification or recognition. However, it can be used in signal processing for tasks that need to recover the full signal like denoising or source separation. I will present my work on deep learning for music source separation, particularly some strategies for data augmentation which makes the framework more robust to variations one might expect in real-life. This research is reproducible and is accompanied by a python library which makes it easy to work with large datasets."
  - id: snakes-ladders-a-taste-of-scala-for-pythonistas
    title: "Snakes & ladders: A taste of Scala for pythonistas"
    speakers: [ruben-berenguel]
    type: talk
    language: en
    duration_minutes: 25
    description: "Scala is the language showing fastest growth in the data science and engineering field. In an area where Python is king, what is so special about Scala? In this talk I'll introduce some of the concepts and ideas that make Scala compelling, and how they relate to how we work with Python."
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/875402167921856512"
  items:
    - file: 2017-06-15-python-june-meetup/01-tiendeo-high-level-reporting-with-office-libraries.webp
      caption: "\"@Tiendeo : high level reporting with office libraries and python\" by Antonio Escartin #pybcn"
      source: "https://x.com/PyBCN/status/875402167921856512"
      time: "19:18"
      talk: tiendeo-high-level-reporting-with-office-libraries-and
    - file: 2017-06-15-python-june-meetup/02-plenty-of-good-questions-for-antonio-pybcn.webp
      caption: "Plenty of good questions for Antonio! #pybcn"
      source: "https://x.com/PyBCN/status/875405763665166337"
      time: "19:32"
    - file: 2017-06-15-python-june-meetup/03-deep-learning-for-signal-processing-by-marius-miro.webp
      caption: "\"Deep Learning for Signal Processing\", by Marius Miron #pybcn"
      source: "https://x.com/PyBCN/status/875406243837378560"
      time: "19:34"
      talk: deep-learning-for-signal-processing
    - file: 2017-06-15-python-june-meetup/04-snakes-ladders-a-taste-of-scala-for-pythonistas-by.webp
      caption: "\"Snakes & ladders: A taste of Scala for pythonistas\", by Ruben Berenguel (@berenguel) #pybcn"
      source: "https://x.com/PyBCN/status/875412321245569024"
      time: "19:58"
      talk: snakes-ladders-a-taste-of-scala-for-pythonistas
    - file: 2017-06-15-python-june-meetup/05-learn-some-scala-and-come-back-to-python-berenguel.webp
      caption: "Learn some scala, and come back to Python! - @berenguel #pybcn"
      source: "https://x.com/PyBCN/status/875417577631207424"
      time: "20:19"
    - file: 2017-06-15-python-june-meetup/06-post-meetup-networking-while-enjoying-awesome-view.webp
      caption: "Post-meetup networking, while enjoying awesome views. Thanks @Tiendeo for hosting us! #pybcn"
      source: "https://x.com/PyBCN/status/875419053090906112"
      time: "20:25"
---
