---
title: "PyDay BCN 2025"
description: "For the community, by the community!"
menu:
  main:
    parent: "PyDay BCN"
weight: 1
aliases:
  - /pyday-bcn-2025
heroBackground: /images/photos/canodrom.png

layout: event

free_text_sections:
  - title: Important dates
    id: important_dates
    content: "<b>29th September</b>: Call for proposals opening: <a href='https://forms.gle/tGnJHW5oNkCFQrXx7' target='_blank' >Workshops</a> and <a target='_blank' href='https://forms.gle/GzYmMU4qvqRHmgCh7'>Lightning talks</a><br/>
      <b>7th November</b>: Call for proposals closing<br/>
      <b>21th November</b>: Program available<br/>
      <b>24th November, 9AM</b>: Early registration open for PyBCN members, PyDay speakers and sponsors<br/>
      <b>25th November, 9AM</b>: General registration open through <a target='_blank' href='https://www.eventbrite.es/e/pyday-2025-tickets-1924233868299?aff=oddtdtcreator'>Eventbrite</a><br/>
      <b>29th November</b>: PyDay BCN 2025"
  - title: Registration
    id: registration
    content: "General registration will open on Tuesday 25th of November, at 9AM through <a target='_blank' href=''>Eventbrite</a>."

sponsors_text: "Would you like to sponsor this event? Please contact us at pyday2025@googlegroups.com<br/><br/>"
sponsor_levels:
  - sponsors_per_line: 2
    sponsors: [okta, rover, pythones, preply]
    name: Gold
  - sponsors_per_line: 3
    sponsors: [ikigai, capitole, orpheus]
    name: Silver
  - sponsors_per_line: 3
    sponsors: [innoit, qilimanjaro, xorq]
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
            - enric-domingo
            - ester-jara
            - javier-ramos-panduro
            - natalia
            - amir-azam
            - david
            - javier-sabariego
            - ely-farres
            - flavie-le-bars
            - cristina-cosma
            - ricardo-ander-egg
            - alberto
            - jordi-bosch            
            - kemalcan-bora
            - kevin-sanchez
            - oriol-abril-pla         
            - camilo-chacon
            - victor-garcia
            - eric-massip
            - ubaldo-hervas
            - david-blazquez
            - kevin-albes
            - brian-power

  - title: Organizers
    id: organizers
    levels:
      - people_per_line: 4
        people:
          - sergi-ramirez
          - toni-espadas
          - jordi-bosch
          - daniel-mesejo

#  - title: Staff
#    id: staff
#    levels:
#      - people_per_line: 4
#        people:
#          - sergi-ramirez
#          - toni-espadas
#          - jordi-bosch
#          - daniel-mesejo
#          - jose-riera
#          - mauricio
#          - brian-power
#          - eva-casas
#          - gaby
#          - Camilo
          
previous_editions:
  - name: PyDay BCN 2024
    url: /events/pyday_bcn/pyday_bcn_2024/
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
    speaker: "PyDay BCN 2025 Organising Committee"
    type: group
    location: "Sala d'actes Ada Lovelace"
    class: middle

  - speaker: "Enric Domingo"
    title: "Build advanced Agentic LLM Apps with LangGraph and LangChain"
    description: "In this workshop we will learn how to build useful LLM agentic workflows in Python using LangChain and LangGraph, open source libraries and the most popular and powerful tools for advanced AI Engineering projects. They are capable of solving complex tasks, doing multiple LLM calls, using memory, structured outputs, popular tools, custom tools and even being able to introduce human-in-the-loop interactions when needed."
    start_time_slot: 9:30
    end_time_slot: 10:45
    track_length: 1
    color: blue
    type: workshop
    language: "English"  
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: "Intermediate experience in Python and basic understanding of LLMs and how to use LLM APIs"
    topic: "LLM"
    location: "Sala d'actes Ada Lovelace"
    repositories: ""
#    repositories: "https://github.com/ericmassip/carbon-home-watcher"

  - speaker: "Ester Jara"
    title: "From Zero to Chatbot: Create Your Own AI Assistant with Python"
    description: "The development of a local AI chatbot using Python is explored step by step. It begins with setting up the environment and loading a compact open-source language model, then guides through creating a structured interaction loop to process input and generate responses. Prompts are designed, conversational context is managed with a rolling history, and a lightweight memory component is added to maintain coherent multi-turn interactions. A short introduction to agentic behaviour illustrates how simple decision-making and task handling can make a chatbot more autonomous. By the end, a fully functional chatbot is built, with a clear understanding of its main components and how they work together."
    start_time_slot: 9:30
    end_time_slot: 10:45
    track_length: 1
    color: yellow
    type: workshop
    language: "Spanish"  
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: "        
       - No prior experience with AI or machine learning
        -  Basic familiarity with Python (variables, functions, running scripts)
        - Laptop with Python 3.9+ installed
        - Ability to install Python packages (pip)
        - Code editor such as VS Code"
    topic: "Artificial Intelligence (IA)"
    location: "Sala Margarita Salas"
    repositories: ""
#    repositories: "https://github.com/ericmassip/carbon-home-watcher"

  - speaker: "Natàlia Padilla, Amir Azam, David Arcos, Javier Sabariego, Ely Farrés & Flavie Le Bars"
    title: "Introduction to Analog Quantum Computing"
    description: "Participants will learn how to design and simulate an analog quantum algorithm using QiliSDK, directly from their laptops.

      QiliSDK is a Python framework for writing digital and analog quantum algorithms and executing them across multiple quantum backends. Its modular design streamlines the development process and enables easy integration with a variety of quantum platforms."
    start_time_slot: 9:30
    end_time_slot: 10:45
    track_length: 1
    color: red
    type: workshop
    language: "English"
    python_level: "<i class=\"fas fa-circle green\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: "pip install qilisdk"
    topic: "Quantum Computing"
    location: "Aula Hady Lamarr"
    repositories: ""
#    repositories: "https://github.com/ericmassip/carbon-home-watcher"

  - speaker: "Javier Ramos Panduro"
    title: "Testeando API's like a boss con BDD"
    description: "Un repaso de como realizar test e2e de nuestras API's utilizando pytest y bdd"
    start_time_slot: 9:30
    end_time_slot: 10:45
    track_length: 1
    color: orange
    type: workshop
    language: "Spanish"  
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle yellow\"></i>"
    requirements: "Python environment y IDE"
    topic: "Testing"
    location: "Sala Hipátia d'Alexandra" 
    repositories: ""    
#    repositories: "https://github.com/ericmassip/carbon-home-watcher"

  - start_time_slot: 11:00
    end_time_slot: 11:15
    track_length: 4
    color: purple
    title: "Coffee break"
    type: coffee
    location: Terrassa
    class: middle

  - speaker: "Cristina Cosma"
    title: "Del texto al dato: cómo entienden las maquinas el lenguaje humano con Python "
    description: "Exploraremos como los ordenadores pueden analizar el lenguaje natural humano, transformarlo en datos y extraer información valiosa a partir de palabras. Aplicaremos técnicas básicas de NLP (procesamiento de lenguaje natural) como el procesamiento de palabras, el análisis de sentimientos, de las intensidades y frecuencias. Visualizaremos y compararemos los resultados para comprender cómo los algoritmos interpretan el tono y el contenido de lo que los humanos expresamos."
    start_time_slot: 11:30
    end_time_slot: 12:45
    track_length: 1
    color: blue
    type: workshop
    language: "Spanish"
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: "Conexión a internet, cuenta de Google (para trabajar en Google Colab a través de librerías ya disponibles sin necesidad de usar consola de comandos (cmd) ni instalar Python en local."
    topic: "Data science, Natural Language Process, Data Visualization"
    location: "Sala d'actes Ada Lovelace"
    repositories: "https://github.com/cristinasprogrammingadventure/PyDay-2025_workshop-Del-Texto-al-Dato_NLP"    

  - speaker: "Ricardo Ander-Egg"
    title: "Crea un agente LLM desde cero, sin frameworks."
    description: "En este taller vamos a desmitificar los agentes LLM y a construir uno desde cero, sin usar frameworks. Entenderás la lógica fundamental que permite a un modelo de lenguaje razonar y usar herramientas externas, programándolo todo con Python y la librería oficial de OpenAI.

    Trabajaremos de forma 100% práctica para implementar el bucle de control que convierte a un LLM en un agente autónomo: recibir un objetivo, pensar qué herramienta usar, ejecutarla y decidir el siguiente paso. El objetivo es que comprendas el mecanismo interno de un agente.

    Al finalizar, serás capaz de:

    - Entender la arquitectura básica de un agente LLM (razonamiento + acción).

    - Implementar un bucle de control para que el LLM pueda usar herramientas.

    - Permitir al modelo ejecutar funciones de Python."
    
    start_time_slot: 11:30
    end_time_slot: 12:45
    track_length: 1
    color: yellow
    type: workshop
    language: "Spanish/English"
    python_level: "<i class=\"fas fa-circle green\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: "Conexión a internet. Python 3.10+. Tener la librería \"openai\" instalada. No se necesitará una API key para el taller. Se recomienda usar un gestor de entornos como uv o virtualenv, aunque no es obligatorio. Cada participante debe tener su entorno listo. Durante el taller se utilizará \"uv\" para gestionar dependencias."
    topic: "LLM"
    location: "Sala Margarita Salas"
    repositories: "https://github.com/polyrand/pyday2025-llm"    

  - speaker: "Alberto Camara"
    title: "Building Multi-Agent System with Pydantic AI"
    description: "A hands-on workshop teaching multi-agent system design using Pydantic AI to analyze arXiv papers. Participants will build cooperating agents that extract citations, analyze context, and link claims to evidence—demonstrating agent orchestration, validation patterns, and structured outputs."
    start_time_slot: 11:30
    end_time_slot: 12:45
    track_length: 1
    color: red
    type: workshop
    language: "English"
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic: "Data Science"
    location: "Aula Hady Lamarr"
    requirements: "Participants should bring a laptop with:

          - Python 3.10+ installed

          - Ollama installed with Llama 3.2 model downloaded

          - Basic familiarity with Python

          - 8GB+ RAM recommended

      No prior experience with AI agents or Pydantic AI required."
    repositories: ""      
#    repositories: "https://github.com/ericmassip/carbon-home-watcher"

  - speaker: "Jordi Bosch"
    title: "Mastering Word Automation with Python"
    description: "Tired of editing Word documents manually and breaking templates by mistake? Join the automation revolution as we see how Python can manage bookmarks, placeholders and structured templates inside .docx files. We’ll discover how to populate fields, update content programmatically and generate consistent documents with just a few lines of code. By the end, you’ll be creating automated Word files smoothly, saving time and reducing errors in your everyday workflows. Get ready to upgrade your document-handling skills!"
    start_time_slot: 11:30
    end_time_slot: 12:45
    track_length: 1
    color: orange
    type: workshop
    language: "Spanish"
    python_level: "<i class=\"fas fa-circle green\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: "Python and DOCX"
    topic: "Artificial Intelligence"
    location: "Sala Hipátia d'Alexandra" 
    repositories: ""    
    #    repositories: "https://github.com/ericmassip/carbon-home-watcher"

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
    title: "Lunch break"
    type: lunch
    location: Terrassa
    class: middle

  - speaker: "Ricardo Ander-Egg"
    title: "Keywords, BM25 y vectores: construyendo un buscador de texto desde cero"
    description: "En este taller aprenderemos cómo funcionan de verdad los buscadores de texto, más allá de las cajas negras de las librerías. Partiremos de los conceptos más básicos (índices, tokens, ranking) y llegaremos hasta técnicas modernas como BM25 y búsqueda vectorial, implementándolo todo a mano desde cero. 
    
    Trabajaremos de forma totalmente práctica: construirás tu propio mini‑buscador, primero basado en keywords y \"scoring\" clásico, y después lo extenderemos con métodos más avanzados y representación vectorial. El objetivo del taller es entender los principios básicos que hay detrás de los motores de búsqueda y cómo se implementan.

    Al finalizar, serás capaz de:

    - Implementar un índice invertido simple y un buscador basado en keywords.

    - Entender y programar un sistema de ranking con TF‑IDF / BM25.

    - Utilizar vectores y similitud de coseno para búsqueda semántica básica.

    - Comparar enfoques y saber cuándo usar palabras clave, BM25 o vectores."
    start_time_slot: 14:00
    end_time_slot: 15:15
    track_length: 1
    color: blue
    type: workshop
    language: "Spanish/English"
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: "Python 3.10+ (cada participante puede decidir seguir el taller con un Jupyter Notebook, Google Colab, scripts de Python, etc). El taller se desarrollará utilizando archivos de texto de Python, pero es apto para seguirlo en un notebook también."
    topic: "LLM"
    location: "Sala d'actes Ada Lovelace"
    repositories: "https://github.com/polyrand/pyday2025-text"
    

  - speaker: "Kevin Sanchez"
    title: "Del Desorden Visual al Significado: Una Aventura con Transformers y Donut"
    description: "En este workshop práctico de 90 minutos exploraremos cómo los modelos basados en Transformers han revolucionado el campo de la visión por computadora, superando arquitecturas clásicas como CNNs en tareas de clasificación, detección y segmentación. A través de un caso de estudio original, aprenderás a:

    - Preparar un dataset para visión por computadora.

    - Implementar un pipeline completo usando Python, PyTorch, HuggingFace y Ollama.

    - Aplicar un Vision Transformer (ViT) y/o modelos híbridos como DETR.

    - Evaluar resultados y visualizar predicciones con herramientas modernas.

    - Comprender cómo extender el pipeline a casos reales de negocio.

    El enfoque será 100% práctico, con código reproducible y materiales descargables para que puedas continuar experimentando después del taller."
    start_time_slot: 14:00
    end_time_slot: 15:15
    track_length: 1
    color: yellow
    type: workshop
    language: "Catalan"
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic: "Computer vision"
    requirements: "Python"
    location: "Sala Margarita Salas"
    repositories: ""    
#    repositories: "https://github.com/ericmassip/carbon-home-watcher"

  - speaker: "Kemalcan Bora"
    title: "House, Controlled by AI (What Could Go Wrong?)"
    description: "This project demonstrates how agentic AI can enable autonomous decision-making and natural-language interaction in smart home systems. By integrating an ESP32 microcontroller with basic sensors (e.g., temperature, motion, or object detection), we show how an AI agent can perceive environmental data, reason about it, and act on user instructions or contextual conditions.

      For example, the agent can:

      - Adjust the air conditioner temperature to 30°C based on voice or text commands.
      - Query fridge inventory data (e.g., count remaining eggs).
      - Detect home occupancy using motion or door sensors."
    start_time_slot: 14:00
    end_time_slot: 15:15
    track_length: 1
    color: red
    type: workshop
    language: "English"
    python_level: "<i class=\"fas fa-circle red\"></i>"
    topic_level: "<i class=\"fas fa-circle red\"></i>"
    requirements: "python, transformers, llama-index"
    topic: "Agent IA"
    location: "Aula Hady Lamarr"
    location: "Sala d'actes Ada Lovelace"
    repositories: ""    
#    repositories: "https://github.com/ericmassip/carbon-home-watcher"

  - speaker: "Oriol Abril"
    title: "Models de regressió bayesians"
    description: "En aquesta xerrada explorarem els models lineals generalitzats (GLMs) dins del paradigma Bayesià a través de la llibreria bambi. Introduirem els GLMs i els seus tres components principals: el predictor lineal, la distribució observacional i la funció d’enllaç. Després veurem el paper que hi juguen les distribucions a priori per als paràmetres del model i com utilitzar-los per a ampliar els GLMs incorporant-hi jerarquia. Tot això ho farem utilitzant la llibreria bambi, una llibreria comunitària de programari lliure que permet definir GLMs a través d’una sintaxis amb fórmules i fer inferència a través de PyMC o NumPyro."
    start_time_slot: 14:00
    end_time_slot: 15:15
    track_length: 1
    color: orange
    type: workshop
    language: "Catalan"
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: "Utilitzarem la última versió de la llibreria bambi durant el taller. Es recomana tenir un virtual environment amb la llibreria ja instal·lada si es vol seguir el taller en directe. El taller també assumeix un nivell intermedi en l'ús de NumPy i Pandas."
    topic: "Statistics and Data Science"
    location: "Sala Hipátia d'Alexandra" 
    repositories: "https://github.com/OriolAbril/pyday2025-bambi"    

  - start_time_slot: 15:30
    end_time_slot: 15:45
    track_length: 4
    color: purple
    title: "Coffee break"
    type: coffee
    location: Claustre
    class: middle

  - speaker: "Camilo Chacón Sartori"
    title: "Agentes Inteligentes que Evolucionan: Software Automodificable con LLMs y Python"
    description: "En este workshop exploraremos cómo construir software automodificable utilizando agentes basados en LLMs, con implementaciones prácticas en Python. Partiremos de los fundamentos de agentes autónomos y LLMs, para mostrar cómo estos sistemas pueden autoevaluarse, reescribirse y adaptarse a nuevas tareas de manera autónoma. La sesión tendrá un énfasis práctico, aprovechando mi experiencia en la integración de la computación evolutiva y LLMs, para que los participantes adquieran herramientas concretas para experimentar con software autoevolutivo."
    start_time_slot: 16:00
    end_time_slot: 17:15
    track_length: 1
    color: blue
    type: workshop
    language: "Spanish"
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: "Portátil y acceso a internet, para poder clonar el repositorio y seguir las instrucciones."
    topic: "IA Generativa"
    location: "Sala d'actes Ada Lovelace"
    repositories: ""    
#    repositories: "https://github.com/ericmassip/carbon-home-watcher"

  - speaker: "Victor Garcia"
    title: "Fabric en Acción: conectando bloques, datos y magia en python"
    description: "En este workshop práctico de 90 minutos exploraremos Fabric, una poderosa herramienta que permite automatizar tareas, orquestar flujos de trabajo y construir pipelines reproducibles en Python. A través de ejemplos concretos aprenderás cómo combinar bloques de código, manejar datos y desplegar procesos complejos de forma elegante y extensible.

      Durante la sesión veremos desde los fundamentos de Fabric hasta casos de uso reales: automatización de tareas repetitivas, integración con servicios externos, ejecución remota y creación de scripts que convierten procesos largos y manuales en flujos automatizados. Todo ello acompañado de demostraciones paso a paso para que puedas aplicar lo aprendido inmediatamente en tus propios proyectos.

      Si buscas potenciar tus habilidades para crear herramientas internas, pipelines de datos o automatizar el día a día con Python, este workshop es para ti. ¡Ven a descubrir cómo Fabric puede convertir tus scripts en auténtica magia productiva!"
    start_time_slot: 16:00
    end_time_slot: 17:15
    track_length: 1
    color: yellow
    type: workshop
    language: "English"
    python_level: "<i class=\"fas fa-circle green\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: ""
    topic: ""
    location: "Sala Margarita Salas"
    repositories: ""    
#    repositories: "https://github.com/ericmassip/carbon-home-watcher"

  - speaker: "Eric Massip"
    title: "HTMX: A love story between a backend dev and a frontend “framework”"
    description: "HTMX brings modern interactivity to the web without the complexity of a full frontend framework. In this workshop, we’ll dig into how HTMX works while staying in the comfort of Django’s views and templates. We’ll explore how hypermedia can simplify frontend development and bring back clarity to the client–server relationship. We’ll then put it all into practice by building a small hypermedia-driven web app that feels reactive and dynamic."
    start_time_slot: 16:00
    end_time_slot: 17:15
    track_length: 1
    color: red
    type: workshop
    language: "English"
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    topic: "Web development"
    location: "Aula Hady Lamarr"
    repositories: "https://github.com/ericmassip/carbon-home-watcher"    

  - speaker: "Ubaldo Hervas"
    title: "Causal Inference: a brief introduction"
    description: "Discover how causal inference separates correlation from causation to drive better decisions. This fast-paced introduction covers key concepts—treatments, counterfactuals, DAGs, confounding, experiments vs. observational data—and practical tools like A/B tests, DiD, and IVs. Learn design principles, common pitfalls, and how to frame questions that unlock credible, actionable insights at scale."
    start_time_slot: 16:00
    end_time_slot: 17:15
    track_length: 1
    color: orange
    type: workshop
    language: "English"  
    python_level: "<i class=\"fas fa-circle yellow\"></i>"
    topic_level: "<i class=\"fas fa-circle green\"></i>"
    requirements: "Notebook and basic python knowledge"
    topic: "Causal Inference & Data Science"
    location: "Sala Hipátia d'Alexandra"
    repositories: ""    
#    repositories: "https://github.com/ericmassip/carbon-home-watcher"

  - start_time_slot: 17:30
    end_time_slot: 17:45
    track_length: 4
    color: purple
    title: "Lightning talks + closing session & Kahoot"
    description: "Lighting talks: 
    
    <br> <b> David Blazquez Garcia </b>: Building an Industrial Knowledge Graph Assistant with Python, Neo4j and FastAPI</br>  
    <br> <b> Kevin Albes </b>: Building Multi-Agent Workflows with Agent Framework</br>
    <br> <b> Brian Power </b>: Python for Data Cleaning - 5 simple examples in real time)</br>"
    type: talk
    location: Sala d'Actes Ada Lovelace
    class: middle
#    repositories: "https://github.com/ericmassip/carbon-home-watcher"
---


## About PyDay BCN 2025

We are excited to announce the **9th edition** of PyDay in Barcelona!

PyDay is an event packed with FREE **Python-related workshops** and activities for the Python community. It is organized once per year. Over the <a href="#previous_editions_section">last eight editions</a>, PyDay has become a fantastic opportunity to share our love for Python and engage users, companies, and newcomers!

#### When and where

It is scheduled for **Saturday 29th November** at <a href="https://maps.app.goo.gl/Uxiao2Dr7uio9o3v9" target="_blank">Canòdrom</a>, from 9:00 a.m. to 18:00 p.m. CET, approximately.

#### A full day of in-person, hands-on workshops

PyDay BCN 2025 will have different **thematic tracks** --e.g. data science, web development, security-- with hands-on workshops lasting about 90 minutes. Participants will learn how to use different libraries, tools and techniques, fully guided by community members and support volunteers.

#### Participate in Kahoot and win prizes!

We will host a Kahoot game with questions about PyBCN and Python in general, with prizes for the fastest players. Will you miss it?!