---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 237927901.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python March Meetup"
date: 2017-03-16
year: 2017
venue: "Skyscanner"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 64
meetup_url: "https://www.meetup.com/python-barcelona/events/237927901/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 237927901 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: data-visualisation-with-python-plotly
    title: "Data visualisation with Python & Plotly"
    speakers: [giovanni-perna]
    type: talk
    language: en
    duration_minutes: 30
    description: "Plotly is a scientific charting library for Python, R, MATLAB and Julia. In this talk we will see how the Python library can be used from command line scripts, in Jupyter notebooks and also in a simple flask application."
  - id: como-automatizamos-la-edicion-de-podcast-en-www
    title: "Cómo automatizamos la edición de podcast en www.entredevyops.es"
    speakers: [david-acacio-albareda]
    type: talk
    language: es
    duration_minutes: 25
    description: "La edición de audio siempre ha estado asociada al uso de software especializado (Garageband, Audacity ...), siendo un proceso manual, largo y de cierta complejidad. En esta charla os queremos presentar cómo hemos automatizado este proceso, utilizando Python y otras herramientas, y las lecciones aprendidas en todo el proceso"
  - id: using-celery-for-bots-slack-and-telegram
    title: "Using celery for bots (Slack and Telegram)"
    speakers: [xavier-orduna]
    type: talk
    language: en
    duration_minutes: 30
    description: "A small presentation on using celery as a fast option to build scalable bots in both platforms. Tips and tricks included!"
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/842457421687738370"
  items:
    - file: 2017-03-16-python-march-meetup/02-data-visualisation-with-python-plotly-by-giovanni.webp
      caption: "\"Data visualisation with Python & Plotly\", by Giovanni Perna #pybcn"
      source: "https://x.com/PyBCN/status/842439670910857219"
      time: "19:17"
      talk: data-visualisation-with-python-plotly
    - file: 2017-03-16-python-march-meetup/03-como-automatizamos-la-edicion-de-podcast-entredevy.webp
      caption: "\"Cómo automatizamos la edición de podcast @EntreDevYOps\", by David Acacio (@david_acacio) #pybcn"
      source: "https://x.com/PyBCN/status/842445808909881344"
      time: "19:41"
    - file: 2017-03-16-python-march-meetup/01-using-celery-for-bots-slack-and-telegram-by-xavier.webp
      caption: "\"Using celery for bots (Slack and Telegram)\", by Xavier Orduña (@xorduna) #pybcn"
      source: "https://x.com/PyBCN/status/842457421687738370"
      time: "20:27"
      talk: using-celery-for-bots-slack-and-telegram
---
