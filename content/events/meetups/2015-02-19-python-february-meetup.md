---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 220028399.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python February Meetup"
date: 2015-02-19
year: 2015
venue: "Parc de Recerca Biomedica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 72
meetup_url: "https://www.meetup.com/python-barcelona/events/220028399/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 220028399 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: high-performance-python
    title: "High Performance Python"
    speakers: [marc-garcia]
    type: talk
    duration_minutes: 40
  - id: zipline-a-powerful-algorithmic-trading-simulator
    title: "Zipline, a powerful algorithmic trading simulator"
    speakers: [jesus-corrius]
    type: lightning
  - id: issue-certificates-with-python-to-build-a-trust-relationship
    title: "Issue certificates with Python to build a trust relationship"
    speakers: [pau-freixes]
    type: lightning
  - id: natural-language-processing-with-python-and-nltk
    title: "Natural Language Processing with Python and NLTK"
    type: talk
    duration_minutes: 20
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/568472498829959168"
  items:
    - file: 2015-02-19-python-february-meetup/05-about-to-start-the-barcelona-python-meetup-pybcn.webp
      caption: "About to start the Barcelona Python Meetup #pybcn"
      source: "https://x.com/PyBCN/status/568471862310772736"
      time: "19:07"
    - file: 2015-02-19-python-february-meetup/01-high-performance-python-by-marc-garcia-mgarcia-pyb.webp
      caption: "High Performance Python, by Marc Garcia (@__mgarcia__) #pybcn"
      source: "https://x.com/PyBCN/status/568472498829959168"
      time: "19:09"
      talk: high-performance-python
    - file: 2015-02-19-python-february-meetup/06-types-of-optimizations-pybcn.webp
      caption: "Types of optimizations #pybcn"
      source: "https://x.com/PyBCN/status/568475832362143745"
      time: "19:22"
    - file: 2015-02-19-python-february-meetup/07-python-optimization-takeaways-pybcn.webp
      caption: "Python Optimization takeaways #pybcn"
      source: "https://x.com/PyBCN/status/568483491006025729"
      time: "19:53"
    - file: 2015-02-19-python-february-meetup/02-natural-language-processing-with-python-and-nltk-b.webp
      caption: "Natural Language Processing with Python and NLTK, by Lusy #pybcn"
      source: "https://x.com/PyBCN/status/568488804119654401"
      time: "20:14"
      talk: natural-language-processing-with-python-and-nltk
    - file: 2015-02-19-python-february-meetup/03-zipline-a-powerful-algorithmic-trading-simulator-b.webp
      caption: "Zipline, a powerful algorithmic trading simulator, by Jesús Corrius (@jcorrius) #pybcn"
      source: "https://x.com/PyBCN/status/568496278100951041"
      time: "20:44"
      talk: zipline-a-powerful-algorithmic-trading-simulator
    - file: 2015-02-19-python-february-meetup/04-issue-certificates-with-python-to-build-a-trust-re.webp
      caption: "Issue certificates with Python to build a trust relationship by Pau Freixes (@pfreixes) #pybcn"
      source: "https://x.com/PyBCN/status/568498483696693248"
      time: "20:52"
      talk: issue-certificates-with-python-to-build-a-trust-relationship
---
