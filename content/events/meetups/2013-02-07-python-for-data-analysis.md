---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 102110082.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python for Data Analysis"
date: 2013-02-07
year: 2013
venue: "Parc de Recerca Biomedica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 55
meetup_url: "https://www.meetup.com/python-barcelona/events/102110082/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 102110082 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: matplotlib
    title: "Matplotlib"
    speakers: [juan-ramon-gonzalez-vallinas]
    type: talk
    duration_minutes: 10
  - id: quick-introduction-to-ipython
    title: "Quick introduction to IPython"
    speakers: [areski-belaid]
    type: talk
    duration_minutes: 5
  - id: ipython-notebook
    title: "IPython Notebook"
    speakers: [areski-belaid]
    type: talk
    duration_minutes: 10
  - id: introduction-to-pandas
    title: "Introduction to Pandas"
    speakers: [maik-roder]
    type: talk
    duration_minutes: 10
  - id: introduction-to-scipy
    title: "Introduction to Scipy"
    speakers: [guillem-serra]
    type: talk
    duration_minutes: 10
  - id: practical-example-of-using-scipy-for-signal-processing-and
    title: "Practical example of using Scipy for signal processing and filtering"
    speakers: [guillem-serra]
    type: talk
    duration_minutes: 5
  - id: introduction-to-scikit-learn-using-ipython-notebook
    title: "Introduction to Scikit-learn (Using IPython Notebook)"
    speakers: [piotr-migdal]
    type: talk
    duration_minutes: 10
  - id: practical-example-of-using-scikit-learn-for-machine-learning
    title: "Practical example of using Scikit-learn for Machine learning"
    speakers: [marc-garcia]
    type: talk
    duration_minutes: 10
  - id: introduction-to-numpy
    title: "Introduction to Numpy"
    speakers: [francesco-benincasa]
    type: talk
    duration_minutes: 10
  - id: using-numpy-to-read-from-netcdf-scientific-format
    title: "Using Numpy to read from NetCDF scientific format"
    speakers: [francesco-benincasa]
    type: talk
    duration_minutes: 5
  - id: gpu-powered-numpy-with-gnumpy
    title: "GPU powered numpy with gnumpy"
    speakers: [xavier-arrufat]
    type: talk
    duration_minutes: 5
---
