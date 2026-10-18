---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 262097404.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python June Meetup"
date: 2019-06-20
year: 2019
venue: "CahootCoworking Barcelona"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 74
meetup_url: "https://www.meetup.com/python-barcelona/events/262097404/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 262097404 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: don-t-talk-scheme
    title: "Don't talk, scheme!"
    speakers: [tin-markovic]
    type: talk
    language: en
    duration_minutes: 25
    description: "Make service integration easier with schemata. Services (Micro or SOA) often introduce misunderstandings between teams and parties. During development, there's always room for change and improvement - things are flexible. This can be problematic with several teams and several services in parallel. Bind them with schema. Enforce the schema programmatically and use it to test. Reuse internal standards through your ecosystem, without consistency issues on your dependents. Examples are in Python: implementation and demonstration of some principles, and how they integrate."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=pQzlYyOKSTk"
  - id: automatize-reports-using-google-slides-api
    title: "Automatize reports using Google Slides API"
    speakers: [victor-perez]
    type: talk
    duration_minutes: 15
    description: "In the presentation I'll try to show the main pain-points between the idea of creation an automatic report and the way we've solved."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=68FOP7sBDes"
  - id: from-legacy-code-to-modern-code
    title: "From legacy code to modern code"
    speakers: [stanislav-geidl]
    type: talk
    language: en
    duration_minutes: 30
    description: "Starting a new project is fun. But what about an existing project consisting of big monolithic legacy code in Python 2 that has no tests and breaks often? Would you start from scratch to rebuild this project? We decided to do it the opposite way - we started to change our current code a step by step. Refactoring the old code was a hard time full of trials and errors. From the beginning, we could only rely on weak monitoring to reveal bugs or not properly working service. We ended up in a position where new release would put us in the risk, and we were afraid to do it. Enhanced monitoring allowed us to stabilize the service until we were able to add tests. With every small improvement our confidence rose, maintenance became easier and adding new features became smoother. Finally, we were ready for the biggest step - switch to Python 3. After a year full of preparations, this exciting and successful work took us only a few days. But we did not stop there. We needed to improve the architecture and break the monolith to single-purpose packages, which we could connect via dependency injection. We followed the SOLID principles which allowed us to make better tests and to make our code more flexible to big changes."
  - id: pytest-recomendaciones-paquetes-basicos-para-testing-en
    title: "Pytest: recomendaciones, paquetes básicos para testing en Python y Django"
    speakers: [andreu-vallbona-plazas]
    type: talk
    description: "Esta charla no trata sobre buenas prácticas de testing sino de la presentación y consejos de uso sobre una selección \"curada\" de plugins de pytest., dentro del gran ecosistema, que hemos ido encontrando durante el desarrollo de proyectos, sobretodo de proyectos con Django. Esta charla está pensada para introducir a los desarrolladores una serie de paquetes para usar conjuntamente con pytest para tareas de testing, bien sea para tests unitarios, funcionales o de integración, y sobretodo, aplicado a proyectos Django. Se explicará brevemente los conceptos básicos de pytest. Algunos de los paquetes que se comentaran serán: pytest-django, pytest-watch, pytest-testmon, model-mommy, pytest-flake8.."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=asdtq4WgbAw"
# A recording of a whole session of this meetup and not of one talk: a
# block of lightning talks, or the introduction of the evening, has no
# talk record for a video to sit on, so the video sits on the event.
# bin/import-videos writes this block from the YouTube export of the
# pybcn-archive: a correction goes to the export or to the script, never
# here. The page prints these under a Recordings heading, after the talks
# (partials/session_videos.html). Not "videos": Hugo reads that key
# as a list of og:video URLs, and a list of records there stops the build.
session_videos:
  - title: "Kiwi Python Tour Intro"
    url: "https://www.youtube.com/watch?v=8H2PrNLEEYQ"
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/1141756308313563139"
  items:
    - file: 2019-06-20-python-june-meetup/01-welcome-to-python-june-meetup-pybcn-https-www-meet.webp
      caption: "Welcome to Python June Meetup! #pybcn https://www.meetup.com/python-185/events/262097404/"
      source: "https://x.com/PyBCN/status/1141756308313563139"
      time: "19:14"
    - file: 2019-06-20-python-june-meetup/02-pytest-recomendaciones-paquetes-basicos-para-testi.webp
      caption: "Pytest: recomendaciones, paquetes básicos para testing en Python y Django - Andreu Vallbona (@avallbona)"
      source: "https://x.com/PyBCN/status/1141758033338540032"
      time: "19:21"
      talk: pytest-recomendaciones-paquetes-basicos-para-testing-en
    - file: 2019-06-20-python-june-meetup/03-automatize-reports-using-google-slides-api-by-vict.webp
      caption: "Automatize reports using Google Slides API by Victor Perez (@vperezb)"
      source: "https://x.com/PyBCN/status/1141770507597078528"
      time: "20:11"
      talk: automatize-reports-using-google-slides-api
    - file: 2019-06-20-python-june-meetup/04-don-t-talk-scheme-make-service-integration-easier.webp
      caption: "Don't talk, scheme! Make service integration easier with schemata, By Tin Marković"
      source: "https://x.com/PyBCN/status/1141776488460705792"
      time: "20:35"
      talk: don-t-talk-scheme

---
