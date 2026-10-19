---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 228851626.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python February Meetup"
date: 2016-02-18
year: 2016
venue: "Skyscanner"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 65
meetup_url: "https://www.meetup.com/python-barcelona/events/228851626/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 228851626 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: bokeh-from-zero-to-contributor
    title: "Bokeh: from zero to contributor"
    speakers: [gabriel-de-maeztu]
    type: talk
  - id: life-coding-packaging-deploying-and-running-a-dummy
    title: "Life coding, packaging, deploying and running a dummy microservice with Python and Docker"
    speakers: [javier-arias-losada]
    type: talk
  - id: django-channels-beyond-request-and-response
    title: "Django Channels: beyond request and response"
    speakers: [aitor-guevara]
    type: talk
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/700382389114183681"
  items:
    - file: 2016-02-18-python-february-meetup/01-our-first-speaker-gabimaeztu-speaking-about-bokeh.webp
      caption: "Our first speaker! @gabimaeztu speaking about Bokeh! \"Bokeh: from zero to contributor\""
      source: "https://x.com/PyBCN/status/700382389114183681"
      time: "19:12"
      talk: bokeh-from-zero-to-contributor
    - file: 2016-02-18-python-february-meetup/03-amazing-brain-connections-represented-using-bokeh.webp
      caption: "Amazing brain connections represented using Bokeh! Thanks @gabimaeztu for coming! #pybcn"
      source: "https://x.com/PyBCN/status/700385590571827200"
      time: "19:25"
    - file: 2016-02-18-python-february-meetup/02-now-life-coding-packaging-deploying-and-running-a.webp
      caption: "Now \"Life coding, packaging, deploying and running a dummy microservice with Python and Docker\" turn! @javier_arilos"
      source: "https://x.com/PyBCN/status/700387960420696064"
      time: "19:34"
      talk: life-coding-packaging-deploying-and-running-a-dummy
    - file: 2016-02-18-python-february-meetup/04-last-questions-to-aitorciki-nice-to-have-you-again.webp
      caption: "Last questions to @aitorciki. Nice to have you again in #pybcn. Thanks!"
      source: "https://x.com/PyBCN/status/700409478294929408"
      time: "21:00"
---
