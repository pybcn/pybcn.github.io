---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 230295390.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python April Meetup"
date: 2016-04-21
year: 2016
venue: "Skyscanner"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 56
meetup_url: "https://www.meetup.com/python-barcelona/events/230295390/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 230295390 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: ingesting-35-million-hotel-images-with-python-in-the-cloud
    title: "Ingesting 35 Million Hotel Images With Python In The Cloud"
    speakers: [alex-vinyals]
    type: talk
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=2VP2d_Ukj3E"
  - id: introduction-to-testing-and-py-test
    title: "Introduction to testing and py.test"
    speakers: [ignasi-fosch]
    type: talk
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=QIy-XGTP4WM"
  - id: comprehensions-in-5-min
    title: "Comprehensions in 5 min"
    speakers: [jordi-soucheiron]
    type: lightning
    duration_minutes: 5
  - id: bots-are-the-new-hype-long-life-to-slackbot
    title: "Bots are the new hype. Long life to slackbot"
    speakers: [gabriel-de-maeztu]
    type: lightning
    duration_minutes: 5
  - id: accloudtant-tool-for-managing-aws-costs
    title: "Accloudtant - tool for managing AWS costs"
    speakers: [ignasi-fosch]
    type: lightning
    duration_minutes: 5
# A recording of a whole session of this meetup and not of one talk: a
# block of lightning talks, or the introduction of the evening, has no
# talk record for a video to sit on, so the video sits on the event.
# bin/import-videos writes this block from the YouTube export of the
# pybcn-archive: a correction goes to the export or to the script, never
# here. The page prints these under a Recordings heading, after the talks
# (partials/session_videos.html). Not "videos": Hugo reads that key
# as a list of og:video URLs, and a list of records there stops the build.
session_videos:
  - title: "Lightning Talk Session"
    url: "https://www.youtube.com/watch?v=R3R9q5mf8Uw"
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/723196695870377984"
  items:
    - file: 2016-04-21-python-april-meetup/01-ingesting-35-million-hotel-images-with-python-in-t.webp
      caption: "Ingesting 35 Million Hotel Images With Python In The Cloud, by Alex Vinyals (@alevinval) #pybcn"
      source: "https://x.com/PyBCN/status/723196695870377984"
      time: "19:08"
      talk: ingesting-35-million-hotel-images-with-python-in-the-cloud
    - file: 2016-04-21-python-april-meetup/02-introduction-to-testing-and-py-test-by-ignasi-fosc.webp
      caption: "Introduction to testing and py.test, by Ignasi Fosch (@ifosch) #pybcn"
      source: "https://x.com/PyBCN/status/723203784336388096"
      time: "19:36"
      talk: introduction-to-testing-and-py-test
    - file: 2016-04-21-python-april-meetup/03-bots-are-the-new-hype-long-life-to-slackbot-by-gab.webp
      caption: "Bots are the new hype. Long life to slackbot, by Gabriel de Maeztu (@gabimaeztu) #pybcn #santi"
      source: "https://x.com/PyBCN/status/723215165223755776"
      time: "20:21"
      talk: bots-are-the-new-hype-long-life-to-slackbot
    - file: 2016-04-21-python-april-meetup/04-accloudtant-tool-for-managing-aws-costs-by-ignasi.webp
      caption: "Accloudtant - tool for managing AWS costs, by Ignasi Fosch (@ifosch): https://github.com/ifosch/accloudtant #pybcn"
      source: "https://x.com/PyBCN/status/723217460896382976"
      time: "20:30"
      talk: accloudtant-tool-for-managing-aws-costs
    - file: 2016-04-21-python-april-meetup/05-comprehensions-in-5-min-by-jordi-soucheiron-jordix.webp
      caption: "Comprehensions in 5 min, by Jordi Soucheiron (@jordixou) #pybcn"
      source: "https://x.com/PyBCN/status/723219991227707392"
      time: "20:40"
      talk: comprehensions-in-5-min

---
