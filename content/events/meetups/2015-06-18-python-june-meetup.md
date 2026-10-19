---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 223101140.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python June Meetup"
date: 2015-06-18
year: 2015
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 56
meetup_url: "https://www.meetup.com/python-barcelona/events/223101140/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 223101140 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: an-introduction-to-the-flask-web-framework-and-a-recipe-for
    title: "An introduction to the Flask Web framework and a recipe for the Google's App Engine"
    speakers: [gabriel-de-maeztu]
    type: talk
  - id: real-time-kpi-metrics-with-django-and-statsd
    title: "Real-time KPI metrics with Django and Statsd"
    speakers: [israel-saeta-perez]
    type: talk
    duration_minutes: 20
  - id: python-and-cancer-genomics
    title: "Python and Cancer Genomics"
    speakers: [loris-mularoni]
    type: talk
    duration_minutes: 20
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/611581671289307136"
  items:
    - file: 2015-06-18-python-june-meetup/01-an-introduction-to-the-flask-web-framework-and-a-r.webp
      caption: "\"An introduction to the Flask Web framework and a recipe for the Google's App Engine\" by Gabriel de Maeztu #pybcn"
      source: "https://x.com/PyBCN/status/611581671289307136"
      time: "19:10"
      talk: an-introduction-to-the-flask-web-framework-and-a-recipe-for
    - file: 2015-06-18-python-june-meetup/03-real-time-kpi-metrics-with-django-graphite-and-sta.webp
      caption: "\"Real-time KPI metrics with Django, Graphite and Statsd\" by Israel Saeta Pérez (@dukebody) #pybcn"
      source: "https://x.com/PyBCN/status/611591342364446720"
      time: "19:48"
    - file: 2015-06-18-python-june-meetup/02-python-and-cancer-genomics-by-loris-mularoni-pybcn.webp
      caption: "\"Python and Cancer Genomics\" by Loris Mularoni #pybcn"
      source: "https://x.com/PyBCN/status/611598407946371072"
      time: "20:16"
      talk: python-and-cancer-genomics
---
