---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 282194482.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python November Meetup (in person!)"
date: 2021-11-25
year: 2021
venue: "TravelPerk"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 29
meetup_url: "https://www.meetup.com/python-barcelona/events/282194482/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 282194482 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: property-based-testing-with-hypothesis
    title: "Property-based testing with hypothesis"
    speakers: [alberto-camara]
    type: talk
    language: en
    duration_minutes: 30
    description: "Property-based testing is an approach to writing unit tests where, instead of using specific examples, we focus on specifying properties which we expect to hold in all cases. This allows for systematic checks against a multitude of examples and quickly finding errors and edge cases.\n\nWe will introduce Hypothesis, a library which allows for property-based testing in a very succint way by integrating with pytest."
  - id: serverless-webapp-using-googleappengine
    title: "Serverless WebApp using GoogleAppEngine"
    speakers: [victor-perez, carlos-galvez]
    type: talk
    language: es
    duration_minutes: 30
    description: "Cómo hemos usado en Tiendeo la suite de Google Cloud (AppEngine, Datastore, Storage) para el prototipado y despliegue de aplicaciones web y como ha evolucionado el proyecto bcnmarket.barcelona para soportar el incremento de tráfico. Reestructuración del repositorio, mejora de la caché, colas (RabbitMQ), indexado a Elastic, API-Swagger, Celery"
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/1463934429278220292"
  items:
    - file: 2021-11-25-python-november-meetup-in-person/08-welcome-to-november-s-python-meetup-https-www-meet.webp
      caption: "Welcome to November's Python Meetup! https://www.meetup.com/python-barcelona/events/282194482/ @berenguel is introducing us"
      source: "https://x.com/PyBCN/status/1463933197444689922"
      time: "19:10"
    - file: 2021-11-25-python-november-meetup-in-person/01-property-based-testing-with-hypothesis-by-alberto.webp
      caption: "\"Property-based testing with hypothesis\", by Alberto Cámara (@b3r2s)"
      source: "https://x.com/PyBCN/status/1463934429278220292"
      time: "19:15"
      talk: property-based-testing-with-hypothesis
    - file: 2021-11-25-python-november-meetup-in-person/02-pip-install-hypothesis.webp
      caption: "pip install hypothesis"
      source: "https://x.com/PyBCN/status/1463936064129798145"
      time: "19:22"
    - file: 2021-11-25-python-november-meetup-in-person/03-serverless-webapp-using-googleappengine-by-victor.webp
      caption: "\"Serverless WebApp using GoogleAppEngine\", by Victor Pérez (@vperezb) and Carlos Gálvez"
      source: "https://x.com/PyBCN/status/1463944314715791362"
      time: "19:54"
      talk: serverless-webapp-using-googleappengine
    - file: 2021-11-25-python-november-meetup-in-person/04-advantages-and-disadvantages-of-google-datastore.webp
      caption: "Advantages and disadvantages of Google Datastore:"
      source: "https://x.com/PyBCN/status/1463946088721920002"
      time: "20:02"
    - file: 2021-11-25-python-november-meetup-in-person/05-demo.webp
      caption: "Demo!"
      source: "https://x.com/PyBCN/status/1463948721201332234"
      time: "20:12"
    - file: 2021-11-25-python-november-meetup-in-person/06-enough-talks-for-today-pizza-time.webp
      caption: "Enough talks for today. Pizza time!! 🍕🍺"
      source: "https://x.com/PyBCN/status/1463953791477329931"
      time: "20:32"
    - file: 2021-11-25-python-november-meetup-in-person/07-thanks-travelperk-for-hosting-python-barcelona.webp
      caption: "Thanks @travelperk for hosting Python Barcelona!"
      source: "https://x.com/PyBCN/status/1463959177789906945"
      time: "20:54"
---
