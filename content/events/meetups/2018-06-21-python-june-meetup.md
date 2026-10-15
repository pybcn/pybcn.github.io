---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 251720316.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python June Meetup"
date: 2018-06-21
year: 2018
venue: "Dow Jones and Company"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 62
meetup_url: "https://www.meetup.com/python-barcelona/events/251720316/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 251720316 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: how-does-that-pyspark-thing-work-and-why-arrow-makes-it
    title: "How does that PySpark thing work? And why Arrow makes it faster?"
    speakers: [ruben-berenguel]
    type: talk
    language: en
    duration_minutes: 45
    description: "Back in ye olde days of Spark, using Python with Spark was an exercise in patience. Data was moving up and down from Python to Scala, being serialised constantly. Leveraging SparkSQL and avoiding UDFs made things better, as well as the constant improvement of the optimisers (Catalyst and Tungsten). But, with Spark 2.3 PySpark has speed up tremendously thanks to the (still experimental) addition of the Arrow serialisers. In this talk we will learn how PySpark has improved its performance in Apache Spark 2.3 by using Apache Arrow. To do this, we will travel through the internals of Spark to find how Python interacts with the Scala core, and some of the internals of Pandas to see how data moves from Python to Scala via Arrow."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=698441URsrc"
  - id: frozen-python-satice-ice-dataloggers
    title: "Frozen Python: satice ice dataloggers"
    speakers: [oriol-sanchez]
    type: talk
    language: en
    duration_minutes: 35
    description: "In this talk we will be about Sea Ice buoys and embedded scientific observation platforms in extreme environments. We will learn how to use python to write drivers, custom data protocols, sensors and GPS integration. Also we will take a look on data visualisation and other painful engineering stories to bring data from field to your server."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=bqphJQnp3Hw"
      - type: site
        url: "https://headingnorthweb.wordpress.com/tag/en-us/"
---
