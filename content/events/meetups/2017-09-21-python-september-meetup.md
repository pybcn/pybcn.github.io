---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 242822182.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python September Meetup"
date: 2017-09-21
year: 2017
venue: "Tiendeo"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 62
meetup_url: "https://www.meetup.com/python-barcelona/events/242822182/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 242822182 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: python-for-robotics-a-quick-introduction-to-rospy
    title: "Python for robotics: a quick introduction to rospy"
    speakers: [juan-pedro-lopez]
    type: talk
    language: en
    duration_minutes: 30
    description: "ROS leads the most innovating developments in the world of robotics, both in the area of academic research and in the developments made by the private sector in what has been called Industry 4.0. Rospy is the Python client library that will allow pythonistas and roboticists to quickly prototype and test their algorithms, letting them take advantage of the wonderful availability of Python modules for Computer Vision, Machine Learning, etc."
  - id: fun-with-python-and-c
    title: "Fun with Python and C++"
    speakers: [jordi-montes]
    type: talk
    language: en
    duration_minutes: 30
    description: "ctypes is a foreign function library for Python. It provides C compatible data types, and allows calling functions from shared libraries. In this talk we will discuss how ctypes can be used to wrap C and C++ libraries in pure Python and when, if ever, is a good idea to do that."
  - id: tiendeo-geotracking-from-online-to-store
    title: "Tiendeo Geotracking: From Online to Store"
    speakers: [ernest-carbonell]
    type: talk
    language: en
    duration_minutes: 30
    description: "Geotracking is a tool developed by Tiendeo that measures the impact of digital campaings in the real world andallow companies to get a better picture of their customers. Based in python, Tiendeo Geotracking is an analysis tool that combines data from multiples sources (geolocation, product-based information) mixed with in-house developed algorithms in order to obtain valuable KPI'S from big data."
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/910917280695033856"
  items:
    - file: 2017-09-21-python-september-meetup/07-about-to-start-september-s-python-meetup-at-tiende.webp
      caption: "About to start September's Python Meetup at @Tiendeo!"
      source: "https://x.com/PyBCN/status/910915174718164993"
      time: "19:14"
    - file: 2017-09-21-python-september-meetup/01-python-for-robotics-a-quick-introduction-to-rospy.webp
      caption: "Python for robotics: a quick introduction to rospy, by @jotape #pybcn"
      source: "https://x.com/PyBCN/status/910917280695033856"
      time: "19:22"
      talk: python-for-robotics-a-quick-introduction-to-rospy
    - file: 2017-09-21-python-september-meetup/02-demo-face-detection-with-rospy.webp
      caption: "Demo: face detection with rospy"
      source: "https://x.com/PyBCN/status/910920907048222720"
      time: "19:37"
    - file: 2017-09-21-python-september-meetup/03-fun-with-python-and-c-by-jomsdev-pybcn.webp
      caption: "Fun with Python and C++, by @jomsdev #pybcn"
      source: "https://x.com/PyBCN/status/910923502923939841"
      time: "19:47"
      talk: fun-with-python-and-c
    - file: 2017-09-21-python-september-meetup/04-live-demo.webp
      caption: "Live demo!"
      source: "https://x.com/PyBCN/status/910930108730499072"
      time: "20:13"
    - file: 2017-09-21-python-september-meetup/05-tiendeo-geotracking-from-online-to-store-by-ernest.webp
      caption: "Tiendeo Geotracking: From Online to Store, by Ernest Carbonell from @Tiendeo #pybcn"
      source: "https://x.com/PyBCN/status/910931864914939906"
      time: "20:20"
      talk: tiendeo-geotracking-from-online-to-store
    - file: 2017-09-21-python-september-meetup/06-lets-manage-lots-of-pickles-rick.webp
      caption: "Lets manage lots of pickles! #Rick"
      source: "https://x.com/PyBCN/status/910935135859683333"
      time: "20:33"
---
