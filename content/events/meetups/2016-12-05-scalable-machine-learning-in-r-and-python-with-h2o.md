---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 235941516.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyLadies BCN Workshop, December 2016"
date: 2016-12-05
year: 2016
venue: "Edifici Històric UB (Aula B7)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 1
meetup_url: "https://www.meetup.com/pyladies-bcn/events/235941516/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 235941516 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: scalable-machine-learning-in-r-and-python-with-h2o
    title: "Scalable Machine Learning in R and Python with H2O"
    speakers: [erin-ledell]
    type: talk
    description: "The focus of this talk is scalable machine learning using the H2O R and Python packages. H2O is an open source, distributed machine learning platform designed for big data, with the added benefit that it's easy to use on a laptop (in addition to a multi-node Hadoop or Spark cluster). The core machine learning algorithms of H2O are implemented in high-performance Java, however, fully-featured APIs are available in R, Python, Scala, REST/JSON, and also through a web interface."
    links:
      - type: github
        url: "https://github.com/h2oai/h2o-3"
---
