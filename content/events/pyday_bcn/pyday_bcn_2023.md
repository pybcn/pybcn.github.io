---
title: "PyDay BCN 2023"
description: "For the community, by the community!"
menu:
  main:
    parent: "PyDay BCN"
weight: 1
aliases:
  - /pyday-bcn-2023
heroBackground: /images/photos/people-pyday-2019.jpg

layout: event

free_text_sections:
  - title: Important dates
    id: important_dates
    content: "<b>2nd October</b>: Call for proposals opening: <a href='https://forms.gle/MdS3Qx64wQs9N7NQ8' target='_blank' >Workshops</a> and <a target='_blank' href='https://forms.gle/RZ2vYzGtWNgUnuBT8'>Lightning talks</a><br/>
      <b>22nd October</b>: Call for proposals closing<br/>
      <b>31st October</b>: Program available<br/>
      <b>3rd November, 9AM</b>: Early registration open for PyBCN members, PyDay speakers and sponsors<br/>
      <b>6th November, 9AM</b>: General registration open through Eventbrite<br/>
      <b>11th November</b>: PyDay BCN 2023"
  - title: Registration
    id: registration
    content: "General registration will open on Monday 6th of November, at 9AM through Eventbrite."

sponsors_text: "Would you like to sponsor this event? Please contact us at pydaybcn2023@googlegroups.com<br/><br/>"
sponsor_levels:
  - sponsors_per_line: 2
    sponsors: [qustodio, travelperk, iomed, flanks, preply]
    name: Gold
  - sponsors_per_line: 3
    sponsors: [aimsun, coopdevs, apsl]
    name: Silver
  - sponsors_per_line: 3
    sponsors: [pythones]
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
            - noe-casas
            - christian-adell
            - pavel-sulimov
            - ferran-jovell
            - alberto-labarga
            - diego-giaquinta
            - oriol-abril-pla
            - gabriel-de-maeztu
            - camilo-chacon
            - israel-saeta

  - title: Organizers
    id: organizers
    levels:
      - people_per_line: 4
        people:
          - natalia
          - alicia-morales
          - patricia-lamadrid
          - elisabeth-ortega-carrasco

previous_editions:
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
    speaker: "PyDay BCN 2023 Organising Committee"
    type: group
    location: Room B5
    class: middle

  - speaker: "Noé Casas"
    title: "Introduction to Neural Networks with PyTorch"
    description: "In this session, we'll delve into the fundamentals of deep learning, explore the basics of PyTorch, and learn how to create and train simple neural networks. You won't need a GPU to run the code from the workshop. All you'll need is a computer with Python, PyTorch, and Jupyter installed."
    start_time_slot: 9:30
    end_time_slot: 10:45
    track_length: 1
    color: blue
    type: workshop
    language: "English"  
    python_level: "<i class=\"fas fa-circle green\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: "Python, PyTorch, Jupyter, Matplotlib."
    topic: "Data science"
    location: Room B6
  - speaker: "Vyron Vasileiadis, Adrià Blanco, Guille Abad and Javier Sabariego"
    title: "Quantum Computing for Everyone"
    description: "Quantum computing stands at the forefront of the next technological revolution, offering promises to solve problems beyond the reach of classical computers. This workshop aims to demystify the complex world of quantum computing, making it accessible to a broad audience, including students, professionals, and enthusiasts with varying levels of expertise in physics and computer science.
    We begin with a gentle introduction to the fundamental principles of quantum computing and key concepts such as superposition, entanglement, and quantum gates.
    
    Moving beyond theory, the focus will shift to practical aspects with an introduction to Qibo, a new open-source framework designed for quantum simulation and experimentation. Qibo provides an intuitive platform for implementing quantum algorithms, making it an ideal tool for both beginners and experienced researchers.
    
    The highlight of the talk will be live demonstrations using Qibo. These demos will showcase how to set up a quantum environment, create simple quantum circuits, and run basic quantum algorithms."
    start_time_slot: 9:30
    end_time_slot: 10:45
    track_length: 1
    color: blue
    type: workshop
    language: "English"  
    python_level: "<i class=\"fas fa-circle green\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: "To have the `qibo` package installed."
    topic: "Quantum Computing"
    location: Room B5
  - speaker: "Christian Adell"
    title: "Automating networks with Nornir"
    description: "In this workshop, we will leverage the Nornir Python framework to automate a network environment (but it could be applied to other infrastructure) in a multi-threaded way. We will also leverage other networking-related libraries such as NAPALM and Netmiko."
    start_time_slot: 9:30
    end_time_slot: 10:45
    track_length: 1
    color: yellow
    type: workshop
    language: "English"
    python_level: "<i class=\"fas fa-circle green\"></i>"
    topic_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic: "Network/Infrastructure Automation"
    location: Room B3
    requirements: "You should have Docker installed."

  - start_time_slot: 11:00
    end_time_slot: 11:15
    track_length: 3
    color: purple
    title: "Coffee break"
    type: coffee
    location: Claustre
    class: middle

  - speaker: ""
    title: "Introduction to Artificial [Emotional] Intelligence: Decode emotions with Deep Learning and Facial Recognition"
    description: "One of the most interesting applications of artificial intelligence is Deep Learning, which involves using unstructured data such as images or text in conjunction with mathematical algorithms to create predictive models that will help us make more accurate decisions and enhance our analytical capabilities."
    start_time_slot: 11:30
    end_time_slot: 12:45
    track_length: 1
    color: blue
    type: workshop
    language: "English"
    python_level: "<i class=\"fas fa-circle green\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: ""
    topic: "Data Science"
    location: Room B6
  - speaker: "Pavel Sulimov"
    title: "Quantum Breakthrough: From Basic Quantum Algorithms to Quantum Generative AI"
    description: "Recently, IBM has announced free access to quantum computers with 100+ qubits. Does it mean that soon anybody will be able to easily crack passwords, hack banking systems and extract government secrets? At this workshop, we'll discuss the pros and potential hurdles of quantum algorithms, as well as look at possibilities of making money with quantum technologies (and Python) - but without breaking the law: from risk assessment to option pricing."
    start_time_slot: 11:30
    end_time_slot: 12:45
    track_length: 1
    color: yellow
    type: workshop
    language: "English"
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle yellow\"></i>"
    requirements: "Numpy, Scipy, Matplotlib, PyTorch, Qiskit"
    topic: "Quantum Computing"
    location: Room B5
  - speaker: "Ferran Jovell"
    title: "Python Packaging 101"
    description: "Have you ever wondered how does the pip install the packages? Would you like to know how to create your very own python package? 
    In this workshop, we will go through on all the necessary steps to get started on creating python packages and uploading them to the Python Packaging Index (PyPI)."
    start_time_slot: 11:30
    end_time_slot: 12:45
    track_length: 1
    color: blue
    type: workshop
    language: "English"
    python_level: "<i class=\"fas fa-circle green\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: "Laptop with latest Python version available"
    topic: "Python Packaging"
    location: Room B3

  - start_time_slot: 13:00
    end_time_slot: 13:00
    track_length: 3
    color: pink
    title: "Group photo"
    type: photo
    location: Claustre
    class: middle

  - start_time_slot: 13:15
    end_time_slot: 13:45
    track_length: 3
    color: purple
    title: "Lunch break"
    type: lunch
    location: Claustre
    class: middle

  - speaker: "Alberto Labarga"
    title: "Creating Virtual Worlds: Generating Synthetic Data for AI Digital Twins"
    description: "In the era of digital transformation, the concept of \"Digital Twins\" has emerged as a powerful tool for simulating, predicting, and optimizing real-world systems. At the heart of these digital replicas lies data, and often, the challenge is to have enough high-quality data to train robust AI models. This is where synthetic data generation comes into play. In this workshop, participants will be introduced to the world of synthetic data generation and its pivotal role in enabling AI-based digital twins. We will delve into the challenges of real-world data, the need for synthetic data, and the methodologies to generate it using Python"
    start_time_slot: 14:00
    end_time_slot: 15:15
    track_length: 1
    color: yellow
    type: workshop
    language: "Spanish"
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: ""
    topic: "Data science"
    location: Room B6
  - speaker: "Diego Giaquinta"
    title: "Creación de APIs con Python y manejo de datos"
    description: "Implementación de APIs con Python, para poder realizar peticiones http e intercambio de información entre aplicaciones y automatizar tareas"
    start_time_slot: 14:00
    end_time_slot: 15:15
    track_length: 1
    color: yellow
    type: workshop
    language: "Spanish"
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic: "API requests"
    requirements: "Python 3.8 or above, VSCode or some similar IDE, FastApi and uvicorn libraries"
    location: Room B5
  - speaker: "Oriol Abril"
    title: "Create a personal website with sphinx"
    description: "Personal websites are becoming more common, and there are countless alternatives to create them. Sphinx might often not make that list, but it can do everything we need, and most python projects use it for their documentation, so it won't require you to learn any new tool."
    start_time_slot: 14:00
    end_time_slot: 15:15
    track_length: 1
    color: blue
    type: workshop
    language: "English"
    python_level: "<i class=\"fas fa-circle green\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: ""
    topic: "Documentation and blogging"
    location: Room B3

  - start_time_slot: 15:30
    end_time_slot: 15:45
    track_length: 3
    color: purple
    title: "Coffee break"
    type: coffee
    location: Claustre
    class: middle

  - speaker: "Gabriel de Maeztu"
    title: "Retrieval Augmented Generation from scratch"
    description: "In this workshop, I will focus on how to build a Retrieval Augmented Generation model from scratch using Postgres pg_vector for efficient similarity search and Hugging Face Transformers for generating human-like text. This workshop is aimed at data scientists, NLP practitioners, and engineers interested in cutting-edge NLP techniques."
    start_time_slot: 16:00
    end_time_slot: 17:15
    track_length: 1
    color: red
    type: workshop
    language: "English"
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle red\"></i>"
    requirements: "Python, Docker"
    topic: "Data Science"
    location: Room B6

  - speaker: "Camilo Chacón"
    title: "Mojo: El poderoso aliado de Python"
    description: "En este workshop, te invitamos a explorar las virtudes de Mojo (https://www.modular.com/mojo), un nuevo lenguaje de programación que pretende ser un aliado de Python. Mojo aspira a ofrecer todas las funcionalidades de Python, y va más allá, al incorporar características adicionales que le permiten alcanzar un rendimiento superior."
    start_time_slot: 16:00
    end_time_slot: 17:15
    track_length: 1
    color: yellow
    type: workshop
    language: "Spanish"
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle yellow\"></i>"
    requirements: ""
    topic: "General, Core"
    location: Room B5

  - speaker: "Israel Saeta"
    title: "Mob programming: Solving coding problems collaboratively"
    description: "Coding together is much more fun than coding alone! In this workshop we will learn from each other by solving a basic coding problem using mob programming and Test Driven Development techniques."
    start_time_slot: 16:00
    end_time_slot: 17:15
    track_length: 1
    color: yellow
    type: workshop
    language: "Spanish"
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requeriments: "Python with pytest installed, code editor, git (for downloading the exercise)."
    topic: "Test driven development"
    location: Room B3

  - start_time_slot: 17:30
    end_time_slot: 17:45
    track_length: 3
    color: purple
    title: "Lightning talks + closing session & Kahoot"
    description: ""
    type: talk
    location: Room B5
    class: middle
---

## About PyDay BCN 2023

We are organizing the **the seventh edition** of PyDay in Barcelona!

PyDay is an event full of FREE **python-related workshops** and activities for the Python community, organized once per year. Over the <a href="#previous_editions_section">last six editions</a>, PyDay has become a great opportunity to share our love for Python and engage users, companies and newcomers into it!

#### When and where

It is scheduled for **Saturday 11th November** in <a href="https://maps.app.goo.gl/RT9THKhxqz3eTvxf7" target="_blank">Universitat de Barcelona</a>, from 9:00am to 18:00pm CET, aprox.

#### A full day of in-person hands-on workshops

PyDay BCN 2023 will have different **thematic tracks** --e.g. data science, web development, security-- with hands-on workshops of about 90 minutes in which participants will learn how to use different libraries, tools and techniques, fully guided by members of the community and support volunteers.

#### Participate in Kahoot and win prizes!

We will host a Kahoot game with questions about PyBCN and Python in general, with prizes for the fastest players. Will you miss it?!
