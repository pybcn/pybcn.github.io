---
title: "PyDay BCN 2022"
description: "For the community, by the community!"
menu:
  main:
    parent: "PyDay BCN"
weight: 1
aliases:
  - /pyday-bcn-2022
heroBackground: /images/photos/canodrom.png

layout: event

free_text_sections:
  - title: Important dates
    id: important_dates
    content: "<b>1st October</b>: Call for proposals opening<br/>
      <b>31th October</b>: Call for proposals closing<br/>
      <b>16th November</b>: Program available<br/>
      <b>18th November, 9AM</b>: Early registration open for PyBCN members, PyDay speakers and sponsors<br/>
      <b>21nd November, 9AM</b>: General registration open through Eventbrite<br/>
      <b>26th November</b>: PyDay BCN 2022"

sponsors_text: "Would you like to sponsor this event? Please contact us at pydaybcn2022@googlegroups.com<br/><br/>"
sponsor_levels:
  - sponsors_per_line: 2
    sponsors: [canodrom]
    name: Venue
  - sponsors_per_line: 2
    sponsors: [cloudblue, rover, qustodio, veriff, apsl]
    name: Gold
  - sponsors_per_line: 3
    sponsors: [coopdevs, somenergia, jobfluent]
    name: Silver
  - sponsors_per_line: 3
    sponsors: [hybridtheory, preply, pythones]
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
            - jimena-escobar
            - kemalcan-bora
            - marc-pous
            - pavel-lonkin
            - pere-miquel-brull
  - title: Organizers
    id: organizers
    levels:
      - people_per_line: 4
        people:
          - natalia
          - lpmayos
          - xavi
          - mireia
          - patricio-reyes

previous_editions:
  - name: PyDay BCN 2021
    url: /events/pyday_bcn/pyday_bcn_2021/
  - name: PyDay BCN 2020
    url: /events/pyday_bcn/pyday_bcn_2020/
  - name: PyDay BCN 2019
    url: /events/pyday_bcn/pyday_bcn_2019/
  - name: PyDay BCN 2018
    url: /events/pyday_bcn/pyday_bcn_2018/
  - name: PyDay BCN 2016
    url: /events/pyday_bcn/pyday_bcn_2016/

spansDuration: 15
numTracks: 3
eventTimes:
  [
    9:00,
    9:15,
    9:30,
    9:45,
    10:00,
    10:15,
    10:30,
    10:45,
    11:00,
    11:15,
    11:30,
    11:45,
    12:00,
    12:15,
    12:30,
    12:45,
    13:00,
    13:15,
    13:30,
    13:45,
    14:00,
    14:15,
    14:30,
    14:45,
    15:00,
    15:15,
    15:30,
    15:45,
    16:00,
    16:15,
    16:30,
    16:45,
    17:00,
    17:15,
    17:30,
    17:45,
  ]
legend: '<i class="fas fa-laptop"></i> Workshop &nbsp;&nbsp;&nbsp; <i class="fas fa-comment"></i> Talk &nbsp;&nbsp; | &nbsp;&nbsp; <i class="fas fa-circle green"></i> Beginner &nbsp;&nbsp;&nbsp; <i class="fas fa-circle yellow"></i> Intermediate &nbsp;&nbsp;&nbsp; <i class="fas fa-circle red"></i> Advanced'
events:
  - start_time_slot: 9:00
    end_time_slot: 9:15
    track_length: 3
    color: purple
    title: "Registration & Welcome"
    speaker: "PyDay BCN 2022 Organising Committee"
    type: group
    location: Sala d'actes Ada Lovelace
    class: middle

  - speaker: "Gema Parreño"
    title: "Machine Learning en producción: Experimentos con versionado de datos con DVC y VSCode"
    description: "El workshop utiliza herramientas OpenSource de DVC y su extension para VSCode para preparar los experimentos de Data Science para su versionado y puesta en producción. Utilizamos el IDE de VS Code y lo transformamos en una plataforma de experimentación de Machine Learning.</br></br>A través de un caso de uso real, veremos las posibilidades que ofrece el implementar practicas de Software a los proyectos de Data Science y herramientas para versionar los experimentos de Machine Learning.</br></br>Objetivo : ayudar a los data scientist a salir de los notebooks y preparar la experimentación y puesta en producción de manera un poco mas robusta ."
    start_time_slot: 9:30
    end_time_slot: 10:45
    track_length: 1
    color: red
    type: workshop
    language: "Spanish"  
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle yellow\"></i>"
    requirements: "<ul><li>Laptop , requirements.txt installed.</li><li>VS Code IDE.</li></ul>"
    topic: "Data Science and MLOPS"
    location: Sala d'actes Ada Lovelace
  - speaker: "Pavel Lonkin"
    title: "Friendly fuzzing for your Python SaaS applications"
    description: "Tired of bugs? Security issues in your Python code? Fuzzing approach can help you to decrease number of issues received from your production environment using only few lines of code! In this topic you are going to:<br/><ul><li>learn what the fuzzing is and what type of fuzzing exists</li><li>learn how it helps to catch the bugs and find potential security issues when you are sleeping</li><li>“fuzz” your first python application</li><li>find the way to fuzz your REST Django application</li><li>discover the instruments to fuzz any API</li></ul>"
    start_time_slot: 9:30
    end_time_slot: 10:45
    track_length: 1
    color: yellow
    type: workshop
    language: "English"  
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: "<ul><li>Initial python knowledges</li><li>Would be great to know Django</li><li>Laptop with installed Docker and Docker Compose</li><//ul>"
    topic: "Security, software development"
    location: Sala Hedy Lamarr / Margarita Salas
  - speaker: "Kemalcan Bora"
    title: "How many ants can carry an elephant? Pushing the limits of AWS Chalice"
    description: "Chalice is a framework for writing serverless apps in python. It allows you to quickly create and deploy applications that use AWS Lambda. Serverless applications generally have some limits like RAM, storage, and CPU.. and the main purpose is simple functions like login, registration, etc. So what if we want to create an ML application? How can we handle our limits? don't panic young Skywalker. We have to push our limits and we'll install NumPy, and Sci-kit learn libraries and our app will roam freely in the cloud in peace."
    start_time_slot: 9:30
    end_time_slot: 10:45
    track_length: 1
    color: blue
    type: workshop
    language: "English"  
    python_level: "<i class=\"fas fa-circle green\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    topic: "Serverless apps"
    location: Sala Hipàtia d'Alexandria
    requirements: "Python, AWS account, AWS chalice framework"

  - start_time_slot: 11:00
    end_time_slot: 11:15
    track_length: 3
    color: purple
    title: "Coffee break"
    type: coffee
    location: Open-air terrace
    class: middle

  - speaker: "Marc Pous"
    title: "Build Air Quality Sensors with Python and choose your own adventure!"
    description: "The goal of this hands-on workshop is to build an Air Quality sensor (with Raspberry Pis) using Python to get the data from the sensors. From here you are going to choose what happens next. Would you like to store the data on a database? Visualize it? Send it to a Cloud? or to a Telegram bot? You choose your own adventure! Everything in the edge using containers, python and balena."
    start_time_slot: 11:30
    end_time_slot: 12:45
    track_length: 1
    color: blue
    type: workshop
    language: "English"  
    python_level: "<i class=\"fas fa-circle green\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: "Laptop"
    topic: "Internet of Things and Air quality sensors"
    location: Sala d'actes Ada Lovelace
  - speaker: "Eva Martín del Pico"
    title: "Build a full-stack app with Flask and Vue"
    description: "In this workshop we will build a complete web application using Flask Python micro framework in the backend and Vue.js JS framework in the frontend. Both Flask and Vue are easy to learn, yet flexible and powerful, making them a great choice for those who want to create modern and robust applications - and do it fast."
    start_time_slot: 11:30
    end_time_slot: 12:45
    track_length: 1
    color: blue
    type: workshop
    language: "English"  
    python_level: "<i class=\"fas fa-circle green\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: "<ul><li>Familiarity with Python and basic understanding of HTML and CSS (ideally JS too, but it is not necessary)</li><li>Laptop with Python3, Flask, NuxtJS and Docker.</li></ul>"
    topic: "Web apps"
    location: Sala Hedy Lamarr / Margarita Salas
  - speaker: "Biel Stela"
    title: "Python as a GIS: Tools, howtos and gotchas"
    description: "Use python as a GIS with Rasterio, Xarray and GeoPandas"
    start_time_slot: 11:30
    end_time_slot: 12:45
    track_length: 1
    color: red
    type: workshop
    language: "English"  
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle yellow\"></i>"
    requirements: "Laptop with conda if attendees want to follow the notebooks and do some exercises, just ears and be present otherwise."
    topic: "Python as a GIS"
    location: Sala Hipàtia d'Alexandria

  - start_time_slot: 13:00
    end_time_slot: 13:00
    track_length: 3
    color: pink
    title: "Group photo"
    type: photo
    location: Open-air terrace
    class: middle

  - start_time_slot: 13:15
    end_time_slot: 13:45
    track_length: 3
    color: purple
    title: "Lunch break"
    type: lunch
    location: Open-air terrace
    class: middle

  - speaker: "Alberto Labarga"
    title: "Building an End-to-End Open-Source Modern Data Platform for Biomedical Data"
    description: "A detailed guide to help you navigate the modern data stack and build your own platform using open-source technologies.<br/><br/>Data engineering has experiences enormous growth in the last years, allowing for rapid progress and innovation as more people than ever are thinking about data resources and how to better leverage them.<br/><br/>In this talk we will explore the related technologies and build from scratch an end-to-end modern data platform for the analysis of medical data. We will be using open-source tools and libraries, including  python-based DBT, Apache Airflow and Querybook.<br/><br/>The platform will consist of the following components:<ul><li>Data warehouse</li><li>Data integration</li><li>Data transformation</li><li>Data orchestration</li><li>Data visualization</li></ul>"
    start_time_slot: 14:00
    end_time_slot: 15:15
    track_length: 1
    color: yellow
    type: workshop
    language: "Spanish or English"  
    python_level: "<i class=\"fas fa-circle green\"></i>"
    topic_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic: "Data engineering"
    location: Sala d'actes Ada Lovelace
    requirements: "Laptop"
  - speaker: "Jimena Escobar Bermúdez"
    title: "Cuando los precios suben: Scrapy"
    description: "Criptomonedas, la guerra en Ucrania, la pandemia, la falta de componentes y toda la serie de catastróficas desdichas que estamos sufriendo nos ha llevado a un punto en el que el precio de todo ha subido. En este taller aprenderemos a usar Scrapy para conseguir descargar, almacenar y comparar los precios de los productos que queramos."
    start_time_slot: 14:00
    end_time_slot: 15:15
    track_length: 1
    color: blue
    type: workshop
    language: "Spanish"  
    python_level: "<i class=\"fas fa-circle green\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    topic: "Scrapy"
    requirements: "Laptop"
    location: Sala Hedy Lamarr / Margarita Salas
  - speaker: "Antonio Molina Garcia-Retamero"
    title: "Inside out. Or how to get your app observable"
    description: "Observability is key in distributed systems and it is gaining importance within the industry. So it is important to understand the concepts behind the idea of observabiity and why is important to us, as developers, to make our developments “observable”. Being able to create software that is easy to debug while systems scales and complexity grows will level up us as developers and will make our clients and employers far happier. This is what this workshop is about. From a brief theory of what observability is to some practices and best practices."
    start_time_slot: 14:00
    end_time_slot: 15:15
    track_length: 1
    color: blue
    type: workshop
    language: "Spanish"  
    python_level: "<i class=\"fas fa-circle green\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: "Laptop"
    topic: "Observability"
    location: Sala Hipàtia d'Alexandria

  - start_time_slot: 15:30
    end_time_slot: 15:45
    track_length: 3
    color: purple
    title: "Lightning talks & coffee"
    type: talk
    location: Sala d'actes Ada Lovelace
    class: middle

  - speaker: "Cheuk Ting Ho"
    title: "Using Numba Effectively Today"
    description: "Numba is syntactically easy to use - just add a decorator, but actually very hard to use effectively. The reason being it is difficult to understand what Numba does to speed up the numeric operation. This workshop will provide all the knowledge that you need to make Numba works for you."
    start_time_slot: 16:00
    end_time_slot: 17:15
    track_length: 1
    color: red
    type: workshop
    language: "English"  
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle yellow\"></i>"
    requirements: "This workshop is for Data scientists or developers who have math-heavy code that would like to speed up with the benefit of Numpy and Numba.<br/><br/>What is required from attendees<br/><br/><ul><li>- A computer with a stable internet connection (useful to look up information);</li><li>- Python 3.8 or above;</li><li>- Jupyter and Numba installed (detail about Python libraries required will be announced later);</li><li>- An opened mind and ready to learn something new</li></ul>"
    topic: "Data Science"
    location: Sala d'actes Ada Lovelace
  - speaker: "Pere Miquel Brull"
    title: "Making sense of your Data Platform with OpenMetadata"
    description: "OpenMetadata is an open-source project (https://open-metadata.org/) that is building a metadata standard and a centralized and shared metadata platform on top of it. In this workshop, we will explore the tool, how it works, and bit by bit we will dive into its implementation and design."
    start_time_slot: 16:00
    end_time_slot: 17:15
    track_length: 1
    color: yellow
    type: workshop
    language: "English"  
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    topic: "Data Management"
    location: Sala Hedy Lamarr / Margarita Salas
    requirements: "For the folks who would like to follow along, a laptop with docker compose"
  - speaker: "Ana Eliza Barbosa"
    title: "TDD Coding Dojo"
    description: "This is a small workshop where participants will solve one coding challenge using TDD and pair programming.<br/>The workshop has one main computer, connected to a projector for the audience to follow up, where 2 participants will try to solve the challenge as much as possible in 5 minutes.<br/>Every 5 minutes the pairs will rotate amongst the participants until they solve the challenge or the workshop time is up.<br/>The goal is to practice TDD with a collaborative approach."
    start_time_slot: 16:00
    end_time_slot: 17:15
    track_length: 1
    color: blue
    type: workshop
    language: "English"  
    python_level: "<i class=\"fas fa-circle green\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    topic: "Test driven development "
    location: Sala Hipàtia d'Alexandria

  - start_time_slot: 17:30
    end_time_slot: 17:45
    track_length: 3
    color: purple
    title: "Closing session & Kahoot"
    speaker: "PyDay BCN 2022 Organising Committee"
    type: group
    location: Sala d'actes Ada Lovelace
    class: middle
---

## About PyDay BCN 2022

We are organizing the **the sixth edition** of PyDay in Barcelona!

PyDay is an event full of FREE **python-related workshops** and activities for the Python community, organized once per year. Over the <a href="#previous_editions_section">last five editions</a>, PyDay has become a great opportunity to share our love for Python and engage users, companies and newcomers into it!

#### When and where

It is scheduled for **Saturday 26th November** in <a href="https://g.page/Canodrom?share" target="_blank">Canòdrom - Ateneu d'Innovació Digital i Democràtica</a>, from 9:30pm to 19:00pm CET, aprox.

#### A full day of in-person hands-on workshops

PyDay BCN 2022 will have different **thematic tracks** --e.g. data science, web development, security-- with hands-on workshops of about 90 minutes in which participants will learn how to use different libraries, tools and techniques, fully guided by members of the community and support volunteers.

#### Participate in Kahoot and win prizes!

We will host a Kahoot game with questions about PyBCN and Python in general, with prizes for the fastest players. Will you miss it?!
