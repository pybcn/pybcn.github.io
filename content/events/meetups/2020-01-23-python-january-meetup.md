---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 267876301.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: Python January Meetup
date: 2020-01-23
year: 2020
venue: Skyscanner
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 65
meetup_url: https://www.meetup.com/python-barcelona/events/267876301/
group: PyBCN
# The talks this meetup announced, read from the description of event 267876301 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: jazz-chord-generation-using-deep-learning
  title: Jazz chord generation using Deep Learning
  speakers:
  - mateusz-dorobek
  type: talk
  language: en
  duration_minutes: 30
  description: I'll tell you about jazz chords progressions generation using recurrent neural networks. Staring with "what is a chord?" I'll go through "How we can represent chord?" and "How we can embed chords?". There will be a lot about music from a computer point of view. I'll show how I've prepared the music data, and how to use recurrent neural networks to generate jazz chords sequences. We will analyze the results and discuss the future of music in a world of AI.
  links:
  - type: video
    url: https://www.youtube.com/watch?v=SMXlwINeKyQ
  - type: site
    url: https://www.mateuszdorobek.pl/
- id: using-pydantic-for-security-static-analysis-of-aws
  title: Using pydantic for security static analysis of AWS cloudformation files
  speakers:
  - oscar-blanco
  type: talk
  language: en
  duration_minutes: 30
  description: In Skyscanner we've developed CFRipper, a tool that checks for security issues in cloudformation files. In order to write this tool we use pydantic heavily to model the cloudformation files. In this talk we'll introduce pydantic and use cfripper and pycfmodel as use cases for the library.
  links:
  - type: video
    url: https://www.youtube.com/watch?v=GnQlVBIcunk
- id: inversion-de-control-e-inyeccion-de-dependencias-teoria-y
  title: Inversión de control e Inyección de dependencias, Teoría y ejemplos usando Injector
  speakers:
  - manuel-gomez
  - daniel-albarral
  type: talk
  language: es
  duration_minutes: 30
  description: La charla constará de dos partes, primero se explicarán los conceptos de Inversión de Control e Inyección de dependencias y para qué podemos usar estas técnicas; a continuación se mostrarán ejemplos de cómo usar estas técnicas en Python mediante la librería Injector.
  links:
  - type: video
    url: https://www.youtube.com/watch?v=u-KDwDqMbCI
  - type: github
    url: https://github.com/alecthomas/injector
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/1220410751074041858"
  items:
    - file: 2020-01-23-python-january-meetup/01-welcome-to-python-january-meetup-pybcn-https-www-m.webp
      caption: "Welcome to Python January Meetup! #PyBCN https://www.meetup.com/python-185/events/267876301/"
      source: "https://x.com/PyBCN/status/1220410751074041858"
      time: "19:19"
    - file: 2020-01-23-python-january-meetup/02-jazz-chord-generation-using-deep-learning-by-mateu.webp
      caption: "\"Jazz chord generation using Deep Learning\" by Mateusz Dorobek"
      source: "https://x.com/PyBCN/status/1220411066347401217"
      time: "19:20"
      talk: jazz-chord-generation-using-deep-learning
    - file: 2020-01-23-python-january-meetup/03-using-pydantic-for-security-static-analysis-of-aws.webp
      caption: "\"Using pydantic for security static analysis of AWS cloudformation files\" by Oscar Blanco (@oscarbc96)"
      source: "https://x.com/PyBCN/status/1220419289460674560"
      time: "19:53"
      talk: using-pydantic-for-security-static-analysis-of-aws
    - file: 2020-01-23-python-january-meetup/04-forbidden-toppings-on-pizza.webp
      caption: "Forbidden toppings on pizza! ❌🍍"
      source: "https://x.com/PyBCN/status/1220422619134074880"
      time: "20:06"
    - file: 2020-01-23-python-january-meetup/05-inversion-de-control-e-inyeccion-de-dependencias-t.webp
      caption: "\"Inversión de control e Inyección de dependencias, Teoría y ejemplos usando `Injector`\" by Manuel Gomez & Daniel Albarral"
      source: "https://x.com/PyBCN/status/1220427960240558081"
      time: "20:27"
      talk: inversion-de-control-e-inyeccion-de-dependencias-teoria-y

---
