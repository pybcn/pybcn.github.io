---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 232559577.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python July Meetup"
date: 2016-07-28
year: 2016
venue: "Skyscanner"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 61
meetup_url: "https://www.meetup.com/python-barcelona/events/232559577/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 232559577 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: efficient-django
    title: "Efficient Django"
    speakers: [david-arcos]
    type: talk
    duration_minutes: 30
    description: "Does Django scale? How to manage traffic peaks? What happens when the database grows too big? How to find the bottlenecks? We will overview the basics concepts on scalability and performance, and then see some tips and tricks. These statements will be backed up with experiments and numbers, to show the timing improvements."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=xlRek0SkGZ8"
  - id: kinto-a-minimalist-json-storage-service
    title: "Kinto - A minimalist JSON storage service"
    speakers: [mathieu-leplatre]
    type: talk
    duration_minutes: 30
    description: "Kinto (https://kinto.readthedocs.io) is a HTTP service - built with Pyramid - with synchronisation and sharing features. It is meant to be easy to use and easy to self-host. In this talk, I'll present the main use-cases (from quick weekend hacks to delivery of security settings to millions of Firefox users), and a quick tour on how we leverage the pluggability of Pyramid."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=S-8tyE62unI"
      - type: site
        url: "https://kinto.readthedocs.io"
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/758711749356953600"
  items:
    - file: 2016-07-28-python-july-meetup/01-efficient-django-by-david-arcos-dzpm-pybcn.webp
      caption: "Efficient Django by David Arcos (@DZPM) #pybcn"
      source: "https://x.com/PyBCN/status/758711749356953600"
      time: "19:12"
      talk: efficient-django
    - file: 2016-07-28-python-july-meetup/02-kinto-a-minimalist-json-storage-service-by-mathieu.webp
      caption: "Kinto - A minimalist JSON storage service by Mathieu Leplatre (@leplatrem) #pybcn"
      source: "https://x.com/PyBCN/status/758729659164921856"
      time: "20:23"
      talk: kinto-a-minimalist-json-storage-service

---
