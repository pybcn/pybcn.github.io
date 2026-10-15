---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 268750446.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "ROS and RoboMaker: programming robots in Python"
date: 2020-02-24
year: 2020
venue: "Marfeel"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 21
meetup_url: "https://www.meetup.com/pyladies-bcn/events/268750446/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 268750446 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: ros-and-robomaker-programming-robots-in-python
    title: "ROS and RoboMaker: programming robots in Python"
    speakers: [esteve-fernandez]
    type: workshop
    description: "ROS has become the defacto framework for robotics, thanks to its opensource nature and its community. Universities, research institutions and private companies have adopted ROS for their robot products, including NASA, Amazon and Toyota. In this workshop we'll use Amazon's AWS RoboMaker to develop robot applications in Python and we'll see how to run our code in simulated comercial robots."
---
