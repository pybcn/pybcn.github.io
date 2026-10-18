---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 277660064.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyLadies BCN Workshop, April 2021"
date: 2021-04-27
year: 2021
# The export records this event as ONLINE, so it had no room.
venue: "Online"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 11
meetup_url: "https://www.meetup.com/pyladies-bcn/events/277660064/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 277660064 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: get-rid-of-matlab-struggling-process-from-matlab-to-python
    title: "Get rid of Matlab! (struggling process from Matlab to Python)"
    speakers: [anna-mujal-colilles]
    type: talk
    language: [en, es]
    description: "After a long mental process I decided to switch from Matlab to Python to process my data. First, I had to decide the platform (IDLE, Spyder, Jupyter Notebook) and I chose one, but I changed after some time.\n\nThen, I started by trying to open a txt file and I spend one entire month to do so (I did not know about the libraries). After all, I am glad I took this decision, but there are still many things to learn yet. Pyhton community is lovelly and there is many work already done.\n\nThe session would consist on explaining my struggling process and exchange ideas on how to optimize it for someone else."
---
