---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 246606586.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python January Meetup"
date: 2018-01-17
year: 2018
venue: "Bynder"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 64
meetup_url: "https://www.meetup.com/python-barcelona/events/246606586/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 246606586 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: exploring-generators-and-coroutines
    title: "Exploring generators and coroutines"
    speakers: [mariano-anaya]
    type: talk
    language: en
    duration_minutes: 40
    description: "Starting from a first introduction to generators, the talk will first cover the basics of them, their syntax, the original design of generators in Python, and all the kind of possibilities they offer in order to improve the performance, and run computations more efficiently. The talk will cover all methods that entail the generator protocol, and the different possibilities they enable from a user perspective. After reviewing the milestones on generators (from PEP-255 introducing generators, PEP-342 adding support for coroutines, PEP-380 allowing to delegate iteration to sub-generators, and more), we will see how coroutines serve asynchronous programming."
  - id: python-vs-julia
    title: "Python vs Julia"
    speakers: [jordi-deu-pons]
    type: talk
    language: en
    duration_minutes: 30
    description: "Data analysis oriented comprative"
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/953690942837534723"
  items:
    - file: 2018-01-17-python-january-meetup/03-thanks-to-bynder-for-hosting-the-barcelona-python.webp
      caption: "Thanks to @bynder for hosting the Barcelona Python Meetup!"
      source: "https://x.com/PyBCN/status/953690814495981569"
      time: "19:09"
    - file: 2018-01-17-python-january-meetup/01-exploring-generators-and-coroutines-by-mariano-ana.webp
      caption: "Exploring generators and coroutines, by Mariano Anaya (@rmarianoa)"
      source: "https://x.com/PyBCN/status/953690942837534723"
      time: "19:10"
      talk: exploring-generators-and-coroutines
    - file: 2018-01-17-python-january-meetup/02-python-vs-julia-by-jordi-deu-pons-elbioc.webp
      caption: "Python vs Julia, by Jordi Deu-Pons (@elbioc)"
      source: "https://x.com/PyBCN/status/953703340046716928"
      time: "19:59"
      talk: python-vs-julia
---
