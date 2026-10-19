---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 300940146.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup May: Computer vision and A/B Testing"
date: 2024-05-23
year: 2024
venue: "Aticco Bogatell - Coworking en Poblenou"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 82
meetup_url: "https://www.meetup.com/python-barcelona/events/300940146/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 300940146 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: using-opencv-in-ai-practical-image-processing-in-python
    title: "Using OpenCV in AI: Practical Image Processing in Python"
    speakers: [paula-oses]
    type: talk
    language: en
    duration_minutes: 30
    description: "This talk focuses on the practical use of OpenCV in the field of artificial intelligence, particularly for Python users. The session will cover the essentials of OpenCV, including basic image operations and advanced preprocessing techniques vital for preparing data for AI models. As an AI Engineer I have used the OpenCV library since my years at university, I have prepared lots of datasets for AI models using this library as well as explored its capabilities in terms of Computer Vision models."
  - id: cluster-experiments-a-simulation-library-to-design-ab-tests
    title: "cluster-experiments, a simulation library to design AB tests"
    speakers: [david-masip]
    type: talk
    language: en
    duration_minutes: 45
    description: "Cluster-experiments is an open-source library that is used at Glovo to design AB tests (assess experiment length, AA tests, etc). We use a simulation approach which can accommodate different types of tests, being more general than what more popular libraries provide."
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/1793686859220193609"
  items:
    - file: 2024-05-23-python-meetup-may-computer-vision-and-a-b-testing/01-welcome-to-python-meetup-may-computer-vision-and-a.webp
      caption: "Welcome to Python Meetup May: Computer vision and A/B Testing https://www.meetup.com/python-barcelona/events/300940146/ Full room!"
      source: "https://x.com/PyBCN/status/1793686859220193609"
      time: "18:54"
    - file: 2024-05-23-python-meetup-may-computer-vision-and-a-b-testing/02-using-opencv-in-ai-practical-image-processing-in-p.webp
      caption: "\"Using OpenCV in AI: Practical Image Processing in Python\", by Paula Osés"
      source: "https://x.com/PyBCN/status/1793687768687902832"
      time: "18:57"
      talk: using-opencv-in-ai-practical-image-processing-in-python
    - file: 2024-05-23-python-meetup-may-computer-vision-and-a-b-testing/03-what-s-more-practical-that-looking-at-the-source-c.webp
      caption: "What's more practical that looking at the source code?"
      source: "https://x.com/PyBCN/status/1793689248605819163"
      time: "19:03"
    - file: 2024-05-23-python-meetup-may-computer-vision-and-a-b-testing/04-cluster-experiments-a-simulation-library-to-design.webp
      caption: "\"cluster-experiments, a simulation library to design AB tests\", by David Masip"
      source: "https://x.com/PyBCN/status/1793694454232293428"
      time: "19:24"
      talk: cluster-experiments-a-simulation-library-to-design-ab-tests
    - file: 2024-05-23-python-meetup-may-computer-vision-and-a-b-testing/05-hello-world.webp
      caption: "Hello world!"
      source: "https://x.com/PyBCN/status/1793697976386510946"
      time: "19:38"

---
