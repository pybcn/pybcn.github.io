---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 259500461.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: Python March Meetup
date: 2019-03-21
year: 2019
venue: Satellogic
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 51
meetup_url: https://www.meetup.com/python-barcelona/events/259500461/
group: PyBCN
# The talks this meetup announced, read from the description of event 259500461 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: houston-we-have-a-snake-python-at-satellogic
  title: 'Houston, we have a snake: Python at Satellogic'
  type: talk
  language: en
  duration_minutes: 30
  description: 'From automating satellite hardware tests to predicting the ripeness of coffee beans, in Satellogic we use Python for all sorts of things. In this talk we will briefly introduce the company and talk about two specific things: Data Science for Products & Solutions, and satellite fleet management.'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=6ELCbtx3GJU
  speakers:
  - albert-pujol-torras
  - juan-luis-cano-rodriguez
- id: pyspark-on-kubernetes-avoiding-the-pain-of-yarn
  title: PySpark on Kubernetes -- Avoiding the pain of YARN
  speakers:
  - holden-karau
  type: talk
  language: en
  duration_minutes: 30
  description: Apache Spark is one of the most popular big data tools, and starting last year has had integrated support for running on Kubernetes. This talk will introduce some of the use cases of Apache Spark quickly (machine learning, ETL, etc.) and then look at the current cluster managers Spark runs on and their limitations. Most of the focus will be around running Python code, and the challenges associated with dependencies along with general challenges like scale-up & down. It's not all sunshine and roses though, I will talk about some of the limitations of our current approach and the work being done to improve this.
  links:
  - type: video
    url: https://www.youtube.com/watch?v=-usvyg6h3wY
- id: codificando-atomos-con-python
  title: Codificando átomos con Python
  speakers:
  - johanna-sanchez
  type: talk
  language: es
  duration_minutes: 30
  description: 'Una breve retrospectiva sobre comunidad: Un resumen sobre el recorrido por Latinoamérica con Argentina en Python, compartiendo Python y filosofía de comunidad. Codificando átomos con Python: Atomistic Simulation Environment - simulación atómica con módulos en Python para la manipulación de átomos, que nos permite analizar simulaciones o realizar visualizaciones, cuya finalidad es crear y analizar estructuras atómicas.'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=t2Z2yscYaQA
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/1108794016521469952"
  items:
    - file: 2019-03-21-python-march-meetup/01-welcome-to-pybcn-march-meetup-houston-we-have-a-sn.webp
      caption: "Welcome to PyBCN March Meetup! \"Houston, we have a snake: Python at @Satellogic\", by Albert Pujol and Juan Luis Cano (@astrojuanlu)"
      source: "https://x.com/PyBCN/status/1108794016521469952"
      time: "19:14"
      talk: houston-we-have-a-snake-python-at-satellogic
    - file: 2019-03-21-python-march-meetup/02-pyspark-on-kubernetes-avoiding-the-pain-of-yarn-by.webp
      caption: "\"PySpark on Kubernetes -- Avoiding the pain of YARN\", by Holden Karau (@holdenkarau)"
      source: "https://x.com/PyBCN/status/1108802526760058887"
      time: "19:48"
      talk: pyspark-on-kubernetes-avoiding-the-pain-of-yarn
    - file: 2019-03-21-python-march-meetup/03-codificando-atomos-con-python-por-johanna-sanchez.webp
      caption: "\"Codificando átomos con Python\", por Johanna Sanchez (@EllaQuimica) de @argenpython"
      source: "https://x.com/PyBCN/status/1108810729375887360"
      time: "20:20"
      talk: codificando-atomos-con-python
    - file: 2019-03-21-python-march-meetup/04-thanks-all-for-coming-and-satellogic-for-hosting-u.webp
      caption: "Thanks all for coming, and @Satellogic for hosting us!"
      source: "https://x.com/PyBCN/status/1108825216543797249"
      time: "21:18"

---
