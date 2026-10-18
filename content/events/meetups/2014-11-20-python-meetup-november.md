---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 203263722.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup November"
date: 2014-11-20
year: 2014
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 60
meetup_url: "https://www.meetup.com/python-barcelona/events/203263722/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 203263722 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: conda-cross-platform-python-agnostic-binary-package-manager
    title: "Conda - Cross-platform, Python-agnostic binary package manager"
    speakers: [christine-doig]
    type: talk
    language: en
    duration_minutes: 20
    links:
      - type: site
        url: "https://conda.pydata.org"
  - id: putting-python-inside-postgresql
    title: "Putting Python inside PostgreSQL"
    speakers: [brian-sutherland]
    type: talk
    language: en
    duration_minutes: 20
    description: "Practical guide to writing triggers and stored procedures for PostgreSQL in Python."
  - id: inside-the-artificial-neural-network
    title: "Inside the Artificial Neural Network"
    speakers: [xavier-arrufat]
    type: talk
    language: en
    duration_minutes: 40
    description: "a visual and intuitive journey to understand how it stores knowledge and how it takes decisions."
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/535503325022937088"
  items:
    - file: 2014-11-20-python-meetup-november/03-conda-and-bokeh-by-christine-doig-ch-doig-pybcn.webp
      caption: "Conda and Bokeh, by Christine Doig (@ch_doig) #pybcn"
      source: "https://x.com/PyBCN/status/535501261425364995"
      time: "19:33"
    - file: 2014-11-20-python-meetup-november/01-putting-python-inside-postgresql-by-brian-sutherla.webp
      caption: "Putting Python inside PostgreSQL, by Brian Sutherland #pybcn"
      source: "https://x.com/PyBCN/status/535503325022937088"
      time: "19:41"
      talk: putting-python-inside-postgresql
    - file: 2014-11-20-python-meetup-november/02-inside-the-artificial-neural-network-by-xavier-arr.webp
      caption: "Inside the Artificial Neural Network, by Xavier Arrufat #pybcn"
      source: "https://x.com/PyBCN/status/535509138097188865"
      time: "20:05"
      talk: inside-the-artificial-neural-network
---
