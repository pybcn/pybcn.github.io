---
title: "PyDay BCN 2024"
description: "For the community, by the community!"
menu:
  main:
    parent: "PyDay BCN"
weight: 1
aliases:
  - /pyday-bcn-2024
heroBackground: /images/photos/canodrom.png

layout: event

free_text_sections:
  - title: Important dates
    id: important_dates
    content: "<b>26th September</b>: Call for proposals opening: <a href='https://forms.gle/GDL2VpUTu4veHbff8' target='_blank' >Workshops</a> and <a target='_blank' href='https://forms.gle/VLDY6zdmRxRsGsmv7'>Lightning talks</a><br/>
      <b>27th October</b>: Call for proposals closing<br/>
      <b>3rd Novembre</b>: Program available<br/>
      <b>4th November, 9AM</b>: Early registration open for PyBCN members, PyDay speakers and sponsors<br/>
      <b>5th November, 9AM</b>: General registration open through <a target='_blank' href='https://www.eventbrite.es/o/associacio-python-barcelona-pybcn-17886618981'>Eventbrite</a><br/>
      <b>9th November</b>: PyDay BCN 2024"
  - title: Registration
    id: registration
    content: "General registration will open on Tuesday 5th of November, at 9AM through <a target='_blank' href='https://www.eventbrite.es/o/associacio-python-barcelona-pybcn-17886618981'>Eventbrite</a>."

sponsors_text: "Would you like to sponsor this event? Please contact us at pyday2024@googlegroups.com<br/><br/>"
sponsor_levels:
  - sponsors_per_line: 2
    sponsors: [lambdaloopers, nagarro, innovamat, protopixel, pythones, isdieducation, coopdevs]
    name: Silver
  - sponsors_per_line: 3
    sponsors: [qilimanjaro, ikigai, hpc-now, shimoku, digitalfems, innoit, business-insights, travelperk, okta, preply, qustodio, codurance, gluecharm, somenergia]
    name: Supporting
  - sponsors_per_line: 3
    sponsors: [pybcn, pyladiesbcn, canodrom]
    name: Organizers

people_sections:
  - title: Speakers
    id: speakers
    levels:
      - people_per_line: 4
        people:
            - jimena-escobar
            - kemalcan-bora
            - xiang-xu
            - dave-pitts
            - paula-bassaganas
            - israel-saeta
            - raul-cumplido
            - marc-ramirez
  - title: Organizers
    id: organizers
    levels:
      - people_per_line: 4
        people:
          - alicia-morales
          - david
          - ferran-jovell
          - lpmayos
          - jose-riera
          

previous_editions:
  - name: PyDay BCN 2023
    url: /events/pyday_bcn/pyday_bcn_2023/
  - name: PyDay BCN 2022
    url: /events/pyday_bcn/pyday_bcn_2022/
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
numTracks: 4
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
    track_length: 4
    color: purple
    title: "Registration & Welcome"
    speaker: "PyDay BCN 2024 Organizing Committee"
    type: group
    location: "Sala d'actes Ada Lovelace"
    class: middle
  - speaker: "Xiang Xu"
    title: "Unboxing Machine Learning Models: Predicting with Numpy After Model Training"
    description: "In this hands-on workshop, we’ll bridge the gap between high-level machine learning libraries (like Scikit-learn and Keras) and the core mathematical principles driving their predictions. Participants will firstly train regression models using machine learning methods like Kernel Ridge Regression (KRR) and Deep Neural Networks (DNNs), save the trained model parameters, and then use only Numpy to replicate the prediction process."
    start_time_slot: 9:30
    end_time_slot: 10:45
    track_length: 1
    color: red
    type: workshop
    language: English
    python_level: "Intermediate"
    topic_level: "Intermediate"
    requirements: "numpy, scikit-learn, and keras installed"
    topic: "Data science, ML"
    location: "Sala d'actes Ada Lovelace"
  - speaker: ""
    title: ""
    description: ""
    start_time_slot: 9:30
    end_time_slot: 10:45
    track_length: 1
    color: grey
    type: workshop
    language: 
    python_level: ""
    topic_level: ""
    requirements: ""
    topic: ""
    location:
  - speaker: "Paula Bassagañas Òdena"
    title: "Discovering ETL Testing: Essential for Your AI Solutions"
    description: "High-quality data is the foundation of effective AI, and rigorous ETL testing ensures your AI models are built on solid ground. ETL (Extract, Transform, Load) processes are vital for extracting, transforming, and loading data into systems for analysis, and well-tested ETLs are crucial for making reliable, data-driven decisions and successful AI implementations."
    start_time_slot: 9:30
    end_time_slot: 10:45
    track_length: 1
    color: yellow
    type: workshop
    language: "English"
    python_level: "Beginner"
    topic_level: "Beginner"
    topic: "Testing"
    location: "Sala Margarita Salas"
    requirements: "A Github account"
  - speaker: "Pablo M"
    title: "No More Script Nightmares: Make Python CLIs That Rock"
    description: ""
    start_time_slot: 9:30
    end_time_slot: 10:45
    track_length: 1
    color: green
    type: workshop
    language: "English"  
    python_level: "Beginner"
    topic_level: "Beginner"
    requirements: ""
    topic: "CLIs and packaging scripts"
    location: "Aula Hedy Lamarr"
  - start_time_slot: 11:00
    end_time_slot: 11:15
    track_length: 4
    color: purple
    title: "Coffee break + Lightning talks"
    type: coffee
    location: Grades
    class: middle

  - speaker: "Oriol Abril Pla"
    title: "Introducció a xarray: etiqueta les teves dades n-dimensionals"
    description: ""
    start_time_slot: 11:30
    end_time_slot: 12:45
    track_length: 1
    color: green
    type: workshop
    language: "Català"
    python_level: "Beginner"
    topic_level: "Beginner"
    requirements: ""
    topic: "Data science"
    location: "Aula Hipàtia d'Alexandria"
  - speaker: "Marc Ramirez Invernon"
    title: "Building data pipelines with SQLMesh"
    description: "There are thousands of companies building pipelines through the DBT tool. However, this library lacks essential elements of software development: Mature Python API, blue-green deployment, and detection of breaking changes. SQLMesh is a new library that introduces all of these by default. I will try to go through the main elements of this library during the workshop to let the audience know more options than DBT"
    start_time_slot: 11:30
    end_time_slot: 12:45
    track_length: 1
    color: blue
    type: workshop
    language: "Spanish"
    python_level: "Beginner"
    topic_level: "Intermediate"
    requirements: "Docker, Vscode"
    topic: "Data engineering"
    location: "Sala Margarita Salas"
  - speaker: "Alex Molas"
    title: "Typing and pattern matching in Python"
    description: "Since 2014, with the introduction of type hints in Python 3.5, Python has been adding support to types while still maintaining its dynamic nature. Later, in Python 3.10, pattern matching was added to Python, which provides a powerful way to match data structures based on their types and values, improving Python’s capability to work with typed data. Both type hints and pattern matching help make code more predictable and robust. In this talk, we’ll answer the following questions: **Introduction to types in Python**: what's a type? which types does python have? What do they mean? **The basics of type hints**: how to define a type hint?  **mypy**: how to use mypy to check that your code does what you expect? **Advanced type hints**: how to define complex type hints? how to define your own types? how to use generic types? **Data validation**: how to use Pydantic and dataclasses for data validation? **Pattern matching**: how to use pattern matching together with type hints to write cleaner and more maintainable code. By the end of this talk, you’ll have a clear understanding of how to use type hints effectively and why they’re a valuable tool in any Python developer’s toolkit"
    start_time_slot: 11:30
    end_time_slot: 12:45
    track_length: 1
    color: yellow
    type: workshop
    language: "English"
    python_level: "Beginner"
    topic_level: "Intermediate"
    requirements: ""
    topic: "Programming"
    location: "Aula Hedy Lamarr"
  - speaker: "Marina Palma"
    title: "Image Generation with AI (GANs and Diffusion Techniques)"
    description: "Explore the techniques of AI-driven image generation, focusing on two powerful models: Generative Adversarial Networks (GANs) and Diffusion Models. We will learn the fundamental principles, practical applications, and differences between these approaches, along with hands-on demonstrations of how AI can be used to generate images."
    start_time_slot: 11:30
    end_time_slot: 12:45
    track_length: 1
    color: red
    type: workshop
    language: "Spanish"
    python_level: "Beginner"
    topic_level: "Beginner"
    requirements: ""
    topic: "Artificial Intelligence"
    location: "Sala d'actes Ada Lovelace"

  - start_time_slot: 13:00
    end_time_slot: 13:00
    track_length: 4
    color: pink
    title: "Group photo"
    type: photo
    location: Grades
    class: middle

  - start_time_slot: 13:15
    end_time_slot: 13:45
    track_length: 4
    color: purple
    title: "Lunch break & Lightning talks"
    type: lunch
    location: Grades
    class: middle

  - speaker: "Kemalcan Bora"
    title: "A kingdom above the clouds: How far can you go on AWS for $1 a month?"
    description: "Let's discover how to create a fully functional serverless application that costs less than your morning coffee!
    We'll build Cloud Kingdom, a cool document processing app that uses AWS Lambda, S3, SQS, and SNS, topped with AI capabilities from Claude. You'll learn how to upload documents, generate automatic summaries, and notify users, all while keeping your wallet happy."
    start_time_slot: 14:00
    end_time_slot: 15:15
    track_length: 1
    color: yellow
    type: workshop
    language: "English"
    python_level: "Advanced"
    topic_level: "Advanced"
    topic: "Serverless development"
    location: "Sala d'actes Ada Lovelace"
    requirements: "AWS Account"
  - speaker: "Raúl Cumplido"
    title: "A deep dive into the Arrow Columnar format with pyarrow and nanoarrow"
    description: "Apache Arrow has become a de-facto standard for efficient in-memory columnar data representation. You might have heard about Arrow or using Arrow, but do you understand the format and why it’s so useful? This workshop will dive deep into the details of the Arrow columnar format, the different types and buffer layouts, and explore those details interactively using the pyarrow and nanoarrow libraries."
    start_time_slot: 14:00
    end_time_slot: 15:15
    track_length: 1
    color: blue
    type: workshop
    language: "English"
    python_level: "Intermediate"
    topic_level: "Intermediate"
    topic: "Apache Arrow, Data Science"
    requirements: "You will be able to find both the requirements and the Notebooks on the following repository: https://github.com/raulcd/2024-pyday-bcn-arrow-workshop"
    location: "Sala Margarita Salas"
  - speaker: "Pol Alvarez Vecino"
    title: "From text to actions: allowing LLMs to use your tools"
    description: "Dive into the world of AI with this hands-on workshop! Learn how to run OpenAI models locally using Python, and then take it a step further by developing custom tools that your AI agent can use. This workshop will bridge the gap between using pre-trained models and creating a personalized AI assistant tailored to your needs."
    start_time_slot: 14:00
    end_time_slot: 15:15
    track_length: 1
    color: red
    type: workshop
    language: "English"
    python_level: "Intermediate"
    topic_level: "Intermediate"
    requirements: "Register account at OpenAI and export token locally: ie. export OPENAPI_KEY=sk..... "
    topic: "Artificial Intelligence / Machine Learning"
    location: "Aula Hedy Lamarr"

  - speaker: "Israel Saeta Pérez"
    title: "Create a static website with Pelican"
    description: "Static site generators are awesome tools to build websites that are fast to develop, maintainable and easy to deploy in a secure and cheap environment. In this workshop we will create and deploy a basic static website using Pelican."
    start_time_slot: 14:00
    end_time_slot: 15:15
    track_length: 1
    color: green
    type: workshop
    language: "English"
    python_level: "Intermediate"
    topic_level: "Intermediate"
    requirements: "Github account"
    topic: "Web development"
    location: "Aula Hipàtia d'Alexandria"

  - start_time_slot: 15:30
    end_time_slot: 15:45
    track_length: 4
    color: purple
    title: "Coffee break & Lightning talks"
    type: coffee
    location: Grades
    class: middle

  - speaker: "Dave Pitts"
    title: "Open Source Databases Python Devs"
    description: "Are you interested in exploring open-source databases? Maybe you have experience with MySQL or PostgreSQL? Perhaps you are unsure which one to pick for your next project, then this workshop is for you. Both are highly successful open-source projects, with many similarities but also some notable differences. I'll also touch on some techniques for optimizing database queries."
    start_time_slot: 16:00
    end_time_slot: 17:15
    track_length: 1
    color: yellow
    type: workshop
    language: "English"
    python_level: "Intermediate"
    topic_level: "Beginner"
    requirements: "Postgres and MySQL installed locally or via Docker"
    topic: "Databases"
    location: "Aula Hipàtia d'Alexandria"
  - speaker: "Manuel Gijón"
    title: "Introduction to data pipelines with Kestra and MLFlow"
    description: ""
    start_time_slot: 16:00
    end_time_slot: 17:15
    track_length: 1
    color: blue
    type: workshop
    language: "English"
    python_level: "Beginner"
    topic_level: "Beginner"
    topic: "Data engineering"
    location: "Sala d'actes Ada Lovelace"
    requirements: "Docker, Conda"
  - speaker: ""
    title: "Predict gender equality with your own Machine Learning model"
    description: ""
    start_time_slot: 16:00
    end_time_slot: 17:15
    track_length: 1
    color: red
    type: workshop
    language: "English"
    python_level: "Beginner"
    topic_level: "Beginner"
    topic: "Data science"
    location: "Sala Margarita Salas"
  - speaker: "Jimena"
    title: "L'Embolic: Videojuegos hechos en el frontend por un lenguaje de backend"
    description: "¿Te gustan los videojuegos? Entonces, seguro sabes que, desde hace años, los juegos diseñados para ejecutarse en el navegador son bastante populares, tanto por la facilidad de desarrollo como por su versatilidad, al poder jugarlos independientemente del sistema operativo.
    ¿Y si te digo que ya no es necesario dominar todos los entresijos del desarrollo frontend para poder crearlos? Hoy en día, podrías programarlos con tus conocimientos de Python.
    PyScript es un framework que permite crear aplicaciones que se ejecutan en el navegador y, con un poco de práctica, ¡incluso podemos desarrollar juegos! Pásate por este taller y te enseñaré cómo hacerlo."
    start_time_slot: 16:00
    end_time_slot: 17:15
    track_length: 1
    color: yellow
    type: workshop
    language: "Spanish"
    python_level: "Intermediate"
    topic_level: "Beginner"
    topic: "Web development, Videogames"
    location: "Aula Hedy Lamarr"

  - start_time_slot: 17:30
    end_time_slot: 17:45
    track_length: 4
    color: purple
    title: "Lightning talks + closing session & Kahoot"
    description: ""
    type: talk
    location: TBD
    class: middle
---


## About PyDay BCN 2024

We are excited to announce the **8th edition** of PyDay in Barcelona!

PyDay is an event packed with FREE **python-related workshops** and activities for the Python community. It is organized once per year. Over the <a href="#previous_editions_section">last seven editions</a>, PyDay has become a fantastic opportunity to share our love for Python and engage users, companies, and newcomers!

#### When and where

It is scheduled for **Saturday 9th November** at <a href="https://maps.app.goo.gl/Uxiao2Dr7uio9o3v9" target="_blank">Canòdrom</a>, from 9:00 a.m. to 18:00 p.m. CET, approximately.

#### A full day of in-person, hands-on workshops

PyDay BCN 2024 will have different **thematic tracks** --e.g. data science, web development, security-- with hands-on workshops lasting about 90 minutes. Participants will learn how to use different libraries, tools and techniques, fully guided by community members and support volunteers.

#### Participate in Kahoot and win prizes!

We will host a Kahoot game with questions about PyBCN and Python in general, with prizes for the fastest players. Will you miss it?!
