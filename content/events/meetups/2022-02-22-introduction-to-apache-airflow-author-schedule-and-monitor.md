---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 283989295.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Introduction to Apache Airflow: author, schedule and monitor workflows"
date: 2022-02-22
year: 2022
venue: "Canòdrom - Ateneu d'Innovació Digital i Democràtica"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 15
meetup_url: "https://www.meetup.com/pyladies-bcn/events/283989295/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 283989295 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: introduction-to-apache-airflow-author-schedule-and-monitor
    title: "Introduction to Apache Airflow: author, schedule and monitor workflows"
    speakers: [esperanza-buitrago]
    type: workshop
    language: en
    description: "Apache Airflow is one of the most popular tools for implementing data engineering, machine learning, and DevOps workflows, and it is used by more than 200 companies such as Airbnb, Yahoo, Paypal, Intel or Stripe.\n\nAirflow allows to programmatically author, schedule and monitor workflows, which are sequence of tasks, started on a schedule or triggered by an event, and it is frequently used to handle big data processing pipelines.\n\nWe are going to work with Airflow from scratch and write our first DAG, accordingly to:\n- airflow operators,\n- operators that we write by ourselves,\n- our own pipelines, using a small operator.\n\nIf time permits, we are also going to find out how to add operators using MongoDB operators."
    links:
      - type: site
        url: "https://gitlab.com/ebuitragod/airflow-playground/-/blob/master/paso-a-paso.txt"
---
