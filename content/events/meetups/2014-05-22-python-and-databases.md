---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 117136682.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python and Databases"
date: 2014-05-22
year: 2014
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 71
meetup_url: "https://www.meetup.com/python-barcelona/events/117136682/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 117136682 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: introduccion-a-sqlalchemy
    title: "Introducción a SQLAlchemy"
    speakers: [jorge-medina]
    type: talk
    duration_minutes: 20
  - id: python-with-mysql
    title: "Python with MySQL"
    speakers: [miquel-camprodon]
    type: talk
    duration_minutes: 20
  - id: mongodb
    title: "MongoDB"
    speakers: [javier-arias-losada]
    type: talk
    duration_minutes: 20
  - id: titandb-scalable-graph-database
    title: "TitanDB ; Scalable Graph Database"
    speakers: [andres-correa-casablanca]
    type: talk
    duration_minutes: 20
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/469535749222961152"
  items:
    - file: 2014-05-22-python-and-databases/02-introduction-to-python-orm-sqlalchemy-by-jorge-med.webp
      caption: "Introduction to python ORM SQLAlchemy, by Jorge Medina #pybcn"
      source: "https://x.com/PyBCN/status/469527412104232960"
      time: "19:17"
    - file: 2014-05-22-python-and-databases/01-python-with-mysql-by-miquel-camprodon-pybcn.webp
      caption: "Python with MySQL, by Miquel Camprodon #pybcn"
      source: "https://x.com/PyBCN/status/469535749222961152"
      time: "19:50"
      talk: python-with-mysql
    - file: 2014-05-22-python-and-databases/01-python-and-mongodb-by-javier-arias-javier-arilos-p.webp
      caption: "Python and MongoDB, by Javier Arias (@javier_arilos) #pybcn"
      source: "https://x.com/PyBCN/status/469544096076673024"
      time: "20:23"
---
