---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 10610722.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "The Barcelona Python Meetup June 2009"
date: 2009-06-25
year: 2009
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 14
meetup_url: "https://www.meetup.com/python-barcelona/events/10610722/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 10610722 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: pitivi-yes-you-can-edit-videos-with-python
    title: "PiTiVi : Yes, you can edit videos with Python"
    speakers: [edward-hervey]
    type: talk
    links:
      - type: site
        url: "https://www.pitivi.org"
  - id: whoosh-a-fast-featureful-full-text-indexing-and-searching
    title: "Whoosh : A fast, featureful full-text indexing and searching library"
    type: talk
    links:
      - type: site
        url: "https://whoosh.ca/"
  - id: unit-testing-yes-but-how
    title: "Unit Testing : Yes, but how?"
    speakers: [maik-roder]
    type: talk
  - id: boost-your-python-career-learn-what-headhunters-clients-are
    title: "Boost your Python career : Learn what headhunters/clients are looking for in a candidate rich market"
    speakers: [jo-gascoigne]
    type: talk
---
