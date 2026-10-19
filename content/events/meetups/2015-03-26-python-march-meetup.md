---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 221215929.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python March Meetup"
date: 2015-03-26
year: 2015
venue: "itnig"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 64
meetup_url: "https://www.meetup.com/python-barcelona/events/221215929/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 221215929 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: spark-ipython
    title: "Spark + iPython"
    speakers: [guillermo-blasco-jimenez]
    type: talk
    duration_minutes: 40
  - id: concurrency-in-python
    title: "Concurrency in Python"
    speakers: [aitor-guevara]
    type: talk
    duration_minutes: 40
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/581173303932518400"
  items:
    - file: 2015-03-26-python-march-meetup/01-spark-ipython-by-guillermo-blasco-theblackboxio-at.webp
      caption: "Spark + iPython, by Guillermo Blasco (@theblackboxio) at @itnig #pybcn"
      source: "https://x.com/PyBCN/status/581156478972751873"
      time: "19:11"
      talk: spark-ipython
    - file: 2015-03-26-python-march-meetup/02-spark-ipython-why-pybcn.webp
      caption: "Spark + ipython, why? #pybcn"
      source: "https://x.com/PyBCN/status/581158394972733440"
      time: "19:18"
      talk: spark-ipython
    - file: 2015-03-26-python-march-meetup/03-networking-at-the-python-barcelona-meetup-at-itnig.webp
      caption: "Networking at the Python Barcelona Meetup at @itnig, thanks to @EstrellaDammCat :) #pybcn"
      source: "https://x.com/PyBCN/status/581172700883845120"
      time: "20:15"
    - file: 2015-03-26-python-march-meetup/01-concurrency-in-python-by-aitor-guevara-aitorciki-a.webp
      caption: "Concurrency in Python, by Aitor Guevara (@aitorciki) at @itnig #pybcn"
      source: "https://x.com/PyBCN/status/581173303932518400"
      time: "20:18"
      talk: concurrency-in-python
    - file: 2015-03-26-python-march-meetup/04-finally-asyncio-for-python-3-aitorciki-at-itnig-py.webp
      caption: "Finally, asyncio for Python 3 - @aitorciki at @itnig #pybcn"
      source: "https://x.com/PyBCN/status/581183553096060928"
      time: "20:58"
---
