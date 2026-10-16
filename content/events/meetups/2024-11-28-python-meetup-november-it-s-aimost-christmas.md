---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 303684105.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup November: It's AImost Christmas"
date: 2024-11-28
year: 2024
venue: "Aticco Bogatell - Coworking en Poblenou"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 61
meetup_url: "https://www.meetup.com/python-barcelona/events/303684105/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 303684105 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: genetic-algorithms-and-clustering-for-optimal-solution
    title: "Genetic Algorithms and Clustering for Optimal Solution Search"
    speakers: [oriol-porta-tovar]
    type: talk
    language: en
    duration_minutes: 30
    description: "The concept of genetic algorithms is explained, which generate populations of solutions, evaluate their performance, select the best ones, and combine them to improve. These algorithms are effective in finding solutions to complex problems through an iterative process of selection, crossover, and mutation."
  - id: from-hours-to-seconds-how-nvidia-rapids-is-revolutionizing
    title: "From hours to seconds: How NVIDIA RAPIDS is Revolutionizing Big Data Processing"
    speakers: [mauricio-volcanes]
    type: talk
    language: en
    duration_minutes: 30
    description: "This talk explores the benefits of NVIDIA RAPIDS, a GPU-accelerated data science framework, compared to traditional CPU-based libraries like Pandas. By benchmarking performance on real-world datasets, we uncover the conditions where RAPIDS excels and demonstrate its potential for accelerating large-scale data workflows. Attendees will learn practical strategies for optimizing workflows, understanding performance trade-offs, and leveraging dataset scaling. The session requires a basic understanding of Python, familiarity with data processing tools like Pandas, and access to a system with a GPU or a Google Collab account."
---
