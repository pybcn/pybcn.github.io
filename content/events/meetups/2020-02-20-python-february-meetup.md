---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 268290923.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python February Meetup"
date: 2020-02-20
year: 2020
venue: "Holaluz"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 28
meetup_url: "https://www.meetup.com/python-barcelona/events/268290923/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 268290923 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: automatically-intercepting-debugging-all-python-http-s
    title: "Automatically intercepting & debugging all Python HTTP(S)"
    speakers: [tim-perry]
    type: talk
    language: en
    duration_minutes: 30
    description: "HTTP Toolkit is an open-source HTTP(S) debugging tool that can completely automatically capture and/or rewrite all HTTP(S) traffic from your Python code, for debugging & testing. That sounds a lot like magic. In this talk, we'll look at how it really works: how HTTP Toolkit can automatically man-in-the-middle all your requests, with no admin permissions or code changes necessary. We'll learn a bit about how HTTP interception works, see why this is useful, and then explore how HTTP Toolkit injects into the Python's own internals to make this happen."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=1R3WiyJhpQs"
      - type: site
        url: "https://httptoolkit.tech/"
  - id: migracode-creating-a-migrant-tech-community
    title: "Migracode: Creating a Migrant-Tech Community"
    speakers: [vincent-van-grondelle]
    type: talk
    language: en
    duration_minutes: 30
    description: "We are currently running Migracode: the first code school for refugees and migrants in Barcelona. Through free tech education we offer vulnerable groups to become Junior Web Developers, and we also help them connect to tech companies throughout Catalunya and Spain, and possibly throughout Europe. We would love to present our project in the Python Community and find potential partners, volunteers and other opportunities. We also have a lot to offer regarding Corporate Social Responsibility and our talk also includes this part."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=QmqrBAKSB6s"
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/1230569930065661952"
  items:
    - file: 2020-02-20-python-february-meetup/04-about-to-start-today-s-meetup-thanks-holaluzeng-fo.webp
      caption: "About to start today's meetup. Thanks @HolaluzEng for hosting us!"
      source: "https://x.com/PyBCN/status/1230558963164311552"
      time: "19:24"
    - file: 2020-02-20-python-february-meetup/05-automatically-intercepting-debugging-all-python-ht.webp
      caption: "\"Automatically intercepting & debugging all Python HTTP(S)\" by Tim Perry (@pimterry)"
      source: "https://x.com/PyBCN/status/1230559515424129026"
      time: "19:27"
      talk: automatically-intercepting-debugging-all-python-http-s
    - file: 2020-02-20-python-february-meetup/06-it-s-magic.webp
      caption: "It's #magic 🤷‍♂️"
      source: "https://x.com/PyBCN/status/1230561043979522053"
      time: "19:33"
    - file: 2020-02-20-python-february-meetup/01-migracode-creating-a-migrant-tech-community-by-vin.webp
      caption: "\"Migracode: Creating a Migrant-Tech Community\" by Vincent van Grondelle (@VsVangrondelle)"
      source: "https://x.com/PyBCN/status/1230569930065661952"
      time: "20:08"
      talk: migracode-creating-a-migrant-tech-community
    - file: 2020-02-20-python-february-meetup/02-how-can-you-volunteer-with-migracodebcn.webp
      caption: "How can you volunteer with @MigracodeBCN?"
      source: "https://x.com/PyBCN/status/1230571857277005824"
      time: "20:16"
    - file: 2020-02-20-python-february-meetup/03-thanks-holaluzeng-for-the-venue-and-the-pizzas.webp
      caption: "Thanks @HolaluzEng for the venue and the pizzas! 👏👏"
      source: "https://x.com/PyBCN/status/1230582036961906689"
      time: "20:56"
---
