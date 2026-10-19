---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 228054096.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python January Meetup"
date: 2016-01-21
year: 2016
venue: "Skyscanner"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 60
meetup_url: "https://www.meetup.com/python-barcelona/events/228054096/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 228054096 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: recommender-systems-in-python
    title: "Recommender Systems in Python"
    speakers: [biel-aparicio-terrasa, david-arazo-marin]
    type: talk
  - id: a-journey-to-using-an-encryption-standard-in-python
    title: "A journey to using an encryption standard in python"
    speakers: [daniel-moreno-medina]
    type: talk
  - id: tracking-django-errors-with-rollbar
    title: "Tracking Django errors with rollbar"
    speakers: [antonio-barcia-garcia]
    type: talk
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/690235396987420676"
  items:
    - file: 2016-01-21-python-january-meetup/01-a-journey-to-using-an-encryption-standard-in-pytho.webp
      caption: "\"A journey to using an encryption standard in python\" by Daniel Moreno #pybcn"
      source: "https://x.com/PyBCN/status/690235396987420676"
      time: "19:11"
      talk: a-journey-to-using-an-encryption-standard-in-python
    - file: 2016-01-21-python-january-meetup/03-recommendation-systems-in-python-by-biel-aparicio.webp
      caption: "\"Recommendation Systems in Python\" by Biel Aparicio y David Arazo #pybcn"
      source: "https://x.com/PyBCN/status/690241657896308736"
      time: "19:36"
    - file: 2016-01-21-python-january-meetup/02-tracking-django-errors-with-rollbar-by-antonio-bar.webp
      caption: "\"Tracking Django errors with Rollbar\" by Antonio Barcia (@ygneo) #pybcn"
      source: "https://x.com/PyBCN/status/690252231979966464"
      time: "20:18"
      talk: tracking-django-errors-with-rollbar
---
