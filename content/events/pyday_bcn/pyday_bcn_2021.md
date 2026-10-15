---
title: "PyDay BCN (2021)"
year: 2021
# The day of this edition, from the Meetup export, which records it per event.
date: 2021-11-27
# The venue of this edition, from the Meetup export, which records it per event.
venue: "Canòdrom"
description: "Post-pandemic edition!"
menu:
  main:
    parent: 'PyDay BCN'
weight: 5
aliases:
- /pyday-bcn-2021
heroBackground: /images/photos/pyday2021.jpeg

layout: event

free_text_sections:
    - title: Important dates
      id: important_dates
      content: "<b>11th October</b>: Call for proposals opening<br/>
        <b>24th October</b>: Call for proposals closing<br/>
        <b>17th November</b>: Program available<br/>
        <b>19th November, 9AM</b>: Early registration open for PyBCN members, PyDay speakers and sponsors<br/>
        <b>22nd November, 9AM</b>: General registration open through <a href=\"https://www.eventbrite.es/e/entradas-pydaybcn-2021-212686419807\" target=\"_blank\">eventbrite</a><br/>
        <b>27th November</b>: PyDay BCN 2021"
    - title: Registration
      id: registration
      content: "Registration to the general public will be open on <b>Monday 22nd November, 9AM</b>, through <a href=\"https://www.eventbrite.es/e/entradas-pydaybcn-2021-212686419807\" target=\"_blank\">eventbrite</a>.<br/><br/>Please have a look at the schedule below and choose which talks you would like to attend beforehand."

sponsor_levels:
    - sponsors_per_line: 2
      sponsors: [canodrom]
      name: Venue
    - sponsors_per_line: 3
      sponsors: [bling, cloudblue, hybridtheory, iomed, onna, preply, qustodio, rover, typeform]
      name: Gold
    - sponsors_per_line: 3
      sponsors: [bmat, digitalfems, edgetier, orpheus, verse]
      name: Supporting

people_sections:
    - title: Speakers
      id: speakers
      levels:
        - people_per_line: 4
          people:
              - albert-franzi-cros
              - alejandro-nicolas
              - alexandre-savio
              - anton-caceres
              - antonio-molina
              - christian-adell
              - david-de-la-iglesia-castro
              - diego-gonzalez
              - elisabeth-ortega-carrasco
              - esperanza-buitrago
              - gabriel-de-maeztu
              - jordi-mur
              - laysa-uchoa
              - marc-pous
              - mariana-meireles
              - matteo-bruno
              - sergi-ortiz
              - vincent-choubard
              - vivek-sharma
    - title: Organizers
      id: organizers
      levels:
        - people_per_line: 4
          people:
              - laura-perez-mayos
              - natalia-padilla
              - david-arcos
              - nuria-pujol-vilanova
              - xavi-francisco-gilabert
              - ruben-berenguel
              - eloi-puertas-prats
              - mireia-alvarez-dominguez

spansDuration: 15
numTracks: 4
eventTimes: ["9:00", "9:15", "9:30", "9:45", "10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45", "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30", "16:45", "17:00", "17:15", "17:30", "17:45"]
legend:
    - type: workshop
    - type: talk
    - separator: true
    - level: beginner
    - level: intermediate
    - level: advanced
    - separator: true
    - type: sponsor

# The rooms of this edition, in the order the grid first names them. A room is
# a record with an id because the colour of a block now comes from it: the
# template gives every room of an event one colour of the agenda palette and
# keeps it for the whole day. See partials/agenda_entry.html.
rooms:
  - id: open-air-terrace
    name: "Open-air terrace"
  - id: room-actes
    name: "Room Actes"
  - id: room-guinardo
    name: "Room Guinardó"
  - id: room-gotica
    name: "Room Gòtica"
  - id: room-raval
    name: "Room Raval"
  - id: all-rooms
    name: "All rooms"

# The talks of this edition: what was said, by whom, in which language. A talk
# carries no time and no room, because it is the content and not the slot.
# agenda below is what places it on the grid, and one talk can take more than
# one slot. The id is derived from the title and is the anchor a photo of the
# gallery links to, so it must not change.
talks:
  - id: how-to-create-data-apps-with-python
    title: "How to create Data apps with Python"
    speakers: [sergi-ortiz]
    type: workshop
    language: es
    topic: "Data Apps"
    duration_minutes: 75
    description: "Data products are the future of data. And Data Apps (and AI Apps) are an important chunk of this future. For Python coders there are many frictions to create Data Apps nowadays, we will try to address them all and create a Data App (FE - BE and DevOps) during the hands on session"
  - id: build-a-chat-application-that-lets-you-speak-multiple
    title: "Build a chat application that lets you speak multiple languages"
    speakers: [diego-gonzalez]
    type: workshop
    language: en
    topic: "Web development"
    duration_minutes: 75
    description: "Learn how to build a chat application that can translate messages across multiple languages using only a few technologies (Python among them, of course!)"
  - id: implementing-your-api-with-fastapi
    title: "Implementing your API with FASTAPI"
    speakers: [esperanza-buitrago]
    type: workshop
    language: en
    topic: "Software Engineering"
    duration_minutes: 75
    description: "Implement your API with FastAPI from scratch and make it run in local."
  - id: building-the-cloud-with-python-getting-started-with-aws-cdk
    title: "Building the Cloud with Python: getting started with AWS CDK"
    speakers: [anton-caceres, alexandre-savio]
    type: workshop
    language: en
    topic: "Cloud-native Python applications"
    duration_minutes: 75
    description: "With emerging cloud technologies it is just a matter of time until most backends run in serverless or container-based environments. This workshop is showcasing a recently released open-source Cloud Development Kit by Amazon, which lets us control cloud resources just like we control our application logic - in pure Python. CDK offers high-level abstraction to define AWS resources imperatively as customizable and reusable Python classes. Unfortunately, there are not many tutorials available yet and the documentation is limited. So we will be happy to share with you how to: 1) Break down AWS infrastructure into reusable constructs represented by Python classes; 2) Combine own and public constructs into Stack applications; 3) Deploy CDK apps to AWS cloud"
  - id: creating-cute-user-interfaces-in-python-with-qt
    title: "Creating cute user interfaces in python with Qt"
    speakers: [elisabeth-ortega-carrasco]
    type: workshop
    language: es
    topic: "User interfaces"
    duration_minutes: 75
    description: "Most of us learn to use python as a command line tool, asking information to the users and passing them to the code as arguments. Some of us later moved to Django and related web development tools, to have a better interaction with the user paying the cost of fighting against the web layout in different languages. Few of us faced tkinter to build our first user interfaces with more or less success, but almost none of us were happy with the result of the user interfaces created in pure python.<br/>In \"Creating cute user interfaces in python with Qt\" I will show you how to enjoy creating user interfaces interactively with some clicks and few lines of code using the PySide6 library with all the Qt potential behind it."
  - id: vector-search-engines-with-python-from-embeddings-to
    title: "Vector search engines with Python: from embeddings to similarity search"
    speakers: [gabriel-de-maeztu]
    type: workshop
    language: en
    topic: "Data Science"
    duration_minutes: 75
    description: "I would cover the following topics, providing to anyone familiar with Python an overall idea about embeddings and similarity search in addition to a tutorial with with a use cases:<br/><ul><li>What are Vector Embeddings?</li><li>What is a Vector Database?</li><li>What is Vector Similarity Search?</li><li>So what do I do with my vector embedding?</li><li>Efficient Filtering of Vectors</li><li>Use cases: text, image, video, audio, graph and relational data</li><li>Let's build a search engine: Semantic textual search with vector embeddings<ol><li>Get the data</li><li>Create the embeddings</li><li>Upload the embeddings</li> <li>Query the data</li></ol></li></ul>"
  - id: introduction-to-django
    title: "Introduction to Django"
    speakers: [vincent-choubard]
    type: workshop
    language: en
    topic: "Web Development"
    duration_minutes: 75
    description: "We are going to build a web app using Django to create a pet profile and store it."
  - id: microservicios-en-la-vida-moderna-un-enfoque-python-centrico
    title: "Microservicios en la vida moderna. Un enfoque python-centrico."
    title_lang: Spanish
    speakers: [antonio-molina, erik-tordera, pablo-fernandez]
    type: workshop
    language: es
    topic: "Architecture"
    duration_minutes: 75
    description: "Las arquitecturas distribuidas y los microservicios están en boca de todos. Unos defienden que son la cura para todos los males mientras que otros advierten que la complejidad añadida puede desembocar en frustraciones y malos sueños. En este workshop, proponemos una reflexión sobre arquitecturas distribuidas a través de un ejercicio práctico. Aunque orientado a desarrollos basados en nuestro querido python, proponemos salir de nuestra zona de confort para profundizar juntos en eso que llamamos dev/ops y de cómo los equipos podemos operar nuestros servicios asi como un primer contacto con las herramientas que nos ayudarán a minimizar los riesgos y las complejidades (tales como Helm, MiniKubes, Istio, GRPC, Prometheus, etc). Acompañanos en este rato a pensar y entender algunos de los problemas, soluciones y buenas prácticas en este tipo de arquitecturas."
  - id: making-mlops-uncool-again
    title: "Making MLOps uncool again"
    speakers: [david-de-la-iglesia-castro]
    type: workshop
    language: es
    topic: "Data science"
    duration_minutes: 75
    description: "In this workshop we will learn how to build an \"MLOps workflow\" by extending the power of Git and GitHub. Using only open source tools and without the need of external platfforms or complicated infrastructure. <br/><br/>We will use [HuggingFace] (https://huggingface.co/) to train a model that automatically adds labels to GitHub issues and we will extend the power of Git with [DVC](https://dvc.org/) and [CML](https://cml.dev/) in order to build a living Data Registry and set up a Continuous Training and Deployment loop for our model."
  - id: causal-data-science-workshop
    title: "Causal Data Science workshop"
    speakers: [jordi-mur]
    type: workshop
    language: en
    topic: "Data science"
    duration_minutes: 75
    description: "Causal data science is a hot topic in the business applications of machine learning that go beyond predicting a value to actually deciding the best intervention to take based on such a prediction. We will briefly provide the key concepts and methods of causal inference (the topic of this year's Nobel prize in economics!), and then move on to some hands-on practice with Jupyter notebooks based on business use cases. No prior knowledge of causal inference is required."
  - id: how-to-beat-imposter-syndrome-confessions-of-a-developer
    title: "How to beat imposter syndrome: confessions of a developer"
    speakers: [matteo-bruno]
    type: talk
    language: en
    duration_minutes: 75
    description: "Do you feel like you don't belong, you don't deserve what you've achieved, everyone in your office is more talented than you? Do you have imposter syndrome... too?<br/><br/>Impostor syndrome is a psychological pattern in which people doubt their accomplishments or talents and have a persistent internalized fear of being exposed as a \"fraud\".<br/><br/>Imposter syndrome is common across all industries, but the increasing pressure to be successful in your professional career is taking its toll on employees, affecting more than half workers, including our speaker :)<br/><br/>After many years working in tech for a lot of companies, (from startups to big corporations) in many business fields, Matteo discovered a way to overcome self-doubt and turn this weird feeling into a booster for greater achievements.<br/><br/>He'd like to share all his experience with everyone, making you understand that feeling inadequate is quite common and that there are ways to approach it in a proactive way."
  - id: building-a-dag-factory
    title: "Building a DAG Factory"
    speakers: [albert-franzi-cros]
    type: talk
    language: en
    duration_minutes: 30
    description: "At Typeform there are several teams that interact with data. Machine learning engineers, data scientists, data analysts, insights teams. None of them should have to worry about Airflow operators, upstream tasks, downstream tasks and all the million ways that writing Airflow DAGs by hand makes you miserable.<br/><br/>This is where the Data Platform teams comes to save the day and create Chester, a DAG factory, powered by a set of API connectors handled by us. Other teams only need to worry about where the data comes from and where it goes to, and write some YAML that describes it. All the rest is handled by Chester's superpowers."
  - id: burnout-paradise-buenas-practicas-para-evitar-el-burnout-en
    title: "Burnout Paradise: buenas prácticas para evitar el burnout en desarrollo"
    title_lang: Spanish
    speakers: [alejandro-nicolas]
    type: talk
    language: es
    duration_minutes: 30
    description: "Durante la conferencia se tratará la programación desde el punto de vista psicológico, tanto a nivel individual como a nivel de equipo. Se presentarán los posibles efectos de una rutina de trabajo mal llevada, se evaluarán las causas y se propondrán sistemas o hábitos que afectarían positivamente al bienestar de un desarrollador en un mundo en el que el trabajo en remoto se ha implantado de manera inesperada en nuestro día a día."
  - id: build-a-machine-learning-iot-device-running-python
    title: "Build a Machine Learning IoT Device running Python"
    speakers: [marc-pous]
    type: workshop
    language: en
    topic: "IOT, ML, Edge AI"
    duration_minutes: 75
    description: "Learn on this workshop how to create a fleet of edge AI devices in a simple way using Python, Edge Impulse and balena.<br/><br/>During the workshop attendants will learn how to create a Bird Watcher using a Raspberry Pi and a USB camera (or Pi Camera). Using Python we will get the feed from the camera, apply machine learning models from Edge Impulse and send telegram messages. Finally we will be able to deploy a fleet of Bird Watchers in a simple way all around the world.<br/><br/>The goal of this session is to introduce IoT and AI topics to Python developers. Topics such as the Internet of Things, Artificial Intelligence and citizen science are consistently united in a single project. "
  - id: the-moons-of-jupyter-widgets-ecosystem
    title: "The moons of Jupyter: widgets ecosystem"
    speakers: [mariana-meireles, laysa-uchoa]
    type: workshop
    language: en
    topic: "Data science, scientific computing"
    duration_minutes: 75
    description: "Jupyter has much more to offer than an interface for notebooks, the widgets ecosystem can leverage your research, dashboards, data visualization and much more!<br/>In the moons of Jupyter workshop we aim to give an overview of the standard widget library as well the expanded ecosystem created by contributors."
  - id: signal-processing-from-neurons-to-mars
    title: "Signal Processing - From Neurons to Mars!"
    speakers: [vivek-sharma]
    type: workshop
    language: en
    topic: "Signal Processing"
    duration_minutes: 75
    description: "What we see around us with time as its one dimension is a Signal! and to comprehend we just need to analyze it. This workshop is all about the last pit. We'll begin by examining some brain impulses, then move on to our environment, and lastly, Mars! Let's see what's going on over there.<br/>You'll learn how to make a frequency-specific filter, how to use the Fourier transform, and how to visualize data. <br/>Don't forget to bring your sense of wonder."
  - id: keeping-sync-between-datasets-with-diffsync
    title: "Keeping sync between datasets with Diffsync"
    speakers: [christian-adell]
    type: workshop
    language: en
    topic: "Data set synchronisation"
    duration_minutes: 75
    description: "Working with multiple data models (and data inventories) while keeping a common state is a problem that involves a diff calculation first and then a synchronisation in one direction or another, sometimes solving the mapping between the data models.<br/>Diffsync (https://github.com/networktocode/diffsync) library helps with this common problem by providing an easy data modeling and structured CRUD operations to update the state."

# The grid, one row per slot of the day, in the order it is printed. A slot
# names the talk it holds, or carries its own label and type when it holds
# none: a break, the group photo, the welcome. The level and the requirements
# sit here and not on the talk, because they are what the slot asks of whoever
# walks into it. A start is always quoted: YAML 1.1 reads an unquoted 9:00 as
# the integer 540.
agenda:
  - start: "9:00"
    credited_as: "PyDay BCN 2021 Organising Committee"
    track_length: 4
    room: open-air-terrace
    type: group
    label: "Registration & Welcome"
    duration_minutes: 15
  - start: "9:30"
    track_length: 1
    room: room-actes
    talk: how-to-create-data-apps-with-python
    python_level: intermediate
    topic_level: beginner
  - start: "9:30"
    track_length: 1
    room: room-guinardo
    talk: build-a-chat-application-that-lets-you-speak-multiple
    python_level: intermediate
    topic_level: intermediate
    sponsor: "Preply"
  - start: "9:30"
    track_length: 1
    room: room-gotica
    talk: implementing-your-api-with-fastapi
    python_level: beginner
    topic_level: beginner
    requirements: "<ul><li>Python3</li><li>Visual Studio Code</li><li>Pip3</li><li>Conda</li><li>We'll do everything from scratch: such as installing FastAPI, uvicorn and typing</li></ul>"
  - start: "9:30"
    track_length: 1
    room: room-raval
    talk: building-the-cloud-with-python-getting-started-with-aws-cdk
    python_level: intermediate
    topic_level: beginner
    requirements: "Python 3.8+"
  - start: "11:00"
    track_length: 4
    room: open-air-terrace
    type: coffee
    label: "Coffee Break"
    duration_minutes: 15
    sponsor: "Bling"
  - start: "11:30"
    track_length: 1
    room: room-actes
    talk: creating-cute-user-interfaces-in-python-with-qt
    python_level: intermediate
    topic_level: beginner
    requirements: "PySide6 (https://pypi.org/project/PySide6/)<br/><br/>Course repo:<br/>Empty and private until some days before the meeting but it will be this: https://github.com/draentropia/pyside-pyday21"
  - start: "11:30"
    track_length: 1
    room: room-guinardo
    talk: vector-search-engines-with-python-from-embeddings-to
    python_level: intermediate
    topic_level: intermediate
    sponsor: "IOMED"
  - start: "11:30"
    track_length: 1
    room: room-gotica
    talk: introduction-to-django
    python_level: beginner
    topic_level: beginner
    requirements: "Ideally have python and django installed on your machine by following <a href=\"https://docs.djangoproject.com/en/3.2/intro/install/\">https://docs.djangoproject.com/en/3.2/intro/install/</a>"
    sponsor: "Rover"
  - start: "11:30"
    track_length: 1
    room: room-raval
    talk: microservicios-en-la-vida-moderna-un-enfoque-python-centrico
    python_level: beginner
    topic_level: intermediate
    sponsor: "Qustodio"
  - start: "13:00"
    track_length: 4
    room: open-air-terrace
    type: photo
    label: "Group photo"
    duration_minutes: 0
  - start: "13:15"
    track_length: 4
    room: open-air-terrace
    type: lunch
    label: "Lunch"
    duration_minutes: 30
  - start: "14:00"
    track_length: 1
    room: room-actes
    talk: making-mlops-uncool-again
    python_level: intermediate
    topic_level: intermediate
    requirements: "A browser (preferably Google Chrome)<br/>Github account."
  - start: "14:00"
    track_length: 1
    room: room-guinardo
    talk: causal-data-science-workshop
    python_level: intermediate
    topic_level: beginner
    requirements: "Bring your own laptop<br/>Libraries: Jupyter notebooks will use DoWhy: https://microsoft.github.io/dowhy/index.html"
  - start: "14:00"
    track_length: 1
    room: room-gotica
    talk: how-to-beat-imposter-syndrome-confessions-of-a-developer
    sponsor: "Onna"
  - start: "14:00"
    track_length: 1
    room: room-raval
    talk: building-a-dag-factory
    sponsor: "Typeform"
  - start: "14:45"
    track_length: 1
    room: room-raval
    talk: burnout-paradise-buenas-practicas-para-evitar-el-burnout-en
    sponsor: "Hybrid Theory"
  - start: "15:30"
    track_length: 4
    room: open-air-terrace
    type: coffee
    label: "Coffee Break"
    duration_minutes: 15
    sponsor: "CloudBlue"
  - start: "16:00"
    track_length: 1
    room: room-actes
    talk: build-a-machine-learning-iot-device-running-python
    python_level: intermediate
    topic_level: beginner
    requirements: "Bring your own Raspberry Pi (3 or 4) with camera (USB or Pi Camera) with your laptop to try to deploy together a ML edge device."
  - start: "16:00"
    track_length: 1
    room: room-guinardo
    talk: the-moons-of-jupyter-widgets-ecosystem
    python_level: intermediate
    topic_level: beginner
    requirements: "https://github.com/jupyter-widgets/tutorial#readme<br/><br/>But a link to a Binder project where you can run the workshop without installing anything on your machine will also be provided. It’s recommendable to install requirements locally, though."
  - start: "16:00"
    track_length: 1
    room: room-gotica
    talk: signal-processing-from-neurons-to-mars
    python_level: beginner
    topic_level: beginner
  - start: "16:00"
    track_length: 1
    room: room-raval
    talk: keeping-sync-between-datasets-with-diffsync
    python_level: intermediate
    topic_level: beginner
    requirements: "Try to run Nautobot Lab (https://github.com/nautobot/nautobot-lab) in Docker, as we'll use it as support during the workshop."
  - start: "17:30"
    credited_as: "PyDay BCN 2021 Organising Committee"
    track_length: 4
    room: all-rooms
    type: group
    label: "Closing session & Kahoot"
    duration_minutes: 15

# Photos published by PyBCN on the day, one per post so no two share a caption,
# which is also the alt text. Imported with bin/import-x-photos, which excludes
# anything the account only shared: that copyright belongs to somebody else.
photos:
  thread: "https://x.com/PyBCN/status/1464506413720420352"
  items:
    - file: pyday-2021/01-gooooood-morning-pydaybcn.jpg
      caption: "Gooooood morning, #PyDayBCN!!"
      source: "https://x.com/PyBCN/status/1464506413720420352"
      time: "09:08"
    - file: pyday-2021/02-kudos-to-our-organizing-team-lpmayos-nataliasirera.jpg
      caption: "Kudos to our organizing team: @lpmayos @nataliasirera @DZPM @llevaNEUS @srxavi @berenguel @eloipuertas @sianna"
      source: "https://x.com/PyBCN/status/1464529899155296257"
      time: "10:41"
    - file: pyday-2021/03-thanks-for-sponsoring-us.jpg
      caption: "Thanks for sponsoring us!"
      source: "https://x.com/PyBCN/status/1464530306246057990"
      time: "10:43"
    - file: pyday-2021/04-build-a-chat-application-that-lets-you-speak-multi.jpg
      caption: "\"Build a chat application that lets you speak multiple languages\", by Diego Gonzalez from @PreplyCom"
      source: "https://x.com/PyBCN/status/1464531105562910720"
      time: "10:46"
      talk: build-a-chat-application-that-lets-you-speak-multiple
    - file: pyday-2021/05-preplycom-building-the-cloud-with-python-getting-s.jpg
      caption: "\"Building the Cloud with Python: getting started with AWS CDK\", by Anton Caceres and Alexandre Savio"
      source: "https://x.com/PyBCN/status/1464531763867357184"
      time: "10:49"
      talk: building-the-cloud-with-python-getting-started-with-aws-cdk
    - file: pyday-2021/06-implementing-your-api-with-fastapi-by-esperanza-bu.jpg
      caption: "\"Implementing your API with FASTAPI\", by Esperanza Buitrago (@ebuitragod)"
      source: "https://x.com/PyBCN/status/1464531971544076290"
      time: "10:50"
      talk: implementing-your-api-with-fastapi
    - file: pyday-2021/07-how-to-create-data-apps-with-python-by-sergi-ortiz.jpg
      caption: "\"How to create Data apps with Python\", by Sergi Ortiz"
      source: "https://x.com/PyBCN/status/1464532219498749958"
      time: "10:51"
      talk: how-to-create-data-apps-with-python
    - file: pyday-2021/08-and-the-catering-for-the-coffee-break-is-ready.jpg
      caption: "And the catering for the coffee break is ready!"
      source: "https://x.com/PyBCN/status/1464532407172931585"
      time: "10:51"
    - file: pyday-2021/09-yes-we-got-the-good-stuff.jpg
      caption: "Yes, we got the good stuff ✌️"
      source: "https://x.com/PyBCN/status/1464545721349193729"
      time: "11:44"
    - file: pyday-2021/10-creating-cute-user-interfaces-in-python-with-qt-by.jpg
      caption: "\"Creating cute user interfaces in python with Qt\", by Elisabeth Ortega (@draentropia)"
      source: "https://x.com/PyBCN/status/1464547004923719684"
      time: "11:49"
      talk: creating-cute-user-interfaces-in-python-with-qt
    - file: pyday-2021/11-microservicios-en-la-vida-moderna-un-enfoque-pytho.jpg
      caption: "\"Microservicios en la vida moderna: Un enfoque python-centrico\", by Antonio Molina (@aydevosotros), Erik Tordera and Pablo Fernández from @qustodio"
      source: "https://x.com/PyBCN/status/1464547526246375433"
      time: "11:51"
      talk: microservicios-en-la-vida-moderna-un-enfoque-python-centrico
    - file: pyday-2021/12-aydevosotros-qustodio-introduction-to-django-by-vi.jpg
      caption: "\"Introduction to Django\", by Vincent Choubard from Rover (@roverdotcom_es)"
      source: "https://x.com/PyBCN/status/1464547803712172039"
      time: "11:53"
      talk: introduction-to-django
    - file: pyday-2021/13-vector-search-engines-with-python-from-embeddings.jpg
      caption: "\"Vector search engines with Python: from embeddings to similarity search\", by Gabriel de Maeztu (@gabimaeztu) from IOMED (@iomed_ehr)"
      source: "https://x.com/PyBCN/status/1464548109808279559"
      time: "11:54"
      talk: vector-search-engines-with-python-from-embeddings-to
    - file: pyday-2021/14-nice-limited-edition-pybcn-stickers.jpg
      caption: "Nice limited-edition @PyBCN stickers!"
      source: "https://x.com/PyBCN/status/1464548681026355201"
      time: "11:56"
    - file: pyday-2021/15-remember-we-ll-take-the-group-photo-at-13h-in-the.jpg
      caption: "Remember, we'll take the group photo at 13h, in the terrace. See you there!"
      source: "https://x.com/PyBCN/status/1464549374147678209"
      time: "11:59"
    - file: pyday-2021/16-at-the-end-of-each-talk-please-use-the-post-its-to.png
      caption: "At the end of each talk, please use the post-its to leave feedback for the speakers:"
      source: "https://x.com/PyBCN/status/1464550721731371008"
      time: "12:04"
    - file: pyday-2021/17-warm-coffe.jpg
      caption: "Warm coffe!"
      source: "https://x.com/PyBCN/status/1464554868568428548"
      time: "12:21"
    - file: pyday-2021/18-save-some-pastries-for-our-guys-at-the-entrance.jpg
      caption: "Save some pastries for our guys at the entrance!!"
      source: "https://x.com/PyBCN/status/1464555890200166403"
      time: "12:25"
    - file: pyday-2021/19-causal-data-science-workshop-by-jordi-mur.jpg
      caption: "\"Causal Data Science workshop\", by Jordi Mur"
      source: "https://x.com/PyBCN/status/1464595512926126084"
      time: "15:02"
      talk: causal-data-science-workshop
    - file: pyday-2021/20-making-mlops-uncool-again-by-david-de-la-iglesia-c.jpg
      caption: "\"Making MLOps uncool again\", by David de la Iglesia Castro (@daviddelachurch)"
      source: "https://x.com/PyBCN/status/1464595698251358217"
      time: "15:03"
      talk: making-mlops-uncool-again
    - file: pyday-2021/21-daviddelachurch-how-to-beat-imposter-syndrome-conf.jpg
      caption: "\"How to beat imposter syndrome: confessions of a developer\", by Matteo Bruno from Onna (@onnahq)"
      source: "https://x.com/PyBCN/status/1464596540283101190"
      time: "15:06"
      talk: how-to-beat-imposter-syndrome-confessions-of-a-developer
    - file: pyday-2021/22-daviddelachurch-onnahq-building-a-dag-factory-by-a.jpg
      caption: "\"Building a DAG Factory\", by Albert Franzi Cros (@FranziCros) from Typeform (@typeform)"
      source: "https://x.com/PyBCN/status/1464597043339534336"
      time: "15:08"
      talk: building-a-dag-factory
    - file: pyday-2021/23-burnout-paradise-buenas-practicas-para-evitar-el-b.jpg
      caption: "\"Burnout Paradise: buenas prácticas para evitar el burnout en desarrollo\", by Alejandro Nicolás (@sander_pm) from Hybrid Theory (@HybridTheory_GL)"
      source: "https://x.com/PyBCN/status/1464600432463032330"
      time: "15:22"
      talk: burnout-paradise-buenas-practicas-para-evitar-el-burnout-en
    - file: pyday-2021/24-sander-pm-hybridtheory-gl-yes-the-lunch-was-delici.jpg
      caption: "(Yes, the lunch was delicious)"
      source: "https://x.com/PyBCN/status/1464600704312659973"
      time: "15:23"
    - file: pyday-2021/25-say-cheese.jpg
      caption: "Say Cheese!"
      source: "https://x.com/PyBCN/status/1464600946181292035"
      time: "15:24"
    - file: pyday-2021/26-build-a-machine-learning-iot-device-running-python.jpg
      caption: "\"Build a Machine Learning IoT Device running Python\", by Marc Pous (@gy4nt)"
      source: "https://x.com/PyBCN/status/1464619233619365899"
      time: "16:36"
      talk: build-a-machine-learning-iot-device-running-python
    - file: pyday-2021/27-the-moons-of-jupyter-widgets-ecosystem-by-mariana.jpg
      caption: "\"The moons of Jupyter: widgets ecosystem\" by Mariana Meireles (@mari_meir) and Laysa Uchoa (@laysauchoa)"
      source: "https://x.com/PyBCN/status/1464619630924865545"
      time: "16:38"
      talk: the-moons-of-jupyter-widgets-ecosystem
    - file: pyday-2021/28-signal-processing-from-neurons-to-mars-by-vivek-sh.jpg
      caption: "\"Signal Processing - From Neurons to Mars!\", by Vivek Sharma"
      source: "https://x.com/PyBCN/status/1464619822386397191"
      time: "16:39"
      talk: signal-processing-from-neurons-to-mars
    - file: pyday-2021/29-keeping-sync-between-datasets-with-diffsync-by-chr.jpg
      caption: "\"Keeping sync between datasets with Diffsync\", by Christian Adell (@chadell0)"
      source: "https://x.com/PyBCN/status/1464620079518208007"
      time: "16:40"
      talk: keeping-sync-between-datasets-with-diffsync
    - file: pyday-2021/30-chadell0-hey-david-hurry-up-and-finish-doing-the-k.jpg
      caption: "Hey David, hurry up and finish doing the Kahoot!!"
      source: "https://x.com/PyBCN/status/1464625183478755331"
      time: "17:00"
    - file: pyday-2021/16-finally-thanks-to-everybody-who-helped-us-organize.jpg
      caption: "Finally, thanks to everybody who helped us organize our biggest 2021 event 💪💪 We hope to see you again in the #PyDayBCN 2022!"
      source: "https://x.com/PyBCN/status/1465217532218982403"
      time: "08:14"
---

## About PyDay BCN 2021 

We are organizing the **the fifth edition** of PyDay in Barcelona!  

PyDay is an event full of FREE **python-related workshops** and activities for the Python community, organized once per year. Over the last four editions, PyDay has become a great opportunity to share our love for Python and engage users, companies and newcomers into it!


### When and where
It is scheduled for **Saturday 27th November** in [Canòdrom - Ateneu d'Innovació Digital i Democràtica](https://g.page/Canodrom?share), from  9:30pm to 19:00pm CET, aprox.



### A full day of in-person hands-on workshops
PyDay BCN 2021 will have different **thematic tracks** --e.g. data science, web development, security-- with hands-on workshops of about 90 minutes in which participants will learn how to use different libraries, tools and techniques, fully guided by members of the community and support volunteers.


### Participate in Kahoot and win prizes!
 We will host a Kahoot game with questions about PyBCN and Python in general, with prizes for the fastest players. Will you miss it?!


### Covid-safe event
We are super excited to be back to in person events, and we are working hard to make PyDay 2021 a safe encounter:
- We will ask all in-person attendees to show a vaccination certificate or have a negative covid test taken in the 24 hours previous to the event.
- We will have a reduced attendance ratio.
- Lunch will take place outside, and we will provide individual meals to each attendee.
- Sanitizer gel will be available in every room.  
