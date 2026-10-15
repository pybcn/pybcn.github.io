---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 11395487.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "The Barcelona Python October Meetup"
date: 2009-10-14
year: 2009
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 12
meetup_url: "https://www.meetup.com/python-barcelona/events/11395487/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 11395487 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: bfg-the-pay-only-for-what-you-eat-python-web-framework
    title: "BFG, the \"pay only for what you eat\" Python web framework."
    speakers: [rok-garbas]
    type: talk
    description: "BFG is a Python web application framework based on WSGI."
    links:
      - type: site
        url: "https://bfg.repoze.org/"
  - id: plotting-data-with-python-and-pylab
    title: "Plotting data with Python and PyLab"
    speakers: [giovanni-dall-olio]
    type: talk
    links:
      - type: site
        url: "https://www.scipy.org/PyLab"
      - type: site
        url: "https://matplotlib.sourceforge.net/"
      - type: site
        url: "https://www.scipy.org/"
      - type: site
        url: "https://numpy.scipy.org/"
      - type: site
        url: "https://ipython.scipy.org/moin/"
  - id: a-quick-look-at-networkx
    title: "A quick look at NetworkX"
    speakers: [javier-diez-perez]
    type: talk
    description: "NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks."
    links:
      - type: site
        url: "https://networkx.lanl.gov/"
---
