---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 245937621.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: Python December Meetup
date: 2017-12-20
year: 2017
venue: Skyscanner
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 52
meetup_url: https://www.meetup.com/python-barcelona/events/245937621/
group: PyBCN
# The talks this meetup announced, read from the description of event 245937621 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: why-lazy-developers-write-beautiful-code
  title: Why lazy developers write beautiful code?
  speakers:
  - javier-arias-losada
  type: talk
  language: en
  duration_minutes: 30
  description: 'There has been a lot of discussion during the last 50 years about the nature of programming: Is it an art like poetry? Is it craftsmanship like pottery? Is it an exact science like physics? Or a non exact science like medicine? Is it engineering like bridge building? Whatever the nature of software development is: during this time, a lot of tools and techniques have appeared to make your lazy-developer life more difficult: Coding conventions, OOP, FP, SOLID, Design Patterns, Tests, TDD, UML, Use-cases, CASE tools, Refactoring, RUP, Agile, SCRUM, Continuous Integration, Code Complexity Metrics, Emergent Architecture, DevOps, SCM... and whatnot! But, sometimes, being a lazy developer makes you do things that seemed counterintuitive, in order to pursue your main objective: WORK LESS.'
- id: catching-asteroids-and-tracking-satellites-with-python
  title: Catching asteroids and tracking satellites with Python
  type: talk
  language: en
  duration_minutes: 30
  description: The use of Python for Astronomy has been rising in the last few years, and now there are more and more applications for Aerospace as well. In this talk we will describe orbit-predictor, a Python library to track Earth-orbiting artificial satellites open sourced this year by Satellogic, and poliastro, a community developed, open source Python library for interplanetary orbit computation and interactive visualization. The development of these libraries posed several interesting challenges aside from the algorithms themselves, such as the need of careful validation against external data from NASA and other sources, acceleration of some core parts using numba to replace FORTRAN code, and thoughtful design of the API to simplify physical unit and astronomical time scales handling on the user side. We will discuss the impact of these challenges on the development, highlight the strengths and limitations of Python for these specific applications and, of course, show some cool pictures of rockets.
  speakers:
  - juan-luis-cano-rodriguez
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/943545149052915712"
  items:
    - file: 2017-12-20-python-december-meetup/01-why-lazy-developers-write-beautiful-code-by-javier.webp
      caption: "Why lazy developers write beautiful code?, by Javier Arias (@javier_arilos)"
      source: "https://x.com/PyBCN/status/943545149052915712"
      time: "19:14"
      talk: why-lazy-developers-write-beautiful-code
    - file: 2017-12-20-python-december-meetup/02-catching-asteroids-and-tracking-satellites-with-py.webp
      caption: "Catching asteroids and tracking satellites with Python, by Juan Luis Cano (@astrojuanlu)"
      source: "https://x.com/PyBCN/status/943559036171116549"
      time: "20:09"
      talk: catching-asteroids-and-tracking-satellites-with-python
    - file: 2017-12-20-python-december-meetup/03-it-s-very-difficult-to-get-external-data-to-test-y.webp
      caption: "\"It's very difficult to get external data to test your algorithm\" - @astrojuanlu"
      source: "https://x.com/PyBCN/status/943564850998870016"
      time: "20:32"
---
