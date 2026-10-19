---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 221444518.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python April Meetup"
date: 2015-04-16
year: 2015
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 62
meetup_url: "https://www.meetup.com/python-barcelona/events/221444518/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 221444518 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: mutable-vs-immutable-objects-and-typical-mistakes
    title: "Mutable vs Immutable objects and typical mistakes"
    speakers: [pablo-enfedaque-vidal]
    type: talk
    duration_minutes: 30
  - id: 15-fails-in-15-minutes-an-interactive-guide-to-shooting
    title: "15 fails in 15 minutes: An interactive guide to shooting yourself in the foot."
    speakers: [manuel-ebert]
    type: talk
    duration_minutes: 15
  - id: practical-webcrawling-with-scrapy
    title: "Practical webcrawling with Scrapy"
    speakers: [ivan-company]
    type: talk
    duration_minutes: 30
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/588751026209083393"
  items:
    - file: 2015-04-16-python-april-meetup/01-practical-webcrawling-with-scrapy-by-ivan-company.webp
      caption: "Practical webcrawling with Scrapy, by Iván Compañy (@pyivanc)"
      source: "https://x.com/PyBCN/status/588751026209083393"
      time: "19:09"
      talk: practical-webcrawling-with-scrapy
    - file: 2015-04-16-python-april-meetup/02-15-fails-in-15-minutes-an-interactive-guide-to-sho.webp
      caption: "15 fails in 15 minutes: An interactive guide to shooting yourself in the foot, by Manuel Ebert (@maebert) #pybcn"
      source: "https://x.com/PyBCN/status/588759705603940352"
      time: "19:43"
      talk: 15-fails-in-15-minutes-an-interactive-guide-to-shooting
    - file: 2015-04-16-python-april-meetup/03-mutable-vs-immutable-objects-and-typical-mistakes.webp
      caption: "Mutable vs Immutable objects and typical mistakes, by Pablo Enfedaque (@pablitoev56)"
      source: "https://x.com/PyBCN/status/588770705464041473"
      time: "20:27"
      talk: mutable-vs-immutable-objects-and-typical-mistakes

---
