---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 238991201.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python April Meetup"
date: 2017-04-20
year: 2017
venue: "Travelperk"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 56
meetup_url: "https://www.meetup.com/python-barcelona/events/238991201/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 238991201 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: when-your-dataframe-is-bigger-than-your-ram-what-s-next
    title: "When your dataframe is bigger than your RAM what's next ?"
    speakers: [gabriel-de-maeztu]
    type: talk
    language: en
    duration_minutes: 30
    description: "Many of us enjoy working with pandas but sometimes your data is just Fat Data too little for Big Data solutions, but you still need to work with the whole dataset. An introduction to Blaze and Dask and how they can help with this stuff from the perspective of someone that knows about pandas, numpy but not about Big Data solutions like Hadoop, Spark Cassandra etc.."
  - id: python-performance-profiling-for-data-analysis
    title: "Python performance profiling for data analysis"
    speakers: [jordi-deu-pons]
    type: talk
    language: en
    duration_minutes: 30
    description: "Examples of usage of cProfiler, line profiler and memory profiler to detect performance problems on data analysis algorithms."
---
