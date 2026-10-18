---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 161424252.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python for beginners / Learn some python"
date: 2014-03-20
year: 2014
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 68
meetup_url: "https://www.meetup.com/python-barcelona/events/161424252/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 161424252 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: execution-model-and-other-must-know-s-for-python-newcomers
    title: "Execution model and other must-know's for Python newcomers"
    speakers: [pablo-enfedaque-vidal]
    type: talk
    duration_minutes: 40
  - id: the-zen-of-python
    title: "The Zen of Python"
    speakers: [david-arcos]
    type: lightning
    description: "It's simple, short and fun, and a good way to introduce the Python philosophy to beginners."
    links:
      - type: site
        url: "https://legacy.python.org/dev/peps/pep-0020/"
  - id: virtualenv-and-pip
    title: "Virtualenv and pip"
    speakers: [alex-maneu]
    type: lightning
    description: "A quick intro of setting up the virtualenv, activating it and installing/uninstalling packages. If it fits I would install two different versions of the same package in separate virtualenvs to illustrate why they are useful."
  - id: list-comprehensions
    title: "List comprehensions"
    speakers: [jordi-gomez-bao]
    type: lightning
  - id: metodos-magicos-en-python
    title: "Métodos mágicos en python"
    speakers: [nacho-gentile]
    type: lightning
    description: "Como sacar partido de los magic methods de python en un ejemplo simple."
  - id: python-2-vs-python-3
    title: "Python 2 vs. Python 3"
    speakers: [pablo-enfedaque-vidal]
    type: lightning
  - id: where-to-find-help-for-python
    title: "Where to find help for Python"
    speakers: [aleta-dunne]
    type: lightning
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/446736550618222592"
  items:
    - file: 2014-03-20-python-for-beginners-learn-some-python/06-introduction-to-python-by-pablo-enfedaque-vidal-pa.webp
      caption: "Introduction to Python, by Pablo Enfedaque Vidal (@pablitoev56) #pybcn"
      source: "https://x.com/PyBCN/status/446712242487443456"
      time: "19:17"
    - file: 2014-03-20-python-for-beginners-learn-some-python/07-mutables-vs-immutables-pybcn.webp
      caption: "Mutables vs. immutables #pybcn"
      source: "https://x.com/PyBCN/status/446724872958644224"
      time: "20:08"
    - file: 2014-03-20-python-for-beginners-learn-some-python/01-the-zen-of-python-by-david-arcos-dzpm-pybcn.webp
      caption: "The Zen of Python, by David Arcos (@DZPM) #pybcn"
      source: "https://x.com/PyBCN/status/446736550618222592"
      time: "20:54"
      talk: the-zen-of-python
    - file: 2014-03-20-python-for-beginners-learn-some-python/02-virtualenv-and-pip-by-alex-maneu-zouave-pybcn.webp
      caption: "Virtualenv and pip, by Alex Maneu (@zouave) #pybcn"
      source: "https://x.com/PyBCN/status/446737043549601792"
      time: "20:56"
      talk: virtualenv-and-pip
    - file: 2014-03-20-python-for-beginners-learn-some-python/03-list-comprehensions-by-jordi-gomez-bao-jgomezb79-p.webp
      caption: "List comprehensions, by Jordi Gomez Bao (@jgomezb79) #pybcn"
      source: "https://x.com/PyBCN/status/446739185815552000"
      time: "21:04"
      talk: list-comprehensions
    - file: 2014-03-20-python-for-beginners-learn-some-python/04-metodos-magicos-en-python-by-nacho-gentile-nachoge.webp
      caption: "Métodos mágicos en Python, by Nacho Gentile (@nachogentile) #pybcn"
      source: "https://x.com/PyBCN/status/446742622154289152"
      time: "21:18"
      talk: metodos-magicos-en-python
    - file: 2014-03-20-python-for-beginners-learn-some-python/05-where-to-find-help-for-python-by-aleta-dunne-dtibu.webp
      caption: "Where to find help for Python, by Aleta Dunne (@dtiburon) #pybcn"
      source: "https://x.com/PyBCN/status/446749040899010560"
      time: "21:44"
      talk: where-to-find-help-for-python
---
