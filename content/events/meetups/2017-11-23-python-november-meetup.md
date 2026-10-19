---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 245182869.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python November Meetup"
date: 2017-11-23
year: 2017
venue: "Travelperk"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 57
meetup_url: "https://www.meetup.com/python-barcelona/events/245182869/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 245182869 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: websockets-and-chatbots
    title: "Websockets and chatbots"
    speakers: [carlos-fenollosa]
    type: talk
    language: en
    duration_minutes: 20
    description: "Websockets are persistent, lightweight connections to send and receive data from a web browser to a web application without constantly performing AJAX queries. An excellent use case for websockets are chatbots, since they send bidirectional data. In this talk we will show how to program a simple websocket server to interact with a basic chatbot"
  - id: cffi-interfacing-c-libraries-using-python
    title: "cffi: Interfacing C libraries using Python"
    speakers: [gerard-marull-paretas]
    type: talk
    language: en
    duration_minutes: 40
    description: "cffi is a foreign function library for Python. It is an alternative to the popular ctypes to interface C libraries. cffi offers much more possibilities than ctypes. In the presentation a brief introduction to cffi will be given together with a ctypes comparison and some real examples showing the power of cffi."
  - id: continuous-deployment-of-web-applications-the-travelperk
    title: "Continuous deployment of Web Applications: The TravelPerk example"
    speakers: [dave-garcia]
    type: talk
    language: en
    duration_minutes: 30
    description: "In TravelPerk, we have achieved the continuous deployment of our current application stack. In this talk we will explain and show how we achieved it, the challenges we faced and the tools we have used. Also we will show possible alternatives to our current implementation."
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/933759562452230149"
  items:
    - file: 2017-11-23-python-november-meetup/01-websockets-and-chatbots-by-cfenollosa-pybcn.webp
      caption: "Websockets and chatbots, by @cfenollosa #pybcn"
      source: "https://x.com/PyBCN/status/933759562452230149"
      time: "19:10"
      talk: websockets-and-chatbots
    - file: 2017-11-23-python-november-meetup/02-cffi-interfacing-c-libraries-using-python-by-gerar.webp
      caption: "cffi: Interfacing C libraries using Python, by Gerard Marull #pybcn"
      source: "https://x.com/PyBCN/status/933768251255001088"
      time: "19:44"
      talk: cffi-interfacing-c-libraries-using-python
    - file: 2017-11-23-python-november-meetup/03-continuous-deployment-of-web-applications-the-trav.webp
      caption: "Continuous deployment of Web Applications: The @TravelPerk example, by Dave García #pybcn"
      source: "https://x.com/PyBCN/status/933776911855210496"
      time: "20:18"
      talk: continuous-deployment-of-web-applications-the-travelperk

---
