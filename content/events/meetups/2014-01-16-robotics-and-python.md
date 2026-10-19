---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 157887662.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Robotics and Python"
date: 2014-01-16
year: 2014
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 61
meetup_url: "https://www.meetup.com/python-barcelona/events/157887662/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 157887662 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: easy-gps-tracker-using-python-arduino
    title: "Easy GPS Tracker using Python & Arduino"
    speakers: [nuria-pujol-vilanova]
    type: talk
    description: "Las diferentes partes del desarrollo de un sencillo GPS Tracker nos servirán para introducir diferentes aspectos de Arduino y Python. Se hablará de Xbee, de tramas GPS, de imágenes georeferenciadas y sobretodo, sobre Python!"
  - id: el-ecosistema-ros-y-python
    title: "El ecosistema ROS y Python"
    speakers: [esteve-fernandez]
    type: talk
    description: "Introducción a los proyectos que desarrollamos en la Open Source Robotics Foundation (ROS, CloudSim y Gazebo)"
  - id: interfacing-with-ros-via-python
    title: "Interfacing with ROS via Python"
    speakers: [sam-pfeiffer]
    type: talk
    description: "Introducción al Sistema Operativo Robótico (ROS) desde el punto de vista de un desarrollador en Python en un caso real: REEM"
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/423876642587815936"
  items:
    - file: 2014-01-16-robotics-and-python/01-a-punto-de-empezar-easy-gps-tracker-using-arduino.webp
      caption: "A punto de empezar 'Easy GPS tracker using Arduino and Python' #pybcn"
      source: "https://x.com/PyBCN/status/423876642587815936"
      time: "18:57"
    - file: 2014-01-16-robotics-and-python/02-final-version-of-llevaneus-gps-tracker-using-ardui.webp
      caption: "Final version of @llevaNEUS GPS Tracker, using Arduino, QT and Python #pybcn"
      source: "https://x.com/PyBCN/status/423884976497905664"
      time: "19:30"
    - file: 2014-01-16-robotics-and-python/03-empieza-the-robot-operating-system-ecosystem-and-p.webp
      caption: "Empieza 'The Robot Operating System ecosystem and Python', por @esteve #ROS #pybcn"
      source: "https://x.com/PyBCN/status/423889253048000513"
      time: "19:47"
    - file: 2014-01-16-robotics-and-python/04-ejemplos-de-robots-que-usan-ros-pybcn.webp
      caption: "Ejemplos de robots que usan ROS #pybcn"
      source: "https://x.com/PyBCN/status/423891026680754176"
      time: "19:54"
    - file: 2014-01-16-robotics-and-python/05-y-ahora-a-real-use-case-of-ros-pybcn.webp
      caption: "Y ahora, 'A real use case of ROS' #pybcn"
      source: "https://x.com/PyBCN/status/423898372614135808"
      time: "20:23"
---
