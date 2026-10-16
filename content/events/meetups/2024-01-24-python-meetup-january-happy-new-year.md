---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 298506663.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup January: Happy New Year!"
date: 2024-01-24
year: 2024
venue: "Adevinta Spain"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 107
meetup_url: "https://www.meetup.com/python-barcelona/events/298506663/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 298506663 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: launch-your-own-python-library-within-the-company
    title: "Launch your own Python Library within the company"
    speakers: [julian-boronat]
    type: talk
    language: en
    duration_minutes: 30
    description: "This presentation will aim to demonstrate a straightforward method for publishing your own Python library to the JFrog Artifactory of your organization; on this opportunity, we are going to do this within Adevinta Spain by implementing the CI/CD part through Github Actions. Key topics to be covered include: 1-Monorepo vs. Multirepo, 2-Package and Versioning, 3-Repository Templates, 4-GHA Marketplace, 5-Testing and 6-Best Practices."
  - id: mastering-pdf-form-filling-with-pypdf
    title: "Mastering PDF Form-Filling with PyPDF"
    speakers: [jordi-bosch]
    type: talk
    language: es
    duration_minutes: 30
    description: "Tired about PDF paperwork? Join the PDF revolution as we see how PyPDF Python library changes how we work with PDF forms completion. We'll discover how to form-fill PDFs with a touch of Python magic. By the end, you'll be a PDF expert, eliminating manual data entry. Get ready to improve your data skills!"
---
