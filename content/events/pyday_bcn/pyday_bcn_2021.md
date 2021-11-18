---
title: "PyDay BCN 2021"
description: "Post-pandemic edition!"
menu:
  main:
    parent: 'PyDay BCN'
weight: 1
aliases:
- /pyday-bcn-2021
heroBackground: https://images.unsplash.com/photo-1504384764586-bb4cdc1707b0?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80

layout: event

important_dates: "<b>11th October</b>: Call for proposals opening<br/>
    <b>24th October</b>: Call for proposals closing<br/>
    <b>17th November</b>: Program available<br/>
    <b>19th November, 9AM</b>: Early registration open for PyBCN members, PyDay speakers and sponsors<br/>
    <b>22nd November, 9AM</b>: General registration open through <a href=\"https://www.eventbrite.es/e/entradas-pydaybcn-2021-212686419807\" target=\"_blank\">eventbrite</a><br/>
    <b>27th November</b>: PyDay BCN 2021"

registration: "Registration to the general public will be open on <b>Monday 22nd November, 9AM</b>, through <a href=\"https://www.eventbrite.es/e/entradas-pydaybcn-2021-212686419807\" target=\"_blank\">eventbrite</a>.<br/><br/>Please have a look at the schedule below and choose which talks you would like to attend beforehand."

sponsor_levels:
    - sponsors_per_line: 3
      sponsors: [bling, cloudblue, hybridtheory, iomed, onna, preply, qustodio, rover, typeform]
      name: Gold
    - sponsors_per_line: 4
      sponsors: [bmat, digitalfems, orpheus, verse]
      name: Supporting

speakers_levels:
    - people_per_line: 4
      people: 
      - albert-franzi
      - alejandro-nicolas
      - anton-caceres
      - antonio-molina
      - christian-adell-querol
      - david-de-la-iglesia-castro
      - diego-gonzalez
      - elisabeth-ortega-carrasco
      - esperanza-buitrago
      - gabriel-de-maeztu
      - jordi-mur
      - marc-pous
      - mariana-meireles
      - matteo-bruno
      - sergi-ortiz
      - vincent-choubard
      - vivek-sharma

organizers_levels:
    - people_per_line: 4
      people:
      - lpmayos
      - natalia
      - david
      - nuria
      - xavi
      - rberenguel
      - eloi
      - mireia
      name: 

previous_editions:
    - name: PyDay BCN 2020
      url: /events/pyday_bcn/pyday_bcn_2020/
    - name: PyDay BCN 2019
      url: /events/pyday_bcn/pyday_bcn_2019/
    - name: PyDay BCN 2018
      url: /events/pyday_bcn/pyday_bcn_2018/
    - name: PyDay BCN 2016
      url: /events/pyday_bcn/pyday_bcn_2016/

spansDuration: 15
numTracks: 4
eventTimes: [9:00, 9:15, 9:30, 9:45, 10:00, 10:15, 10:30, 10:45, 11:00, 11:15, 11:30, 11:45, 12:00, 12:15, 12:30, 12:45, 13:00, 13:15, 13:30, 13:45, 14:00, 14:15, 14:30, 14:45, 15:00, 15:15, 15:30, 15:45, 16:00, 16:15, 16:30, 16:45, 17:00, 17:15, 17:30, 17:45]
legend: "<i class=\"fas fa-laptop\"></i> Workshop &nbsp;&nbsp;&nbsp; <i class=\"fas fa-comment\"></i> Talk &nbsp;&nbsp; | &nbsp;&nbsp; <i class=\"fas fa-circle green\"></i> Beginner &nbsp;&nbsp;&nbsp; <i class=\"fas fa-circle yellow\"></i> Intermediate &nbsp;&nbsp;&nbsp; <i class=\"fas fa-circle red\"></i> Advanced &nbsp;&nbsp; | &nbsp;&nbsp; <i class=\"fas fa-star gold\"></i> Sponsored event"
events:
    - start_time_slot: 9:00
      end_time_slot: 9:15
      track_length: 4
      color: purple
      title: "Registration & Welcome"
      speaker: "PyDay BCN 2021 Organising Committee"
      type: group
      location: Open-air terrace
      class: middle

    - speaker: "Sergi Ortiz"
      title: "How to create Data apps with Python"
      description: "Data products are the future of data. And Data Apps (and AI Apps) are an important chunk of this future. For Python coders there are many frictions to create Data Apps nowadays, we will try to address them all and create a Data App (FE - BE and DevOps) during the hands on session"
      start_time_slot: 9:30
      end_time_slot: 10:45
      track_length: 1
      color: green
      language: "Spanish"
      type: workshop
      topic: Data Apps
      python_level: "<i class=\"fas fa-circle yellow\"></i>"
      topic_level: "<i class=\"fas fa-circle green\"></i>"
      location: Room Actes
    - speaker: "Diego Gonzalez"
      sponsor: Preply
      title: "Build a chat application that lets you speak multiple languages"
      description: "Learn how to build a chat application that can translate messages across multiple languages using only a few technologies (Python among them, of course!)"
      start_time_slot: 9:30
      end_time_slot: 10:45
      track_length: 1
      color: orange
      language: "English"
      type: workshop
      topic: Web development
      python_level: "<i class=\"fas fa-circle yellow\"></i>"
      topic_level: "<i class=\"fas fa-circle yellow\"></i>"
      location: Room Guinardó
    - speaker: "Esperanza Buitrago"
      title: "Implementing your API with FASTAPI"
      description: "Implement your API with FastAPI from scratch and make it run in local."
      start_time_slot: 9:30
      end_time_slot: 10:45
      track_length: 1
      color: green
      language: "English"
      type: workshop
      topic: Software Engineering
      python_level: "<i class=\"fas fa-circle green\"></i>"
      topic_level: "<i class=\"fas fa-circle green\"></i>"
      location: Room Gòtica
    - speaker: "Anton Caceres"
      title: "Building the Cloud with Python: getting started with AWS CDK"
      description: "With emerging cloud technologies it is just a matter of time until most backends run in serverless or container-based environments. This workshop is showcasing a recently released open-source Cloud Development Kit by Amazon, which lets us control cloud resources just like we control our application logic - in pure Python.
                    CDK offers high-level abstraction to define AWS resources imperatively as customizable and reusable Python classes. Unfortunately, there are not many tutorials available yet and the documentation is limited. So we will be happy to share with you how to: 1) Break down AWS infrastructure into reusable constructs represented by Python classes; 2) Combine own and public constructs into Stack applications; 3) Deploy CDK apps to AWS cloud"
      start_time_slot: 9:30
      end_time_slot: 10:45
      track_length: 1
      color: red
      language: "English"
      type: workshop
      topic: Cloud-native Python applications
      python_level: "<i class=\"fas fa-circle yellow\"></i>"
      topic_level: "<i class=\"fas fa-circle green\"></i>"
      location: Room Raval

    - start_time_slot: 11:00
      end_time_slot: 11:15
      track_length: 4
      color: purple
      title: "Coffee Break"
      sponsor: Bling
      type: coffee
      location: Open-air terrace
      class: middle

    - speaker: "Elisabeth Ortega"
      title: "Creating cute user interfaces in python with Qt"
      description: "Most of us learn to use python as a command line tool, asking information to the users and passing them to the code as arguments. Some of us later moved to Django and related web development tools, to have a better interaction with the user paying the cost of fighting against the web layout in different languages. Few of us faced tkinter to build our first user interfaces with more or less success, but almost none of us were happy with the result of the user interfaces created in pure python.<br/>In \"Creating cute user interfaces in python with Qt\" I will show you how to enjoy creating user interfaces interactively with some clicks and few lines of code using the PySide6 library with all the Qt potential behind it."
      requirements: "PySide6 (https://pypi.org/project/PySide6/)<br/><br/>Course repo:<br/>Empty and private until some days before the meeting but it will be this: https://github.com/draentropia/pyside-pyday21"
      start_time_slot: 11:30
      end_time_slot: 12:45
      track_length: 1
      color: green
      language: "Spanish"
      type: workshop
      topic: User interfaces
      python_level: "<i class=\"fas fa-circle yellow\"></i>"
      topic_level: "<i class=\"fas fa-circle green\"></i>"
      location: Room Actes
    - speaker: "Gabriel de Maeztu"
      sponsor: IOMED
      title: "Vector search engines with Python: from embeddings to similarity search"
      description: "I would cover the following topics, providing to anyone familiar with Python an overall idea about embeddings and similarity search in addition to a tutorial with with a use cases:<br/><ul><li>What are Vector Embeddings?</li><li>What is a Vector Database?</li><li>What is Vector Similarity Search?</li><li>So what do I do with my vector embedding?</li><li>Efficient Filtering of Vectors</li><li>Use cases: text, image, video, audio, graph and relational data</li><li>Let's build a search engine: Semantic textual search with vector embeddings<ol><li>Get the data</li><li>Create the embeddings</li><li>Upload the embeddings</li> <li>Query the data</li></ol></li></ul>"
      start_time_slot: 11:30
      end_time_slot: 12:45
      track_length: 1
      color: blue
      language: "English"
      type: workshop
      topic: Data Science
      python_level: "<i class=\"fas fa-circle yellow\"></i>"
      topic_level: "<i class=\"fas fa-circle yellow\"></i>"
      location: Room Guinardó
    - speaker: "Vincent Choubard"
      sponsor: Rover
      title: "Introduction to Django"
      description: "We are going to build a web app using Django to create a pet profile and store it."
      start_time_slot: 11:30
      end_time_slot: 12:45
      track_length: 1
      color: orange
      language: "English"
      type: workshop
      topic: Web Development
      python_level: "<i class=\"fas fa-circle green\"></i>"
      topic_level: "<i class=\"fas fa-circle green\"></i>"
      location: Room Gòtica
      requirements: "Ideally have python and django installed on your machine by following <a href=\"https://docs.djangoproject.com/en/3.2/intro/install/\">https://docs.djangoproject.com/en/3.2/intro/install/</a>"
    - speaker: "Antonio Molina"
      sponsor: Qustodio
      title: "Microservicios en la vida moderna. Un enfoque python-centrico."
      description: "Las arquitecturas distribuidas y los microservicios están en boca de todos. Unos defienden que son la cura para todos los males mientras que otros advierten que la complejidad añadida puede desembocar en frustraciones y malos sueños. En este workshop, proponemos una reflexión sobre arquitecturas distribuidas a través de un ejercicio práctico. Aunque orientado a desarrollos basados en nuestro querido python, proponemos salir de nuestra zona de confort para profundizar juntos en eso que llamamos dev/ops y de cómo los equipos podemos operar nuestros servicios asi como un primer contacto con las herramientas que nos ayudarán a minimizar los riesgos y las complejidades (tales como Helm, MiniKubes, Istio, GRPC, Prometheus, etc). Acompañanos en este rato a pensar y entender algunos de los problemas, soluciones y buenas prácticas en este tipo de arquitecturas."
      start_time_slot: 11:30
      end_time_slot: 12:45
      track_length: 1
      color: red
      language: "Spanish"
      type: workshop
      topic: Architecture
      python_level: "<i class=\"fas fa-circle green\"></i>"
      topic_level: "<i class=\"fas fa-circle yellow\"></i>"
      location: Room Raval

    - start_time_slot: 13:00
      end_time_slot: 13:00
      track_length: 4
      color: pink
      title: "Group photo"
      type: photo
      location: Open-air terrace
      class: middle

    - start_time_slot: 13:15
      end_time_slot: 13:45
      track_length: 4
      color: purple
      title: "Lunch"
      type: lunch
      location: Open-air terrace
      class: middle

    - speaker: "David de la Iglesia Castro"
      title: "Making MLOps uncool again"
      description: "In this workshop we will learn how to build an \"MLOps workflow\" by extending the power of Git and GitHub. Using only open source tools and without the need of external platfforms or complicated infrastructure. <br/><br/>We will use [HuggingFace] (https://huggingface.co/) to train a model that automatically adds labels to GitHub issues and we will extend the power of Git with [DVC](https://dvc.org/) and [CML](https://cml.dev/) in order to build a living Data Registry and set up a Continuous Training and Deployment loop for our model."
      start_time_slot: 14:00
      end_time_slot: 15:15
      track_length: 1
      color: blue
      language: "Spanish"
      type: workshop
      topic: Data science
      python_level: "<i class=\"fas fa-circle yellow\"></i>"
      topic_level: "<i class=\"fas fa-circle yellow\"></i>"
      location: Room Actes
      requirements: "A browser (preferably Google Chrome)<br/>Github account."
    - speaker: "Jordi Mur"
      title: "Causal Data Science workshop"
      description: "Causal data science is a hot topic in the business applications of machine learning that go beyond predicting a value to actually deciding the best intervention to take based on such a prediction. We will briefly provide the key concepts and methods of causal inference (the topic of this year's Nobel prize in economics!), and then move on to some hands-on practice with Jupyter notebooks based on business use cases. No prior knowledge of causal inference is required."
      requirements: "Bring your own laptop<br/>Libraries: Jupyter notebooks will use DoWhy: https://microsoft.github.io/dowhy/index.html"
      start_time_slot: 14:00
      end_time_slot: 15:15
      track_length: 1
      color: blue
      language: "English"
      type: workshop
      topic: Data science
      python_level: "<i class=\"fas fa-circle yellow\"></i>"
      topic_level: "<i class=\"fas fa-circle green\"></i>"
      location: Room Guinardó
    - speaker: "Matteo Bruno"
      sponsor: Onna
      title: "How to beat imposter syndrome: confessions of a developer"
      description: "Do you feel like you don’t belong, you don’t deserve what you’ve achieved, everyone in your office is more talented than you? Do you have imposter syndrome… too?<br/><br/>Impostor syndrome is a psychological pattern in which people doubt their accomplishments or talents and have a persistent internalized fear of being exposed as a \"fraud\".<br/><br/>Imposter syndrome is common across all industries, but the increasing pressure to be successful in your professional career is taking its toll on employees, affecting more than half workers, including our speaker :)<br/><br/>After many years working in tech for a lot of companies, (from startups to big corporations) in many business fields, Matteo discovered a way to overcome self-doubt and turn this weird feeling into a booster for greater achievements.<br/><br/>He’d like to share all his experience with everyone, making you understand that feeling inadequate is quite common and that there are ways to approach it in a proactive way."
      start_time_slot: 14:00
      end_time_slot: 15:15
      track_length: 1
      color: yellow
      language: "English"
      type: talk
      location: Room Gòtica
    - speaker: "Albert Franzi Cros"
      sponsor: Typeform
      title: "Building a DAG Factory"
      description: "At Typeform there are several teams that interact with data. Machine learning engineers, data scientists, data analysts, insights teams. None of them should have to worry about Airflow operators, upstream tasks, downstream tasks and all the million ways that writing Airflow DAGs by hand makes you miserable.<br/><br/>This is where the Data Platform teams comes to save the day and create Chester, a DAG factory, powered by a set of API connectors handled by us. Other teams only need to worry about where the data comes from and where it goes to, and write some YAML that describes it. All the rest is handled by Chester's superpowers."
      start_time_slot: 14:00
      end_time_slot: 14:30
      track_length: 1
      color: red
      language: "English"
      type: talk
      location: Room Raval
    - speaker: "Alejandro Nicolás"
      sponsor: Hybrid Theory
      title: "Burnout Paradise: buenas prácticas para evitar el burnout en desarrollo"
      description: "Durante la conferencia se tratará la programación desde el punto de vista psicológico, tanto a nivel individual como a nivel de equipo. Se presentarán los posibles efectos de una rutina de trabajo mal llevada, se evaluarán las causas y se propondrán sistemas o hábitos que afectarían positivamente al bienestar de un desarrollador en un mundo en el que el trabajo en remoto se ha implantado de manera inesperada en nuestro día a día."
      start_time_slot: 14:45
      end_time_slot: 15:15
      track_length: 1
      color: yellow
      language: "Spanish"
      type: talk
      location: Room Raval

    - start_time_slot: 15:30
      end_time_slot: 15:45
      track_length: 4
      color: purple
      title: "Coffee Break"
      sponsor: CloudBlue
      type: coffee
      location: Open-air terrace
      class: middle

    - speaker: "Marc Pous"
      title: "Build a Machine Learning IoT Device running Python"
      description: "Learn on this workshop how to create a fleet of edge AI devices in a simple way using Python, Edge Impulse and balena.<br/><br/>During the workshop attendants will learn how to create a Bird Watcher using a Raspberry Pi and a USB camera (or Pi Camera). Using Python we will get the feed from the camera, apply machine learning models from Edge Impulse and send telegram messages. Finally we will be able to deploy a fleet of Bird Watchers in a simple way all around the world.<br/><br/>The goal of this session is to introduce IoT and AI topics to Python developers. Topics such as the Internet of Things, Artificial Intelligence and citizen science are consistently united in a single project. "
      requirements: "Bring your own Raspberry Pi (3 or 4) with camera (USB or Pi Camera) with your laptop to try to deploy together a ML edge device."
      start_time_slot: 16:00
      end_time_slot: 17:15
      track_length: 1
      color: blue
      language: "English"
      type: workshop
      topic: IOT, ML, Edge AI
      python_level: "<i class=\"fas fa-circle yellow\"></i>"
      topic_level: "<i class=\"fas fa-circle green\"></i>"
      location: Room Actes
    - speaker: "Mariana Meireles"
      title: "The moons of Jupyter: widgets ecosystem"
      description: "Jupyter has much more to offer than an interface for notebooks, the widgets ecosystem can leverage your research, dashboards, data visualization and much more!<br/>In the moons of Jupyter workshop we aim to give an overview of the standard widget library as well the expanded ecosystem created by contributors."
      start_time_slot: 16:00
      end_time_slot: 17:15
      track_length: 1
      color: blue
      language: "English"
      type: workshop
      topic: Data science, scientific computing
      python_level: "<i class=\"fas fa-circle yellow\"></i>"
      topic_level: "<i class=\"fas fa-circle green\"></i>"
      location: Room Guinardó
    - speaker: "Vivek Sharma"
      title: "Signal Processing - From Neurons to Mars!"
      description: "What we see around us with time as its one dimension is a Signal! and to comprehend we just need to analyze it. This workshop is all about the last pit. We'll begin by examining some brain impulses, then move on to our environment, and lastly, Mars! Let's see what's going on over there.<br/>You'll learn how to make a frequency-specific filter, how to use the Fourier transform, and how to visualize data. <br/>Don't forget to bring your sense of wonder."
      start_time_slot: 16:00
      end_time_slot: 17:15
      track_length: 1
      color: blue
      language: "English"
      type: workshop
      topic: Signal Processing
      python_level: "<i class=\"fas fa-circle green\"></i>"
      topic_level: "<i class=\"fas fa-circle green\"></i>"
      location: Room Gòtica
    - speaker: "Christian Adell"
      title: "Keeping sync between datasets with Diffsync"
      description: "Working with multiple data models (and data inventories) while keeping a common state is a problem that involves a diff calculation first and then a synchronisation in one direction or another, sometimes solving the mapping between the data models.<br/>Diffsync (https://github.com/networktocode/diffsync) library helps with this common problem by providing an easy data modeling and structured CRUD operations to update the state."
      start_time_slot: 16:00
      end_time_slot: 17:15
      track_length: 1
      color: green
      language: "English"
      type: workshop
      topic: Data set synchronisation
      python_level: "<i class=\"fas fa-circle green\"></i>"
      topic_level: "<i class=\"fas fa-circle green\"></i>"
      location: Room Raval

    - start_time_slot: 17:30
      end_time_slot: 17:45
      track_length: 4
      color: purple
      title: "Closing session & Kahoot"
      speaker: "PyDay BCN 2021 Organising Committee"
      type: group
      location: All rooms
      class: middle

        
---

## About PyDay BCN 2021 

We are organizing the **the fifth edition** of PyDay in Barcelona!  

PyDay is an event full of FREE **python-related workshops** and activities for the Python community, organized once per year. Over the <a href="#previous_editions_section">last four editions</a>, PyDay has become a great opportunity to share our love for Python and engage users, companies and newcomers into it!


#### When and where
It is scheduled for **Saturday 27th November** in <a href="https://g.page/Canodrom?share" target="_blank">Canòdrom - Ateneu d'Innovació Digital i Democràtica</a>, from  9:30pm to 19:00pm CET, aprox.



#### A full day of in-person hands-on workshops
PyDay BCN 2021 will have different **thematic tracks** --e.g. data science, web development, security-- with hands-on workshops of about 90 minutes in which participants will learn how to use different libraries, tools and techniques, fully guided by members of the community and support volunteers.


#### Participate in Kahoot and win prizes!
 We will host a Kahoot game with questions about PyBCN and Python in general, with prizes for the fastest players. Will you miss it?!


#### Covid-safe event
We are super excited to be back to in person events, and we are working hard to make PyDay 2021 a safe encounter:
- We will ask all in-person attendees to show a vaccination certificate or have a negative covid test taken in the 24 hours previous to the event.
- We will have a reduced attendance ratio.
- Lunch will take place outside, and we will provide individual meals to each attendee.
- Sanitizer gel will be available in every room.  