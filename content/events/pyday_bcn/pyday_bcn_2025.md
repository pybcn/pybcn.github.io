---
title: "PyDay BCN (2025)"
year: 2025
# The day of this edition. It is not in the Meetup export: the registration
# of 2025 ran on Eventbrite.
date: 2025-11-29
# The venue of this edition, from the room names and the hero image of this page: this edition sold tickets on Eventbrite and was never a Meetup event.
venue: "Canòdrom"
description: "For the community, by the community!"
menu:
  main:
    parent: "PyDay BCN"
weight: 1
aliases:
  - /pyday-bcn-2025
heroBackground: /images/photos/canodrom.jpg

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
    content: "General registration will open on Tuesday 25th of November, at 9AM through <a target='_blank' href='https://www.eventbrite.es/e/pyday-2025-tickets-1924233868299?aff=oddtdtcreator'>Eventbrite</a>."

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
            - natalia-padilla
            - amir-azam
            - david-arcos
            - javier-sabariego
            - ely-farres-palomeras
            - flavie-le-bars
            - cristina-cosma
            - ricardo-ander-egg-aguilar
            - alberto-camara
            - jordi-bosch            
            - kemalcan-bora
            - kevin-sanchez-sancho
            - oriol-abril-pla         
            - camilo-chacon-sartori
            - victor-garcia-dominguez
            - eric-massip
            - ubaldo-hervas
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
          - daniel-mesejo-leon

#  - title: Staff
#    id: staff
#    levels:
#      - people_per_line: 4
#        people:
#          - sergi-ramirez
#          - toni-espadas
#          - jordi-bosch
#          - daniel-mesejo-leon
#          - jose-riera-sanchez
#          - mauricio
#          - brian-power
#          - eva-casas
#          - gaby
#          - Camilo
          
spansDuration: 15
numTracks: 4
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
  - id: sala-margarita-salas
    name: "Sala Margarita Salas"
  - id: sala-hedy-lamarr
    name: "Sala Hedy Lamarr"
  - id: sala-hipatia-dalexandria
    name: "Sala Hipàtia d'Alexandria"
  - id: terrassa
    name: "Terrassa"
  - id: grades
    name: "Grades"
  - id: claustre
    name: "Claustre"

# The talks of this edition: what was said, by whom, in which language. A talk
# carries no time and no room, because it is the content and not the slot.
# agenda below is what places it on the grid, and one talk can take more than
# one slot. The id is derived from the title and is the anchor a photo of the
# gallery links to, so it must not change.
talks:
  - id: build-advanced-agentic-llm-apps-with-langgraph-and-langchain
    title: "Build advanced Agentic LLM Apps with LangGraph and LangChain"
    speakers: [enric-domingo]
    type: workshop
    language: en
    topic: "LLM"
    duration_minutes: 75
    description: "In this workshop we will learn how to build useful LLM agentic workflows in Python using LangChain and LangGraph, open source libraries and the most popular and powerful tools for advanced AI Engineering projects. They are capable of solving complex tasks, doing multiple LLM calls, using memory, structured outputs, popular tools, custom tools and even being able to introduce human-in-the-loop interactions when needed."
    links:
      - type: github
        url: "https://github.com/enricd/langgraph_agents_pyday_bcn"
  - id: from-zero-to-chatbot-create-your-own-ai-assistant-with
    title: "From Zero to Chatbot: Create Your Own AI Assistant with Python"
    speakers: [ester-jara]
    type: workshop
    language: es
    topic: "Artificial Intelligence (IA)"
    duration_minutes: 75
    description: "The development of a local AI chatbot using Python is explored step by step. It begins with setting up the environment and loading a compact open-source language model, then guides through creating a structured interaction loop to process input and generate responses. Prompts are designed, conversational context is managed with a rolling history, and a lightweight memory component is added to maintain coherent multi-turn interactions. A short introduction to agentic behaviour illustrates how simple decision-making and task handling can make a chatbot more autonomous. By the end, a fully functional chatbot is built, with a clear understanding of its main components and how they work together."
    links:
      - type: github
        url: "https://github.com/esterjara/ai-chatbot-workshop"
  - id: introduction-to-analog-quantum-computing
    title: "Introduction to Analog Quantum Computing"
    speakers: [natalia-padilla, amir-azam, david-arcos, javier-sabariego, ely-farres-palomeras, flavie-le-bars]
    type: workshop
    language: en
    topic: "Quantum Computing"
    duration_minutes: 75
    description: "Participants will learn how to design and simulate an analog quantum algorithm using QiliSDK, directly from their laptops.\nQiliSDK is a Python framework for writing digital and analog quantum algorithms and executing them across multiple quantum backends. Its modular design streamlines the development process and enables easy integration with a variety of quantum platforms."
    links:
      - type: slides
        label: "Presentation"
        url: "https://docs.google.com/presentation/d/1QHQHSbCnpdEJj2BLAFIFk0M0lbjLM6StTgbNojUBcQk/edit"
      - type: notebooks
        label: "Workshop Notebooks"
        url: "https://drive.google.com/drive/folders/18ds2Onl0hqW3NMJ7FpgErkaRtYvslrHK"
  - id: testeando-apis-like-a-boss-con-bdd
    title: "Testeando API's like a boss con BDD"
    title_lang: Spanish
    speakers: [javier-ramos-panduro]
    type: workshop
    language: es
    topic: "Testing"
    duration_minutes: 75
    description: "Un repaso de como realizar test e2e de nuestras API's utilizando pytest y bdd"
    links:
      - type: github
        url: "https://github.com/breadhardIT/pytest-pybdd"
  - id: del-texto-al-dato-como-entienden-las-maquinas-el-lenguaje
    title: "Del texto al dato: cómo entienden las maquinas el lenguaje humano con Python"
    title_lang: Spanish
    speakers: [cristina-cosma]
    type: workshop
    language: es
    topic: "Data science, Natural Language Process, Data Visualization"
    duration_minutes: 75
    description: "Exploraremos como los ordenadores pueden analizar el lenguaje natural humano, transformarlo en datos y extraer información valiosa a partir de palabras. Aplicaremos técnicas básicas de NLP (procesamiento de lenguaje natural) como el procesamiento de palabras, el análisis de sentimientos, de las intensidades y frecuencias. Visualizaremos y compararemos los resultados para comprender cómo los algoritmos interpretan el tono y el contenido de lo que los humanos expresamos."
    links:
      - type: github
        url: "https://github.com/cristinasprogrammingadventure/PyDay-2025_workshop-Del-Texto-al-Dato_NLP"
  - id: crea-un-agente-llm-desde-cero-sin-frameworks
    title: "Crea un agente LLM desde cero, sin frameworks."
    title_lang: Spanish
    speakers: [ricardo-ander-egg-aguilar]
    type: workshop
    language: [en, es]
    topic: "LLM"
    duration_minutes: 75
    description: "En este taller vamos a desmitificar los agentes LLM y a construir uno desde cero, sin usar frameworks. Entenderás la lógica fundamental que permite a un modelo de lenguaje razonar y usar herramientas externas, programándolo todo con Python y la librería oficial de OpenAI.\nTrabajaremos de forma 100% práctica para implementar el bucle de control que convierte a un LLM en un agente autónomo: recibir un objetivo, pensar qué herramienta usar, ejecutarla y decidir el siguiente paso. El objetivo es que comprendas el mecanismo interno de un agente.\nAl finalizar, serás capaz de:\n- Entender la arquitectura básica de un agente LLM (razonamiento + acción).\n- Implementar un bucle de control para que el LLM pueda usar herramientas.\n- Permitir al modelo ejecutar funciones de Python."
    links:
      - type: github
        url: "https://github.com/polyrand/pyday2025-llm"
  - id: building-multi-agent-system-with-pydantic-ai
    title: "Building Multi-Agent System with Pydantic AI"
    speakers: [alberto-camara]
    type: workshop
    language: en
    topic: "Data Science"
    duration_minutes: 75
    description: "A hands-on workshop teaching multi-agent system design using Pydantic AI to analyze arXiv papers. Participants will build cooperating agents that extract citations, analyze context, and link claims to evidence-demonstrating agent orchestration, validation patterns, and structured outputs."
    links:
      - type: github
        url: "https://github.com/ber2/2025-pyday-multiagents-pydantic-ai"
  - id: mastering-word-automation-with-python
    title: "Mastering Word Automation with Python"
    speakers: [jordi-bosch]
    type: workshop
    language: es
    topic: "Artificial Intelligence"
    duration_minutes: 75
    description: "Tired of editing Word documents manually and breaking templates by mistake? Join the automation revolution as we see how Python can manage bookmarks, placeholders and structured templates inside .docx files. We'll discover how to populate fields, update content programmatically and generate consistent documents with just a few lines of code. By the end, you'll be creating automated Word files smoothly, saving time and reducing errors in your everyday workflows. Get ready to upgrade your document-handling skills!"
    links:
      - type: github
        url: "https://github.com/jordiba90/PyBcn-PyDay-2024.11.29-Docx"
  - id: keywords-bm25-y-vectores-construyendo-un-buscador-de-texto
    title: "Keywords, BM25 y vectores: construyendo un buscador de texto desde cero"
    title_lang: Spanish
    speakers: [ricardo-ander-egg-aguilar]
    type: workshop
    language: [en, es]
    topic: "LLM"
    duration_minutes: 75
    description: "En este taller aprenderemos cómo funcionan de verdad los buscadores de texto, más allá de las cajas negras de las librerías. Partiremos de los conceptos más básicos (índices, tokens, ranking) y llegaremos hasta técnicas modernas como BM25 y búsqueda vectorial, implementándolo todo a mano desde cero.\nTrabajaremos de forma totalmente práctica: construirás tu propio mini-buscador, primero basado en keywords y \"scoring\" clásico, y después lo extenderemos con métodos más avanzados y representación vectorial. El objetivo del taller es entender los principios básicos que hay detrás de los motores de búsqueda y cómo se implementan.\nAl finalizar, serás capaz de:\n- Implementar un índice invertido simple y un buscador basado en keywords.\n- Entender y programar un sistema de ranking con TF-IDF / BM25.\n- Utilizar vectores y similitud de coseno para búsqueda semántica básica.\n- Comparar enfoques y saber cuándo usar palabras clave, BM25 o vectores."
    links:
      - type: github
        url: "https://github.com/polyrand/pyday2025-text"
  - id: del-desorden-visual-al-significado-una-aventura-con
    title: "Del Desorden Visual al Significado: Una Aventura con Transformers y Donut"
    title_lang: Spanish
    speakers: [kevin-sanchez-sancho]
    type: workshop
    language: ca
    topic: "Computer vision"
    duration_minutes: 75
    description: "En este workshop práctico de 90 minutos exploraremos cómo los modelos basados en Transformers han revolucionado el campo de la visión por computadora, superando arquitecturas clásicas como CNNs en tareas de clasificación, detección y segmentación. A través de un caso de estudio original, aprenderás a:\n- Preparar un dataset para visión por computadora.\n- Implementar un pipeline completo usando Python, PyTorch, HuggingFace y Ollama.\n- Aplicar un Vision Transformer (ViT) y/o modelos híbridos como DETR.\n- Evaluar resultados y visualizar predicciones con herramientas modernas.\n- Comprender cómo extender el pipeline a casos reales de negocio.\nEl enfoque será 100% práctico, con código reproducible y materiales descargables para que puedas continuar experimentando después del taller."
    links:
      - type: github
        url: "https://github.com/kevinSanchez21/pyday_2025_vision_transformers"
  - id: house-controlled-by-ai-what-could-go-wrong
    title: "House, Controlled by AI (What Could Go Wrong?)"
    speakers: [kemalcan-bora]
    type: workshop
    language: en
    topic: "Agent IA"
    duration_minutes: 75
    description: "This project demonstrates how agentic AI can enable autonomous decision-making and natural-language interaction in smart home systems. By integrating an ESP32 microcontroller with basic sensors (e.g., temperature, motion, or object detection), we show how an AI agent can perceive environmental data, reason about it, and act on user instructions or contextual conditions.\nFor example, the agent can:\n- Adjust the air conditioner temperature to 30°C based on voice or text commands. - Query fridge inventory data (e.g., count remaining eggs). - Detect home occupancy using motion or door sensors."
    links:
      - type: github
        url: "https://github.com/kemalcanbora/pybcn2025"
  - id: models-de-regressio-bayesians
    title: "Models de regressió bayesians"
    title_lang: Catalan
    speakers: [oriol-abril-pla]
    type: workshop
    language: ca
    topic: "Statistics and Data Science"
    duration_minutes: 75
    description: "En aquesta xerrada explorarem els models lineals generalitzats (GLMs) dins del paradigma Bayesià a través de la llibreria bambi. Introduirem els GLMs i els seus tres components principals: el predictor lineal, la distribució observacional i la funció d'enllaç. Després veurem el paper que hi juguen les distribucions a priori per als paràmetres del model i com utilitzar-los per a ampliar els GLMs incorporant-hi jerarquia. Tot això ho farem utilitzant la llibreria bambi, una llibreria comunitària de programari lliure que permet definir GLMs a través d'una sintaxis amb fórmules i fer inferència a través de PyMC o NumPyro."
    links:
      - type: github
        url: "https://github.com/OriolAbril/pyday2025-bambi"
  - id: agentes-inteligentes-que-evolucionan-software
    title: "Agentes Inteligentes que Evolucionan: Software Automodificable con LLMs y Python"
    title_lang: Spanish
    speakers: [camilo-chacon-sartori]
    type: workshop
    language: es
    topic: "IA Generativa"
    duration_minutes: 75
    description: "En este workshop exploraremos cómo construir software automodificable utilizando agentes basados en LLMs, con implementaciones prácticas en Python. Partiremos de los fundamentos de agentes autónomos y LLMs, para mostrar cómo estos sistemas pueden autoevaluarse, reescribirse y adaptarse a nuevas tareas de manera autónoma. La sesión tendrá un énfasis práctico, aprovechando mi experiencia en la integración de la computación evolutiva y LLMs, para que los participantes adquieran herramientas concretas para experimentar con software autoevolutivo."
    links:
      - type: github
        url: "https://github.com/camilochs/pydaybcn2025-workshop-code-evolution"
  - id: fabric-en-accion-conectando-bloques-datos-y-magia-en-python
    title: "Fabric en Acción: conectando bloques, datos y magia en python"
    title_lang: Spanish
    speakers: [victor-garcia-dominguez]
    type: workshop
    language: en
    duration_minutes: 75
    description: "En este workshop práctico de 90 minutos exploraremos Fabric, una poderosa herramienta que permite automatizar tareas, orquestar flujos de trabajo y construir pipelines reproducibles en Python. A través de ejemplos concretos aprenderás cómo combinar bloques de código, manejar datos y desplegar procesos complejos de forma elegante y extensible.\nDurante la sesión veremos desde los fundamentos de Fabric hasta casos de uso reales: automatización de tareas repetitivas, integración con servicios externos, ejecución remota y creación de scripts que convierten procesos largos y manuales en flujos automatizados. Todo ello acompañado de demostraciones paso a paso para que puedas aplicar lo aprendido inmediatamente en tus propios proyectos.\nSi buscas potenciar tus habilidades para crear herramientas internas, pipelines de datos o automatizar el día a día con Python, este workshop es para ti. ¡Ven a descubrir cómo Fabric puede convertir tus scripts en auténtica magia productiva!"
    links:
      - type: github
        url: "https://github.com/ramitjans/pyDay25_fabrik_with_python"
  - id: htmx-a-love-story-between-a-backend-dev-and-a-frontend
    title: "HTMX: A love story between a backend dev and a frontend \"framework\""
    speakers: [eric-massip]
    type: workshop
    language: en
    topic: "Web development"
    duration_minutes: 75
    description: "HTMX brings modern interactivity to the web without the complexity of a full frontend framework. In this workshop, we'll dig into how HTMX works while staying in the comfort of Django's views and templates. We'll explore how hypermedia can simplify frontend development and bring back clarity to the client-server relationship. We'll then put it all into practice by building a small hypermedia-driven web app that feels reactive and dynamic."
    links:
      - type: github
        url: "https://github.com/ericmassip/carbon-home-watcher"
  - id: causal-inference-a-brief-introduction
    title: "Causal Inference: a brief introduction"
    speakers: [ubaldo-hervas]
    type: workshop
    language: en
    topic: "Causal Inference & Data Science"
    duration_minutes: 75
    description: "Discover how causal inference separates correlation from causation to drive better decisions. This fast-paced introduction covers key concepts-treatments, counterfactuals, DAGs, confounding, experiments vs. observational data-and practical tools like A/B tests, DiD, and IVs. Learn design principles, common pitfalls, and how to frame questions that unlock credible, actionable insights at scale."
    links:
      - type: github
        label: "Github"
        url: "https://github.com/UbaldoHervas/PyDay-BCN-2025"
      - type: link
        label: "Leanalytics"
        url: "https://leanalytics.substack.com/p/022-caso-practico-diferencia-en-diferencias-datos-sinteticos"
  - id: lightning-talks-closing-session-kahoot
    title: "Lightning talks + closing session & Kahoot"
    type: talk
    duration_minutes: 15
    description: "Lighting talks:\n<br> <b> Kevin Albes </b>: Building Multi-Agent Workflows with Agent Framework<br> <br> <b> Brian Power </b>: Five python code samples I show clients who know nothing about Python. And to those who know too much.<br>"

# The grid, one row per slot of the day, in the order it is printed. A slot
# names the talk it holds, or carries its own label and type when it holds
# none: a break, the group photo, the welcome. The level and the requirements
# sit here and not on the talk, because they are what the slot asks of whoever
# walks into it. A start is always quoted: YAML 1.1 reads an unquoted 9:00 as
# the integer 540.
agenda:
  - start: "9:00"
    credited_as: "PyDay BCN 2025 Organising Committee"
    track_length: 4
    room: sala-dactes-ada-lovelace
    type: group
    label: "Registration & Welcome"
    duration_minutes: 15
  - start: "9:30"
    track_length: 1
    room: sala-dactes-ada-lovelace
    talk: build-advanced-agentic-llm-apps-with-langgraph-and-langchain
    python_level: intermediate
    topic_level: beginner
    requirements: "Intermediate experience in Python and basic understanding of LLMs and how to use LLM APIs"
  - start: "9:30"
    track_length: 1
    room: sala-margarita-salas
    talk: from-zero-to-chatbot-create-your-own-ai-assistant-with
    python_level: intermediate
    topic_level: beginner
    requirements: "- No prior experience with AI or machine learning -  Basic familiarity with Python (variables, functions, running scripts) - Laptop with Python 3.9+ installed - Ability to install Python packages (pip) - Code editor such as VS Code"
  - start: "9:30"
    track_length: 1
    room: sala-hedy-lamarr
    talk: introduction-to-analog-quantum-computing
    python_level: beginner
    topic_level: beginner
    requirements: "pip install qilisdk"
  - start: "9:30"
    track_length: 1
    room: sala-hipatia-dalexandria
    talk: testeando-apis-like-a-boss-con-bdd
    python_level: intermediate
    topic_level: intermediate
    requirements: "Python environment y IDE"
  - start: "11:00"
    track_length: 4
    room: terrassa
    type: coffee
    label: "Coffee break"
    duration_minutes: 15
  - start: "11:30"
    track_length: 1
    room: sala-dactes-ada-lovelace
    talk: del-texto-al-dato-como-entienden-las-maquinas-el-lenguaje
    python_level: intermediate
    topic_level: beginner
    requirements: "Conexión a internet, cuenta de Google (para trabajar en Google Colab a través de librerías ya disponibles sin necesidad de usar consola de comandos (cmd) ni instalar Python en local."
  - start: "11:30"
    track_length: 1
    room: sala-margarita-salas
    talk: crea-un-agente-llm-desde-cero-sin-frameworks
    python_level: beginner
    topic_level: beginner
    requirements: "Conexión a internet. Python 3.10+. Tener la librería \"openai\" instalada. No se necesitará una API key para el taller. Se recomienda usar un gestor de entornos como uv o virtualenv, aunque no es obligatorio. Cada participante debe tener su entorno listo. Durante el taller se utilizará \"uv\" para gestionar dependencias."
  - start: "11:30"
    track_length: 1
    room: sala-hedy-lamarr
    talk: building-multi-agent-system-with-pydantic-ai
    python_level: intermediate
    topic_level: intermediate
    requirements: "Participants should bring a laptop with:\n- Python 3.10+ installed\n- Ollama installed with Llama 3.2 model downloaded\n- Basic familiarity with Python\n- 8GB+ RAM recommended\nNo prior experience with AI agents or Pydantic AI required."
  - start: "11:30"
    track_length: 1
    room: sala-hipatia-dalexandria
    talk: mastering-word-automation-with-python
    python_level: beginner
    topic_level: beginner
    requirements: "Python and DOCX"
  - start: "13:00"
    track_length: 4
    room: grades
    type: photo
    label: "Group photo"
    duration_minutes: 0
  - start: "13:15"
    track_length: 4
    room: terrassa
    type: lunch
    label: "Lunch break"
    duration_minutes: 30
  - start: "14:00"
    track_length: 1
    room: sala-dactes-ada-lovelace
    talk: keywords-bm25-y-vectores-construyendo-un-buscador-de-texto
    python_level: intermediate
    topic_level: beginner
    requirements: "Python 3.10+ (cada participante puede decidir seguir el taller con un Jupyter Notebook, Google Colab, scripts de Python, etc). El taller se desarrollará utilizando archivos de texto de Python, pero es apto para seguirlo en un notebook también."
  - start: "14:00"
    track_length: 1
    room: sala-margarita-salas
    talk: del-desorden-visual-al-significado-una-aventura-con
    python_level: intermediate
    topic_level: intermediate
    requirements: "Python"
  - start: "14:00"
    track_length: 1
    room: sala-hedy-lamarr
    talk: house-controlled-by-ai-what-could-go-wrong
    python_level: advanced
    topic_level: advanced
    requirements: "python, transformers, llama-index"
  - start: "14:00"
    track_length: 1
    room: sala-hipatia-dalexandria
    talk: models-de-regressio-bayesians
    python_level: intermediate
    topic_level: beginner
    requirements: "Utilitzarem la última versió de la llibreria bambi durant el taller. Es recomana tenir un virtual environment amb la llibreria ja instal·lada si es vol seguir el taller en directe. El taller també assumeix un nivell intermedi en l'ús de NumPy i Pandas."
  - start: "15:30"
    track_length: 4
    room: claustre
    type: coffee
    label: "Coffee break"
    duration_minutes: 15
  - start: "16:00"
    track_length: 1
    room: sala-dactes-ada-lovelace
    talk: agentes-inteligentes-que-evolucionan-software
    python_level: intermediate
    topic_level: beginner
    requirements: "Portátil y acceso a internet, para poder clonar el repositorio y seguir las instrucciones."
  - start: "16:00"
    track_length: 1
    room: sala-margarita-salas
    talk: fabric-en-accion-conectando-bloques-datos-y-magia-en-python
    python_level: beginner
    topic_level: beginner
  - start: "16:00"
    track_length: 1
    room: sala-hedy-lamarr
    talk: htmx-a-love-story-between-a-backend-dev-and-a-frontend
    python_level: intermediate
    topic_level: beginner
  - start: "16:00"
    track_length: 1
    room: sala-hipatia-dalexandria
    talk: causal-inference-a-brief-introduction
    python_level: intermediate
    topic_level: beginner
    requirements: "Notebook and basic python knowledge"
  - start: "17:30"
    track_length: 4
    room: sala-dactes-ada-lovelace
    talk: lightning-talks-closing-session-kahoot

---


## About PyDay BCN 2025

We are excited to announce the **9th edition** of PyDay in Barcelona!

PyDay is an event packed with FREE **Python-related workshops** and activities for the Python community. It is organized once per year. Over the last eight editions, PyDay has become a fantastic opportunity to share our love for Python and engage users, companies, and newcomers!

### When and where

It is scheduled for **Saturday 29th November** at [Canòdrom](https://maps.app.goo.gl/Uxiao2Dr7uio9o3v9), from 9:00 a.m. to 18:00 p.m. CET, approximately.

### A full day of in-person, hands-on workshops

PyDay BCN 2025 will have different **thematic tracks** --e.g. data science, web development, security-- with hands-on workshops lasting about 90 minutes. Participants will learn how to use different libraries, tools and techniques, fully guided by community members and support volunteers.

### Participate in Kahoot and win prizes!

We will host a Kahoot game with questions about PyBCN and Python in general, with prizes for the fastest players. Will you miss it?!
