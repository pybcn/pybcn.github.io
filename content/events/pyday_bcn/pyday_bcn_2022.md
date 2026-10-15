---
title: "PyDay BCN (2022)"
year: 2022
# The day of this edition, from the Meetup export, which records it per event.
date: 2022-11-26
# The venue of this edition, from the Meetup export, which records it per event.
venue: "Canòdrom"
description: "For the community, by the community!"
menu:
  main:
    parent: "PyDay BCN"
weight: 4
aliases:
  - /pyday-bcn-2022
heroBackground: /images/photos/canodrom.jpg

layout: event

free_text_sections:
  - title: Important dates
    id: important_dates
    content: "<b>1st October</b>: Call for proposals opening<br/>
      <b>31th October</b>: Call for proposals closing<br/>
      <b>16th November</b>: Program available<br/>
      <b>18th November, 9AM</b>: Early registration open for PyBCN members, PyDay speakers and sponsors<br/>
      <b>21nd November, 9AM</b>: General registration open through <a target='_blank' href='https://www.eventbrite.es/e/entradas-pydaybcn-2022-470666304587'>Eventbrite</a><br/>
      <b>26th November</b>: PyDay BCN 2022"
  - title: Registration
    id: registration
    content: "General registration will open on Monday 21st of November, at 9AM through <a target='_blank' href='https://www.eventbrite.es/e/entradas-pydaybcn-2022-470666304587'>Eventbrite</a>."

sponsor_levels:
  - sponsors_per_line: 2
    sponsors: [canodrom]
    name: Venue
  - sponsors_per_line: 2
    sponsors: [cloudblue, rover, qustodio, veriff, apsl]
    name: Gold
  - sponsors_per_line: 3
    sponsors: [coopdevs, somenergia, jobfluent, iomed]
    name: Silver
  - sponsors_per_line: 3
    sponsors: [hybridtheory, preply, pythones, digitalfems]
    name: Supporting
  - sponsors_per_line: 2
    sponsors: [pybcn, pyladiesbcn]
    name: Organizers


people_sections:
  - title: Speakers
    id: speakers
    levels:
      - people_per_line: 4
        people:
            - alberto-labarga
            - ana-eliza-barbosa
            - antonio-molina
            - biel-stela-ballester
            - cheuk-ting-ho
            - eva-martin-del-pico
            - gema-parreno
            - jimena-escobar-bermudez
            - kemalcan-bora
            - marc-pous
            - pavel-lonkin
            - pere-miquel-brull
  - title: Organizers
    id: organizers
    levels:
      - people_per_line: 4
        people:
          - natalia-padilla
          - laura-perez-mayos
          - xavi-francisco-gilabert
          - mireia-alvarez-dominguez

spansDuration: 15
numTracks: 3
eventTimes:
  [
    "9:00",
    "9:15",
    "9:30",
    "9:45",
    "10:00",
    "10:15",
    "10:30",
    "10:45",
    "11:00",
    "11:15",
    "11:30",
    "11:45",
    "12:00",
    "12:15",
    "12:30",
    "12:45",
    "13:00",
    "13:15",
    "13:30",
    "13:45",
    "14:00",
    "14:15",
    "14:30",
    "14:45",
    "15:00",
    "15:15",
    "15:30",
    "15:45",
    "16:00",
    "16:15",
    "16:30",
    "16:45",
    "17:00",
    "17:15",
    "17:30",
    "17:45",
  ]
legend:
  - type: workshop
  - type: talk
  - separator: true
  - level: beginner
  - level: intermediate
  - level: advanced

# The rooms of this edition, in the order the grid first names them. A room is
# a record with an id because the colour of a block now comes from it: the
# template gives every room of an event one colour of the agenda palette and
# keeps it for the whole day. See partials/agenda_entry.html.
rooms:
  - id: sala-dactes-ada-lovelace
    name: "Sala d'actes Ada Lovelace"
  - id: sala-hedy-lamarr-margarita-salas
    name: "Sala Hedy Lamarr / Margarita Salas"
  - id: sala-hipatia-dalexandria
    name: "Sala Hipàtia d'Alexandria"
  - id: open-air-terrace
    name: "Open-air terrace"

# The talks of this edition: what was said, by whom, in which language. A talk
# carries no time and no room, because it is the content and not the slot.
# agenda below is what places it on the grid, and one talk can take more than
# one slot. The id is derived from the title and is the anchor a photo of the
# gallery links to, so it must not change.
talks:
  - id: machine-learning-en-produccion-experimentos-con-versionado
    title: "Machine Learning en producción: Experimentos con versionado de datos con DVC y VSCode"
    title_lang: Spanish
    speakers: [gema-parreno]
    type: workshop
    language: es
    topic: "Data Science and MLOPS"
    duration_minutes: 75
    description: "El workshop utiliza herramientas OpenSource de DVC y su extension para VSCode para preparar los experimentos de Data Science para su versionado y puesta en producción. Utilizamos el IDE de VS Code y lo transformamos en una plataforma de experimentación de Machine Learning.<br><br>A través de un caso de uso real, veremos las posibilidades que ofrece el implementar practicas de Software a los proyectos de Data Science y herramientas para versionar los experimentos de Machine Learning.<br><br>Objetivo : ayudar a los data scientist a salir de los notebooks y preparar la experimentación y puesta en producción de manera un poco mas robusta ."
  - id: friendly-fuzzing-for-your-python-saas-applications
    title: "Friendly fuzzing for your Python SaaS applications"
    speakers: [pavel-lonkin]
    type: workshop
    language: en
    topic: "Security, software development"
    duration_minutes: 75
    description: "Tired of bugs? Security issues in your Python code? Fuzzing approach can help you to decrease number of issues received from your production environment using only few lines of code! In this topic you are going to:<br/><ul><li>learn what the fuzzing is and what type of fuzzing exists</li><li>learn how it helps to catch the bugs and find potential security issues when you are sleeping</li><li>\"fuzz\" your first python application</li><li>find the way to fuzz your REST Django application</li><li>discover the instruments to fuzz any API</li></ul>"
  - id: how-many-ants-can-carry-an-elephant-pushing-the-limits-of
    title: "How many ants can carry an elephant? Pushing the limits of AWS Chalice"
    speakers: [kemalcan-bora]
    type: workshop
    language: en
    topic: "Serverless apps"
    duration_minutes: 75
    description: "Chalice is a framework for writing serverless apps in python. It allows you to quickly create and deploy applications that use AWS Lambda. Serverless applications generally have some limits like RAM, storage, and CPU.. and the main purpose is simple functions like login, registration, etc. So what if we want to create an ML application? How can we handle our limits? don't panic young Skywalker. We have to push our limits and we'll install NumPy, and Sci-kit learn libraries and our app will roam freely in the cloud in peace."
  - id: build-air-quality-sensors-with-python-and-choose-your-own
    title: "Build Air Quality Sensors with Python and choose your own adventure!"
    speakers: [marc-pous]
    type: workshop
    language: en
    topic: "Internet of Things and Air quality sensors"
    duration_minutes: 75
    description: "The goal of this hands-on workshop is to build an Air Quality sensor (with Raspberry Pis) using Python to get the data from the sensors. From here you are going to choose what happens next. Would you like to store the data on a database? Visualize it? Send it to a Cloud? or to a Telegram bot? You choose your own adventure! Everything in the edge using containers, python and balena."
  - id: build-a-full-stack-app-with-flask-and-vue
    title: "Build a full-stack app with Flask and Vue"
    speakers: [eva-martin-del-pico]
    type: workshop
    language: en
    topic: "Web apps"
    duration_minutes: 75
    description: "In this workshop we will build a complete web application using Flask Python micro framework in the backend and Vue.js JS framework in the frontend. Both Flask and Vue are easy to learn, yet flexible and powerful, making them a great choice for those who want to create modern and robust applications - and do it fast."
  - id: python-as-a-gis-tools-howtos-and-gotchas
    title: "Python as a GIS: Tools, howtos and gotchas"
    speakers: [biel-stela-ballester]
    type: workshop
    language: en
    topic: "Python as a GIS"
    duration_minutes: 75
    description: "Use python as a GIS with Rasterio, Xarray and GeoPandas"
  - id: building-an-end-to-end-open-source-modern-data-platform-for
    title: "Building an End-to-End Open-Source Modern Data Platform for Biomedical Data"
    speakers: [alberto-labarga]
    type: workshop
    language: [en, es]
    topic: "Data engineering"
    duration_minutes: 75
    description: "A detailed guide to help you navigate the modern data stack and build your own platform using open-source technologies.<br/><br/>Data engineering has experiences enormous growth in the last years, allowing for rapid progress and innovation as more people than ever are thinking about data resources and how to better leverage them.<br/><br/>In this talk we will explore the related technologies and build from scratch an end-to-end modern data platform for the analysis of medical data. We will be using open-source tools and libraries, including python-based DBT, Apache Airflow and Querybook.<br/><br/>The platform will consist of the following components:<ul><li>Data warehouse</li><li>Data integration</li><li>Data transformation</li><li>Data orchestration</li><li>Data visualization</li></ul>"
  - id: cuando-los-precios-suben-scrapy
    title: "Cuando los precios suben: Scrapy"
    title_lang: Spanish
    speakers: [jimena-escobar-bermudez]
    type: workshop
    language: es
    topic: "Scrapy"
    duration_minutes: 75
    description: "Criptomonedas, la guerra en Ucrania, la pandemia, la falta de componentes y toda la serie de catastróficas desdichas que estamos sufriendo nos ha llevado a un punto en el que el precio de todo ha subido. En este taller aprenderemos a usar Scrapy para conseguir descargar, almacenar y comparar los precios de los productos que queramos."
  - id: inside-out-or-how-to-get-your-app-observable
    title: "Inside out. Or how to get your app observable"
    speakers: [antonio-molina]
    type: workshop
    language: es
    topic: "Observability"
    duration_minutes: 75
    description: "Observability is key in distributed systems and it is gaining importance within the industry. So it is important to understand the concepts behind the idea of observabiity and why is important to us, as developers, to make our developments \"observable\". Being able to create software that is easy to debug while systems scales and complexity grows will level up us as developers and will make our clients and employers far happier. This is what this workshop is about. From a brief theory of what observability is to some practices and best practices."
  - id: lightning-talks-session-1-coffee
    title: "Lightning talks (session 1) & coffee"
    type: talk
    duration_minutes: 15
    description: " <h2>Lightning talks</h2>\n<b>How to beat your friends in fantasy football</b><br> <i>Alex Molas</i> <p><q>Have you ever wondered how to win your friends in a football fantasy league? In this talk I will show how to use python to get the best performant team by using web scraping, operations research, and machine learning!</q></p>\n<b>Measuring media bias</b><br> <i>Luis Ignacio Menéndez</i> <p><q>We'd like to talk about a research project (working progress) trying to measure media bias in Spanish TV news. For this, we employ techniques of speech recognition, speaker diarization and text analysis. This project is carried on by PhD students of the Economics department at Universitat Autònoma de Barcelona.</q></p>\n<b>Astropy 5.X: astronomical tools for everybody</b><br> <i>Francesc Vilardell Sallés</i> <p><q>Astropy is now a mature python library with over 34.000 commits on Github and hundreds of contributors. Astropy is still little known beyond the astronomical community, but offers several powerful tools that are useful to all python developers. In this lightning talk I will present some of these tools. </q></p>\n<b>Fighting climate change the Python way</b><br> <i>Rafael Giménez</i> <p><q>The Digital Team at Cetaqua works in bringing state of the art AI (Computer Vision, Reinforcement Learning) to one of the most crucial issues of our time: water and environmental management. The talk aims to briefly showcase how we use Python for that.</q></p>\n<b>PyCamp España </b><br> <i>Johanna Sanchez</i> <p><q>Invitación a la comunidad para participar de un evento diferente</q></p>\n<b>PyLadies España y PyCon ES 2023</b><br> <i>Johanna Sanchez</i> <p><q>Invitación a la comunidad para participar en conferencia y comunidades</q></p> "
  - id: using-numba-effectively-today
    title: "Using Numba Effectively Today"
    speakers: [cheuk-ting-ho]
    type: workshop
    language: en
    topic: "Data Science"
    duration_minutes: 75
    description: "Numba is syntactically easy to use - just add a decorator, but actually very hard to use effectively. The reason being it is difficult to understand what Numba does to speed up the numeric operation. This workshop will provide all the knowledge that you need to make Numba works for you."
  - id: making-sense-of-your-data-platform-with-openmetadata
    title: "Making sense of your Data Platform with OpenMetadata"
    speakers: [pere-miquel-brull]
    type: workshop
    language: en
    topic: "Data Management"
    duration_minutes: 75
    description: "OpenMetadata is an open-source project (https://open-metadata.org/) that is building a metadata standard and a centralized and shared metadata platform on top of it. In this workshop, we will explore the tool, how it works, and bit by bit we will dive into its implementation and design."
  - id: tdd-coding-dojo
    title: "TDD Coding Dojo"
    speakers: [ana-eliza-barbosa]
    type: workshop
    language: en
    topic: "Test driven development"
    duration_minutes: 75
    description: "Nowadays software products are becoming so complex that is unimaginable that one software engineer would develop it alone without any sort of automated testing, so let's get together to practice Test Driven Development while pair programming with the other workshop participants. We will solve some code challenges together, under a bit of friendly time pressure and changing development hats every 5 minutes. If you are interested in knowing how it all looks like then join the workshop!"
  - id: lightning-talks-session-2-closing-session-kahoot
    title: "Lightning talks (session 2) + closing session & Kahoot"
    type: talk
    duration_minutes: 15
    description: " <h2>Lightning talks</h2>\n<b>Intenciones ganadoras: Cómo implementar la arquitectura de un chatbot basado en intenciones</b><br> <i>Nadal Llabrés Belmar</i> <p><q>En esta charla explicaremos los aspectos fundamentales de cómo diseñar e implementar un chatbot basado en el reconocimiento de intenciones desde el punto de vista de la ingeniería de Software. Mediante un caso de uso, exploramos cómo diseñar e implementar una arquitectura que nos permita integrar y gestionar la base de conocimiento que requiere el bot para su aprendizaje, integrar un motor de reconocimiento de intenciones que sea capaz de entender a los usuarios a partir de un entendimiento contextual de una conversación e integrar un sistema de respuestas en distintos formatos (voz, texto, imágenes, vídeos).</q></p>\n<b>Satellite super-resolution and 3d scenes</b><br> <i>Biel Stela</i> <p><q>Match the resolution of Landsat imagery to fine grained Sentinel using Deep Learning, then create dynamic evolving scenes with blender. </q></p>\n<b>trrex: Efficient keyword extraction with regex</b><br> <i>Daniel Mesejo</i> <p><q>In this talk I'm going to introduce the trrex package, for performing efficient keyword extraction with regular expressions. Additionally I'll show how to integrate it with pandas for text cleaning, how to use it with spacy to build a gazetteer and how to perform fuzzy matching with the regex library.</q></p>\n<b>Transactions</b><br> <i>Christian Barra</i> <p><q>The goal of the LT is to give to the audience a brief overview about DB transactions, why there are important and how to leverage them for some specific use cases where they play a critical role.</q></p>\n<b>Optimal binning using Python</b><br> <i>Guillermo Navas Palencia</i> <p><q>Presentation of the OptBinning library, a Python library to perform optimal binning and scorecard modelling. Description of main features, current roadmap and applications.</q></p> "

# The grid, one row per slot of the day, in the order it is printed. A slot
# names the talk it holds, or carries its own label and type when it holds
# none: a break, the group photo, the welcome. The level and the requirements
# sit here and not on the talk, because they are what the slot asks of whoever
# walks into it. A start is always quoted: YAML 1.1 reads an unquoted 9:00 as
# the integer 540.
agenda:
  - start: "9:00"
    credited_as: "PyDay BCN 2022 Organising Committee"
    track_length: 3
    room: sala-dactes-ada-lovelace
    type: group
    label: "Registration & Welcome"
    duration_minutes: 15
  - start: "9:30"
    track_length: 1
    room: sala-dactes-ada-lovelace
    talk: machine-learning-en-produccion-experimentos-con-versionado
    python_level: intermediate
    topic_level: intermediate
    requirements: "<ul><li>Laptop , requirements.txt installed.</li><li>VS Code IDE.</li></ul>"
  - start: "9:30"
    track_length: 1
    room: sala-hedy-lamarr-margarita-salas
    talk: friendly-fuzzing-for-your-python-saas-applications
    python_level: intermediate
    topic_level: beginner
    requirements: "<ul><li>Initial python knowledges</li><li>Would be great to know Django</li><li>Laptop with installed Docker and Docker Compose</li><//ul>"
  - start: "9:30"
    track_length: 1
    room: sala-hipatia-dalexandria
    talk: how-many-ants-can-carry-an-elephant-pushing-the-limits-of
    python_level: beginner
    topic_level: beginner
    requirements: "Python, AWS account, AWS chalice framework"
  - start: "11:00"
    track_length: 3
    room: open-air-terrace
    type: coffee
    label: "Coffee break"
    duration_minutes: 15
  - start: "11:30"
    track_length: 1
    room: sala-dactes-ada-lovelace
    talk: build-air-quality-sensors-with-python-and-choose-your-own
    python_level: beginner
    topic_level: beginner
    requirements: "Laptop"
  - start: "11:30"
    track_length: 1
    room: sala-hedy-lamarr-margarita-salas
    talk: build-a-full-stack-app-with-flask-and-vue
    python_level: beginner
    topic_level: beginner
    requirements: "<ul><li>Familiarity with Python and basic understanding of HTML and CSS (ideally JS too, but it is not necessary)</li><li>Laptop with Python3, Flask, NuxtJS and Docker.</li></ul>"
  - start: "11:30"
    track_length: 1
    room: sala-hipatia-dalexandria
    talk: python-as-a-gis-tools-howtos-and-gotchas
    python_level: intermediate
    topic_level: intermediate
    requirements: "Laptop with conda if attendees want to follow the notebooks and do some exercises, just ears and be present otherwise."
  - start: "13:00"
    track_length: 3
    room: open-air-terrace
    type: photo
    label: "Group photo"
    duration_minutes: 0
  - start: "13:15"
    track_length: 3
    room: open-air-terrace
    type: lunch
    label: "Lunch break"
    duration_minutes: 30
  - start: "14:00"
    track_length: 1
    room: sala-dactes-ada-lovelace
    talk: building-an-end-to-end-open-source-modern-data-platform-for
    python_level: beginner
    topic_level: intermediate
    requirements: "Follow the installation steps in https://github.com/alabarga/pybcn22-modern-data-stack"
  - start: "14:00"
    track_length: 1
    room: sala-hedy-lamarr-margarita-salas
    talk: cuando-los-precios-suben-scrapy
    python_level: beginner
    topic_level: beginner
    requirements: "Laptop"
  - start: "14:00"
    track_length: 1
    room: sala-hipatia-dalexandria
    talk: inside-out-or-how-to-get-your-app-observable
    python_level: beginner
    topic_level: beginner
    requirements: "Laptop"
  - start: "15:30"
    track_length: 3
    room: sala-dactes-ada-lovelace
    talk: lightning-talks-session-1-coffee
  - start: "16:00"
    track_length: 1
    room: sala-dactes-ada-lovelace
    talk: using-numba-effectively-today
    python_level: intermediate
    topic_level: intermediate
    requirements: "This workshop is for Data scientists or developers who have math-heavy code that would like to speed up with the benefit of Numpy and Numba.<br/><br/>What is required from attendees<br/><br/><ul><li>- A computer with a stable internet connection (useful to look up information);</li><li>- Python 3.8 or above;</li><li>- Jupyter and Numba installed (detail about Python libraries required will be announced later);</li><li>- An opened mind and ready to learn something new</li></ul>"
  - start: "16:00"
    track_length: 1
    room: sala-hedy-lamarr-margarita-salas
    talk: making-sense-of-your-data-platform-with-openmetadata
    python_level: intermediate
    topic_level: beginner
    requirements: "For the folks who would like to follow along, a laptop with docker compose"
  - start: "16:00"
    track_length: 1
    room: sala-hipatia-dalexandria
    talk: tdd-coding-dojo
    python_level: beginner
    topic_level: beginner
  - start: "17:30"
    track_length: 3
    room: sala-dactes-ada-lovelace
    talk: lightning-talks-session-2-closing-session-kahoot

---

## About PyDay BCN 2022

We are organizing the **the sixth edition** of PyDay in Barcelona!

PyDay is an event full of FREE **python-related workshops** and activities for the Python community, organized once per year. Over the last five editions, PyDay has become a great opportunity to share our love for Python and engage users, companies and newcomers into it!

### When and where

It is scheduled for **Saturday 26th November** in [Canòdrom - Ateneu d'Innovació Digital i Democràtica](https://g.page/Canodrom?share), from 9:30pm to 19:00pm CET, aprox.

### A full day of in-person hands-on workshops

PyDay BCN 2022 will have different **thematic tracks** --e.g. data science, web development, security-- with hands-on workshops of about 90 minutes in which participants will learn how to use different libraries, tools and techniques, fully guided by members of the community and support volunteers.

### Participate in Kahoot and win prizes!

We will host a Kahoot game with questions about PyBCN and Python in general, with prizes for the fastest players. Will you miss it?!
