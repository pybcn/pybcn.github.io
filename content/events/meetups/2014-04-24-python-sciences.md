---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 169870182.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python & Sciences"
date: 2014-04-24
year: 2014
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 71
meetup_url: "https://www.meetup.com/python-barcelona/events/169870182/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 169870182 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: introduction-to-ipython-notebook
    title: "Introduction to Ipython Notebook"
    type: talk
  - id: introduction-to-python-for-data-analysis-overview-of-numpy
    title: "Introduction to Python for Data Analysis - Overview of numpy, scipy and pandas"
    speakers: [christine-doig]
    type: talk
  - id: introduction-to-pandas
    title: "Introduction to Pandas"
    speakers: [piotr-migdal]
    type: talk
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/459394310275084289"
  items:
    - file: 2014-04-24-python-sciences/01-introduction-to-ipython-notebook-by-loris-mularoni.webp
      caption: "Introduction to IPython Notebook, by Loris Mularoni (@LorisMularoni) #pybcn"
      source: "https://x.com/PyBCN/status/459394310275084289"
      time: "20:11"
      talk: introduction-to-ipython-notebook
    - file: 2014-04-24-python-sciences/03-introduction-to-python-for-data-analysis-by-christ.webp
      caption: "Introduction to Python for Data Analysis, by Christine Doig (@ch_doig) #pybcn"
      source: "https://x.com/PyBCN/status/459406658519961600"
      time: "21:00"
    - file: 2014-04-24-python-sciences/02-introduction-to-pandas-by-piotr-migdal-pmigdal-pyb.webp
      caption: "Introduction to Pandas, by Piotr Migdal (@pmigdal) #pybcn"
      source: "https://x.com/PyBCN/status/459412929951985664"
      time: "21:25"
      talk: introduction-to-pandas
---
