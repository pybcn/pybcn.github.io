---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 314765662.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup May"
date: 2026-05-21
year: 2026
venue: "Erni Consulting"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 47
meetup_url: "https://www.meetup.com/python-barcelona/events/314765662/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 314765662 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: from-scripts-to-systems-scaling-your-python-analysis-with
    title: "From Scripts to Systems: Scaling Your Python Analysis with Apache Airflow"
    speakers: [marc-gonzalez-planas]
    type: talk
    language: en
    duration_minutes: 30
    description: "Data Analysts often face a \"production wall\" where local Python scripts struggle to meet the demands of a live environment. Moving from ad-hoc analysis to scalable data products requires a shift in focus toward governance, observability, and idempotency. Without proper orchestration, we can fail.\n\nLet's learn how to bridge that gap by refactoring standard Python scripts into automated pipelines using Apache Airflow. We will explore the transition to an \"orchestration\" mindset, focusing on how to use Directed Acyclic Graphs (DAGs) and the TaskFlow API to transform modular Python functions into a an automatic system."
  - id: how-to-stop-an-epidemic-using-the-atomica-package
    title: "How to Stop an Epidemic using the Atomica Package"
    speakers: [eloisa-perez-bennetts]
    type: talk
    language: en
    duration_minutes: 30
    description: "Infectious diseases are a major global health challenge, claiming over 13 million lives each year. Despite the availability of interventions - such as vaccination, testing and treatment - determining the most effective strategy can be challenging, as this depends on complex factors like outbreak severity, funding limitations and sociopolitical influences. Computational modelling offers a powerful tool to assess the potential outcomes of different public health responses, but the difficulty of building fit-for-purpose epidemiological models from scratch is a barrier to widespread use.\n\nAtomica, a Python-based open source simulation engine, addresses this challenge by simplifying the development of epidemiological models. It allows users to create highly configurable data-driven simulations that incorporate disease transmission, intervention strategies and budget constraints. With its user-friendly design and robust capabilities, Atomica allows us to forecast the potential consequences of public health strategies in specific settings. This insight enables policymakers and health organisations to make evidence-based choices, ultimately improving intervention effectiveness and saving lives."
---
