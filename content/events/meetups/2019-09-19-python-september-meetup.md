---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 264597651.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python September Meetup"
date: 2019-09-19
year: 2019
venue: "BitPhy"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 48
meetup_url: "https://www.meetup.com/python-barcelona/events/264597651/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 264597651 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: data-quality-and-how-we-are-trying-to-break-the-80-20
    title: "Data Quality and how we are trying to break the 80/20 cleaning rule"
    speakers: [ana-dorofei]
    type: talk
    language: en
    duration_minutes: 30
    description: "We have all heard data scientists spend only about 20% of their precious time developing algorithms and building machine learning models. Let's look a bit into the less sexy aspect of Data Science which takes 80% of our time - cleaning and organizing the data - and a couple of ideas towards automating it with Python."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=b8s8a71AYd8"
  - id: python-for-the-management-of-iot-platforms-at-worldsensing
    title: "Python for the management of IoT platforms at Worldsensing"
    speakers: [toni-martinez-del-hoyo]
    type: talk
    language: en
    duration_minutes: 30
    description: "Overview on the tech stack and architecture at the Innovation department of Worldsensing to bridge the gap between our IoT sensors and our data monitoring application."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=JzX9WAv7PVM"
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/1174736672845705216"
  items:
    - file: 2019-09-19-python-september-meetup/05-welcome-to-python-barcelona-by-nataliasirera.webp
      caption: "Welcome to Python Barcelona, by @nataliasirera"
      source: "https://x.com/PyBCN/status/1174735529469984769"
      time: "19:22"
    - file: 2019-09-19-python-september-meetup/06-come-to-the-pydaybcn-send-proposals-join-us-at-the.webp
      caption: "Come to the #PyDayBCN! Send proposals! Join us at the mentoring session! by @DZPM"
      source: "https://x.com/PyBCN/status/1174736115816943616"
      time: "19:24"
    - file: 2019-09-19-python-september-meetup/01-data-quality-and-how-we-are-trying-to-break-the-80.webp
      caption: "\"Data Quality and how we are trying to break the 80/20 cleaning rule\" by Ana Dorofei"
      source: "https://x.com/PyBCN/status/1174736672845705216"
      time: "19:27"
      talk: data-quality-and-how-we-are-trying-to-break-the-80-20
    - file: 2019-09-19-python-september-meetup/02-there-is-one-way-to-do-it-right-and-many-ways-to-m.webp
      caption: "\"There is one way to do it right, and many ways to mess it up\" - Alberto Cámara"
      source: "https://x.com/PyBCN/status/1174742270429585409"
      time: "19:49"
    - file: 2019-09-19-python-september-meetup/03-it-started-as-fiction-and-now-it-seems-to-be-scien.webp
      caption: "\"It started as fiction, and now it seems to be science fiction. Let's see which word we keep\" - Sergi Ortiz"
      source: "https://x.com/PyBCN/status/1174742700312137730"
      time: "19:51"
    - file: 2019-09-19-python-september-meetup/04-python-for-the-management-of-iot-platforms-at-worl.webp
      caption: "\"Python for the management of IoT platforms at Worldsensing\" by Toni Martínez del Hoyo (@tonidelhoyo)"
      source: "https://x.com/PyBCN/status/1174746936307593222"
      time: "20:07"
      talk: python-for-the-management-of-iot-platforms-at-worldsensing
---
