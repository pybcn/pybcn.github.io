---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 225254712.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python September Meetup"
date: 2015-09-22
year: 2015
venue: "Skyscanner"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 64
meetup_url: "https://www.meetup.com/python-barcelona/events/225254712/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 225254712 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: hacking-the-bcn-housing-market-scrapy
    title: "\"Hacking the BCN housing market\" (Scrapy)"
    speakers: [tudor-barbu]
    type: talk
    language: en
    duration_minutes: 10
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=QJ1YKtM0Kjw"
  - id: tecnicas-osint-python
    title: "Técnicas OSINT & Python"
    speakers: [albert-sanchez]
    type: talk
    language: es
    duration_minutes: 30
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=1mr0Gx7qJ5E"
  - id: image-processing-for-beginners
    title: "Image processing for beginners"
    speakers: [prassanna-ganesh]
    type: talk
    language: en
    duration_minutes: 30
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/646387703106412544"
  items:
    - file: 2015-09-22-python-september-meetup/02-hacking-the-bcn-housing-market-by-tudor-barbu-mota.webp
      caption: "Hacking the BCN housing market, by Tudor Barbu (@motanelu) #pybcn"
      source: "https://x.com/PyBCN/status/646371088189014016"
      time: "19:10"
    - file: 2015-09-22-python-september-meetup/03-tecnicas-osint-python-by-albert-sanchez-state-x-py.webp
      caption: "Técnicas OSINT & Python, by Albert Sanchez (@State_X) #pybcn"
      source: "https://x.com/PyBCN/status/646376911845916672"
      time: "19:33"
      talk: tecnicas-osint-python
    - file: 2015-09-22-python-september-meetup/01-image-processing-for-beginners-by-prassanna-ganesh.webp
      caption: "Image processing for beginners, by Prassanna Ganesh #pybcn"
      source: "https://x.com/PyBCN/status/646387703106412544"
      time: "20:16"
      talk: image-processing-for-beginners
    - file: 2015-09-22-python-september-meetup/04-great-talks-thanks-skyscanner-for-the-pizza-beers.webp
      caption: "Great talks! Thanks @Skyscanner for the pizza & beers! #pybcn"
      source: "https://x.com/PyBCN/status/646400405795115008"
      time: "21:07"
---
