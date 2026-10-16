---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 61737702.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Talks"
date: 2012-05-17
year: 2012
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 37
meetup_url: "https://www.meetup.com/python-barcelona/events/61737702/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 61737702 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: introduction-to-regular-expressions
    title: "Introduction to Regular expressions"
    speakers: [eloi-crespillo]
    type: talk
    links:
      - type: site
        url: "https://docs.python.org/library/re.html"
  - id: introduction-to-the-python-debugger-pdb
    title: "Introduction to the Python debugger (PDB)"
    speakers: [raul-cumplido]
    type: talk
  - id: must-know-python-libraries-for-a-web-python-developer
    title: "Must-know python libraries for a (web) python developer"
    speakers: [domen-kozar]
    type: talk
  - id: getting-started-with-pandas
    title: "Getting started with Pandas"
    speakers: [maik-roder]
    type: talk
    links:
      - type: site
        url: "https://pandas.pydata.org/"
  - id: overview-of-python-web-scraping-tools
    title: "Overview of Python web scraping tools"
    speakers: [maik-roder]
    type: talk
---
