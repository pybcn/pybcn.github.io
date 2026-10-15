---
title: "PyDay BCN (2023)"
year: 2023
# The day of this edition, from the Meetup export, which records it per event.
date: 2023-11-11
# The venue of this edition, from the Meetup export, which records it per event.
venue: "Universitat de Barcelona"
description: "For the community, by the community!"
menu:
  main:
    parent: "PyDay BCN"
weight: 3
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
      <b>6th November, 9AM</b>: General registration open through <a target='_blank' href='https://www.eventbrite.es/e/entradas-pydaybcn-2023-751258453257?aff=oddtdtcreator'>Eventbrite</a><br/>
      <b>11th November</b>: PyDay BCN 2023"
  - title: Registration
    id: registration
    content: "General registration will open on Monday 6th of November, at 9AM through <a target='_blank' href='https://www.eventbrite.es/e/entradas-pydaybcn-2023-751258453257?aff=oddtdtcreator'>Eventbrite</a>."

sponsor_levels:
  - sponsors_per_line: 2
    sponsors: [qustodio, travelperk, iomed, flanks, preply]
    name: Gold
  - sponsors_per_line: 3
    sponsors: [aimsun, coopdevs, apsl, somenergia]
    name: Silver
  - sponsors_per_line: 3
    sponsors: [pythones, ikigai]
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
            - vyron-vasileiadis
            - adria-blanco
            - guillermo-abad
            - javier-sabariego
            - christian-adell
            - pavel-sulimov
            - ferran-jovell
            - alberto-labarga
            - diego-giaquinta
            - oriol-abril-pla
            - gabriel-de-maeztu
            - camilo-chacon-sartori
            - israel-saeta-perez
            - emanuel-frazao

  - title: Organizers
    id: organizers
    levels:
      - people_per_line: 4
        people:
          - natalia-padilla
          - alicia-morales-carrasco
          - patricia-lamadrid-robles
          - elisabeth-ortega-carrasco

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
  - id: room-b5
    name: "Room B5"
  - id: room-b6
    name: "Room B6"
  - id: room-b3
    name: "Room B3"
  - id: claustre
    name: "Claustre"

# The talks of this edition: what was said, by whom, in which language. A talk
# carries no time and no room, because it is the content and not the slot.
# agenda below is what places it on the grid, and one talk can take more than
# one slot. The id is derived from the title and is the anchor a photo of the
# gallery links to, so it must not change.
talks:
  - id: introduction-to-neural-networks-with-pytorch
    title: "Introduction to Neural Networks with PyTorch"
    speakers: [noe-casas]
    type: workshop
    language: en
    topic: "Data science"
    duration_minutes: 75
    description: "In this session, we'll delve into the fundamentals of deep learning, explore the basics of PyTorch, and learn how to create and train simple neural networks. You won't need a GPU to run the code from the workshop. All you'll need is a computer with Python, PyTorch, and Jupyter installed."
  - id: quantum-computing-for-everyone
    title: "Quantum Computing for Everyone"
    speakers: [vyron-vasileiadis, adria-blanco, guillermo-abad, javier-sabariego]
    type: workshop
    language: en
    topic: "Quantum Computing"
    duration_minutes: 75
    description: "Quantum computing stands at the forefront of the next technological revolution, offering promises to solve problems beyond the reach of classical computers. This workshop aims to demystify the complex world of quantum computing, making it accessible to a broad audience, including students, professionals, and enthusiasts with varying levels of expertise in physics and computer science. We begin with a gentle introduction to the fundamental principles of quantum computing and key concepts such as superposition, entanglement, and quantum gates.\nMoving beyond theory, the focus will shift to practical aspects with an introduction to Qibo, a new open-source framework designed for quantum simulation and experimentation. Qibo provides an intuitive platform for implementing quantum algorithms, making it an ideal tool for both beginners and experienced researchers.\nThe highlight of the talk will be live demonstrations using Qibo. These demos will showcase how to set up a quantum environment, create simple quantum circuits, and run basic quantum algorithms."
  - id: automating-networks-with-nornir
    title: "Automating networks with Nornir"
    speakers: [christian-adell]
    type: workshop
    language: en
    topic: "Network/Infrastructure Automation"
    duration_minutes: 75
    description: "In this workshop, we will leverage the Nornir Python framework to automate a network environment (but it could be applied to other infrastructure) in a multi-threaded way. We will also leverage other networking-related libraries such as NAPALM and Netmiko."
  - id: introduction-to-artificial-emotional-intelligence-decode
    title: "Introduction to Artificial [Emotional] Intelligence: Decode emotions with Deep Learning and Facial Recognition"
    speakers: [emanuel-frazao]
    type: workshop
    language: en
    topic: "Data Science"
    duration_minutes: 75
    description: "One of the most interesting applications of artificial intelligence is Deep Learning, which involves using unstructured data such as images or text in conjunction with mathematical algorithms to create predictive models that will help us make more accurate decisions and enhance our analytical capabilities."
  - id: quantum-breakthrough-from-basic-quantum-algorithms-to
    title: "Quantum Breakthrough: From Basic Quantum Algorithms to Quantum Generative AI"
    speakers: [pavel-sulimov]
    type: workshop
    language: en
    topic: "Quantum Computing"
    duration_minutes: 75
    description: "Recently, IBM has announced free access to quantum computers with 100+ qubits. Does it mean that soon anybody will be able to easily crack passwords, hack banking systems and extract government secrets? At this workshop, we'll discuss the pros and potential hurdles of quantum algorithms, as well as look at possibilities of making money with quantum technologies (and Python) - but without breaking the law: from risk assessment to option pricing."
  - id: python-packaging-101
    title: "Python Packaging 101"
    speakers: [ferran-jovell]
    type: workshop
    language: en
    topic: "Python Packaging"
    duration_minutes: 75
    description: "Have you ever wondered how does the pip install the packages? Would you like to know how to create your very own python package? In this workshop, we will go through on all the necessary steps to get started on creating python packages and uploading them to the Python Packaging Index (PyPI)."
  - id: creating-virtual-worlds-generating-synthetic-data-for-ai
    title: "Creating Virtual Worlds: Generating Synthetic Data for AI Digital Twins"
    speakers: [alberto-labarga]
    type: workshop
    language: es
    topic: "Data science"
    duration_minutes: 75
    description: "In the era of digital transformation, the concept of \"Digital Twins\" has emerged as a powerful tool for simulating, predicting, and optimizing real-world systems. At the heart of these digital replicas lies data, and often, the challenge is to have enough high-quality data to train robust AI models. This is where synthetic data generation comes into play. In this workshop, participants will be introduced to the world of synthetic data generation and its pivotal role in enabling AI-based digital twins. We will delve into the challenges of real-world data, the need for synthetic data, and the methodologies to generate it using Python"
  - id: creacion-de-apis-con-python-y-manejo-de-datos
    title: "Creación de APIs con Python y manejo de datos"
    title_lang: Spanish
    speakers: [diego-giaquinta]
    type: workshop
    language: es
    topic: "API requests"
    duration_minutes: 75
    description: "Implementación de APIs con Python, para poder realizar peticiones http e intercambio de información entre aplicaciones y automatizar tareas"
  - id: create-a-personal-website-with-sphinx
    title: "Create a personal website with sphinx"
    speakers: [oriol-abril-pla]
    type: workshop
    language: en
    topic: "Documentation and blogging"
    duration_minutes: 75
    description: "Personal websites are becoming more common, and there are countless alternatives to create them. Sphinx might often not make that list, but it can do everything we need, and most python projects use it for their documentation, so it won't require you to learn any new tool."
  - id: lightning-talks-session-1-coffee-break
    title: "Lightning talks (session 1) & Coffee break"
    type: talk
    duration_minutes: 15
    description: " <h2>Lightning talks</h2>\n<b>Data Visualization using Blender</b><br> <i>Muhammad Usman</i> <p><q>Welcome to the 'Data Visualization using Python in Blender' adventure - where your data turns into a magic carpet ride through enchanted forests and talking teapots! Just like a certain enchanted rose or a friendly blue genie, we'll use Python scripting in Blender to bring your data to life in whimsical 3D visualizations, animated charts, and interactive scenes that would make any animated teapot dance with joy!</q></p>\n<b>Writing Code Is Not Your Job: Thoughts On Data Science On A Post-chatGPT World</b><br> <i>Álvaro Durán </i> <p><q>ChatGPT has taken the world by storm. Self-proclaimed futurists such as Chamath Palihapitiya have predicted the disruption of many multi-million dollar companies as a result. The role of data scientists, as a result, will be diminished if a machine can understand unstructured text.</q></p>\n<b>PyCamp 2024</b><br> <i>Israel Saeta</i> <p><q>We will present the PyCamp 2024 event that will take place in Girona next spring.</q></p>\n<b>Algorithmic Fairness (Ethics in Data)</b><br> <i>Neema Balolebwami Nelly</i> <p><q>Gain a profound understanding of the ethical dimensions in data-driven systems, focusing on algorithmic fairness. Discover how to implement fairness principles to promote just and equitable outcomes in your software projects.</q></p>\n<b>Demystifying LLM deployments in AWS SageMaker</b><br> <i>Guillermo Blasco</i> <p><q>OS LLMs (falcon, lama, mistral,...) can be challenging to deploy for production, but they are not! We will deploy lince-zero (fine tune of falcon7b by clibrain) in AWS SageMaker in 3 minutes from sage maker studio notebooks with python!</q></p> "
  - id: retrieval-augmented-generation-from-scratch
    title: "Retrieval Augmented Generation from scratch"
    speakers: [gabriel-de-maeztu]
    type: workshop
    language: en
    topic: "Data Science"
    duration_minutes: 75
    description: "In this workshop, I will focus on how to build a Retrieval Augmented Generation model from scratch using Postgres pg_vector for efficient similarity search and Hugging Face Transformers for generating human-like text. This workshop is aimed at data scientists, NLP practitioners, and engineers interested in cutting-edge NLP techniques."
  - id: mojo-el-poderoso-aliado-de-python
    title: "Mojo: El poderoso aliado de Python"
    title_lang: Spanish
    speakers: [camilo-chacon-sartori]
    type: workshop
    language: es
    topic: "General, Core"
    duration_minutes: 75
    description: "En este workshop, te invitamos a explorar las virtudes de Mojo (https://www.modular.com/mojo), un nuevo lenguaje de programación que pretende ser un aliado de Python. Mojo aspira a ofrecer todas las funcionalidades de Python, y va más allá, al incorporar características adicionales que le permiten alcanzar un rendimiento superior."
  - id: mob-programming-solving-coding-problems-collaboratively
    title: "Mob programming: Solving coding problems collaboratively"
    speakers: [israel-saeta-perez]
    type: workshop
    language: es
    topic: "Test driven development"
    duration_minutes: 75
    description: "Coding together is much more fun than coding alone! In this workshop we will learn from each other by solving a basic coding problem using mob programming and Test Driven Development techniques."
  - id: lightning-talks-session-2-closing-session-kahoot
    title: "Lightning talks (session 2) & Closing session & Kahoot"
    type: talk
    duration_minutes: 15
    description: " <h2>Lightning talks</h2>\n<b>Creación de APIs con Python y manejo de datos</b><br> <i>Diego Giaquinta</i> <p><q>Implementación sencilla de APIs con Python, para poder realizar peticiones http e intercambio de información entre aplicaciones.</q></p>\n<b>Step4ward: Empowering Women in Tech</b><br> <i>Susana Vázquez y Coral Olivares</i> <p><q>Come explore step4ward, a non-profit organization passionately crafted BY and FOR women. In just 5 minutes, learn how we're all about supporting women in the tech job market. We provide advice, build a community, and help with interview prep and early career steps. Let's break barriers and boost women in tech together!</q></p>\n<b>Common Security Vulnerabilities for Developers</b><br> <i>Dan Neciu</i> <p><q>Best practices for developers to protect themselves from scams and hacking attempts</q></p>\n<b>Machine Learning for time-series analysis in the context of IoT</b><br> <i>Raziel Amador</i> <p><q>In this light talk, I would like to present my implementation of temperature and humidity monitoring using Iot (Raspberry Pi, DHT22 sensor, all in Docker services), and Machine learning for time series analysis.</q></p>\n<b>How to support the Python open source ecosytem</b><br> <i>Oriol Abril</i> <p><q>I will showcase a wide array of ways for anyone to support the Python open source ecosystem, with a special focus on financial support. I won't have any special focus on special communities or libraries but will aim for a general overview: including open source contributions as part of one's job description, sponsoring events and/or libraries, donating to foundations that act as umbrella for the exisiting projects...</q></p>\n<b>Tinymem: a game under 40 lines and under 30mm</b><br> <i>Isaac Bernat</i> <p><q>We'll go through <a href='https://github.com/isaacbernat/tinymem' target='_blank'>tinymem</a>, a working example of a game programmed in MicroPython which has menus, audio, sprites, text, button inputs... All this under 40 lines of code available for the <a href='https://thumby.us/' target='_blank'>Thumby</a> hardware, which is a miniature Raspberry Pi Pico based console.</q></p> "

# The grid, one row per slot of the day, in the order it is printed. A slot
# names the talk it holds, or carries its own label and type when it holds
# none: a break, the group photo, the welcome. The level and the requirements
# sit here and not on the talk, because they are what the slot asks of whoever
# walks into it. A start is always quoted: YAML 1.1 reads an unquoted 9:00 as
# the integer 540.
agenda:
  - start: "9:00"
    credited_as: "PyDay BCN 2023 Organising Committee"
    track_length: 3
    room: room-b5
    type: group
    label: "Registration & Welcome"
    duration_minutes: 15
  - start: "9:30"
    track_length: 1
    room: room-b6
    talk: introduction-to-neural-networks-with-pytorch
    python_level: beginner
    topic_level: beginner
    requirements: "Python, PyTorch, Jupyter, Matplotlib."
  - start: "9:30"
    track_length: 1
    room: room-b5
    talk: quantum-computing-for-everyone
    python_level: beginner
    topic_level: beginner
    requirements: "To have the `qibo` package installed."
  - start: "9:30"
    track_length: 1
    room: room-b3
    talk: automating-networks-with-nornir
    python_level: beginner
    topic_level: intermediate
  - start: "11:00"
    track_length: 3
    room: claustre
    type: coffee
    label: "Coffee break"
    duration_minutes: 15
  - start: "11:30"
    track_length: 1
    room: room-b6
    talk: introduction-to-artificial-emotional-intelligence-decode
    python_level: beginner
    topic_level: beginner
  - start: "11:30"
    track_length: 1
    room: room-b5
    talk: quantum-breakthrough-from-basic-quantum-algorithms-to
    python_level: intermediate
    topic_level: intermediate
    requirements: "Numpy, Scipy, Matplotlib, PyTorch, Qiskit"
  - start: "11:30"
    track_length: 1
    room: room-b3
    talk: python-packaging-101
    python_level: beginner
    topic_level: beginner
    requirements: "Laptop with latest Python version available and git installed"
  - start: "13:00"
    track_length: 3
    room: claustre
    type: photo
    label: "Group photo"
    duration_minutes: 0
  - start: "13:15"
    track_length: 3
    room: claustre
    type: lunch
    label: "Lunch break"
    duration_minutes: 30
  - start: "14:00"
    track_length: 1
    room: room-b6
    talk: creating-virtual-worlds-generating-synthetic-data-for-ai
    python_level: intermediate
    topic_level: beginner
  - start: "14:00"
    track_length: 1
    room: room-b5
    talk: creacion-de-apis-con-python-y-manejo-de-datos
    python_level: intermediate
    topic_level: intermediate
    requirements: "Python 3.8 or above, VSCode or some similar IDE, FastApi and uvicorn libraries"
  - start: "14:00"
    track_length: 1
    room: room-b3
    talk: create-a-personal-website-with-sphinx
    python_level: beginner
    topic_level: beginner
  - start: "15:30"
    track_length: 3
    room: room-b5
    talk: lightning-talks-session-1-coffee-break
  - start: "16:00"
    track_length: 1
    room: room-b6
    talk: retrieval-augmented-generation-from-scratch
    python_level: intermediate
    topic_level: advanced
    requirements: "Python, Docker"
  - start: "16:00"
    track_length: 1
    room: room-b5
    talk: mojo-el-poderoso-aliado-de-python
    python_level: intermediate
    topic_level: intermediate
  - start: "16:00"
    track_length: 1
    room: room-b3
    talk: mob-programming-solving-coding-problems-collaboratively
    python_level: intermediate
    topic_level: beginner
    requirements: "Python with pytest installed, code editor, git (for downloading the exercise)."
  - start: "17:30"
    track_length: 3
    room: room-b5
    talk: lightning-talks-session-2-closing-session-kahoot

# Photos published by PyBCN on the day, one per post so no two share a caption,
# which is also the alt text. Imported with bin/import-x-photos, which excludes
# anything the account only shared: that copyright belongs to somebody else.
photos:
  thread: "https://x.com/PyBCN/status/1723274179888230446"
  items:
    - file: pyday-2023/01-welcome-to-the-pydaybcn-2023-https-pybcn-org-event.jpg
      caption: "Welcome to the #PyDayBCN 2023! https://pybcn.org/events/pyday_bcn/pyday_bcn_2023/"
      source: "https://x.com/PyBCN/status/1723274179888230446"
      time: "10:39"
    - file: pyday-2023/02-pydaybcn-is-an-event-full-of-free-python-related-w.jpg
      caption: "#PyDayBCN is an event full of free python-related workshops and activities for the Barcelona Python community, organized once per year"
      source: "https://x.com/PyBCN/status/1723274187488256485"
      time: "10:39"
    - file: pyday-2023/03-introduction-to-neural-networks-with-pytorch-by-no.jpg
      caption: "\"Introduction to Neural Networks with PyTorch\", by Noé Casas"
      source: "https://x.com/PyBCN/status/1723274805997179294"
      time: "10:41"
      talk: introduction-to-neural-networks-with-pytorch
    - file: pyday-2023/04-quantum-computing-for-everyone-by-vyron-vasileiadi.jpg
      caption: "\"Quantum Computing for Everyone\", by Vyron Vasileiadis, Adrià Blanco, Guille Abad and Javier Sabariego"
      source: "https://x.com/PyBCN/status/1723275563450675247"
      time: "10:44"
      talk: quantum-computing-for-everyone
    - file: pyday-2023/05-automating-networks-with-nornir-by-christian-adell.jpg
      caption: "\"Automating networks with Nornir\", by Christian Adell"
      source: "https://x.com/PyBCN/status/1723275859388244070"
      time: "10:45"
      talk: automating-networks-with-nornir
    - file: pyday-2023/06-introduction-to-artificial-emotional-intelligence.jpg
      caption: "\"Introduction to Artificial [Emotional] Intelligence: Decode emotions with Deep Learning and Facial Recognition\" by Emanuel Frazao"
      source: "https://x.com/PyBCN/status/1723305285027082336"
      time: "12:42"
      talk: introduction-to-artificial-emotional-intelligence-decode
    - file: pyday-2023/07-quantum-breakthrough-from-basic-quantum-algorithms.jpg
      caption: "\"Quantum Breakthrough: From Basic Quantum Algorithms to Quantum Generative AI\" by Pavel Sulimov"
      source: "https://x.com/PyBCN/status/1723305399871254963"
      time: "12:43"
      talk: quantum-breakthrough-from-basic-quantum-algorithms-to
    - file: pyday-2023/08-python-packaging-101-by-ferran-jovell.jpg
      caption: "\" Python Packaging 101\", by Ferran Jovell"
      source: "https://x.com/PyBCN/status/1723306078576816327"
      time: "12:46"
      talk: python-packaging-101
    - file: pyday-2023/09-had-a-great-lunch-break-thanks-sponsors.jpg
      caption: "Had a great lunch break. Thanks, sponsors!"
      source: "https://x.com/PyBCN/status/1723328858223501495"
      time: "14:16"
    - file: pyday-2023/10-creating-virtual-worlds-generating-synthetic-data.jpg
      caption: "\"Creating Virtual Worlds: Generating Synthetic Data for AI Digital Twins\", by Alberto Labarga"
      source: "https://x.com/PyBCN/status/1723329782849376654"
      time: "14:20"
      talk: creating-virtual-worlds-generating-synthetic-data-for-ai
    - file: pyday-2023/11-creacion-de-apis-con-python-y-manejo-de-datos-by-d.jpg
      caption: "\"Creación de APIs con Python y manejo de datos\", by Diego Giaquinta"
      source: "https://x.com/PyBCN/status/1723330041860202798"
      time: "14:21"
      talk: creacion-de-apis-con-python-y-manejo-de-datos
    - file: pyday-2023/12-create-a-personal-website-with-sphinx-by-oriol-abr.jpg
      caption: "\"Create a personal website with sphinx\", by Oriol Abril"
      source: "https://x.com/PyBCN/status/1723330176501596620"
      time: "14:21"
      talk: create-a-personal-website-with-sphinx
    - file: pyday-2023/13-retrieval-augmented-generation-from-scratch-by-gab.jpg
      caption: "\"Retrieval Augmented Generation from scratch\", by Gabriel de Maeztu"
      source: "https://x.com/PyBCN/status/1723370453249479067"
      time: "17:01"
      talk: retrieval-augmented-generation-from-scratch
    - file: pyday-2023/14-gabimaeztu-iomed-ehr-mojo-el-poderoso-aliado-de-py.jpg
      caption: "\"Mojo: El poderoso aliado de Python\", by Camilo Chacón"
      source: "https://x.com/PyBCN/status/1723370632065233082"
      time: "17:02"
      talk: mojo-el-poderoso-aliado-de-python
    - file: pyday-2023/15-gabimaeztu-iomed-ehr-mob-programming-solving-codin.jpg
      caption: "\"Mob programming: Solving coding problems collaboratively\", by Israel Saeta"
      source: "https://x.com/PyBCN/status/1723370811296190680"
      time: "17:03"
      talk: mob-programming-solving-coding-problems-collaboratively
    - file: pyday-2023/16-data-visualization-using-blender-by-muhammad-usman.jpg
      caption: "\"Data Visualization using Blender\", by Muhammad Usman"
      source: "https://x.com/PyBCN/status/1723389842363441256"
      time: "18:18"
    - file: pyday-2023/17-writing-code-is-not-your-job-thoughts-on-data-scie.jpg
      caption: "\"Writing Code Is Not Your Job: Thoughts On Data Science On A Post-chatGPT World\", by Álvaro Durán"
      source: "https://x.com/PyBCN/status/1723390142935687275"
      time: "18:20"
    - file: pyday-2023/18-pycamp-2024-by-israel-saeta.jpg
      caption: "\"PyCamp 2024\", by Israel Saeta"
      source: "https://x.com/PyBCN/status/1723390346946576517"
      time: "18:20"
    - file: pyday-2023/19-demystifying-llm-deployments-in-aws-sagemaker-by-g.jpg
      caption: "\"Demystifying LLM deployments in AWS SageMaker\", by Guillermo Blasco"
      source: "https://x.com/PyBCN/status/1723390541499359647"
      time: "18:21"
    - file: pyday-2023/20-step4ward-empowering-women-in-tech-by-susana-vazqu.jpg
      caption: "\"Step4ward: Empowering Women in Tech\", by Susana Vázquez and Coral Olivares"
      source: "https://x.com/PyBCN/status/1723391091230065006"
      time: "18:23"
    - file: pyday-2023/21-common-security-vulnerabilities-for-developers-by.jpg
      caption: "\"Common Security Vulnerabilities for Developers\", by Dan Neciu"
      source: "https://x.com/PyBCN/status/1723391244942864452"
      time: "18:24"
    - file: pyday-2023/22-machine-learning-for-time-series-analysis-in-the-c.jpg
      caption: "\"Machine Learning for time-series analysis in the context of IoT\", by Raziel Amador"
      source: "https://x.com/PyBCN/status/1723391406733959312"
      time: "18:25"
    - file: pyday-2023/23-how-to-support-the-python-open-source-ecosytem-by.jpg
      caption: "\"How to support the Python open source ecosytem\", by Oriol Abril"
      source: "https://x.com/PyBCN/status/1723391549793350102"
      time: "18:25"
    - file: pyday-2023/24-tinymem-a-game-under-40-lines-and-under-30mm-by-is.jpg
      caption: "\"Tinymem: a game under 40 lines and under 30mm\", by Isaac Bernat"
      source: "https://x.com/PyBCN/status/1723391728705495145"
      time: "18:26"
    - file: pyday-2023/25-thank-you-all-for-sponsoring-speaking-organizing-a.jpg
      caption: "Thank you all for sponsoring, speaking, organizing, and for assisting!"
      source: "https://x.com/PyBCN/status/1723392641125974477"
      time: "18:29"
    - file: pyday-2023/26-let-s-play-a-game.jpg
      caption: "Let's play a game!"
      source: "https://x.com/PyBCN/status/1723393250931696010"
      time: "18:32"
    - file: pyday-2023/27-congratulations-to-the-winners.jpg
      caption: "Congratulations to the winners!"
      source: "https://x.com/PyBCN/status/1723394075527630978"
      time: "18:35"
    - file: pyday-2023/28-thanks-qustodio-qustodio-for-sponsoring-us.jpg
      caption: "Thanks Qustodio (@qustodio) for sponsoring us!"
      source: "https://x.com/PyBCN/status/1723397962334691551"
      time: "18:51"
    - file: pyday-2023/29-thanks-travelperk-travelperk-for-sponsoring-us.jpg
      caption: "Thanks Travelperk (@travelperk) for sponsoring us!"
      source: "https://x.com/PyBCN/status/1723398182476873915"
      time: "18:52"
    - file: pyday-2023/30-thanks-iomed-iomed-ehr-for-sponsoring-us.jpg
      caption: "Thanks IOMED (@iomed_ehr) for sponsoring us!"
      source: "https://x.com/PyBCN/status/1723398493765583099"
      time: "18:53"
    - file: pyday-2023/31-thanks-flanks-flanks-io-for-sponsoring-us.jpg
      caption: "Thanks Flanks (@Flanks_io) for sponsoring us!"
      source: "https://x.com/PyBCN/status/1723398651215487073"
      time: "18:53"
    - file: pyday-2023/32-thanks-preply-preplycom-for-sponsoring-us.jpg
      caption: "Thanks Preply (@PreplyCom) for sponsoring us!"
      source: "https://x.com/PyBCN/status/1723398866970591424"
      time: "18:54"
    - file: pyday-2023/33-thank-you-for-the-pydaybcn.jpg
      caption: "Thank you for the #PyDayBCN! ❤️"
      source: "https://x.com/PyBCN/status/1723405506839027714"
      time: "19:21"
---

## About PyDay BCN 2023

We are organizing the **the seventh edition** of PyDay in Barcelona!

PyDay is an event full of FREE **python-related workshops** and activities for the Python community, organized once per year. Over the last six editions, PyDay has become a great opportunity to share our love for Python and engage users, companies and newcomers into it!

### When and where

It is scheduled for **Saturday 11th November** in [Universitat de Barcelona](https://maps.app.goo.gl/RT9THKhxqz3eTvxf7), from 9:00am to 18:00pm CET, aprox.

### A full day of in-person hands-on workshops

PyDay BCN 2023 will have different **thematic tracks** --e.g. data science, web development, security-- with hands-on workshops of about 90 minutes in which participants will learn how to use different libraries, tools and techniques, fully guided by members of the community and support volunteers.

### Participate in Kahoot and win prizes!

We will host a Kahoot game with questions about PyBCN and Python in general, with prizes for the fastest players. Will you miss it?!
