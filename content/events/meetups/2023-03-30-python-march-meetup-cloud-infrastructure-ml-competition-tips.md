---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 292399353.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python March Meetup: Cloud Infrastructure & ML Competition tips"
date: 2023-03-30
year: 2023
venue: "Ocado Technology"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 72
meetup_url: "https://www.meetup.com/python-barcelona/events/292399353/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 292399353 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: cloud-infrastructure-the-software-way
    title: "Cloud Infrastructure, the Software Way"
    speakers: [joan-garcia]
    type: talk
    language: en
    duration_minutes: 30
    description: "Have you ever managed a cloud infrastructure? If so, managing a bunch of static files representing your infrastructure probably sounds familiar to you. This is not strange, as cloud infrastructure management is a natural evolution of on-premises infrastructure management, where all the resources are traditionally managed with templates. What's the problem? You might ask yourself. The problems come when you start scaling up your environments, which is a common scenario in the cloud world, as opposed to on-premises. What if we take a look at our software development colleagues? This is precisely where software development shines. There, we have lots of ways to test our code, several mechanisms to avoid duplication and plenty of tools to ensure the quality of our code. Can we leverage these techniques to manage our cloud infrastructure? Thankfully, the cloud providers thought the same and gave us some frameworks that are closer to software development than traditional infrastructure management. In this session, we will leverage CDK, the Cloud Development Kit framework from AWS, to apply all the good practices from Software Development into the world of Cloud Infrastructure Management."
  - id: the-archival-datathon-ml-competition-tips
    title: "The Archival Datathon: ML competition tips"
    speakers: [alberto-camara]
    type: talk
    language: en
    duration_minutes: 30
    description: "How can we approach a Machine Learning competition with agility? What similarities & differences are there with respect to doing Machine Learning in production? By looking at the real experience of participating in a Kaggle competition, we will discuss how to structure work, and what techniques and tools are at the hand of a practicing Data Scientist to ensure making the most out of their time."
---
