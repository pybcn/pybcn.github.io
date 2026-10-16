---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 286238841.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python June Meetup: Running Serverless & Data Pipelines with Yaetos"
date: 2022-06-15
year: 2022
venue: "Aticco Verdaguer - El teu coworking a Gràcia"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 54
meetup_url: "https://www.meetup.com/python-barcelona/events/286238841/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 286238841 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: run-the-extra-mile-with-serverless
    title: "Run the extra mile with serverless"
    speakers: [mohammed-bouabid]
    type: talk
    language: en
    duration_minutes: 30
    description: "sennder is migration from monolith to microservices. We will explain the requirements and architecture that they're working on, and see some live coding on how to consume Kafka events using AWS Lambda."
  - id: creating-python-data-pipelines-with-yaetos
    title: "Creating Python Data Pipelines with Yaetos"
    speakers: [arthur-prevot]
    type: talk
    language: en
    duration_minutes: 30
    description: "The talk will describe the challenges of creating python data pipelines and putting them in production in the cloud, and how Yaetos can help. It is targeted at data engineers, data scientists, analysts and python enthusiasts. Yaetos is a data framework, simplifying the use of Apache Spark in the AWS cloud, and with implementations in production at Infojobs and The Hotels Network."
    links:
      - type: github
        url: "https://github.com/arthurprevot/yaetos"
---
