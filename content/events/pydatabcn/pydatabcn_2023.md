---
title: "PyDataBCN 2023"
description: "The annual gathering for Pythonists in love with data!"
menu:
  main:
    parent: "PyDataBCN"
weight: 2
aliases:
  - /pydatabcn-2023
heroBackground: /images/photos/canodrom.png

layout: event

free_text_sections:
  - title: Important dates
    id: important_dates
    content: "<b>11th April</b>: Call for proposals opening<br/>
      <b>10th May</b>: Call for proposals closing<br/>
      <b>24th May</b>: Program available<br/>
      <b>26th May,10AM</b>: Early registration open for speakers, sponsors and PyLadiesBCN members<br/>
      <b>29th May, 9AM</b>: General registration open through <a target='_blank' href='https://www.eventbrite.com/e/entradas-pydatabcn-2023-643559583037'>Eventbrite</a><br/>
      <b>10th June</b>: PyDataBCN 2023"
  - title: Call for Sponsors
    id: call_for_sponsors
    content: "<p>Attention all potential sponsors! PyDataBCN is an exciting new event that brings together the Data Science and Data Engineering community working with Python in Barcelona. This event provides a unique opportunity for sponsors to showcase their products and services, connect with industry experts and thought leaders, and demonstrate their commitment to the data science and engineering community.</p><p>As a sponsor of PyDataBCN, you will be able to reach a diverse and engaged audience of data scientists, engineers, and enthusiasts. Our <code>sponsorship packages</code> are tailored to meet the needs of different organizations and budgets. We offer various sponsorship levels that provide a range of benefits, including branding opportunities and speaking slots.</p><p>In addition to the benefits of sponsorship, your support will also help us make PyDataBCN a huge success. As a non-profit event, we rely on the generosity of our sponsors to cover the costs of organizing the event and ensure that it is accessible to everyone in the data science and engineering community.</p><p>Don't miss this unique opportunity to showcase your brand and support the data science and engineering community in Barcelona. Contact us today at <a href='mailto:pydatabcn2023@googlegroups.com'>pydatabcn2023@googlegroups.com</a> to learn more about our sponsorship packages and how you can get involved in PyDataBCN.</p>"
  - title: Registration
    id: registration
    content: "General registration will open on Monday 29th of May, at 9AM through <a target='_blank' href='https://www.eventbrite.com/e/entradas-pydatabcn-2023-643559583037'>Eventbrite</a>."

sponsors_text: "Would you like to sponsor this event? Please take a look at our [Call for Sponsors](#call_for_sponsors)"

sponsor_levels:
  - sponsors_per_line: 2
    sponsors: [canodrom]
    name: Venue
  - sponsors_per_line: 2
    sponsors: ['iomed']
    name: Gold
  - sponsors_per_line: 3
    sponsors: ['aimsun', 'nuclia', 'somenergia', 'shimoku']
    name: Silver
  - sponsors_per_line: 3
    sponsors: ['apsl', 'digitalfems', 'rakuten', 'pythones', 'kiwi']
    name: Supporting
  - sponsors_per_line: 2
    sponsors: [pyladiesbcn, pybcn]
    name: Organizers


people_sections:
    - title: Speakers
      id: speakers
      levels:
        - people_per_line: 4
          people:
            - adrian-garcia-riber
            - albert-pujol-torras
            - alvaro-duran-barata
            - amalia_vradi
            - carmen-iniesta-lopez
            - daniel-sanchez-santolaya
            - diego-quintana
            - edgar-sarria-tenes
            - fiorella-piriz-sapio
            - juan-bernardo-lince
            - juan-luis-cano
            - miquel-sarrias
            - monica-dominguez
            - nikita-polovinkin
            - oriol-abril-pla
            - rajdeep-pal
            - ricardo-ander-egg
            - ruben-afonso
            - sergi-baena-miret
            - thais-ruiz-de-alda
    - title: Organizers
      id: organizers
      levels:
        - people_per_line: 4
          people:
            - lpmayos
            - natalia
            - elisabeth-ortega-carrasco
            - amalia_vradi
            - ariadna_fernandez_estevez
            - paula_szewach
            - nuria
            - mireia

spansDuration: 15
numTracks: 4
eventTimes: [9:00, 9:15, 9:30, 9:45, 10:00, 10:15, 10:30, 10:45, 11:00, 11:15, 11:30, 11:45, 12:00, 12:15, 12:30, 12:45, 13:00, 13:15, 13:30, 13:45, 14:00, 14:15, 14:30, 14:45, 15:00, 15:15, 15:30, 15:45, 16:00, 16:15, 16:30, 16:45, 17:00, 17:15, 17:30, 17:45]
legend: "<i class=\"fas fa-laptop\"></i> Workshop &nbsp;&nbsp;&nbsp; <i class=\"fas fa-comment\"></i> Talk &nbsp;&nbsp; | &nbsp;&nbsp; <i class=\"fas fa-circle green\"></i> Beginner &nbsp;&nbsp;&nbsp; <i class=\"fas fa-circle yellow\"></i> Intermediate &nbsp;&nbsp;&nbsp; <i class=\"fas fa-circle red\"></i> Advanced &nbsp;&nbsp; | &nbsp;&nbsp; <i class=\"fas fa-star gold\"></i> Sponsored event"
events:
    - start_time_slot: 9:00
      end_time_slot: 9:15
      track_length: 4
      color: blue
      title: "Registration & Welcome"
      speaker: "PyDataBCN Organising Committee"
      type: group
      location: Open-air terrace
      class: middle

    - speaker: "Juan Luis Cano Rodríguez"
      title: "Convierte tus notebooks de Jupyter en código mantenible con Kedro"
      description: "Los notebooks han sido fundamentales para el surgimiento de la ciencia de datos como campo, ya que brindan una interfaz fácil de usar, ofrecen un feedback rápido, y constituyen tanto un entorno de desarrollo como un formato de intercambio. Sin embargo, también se reconoce ampliamente que a menudo plantean problemas de reproducibilidad y mantenibilidad: el 90 % de los notebooks de Jupyter publicados no indican explícitamente las dependencias de los paquetes (Wang et al, 2021), y el 96 % de ellos contener errores o estado oculto que impidió obtener los mismos resultados después de volver a ejecutar (Pimentel et al, 2019).  Se han propuesto varias herramientas y enfoques para mitigar los problemas de los notebooks para datos de producción. ciencia. En este taller, los autores proponen un flujo de trabajo que consiste en la refactorización iterativa de notebooks de Jupyter: mediante la extracción incremental de referencias de datos y lógica de negocio en módulos reutilizables de Python, los participantes serán capaces de explotar las capacidades dinámicas de los notebooks manteniendo su complejidad bajo control. Estos módulos de Python harán uso de Kedro, un framework Python para crear pipelines de datos reproducibles, mantenibles y modulares."
      start_time_slot: 9:30
      end_time_slot: 10:45
      track_length: 1
      color: orange
      python_level: "<i class=\"fas fa-circle yellow\"></i>"
      topic_level: "<i class=\"fas fa-circle green\"></i>"
      type: workshop
      topic: "(Maintainable) Data Science"
      location: Sala d'actes Ada Lovelace
      requirements: "Experiencia con Python, conocimiento básico de Jupyter y pandas"
      language: "Spanish"
    - speaker: "Amalia Vradi"
      title: "Jupyter Notebooks 101"
      description: "This will be an interactive workshop on Jupyter Notebooks, the popular web application that enables you to create and share documents that contain live code, equations, visualizations and narrative text. In this beginner-friendly session, you'll discover what Jupyter Notebooks are and what you can do with them. We'll also introduce you to Google Colab and Kaggle, two platforms that offer free, cloud-based versions of Notebooks. You'll get hands-on experience with installing and using them, as well as experimenting with the features offered by the platforms. Bring your laptop and your curiosity and learn how to take your data science projects to the next level using Jupyter Notebooks!"
      start_time_slot: 9:30
      end_time_slot: 10:45
      track_length: 1
      color: grey
      python_level: "<i class=\"fas fa-circle green\"></i>"
      topic_level: "<i class=\"fas fa-circle green\"></i>"
      type: workshop
      topic: "Data Analysis"
      location: Aula Hedy Lamarr
      requirements: ""
      language: "English"
    - speaker: "Fiorella Piriz Sapio"
      title: "Data orchestration with Airflow"
      description: "Introduction to the Python-based data orchestration tool, Airflow. We will learn about airflow components and create the first Dags using some of its main operators and connectors. Finally, we will learn how to connect Airflow with Kubernetes and Spark."
      start_time_slot: 9:30
      end_time_slot: 10:45
      track_length: 1
      color: grey
      python_level: "<i class=\"fas fa-circle yellow\"></i>"
      topic_level: "<i class=\"fas fa-circle yellow\"></i>"
      type: workshop
      topic: "Big Data Analysis"
      location: Sala Margarita Salas
      requirements: "Python, Airflow > 2.0.0 (can be easily installed with Pypi), optional: S3, Spark, Kubernetes. Please see: https://github.com/Fiorellaps/airflow_workshop_pybcn/tree/main"
      language: "Spanish"
    - speaker: "Ricardo Ander-Egg Aguilar"
      title: "De los datos al modelo en producción"
      description: "Comenzaremos con un conjunto de datos de imágenes sin procesar, entrenaremos un modelo de aprendizaje automático usando fastai/PyTorch y crearemos una aplicación web con FastAPI para permitir que los usuarios interactúen con el modelo."
      start_time_slot: 9:30
      end_time_slot: 10:45
      track_length: 1
      color: purple
      python_level: "<i class=\"fas fa-circle yellow\"></i>"
      topic_level: "<i class=\"fas fa-circle green\"></i>"
      type: workshop
      topic: "Machine Learning"
      location: Aula Hipàtia d'Alexandria
      requirements: "Solid knowledge of Python and some basic knowledge of web development (HTML). Virtual environment and editor already set up (https://github.com/polyrand/pydatabcn-imgapp-workshop1). Optional: Docker."
      language: "Spanish"

    - start_time_slot: 11:00
      end_time_slot: 11:15
      track_length: 4
      color: blue
      title: "Coffee break"
      type: coffee
      location: Open-air terrace
      class: middle

    - speaker: "Juan Bernardo Lince"
      title: "Data Analytics with Python"
      description: "Introduction to Data Analytics with Python and Pandas, building a parallel with Excel on how to create columns, summarize information and retrieve quick statistics. Questions, such as “how can we process data with code?” and “which issues should I be addressing with data?” will be explored, through guided examples on a dataset, to answer business inquiries.<br/><br/>In the second part, examples on Pandas built-in quick plots will be provided. Additionally, we will use Seaborn to create charts and other visual information that enable us to show the answers from the analysis, in a clear and objective manner."
      start_time_slot: 11:30
      end_time_slot: 12:45
      track_length: 1
      color: grey
      python_level: "<i class=\"fas fa-circle green\"></i>"
      topic_level: "<i class=\"fas fa-circle green\"></i>"
      type: workshop
      topic: "Data Analysis"
      location: Sala d'actes Ada Lovelace
      requirements: ""
      language: "English"
    - speaker: "Amalia Vradi"
      title: "Train Your Own Image Classification Model in Minutes"
      description: "Learn how to train your own image classification model with fastai in this hands-on workshop. You'll discover how easy it is to build a custom model to classify any type of image you want, without needing any special hardware or software. We'll use Google Colab and Kaggle's free GPU instances to train our models, so all you need is your laptop and a curious mindset. Join us to explore the exciting world of computer vision!"
      start_time_slot: 11:30
      end_time_slot: 12:45
      track_length: 1
      color: purple
      python_level: "<i class=\"fas fa-circle green\"></i>"
      topic_level: "<i class=\"fas fa-circle green\"></i>"
      type: workshop
      topic: "Deep Learning, Artificial Intelligence"
      location: Aula Hedy Lamarr
      requirements: "A google account (to be able to use Google Colab) or a Kaggle account, for using free GPU instances"
      language: "English"
    - speaker: "Daniel Sánchez Santolaya"
      title: "Machine Learning Robustness and Monitoring"
      description: "Mercury is a python library used in BBVA in data science projects. Recently, we open-sourced some parts of the library to the python and data science community.<br/><br/>In this workshop, we will introduce mercury.robust and mercury.monitoring. With mercury.robust we can perform dataset and model testing to detect undesirable conditions such as high level of noise in the labels, label leaking in the features of the dataset, or model excessive sensitivity to drift in certain features. Mercury.monitoring includes components that can help us detect data drift in our inference data and estimate the performance of our model when real labels are not available yet.<br/><br/>During the workshop we will use components of these libraries during different phases of a machine learning project: dataset generation, model training, and model inference.<br/><br/>The workshop is intended for data scientists and machine learning engineers interested in tools that can help improve the robustness and performance degradation detection of their machine learning models."
      start_time_slot: 11:30
      end_time_slot: 12:45
      track_length: 1
      color: purple
      python_level: "<i class=\"fas fa-circle yellow\"></i>"
      topic_level: "<i class=\"fas fa-circle yellow\"></i>"
      type: workshop
      topic: "Machine Learning Robustness and Monitoring"
      location: Sala Margarita Salas
      requirements: "Laptop with python installed (or alternatively laptop with access to Google Colab can be used as well)"
      language: "English"
    - speaker: "Ricardo Ander-Egg Aguilar"
      title: "Índices invertidos desde cero"
      description: "Muchas bases de datos utilizan índices invertidos para permitir realizar búsquedas de texto completo (full-text search). Veremos cómo funciona un índice invertido y crearemos uno desde cero. También aprenderemos a clasificar los resultados de una búsqueda implementando TF-IDF."
      start_time_slot: 11:30
      end_time_slot: 12:45
      track_length: 1
      color: orange
      python_level: "<i class=\"fas fa-circle yellow\"></i>"
      topic_level: "<i class=\"fas fa-circle green\"></i>"
      type: workshop
      topic: "Data Engineering"
      location: Aula Hipàtia d'Alexandria
      requirements: "Conocimiento de elementos de Python como funciones, clases, bucles, comprensiones de listas, generadores, etc. Conocer las estructuras de datos principales de Python (listas, sets, tuples, diccionarios...). Habilidades básicas de procesamiento de texto (manipular cadenas de texto y conocimiento básico de expresiones regulares (regex)).  Para el taller solamente utilizaremos la librería estándar de Python. Se recomienda usar Python 3.7 o superior."
      language: "Spanish"

    - start_time_slot: 13:00
      end_time_slot: 13:00
      track_length: 4
      color: blue
      title: "Group photo"
      type: photo
      location: Open-air terrace
      class: middle

    - start_time_slot: 13:15
      end_time_slot: 13:45
      track_length: 4
      color: blue
      title: "Lunch break"
      type: lunch
      location: Open-air terrace
      class: middle

    - speaker: "Ruben Afonso"
      title: "Fine-tuning of LLM models for text processing"
      description: "In this workshop we will review how to leverage your Python skills to reuse and fine-tune some of the latest Generative LLM (Large Language Models) available and strategies to tackle specific use cases such as text summarisation and question-answering"
      start_time_slot: 14:00
      end_time_slot: 15:15
      track_length: 1
      color: purple
      python_level: "<i class=\"fas fa-circle yellow\"></i>"
      topic_level: "<i class=\"fas fa-circle green\"></i>"
      type: workshop
      topic: "Artificial Intelligence"
      location: Sala d'actes Ada Lovelace
      requirements: "https://gist.github.com/rubenafo/b91861b37f31d16ee7b8d86e707a9f9f"
      language: "English"
    - speaker: "Nikita Polovinkin"
      title: "Foundations of Machine Learning: exploring use cases and typical tasks"
      description: "In this workshop you will learn the logic and foundations behind Machine Learning, to better understand how it can be used and where not to. The Different use cases of Machine Learning, and practical exercises of the most typical Machine Learning tasks: regression and classification. Finally how to predict the gender pay gap based on some features such as job descriptions, age and other demographics."
      start_time_slot: 14:00
      end_time_slot: 15:15
      track_length: 1
      color: purple
      python_level: "<i class=\"fas fa-circle green\"></i>"
      topic_level: "<i class=\"fas fa-circle green\"></i>"
      type: workshop
      topic: "Machine Learning"
      location: Aula Hedy Lamarr
      requirements: ""
      language: "English"
    - speaker: "Carmen Iniesta López"
      title: "Ask your data! Build a full pipeline to get generative answers from a text dataset"
      description: "The goal of this workshop is to teach attendees how to build a full pipeline to generate sentence embeddings from a given dataset, index them in a vector database for semantic search, and integrate search results as context for a LLM. "
      start_time_slot: 14:00
      end_time_slot: 15:15
      track_length: 1
      color: purple
      python_level: "<i class=\"fas fa-circle yellow\"></i>"
      topic_level: "<i class=\"fas fa-circle yellow\"></i>"
      type: workshop
      location: Sala Margarita Salas
      requirements: "Intermediate knowledge of Python programming, understanding of natural language processing and semantic search concepts, enthusiasm and willingness to learn and collaborate.<br/>Technical requirements: Laptop with python >= 3.9 installed and HF’s SentenceTransformers. Nucliadb is optional, if not installed we’ll do it together during the workshop. A requirements.txt and more details  will be provided prior to the event."
      language: "English"
      topic: "Machine Learning, NLP, Semantic search, Generative AI "
    - speaker: "Oriol Abril Pla"
      title: "Com visualitzar incertesa i models probabilistics"
      description: "Aprèn a visualitzar paràmetres i prediccions de models probabilístics emprant histogrames, estimadors nuclears de densitat (KDE), gràfics de punts per quantils i funcions de distribució empíriques"
      start_time_slot: 14:00
      end_time_slot: 15:15
      track_length: 1
      color: grey
      python_level: "<i class=\"fas fa-circle yellow\"></i>"
      topic_level: "<i class=\"fas fa-circle green\"></i>"
      type: workshop
      location: Aula Hipàtia d'Alexandria
      requirements: "Cal certa comoditat a l'hora de treballar amb Python, NumPy i Matplotlib. Tots els gràfics seran introduïts abans d'utilitzar-se, però és recomanable tenir coneixements bàsics d'estadística."
      language: "Catalan"
      topic: "Data Visualization"

    - start_time_slot: 15:30
      end_time_slot: 15:45
      track_length: 4
      color: blue
      title: "Coffee break"
      type: coffee
      location: Open-air terrace
      class: middle

    - speaker: "Adrián García Riber, Albert Pujol Torras, Alvaro Duran Barata, Diego Quintana, Edgar Sarria, Miquel Sàrrias, Monica Dominguez, Rajdeep Pal, Ricardo Ander-Egg Aguilar, Sergi Baena, Thais Ruiz de Alda"
      title: "Lightning talks session"
      description: "<p><b>How Data Scientists Can Be More Productive with the Power of Static Typing</b> - Alvaro Duran<br/>Data scientists frequently find themselves in situations where they need to verify that some intermediate step in a data pipeline works as expected, and tools such as Jupiter notebooks, where each step is explicitly shown to the user, are very useful at that. However, it can become quite cumbersome and time-consuming as the data pipeline grows more complex.<br/>That's where static typing comes in. By using types in our code, we can introduce our data into a structured pipeline and catch errors early on, before they have the chance to cause any real problems. This is particularly useful when working with large datasets, where a small error can have a significant impact on our results.<br/>But what exactly do we mean by 'types'? Essentially, types are a way of specifying the kind of data that a variable or function will handle. For example, we might specify that a certain variable should only contain integers, or that a certain function should only accept strings.<br/>By using types, we can catch errors early on in the development process, rather than having to wait until runtime to discover them. This can save us a lot of time and effort in the long run, as we can catch errors before they have a chance to cause any real damage.<br/>Now, you might be thinking, 'but doesn't introducing types make our code more complex?' And the answer is, not necessarily. In fact, Python has built-in support for types that makes it easy to incorporate them into our code.<br/>Of course, that is just the first part of the puzzle. Good type systems are analogous to test suites: they require some effort, but the payoff is immense.<br/>This talk will cover the very basics of how data scientists can benefit from using types, not only on their production code, but even on crude prototypes, giving some peace of mind by making illegal states unrepresentable.</p><p><b>Astronomical data Sonification</b> - Adrián García Riber<br/>The current development of massive astronomical archives and virtual observatory technology (VO) offers a wide range of data products and services that can be explored with a personal computer through interoperable technology. The use of sonification and musification in multimodal displays for the exploration of astronomical data offers an additional domain (complementary to visualization), that allows researchers to get immersed in their case studies, navigating the massive downloads of big data generated by space telescopes, and that makes stellar catalogs and databases more accessible for blind-visually impaired (BVI) users. In this talk I would like to introduce the collection of Python and TensorFlow Sonification prototypes developed in my PhD to generate multimodal representations of astronomical data using Deep Learning and Neural Networks.</p><p><b>Python models and alerts within dbt with dbt-fal and novu</b> - Diego Quintana<br/>How to trigger alarms and run python models within dbt with dbt-fal and novu. <br/>dbt is the T in the ELT pipe. Although dbt allows for python model since version 1.3, its support is limited. dbt-fal enables running python models and python code in general within a model. A simple demo will be shown, with a forecasting model is trained as part of a dbt pipeline and an alarm is triggered with novu, an open source notification infrastructure.</p><p><b>Serverless Machine Learning: Streamlining Deployment and Scaling of ML Services</b> - Rajdeep Pal<br/>The topic of deploying machine learning services using a serverless architecture is focused on leveraging cloud computing services to simplify the deployment and scaling of machine learning models. Using a serverless approach, developers can focus on writing code for their ML models without worrying about infrastructure setup and management. The serverless model also provides automatic scaling of resources to meet the demands of incoming requests, reducing the need for manual intervention and ensuring that services remain highly available. This talk would cover the benefits of using a serverless approach to deploy machine learning services and provide practical guidance on how to implement it effectively. It would also explore the challenges and trade-offs involved in using serverless architecture for ML services, such as performance considerations, security, and cost optimisation.</p><p><b>Practical considerations when using chatGPT in production for multilanguage processing</b> - Albert Pujol Torras<br/>We will describe the results of empirical measurements of the behavior of LLMs to automate NLP processes depending on both  the language in which the prompt is written, the lenguage of the  text to be analyzed as well as some practical considerations to take into account when considering putting in  production this type of Models.</p><p><b>International Data Spaces: Implementing the European Strategy on Data</b> - Miquel Sarrias<br/>The International Data Spaces (IDS) initiative aims at cross-sectoral data sovereignty and data interoperability. It sets forth a Reference Architecture Model basing on open standards and contributing to global standards. By specifying data usage constraints, it defines the terms and conditions for the data economy. Data spaces are key to the global, digital economy. The European Commission is defining Europe’s path forward into the digital economy of the future. A core element of their vision: international data spaces grounded in European values of trust and the self-determination of data usage by data providers, that we call data sovereignty.</p><p><b>Forecasting in the integral water cycle</b> - Sergi Baena-Miret<br/>Droughts can have severe impacts on water availability, demand, and quality, affecting water allocation, infrastructure planning, and environmental protection. Accurate forecasting of droughts is essential for mitigating their impacts by enabling effective water management strategies. Various techniques such as statistical models, machine learning, and remote sensing are used for drought forecasting in the integral water cycle. However, challenges such as data scarcity, non-stationarity, and uncertainty in climate change projections pose significant challenges for accurate forecasting.</p><p><b>MusicMetaData & algorithmic diversity perrspective</b> - Thais Ruiz de Alda<br/>We want to talk about the current challenge de music industry is facing around metadata and the challenges that including a gender perspective can imply. The talk will cover the story of music metadata and how Digitalfems is challenging the musical descriptive metadata status quo to develop an ADM system that will include gender diversity in a  beta testing/lab environment with the support of different institutions such as FECYT, UPC and other relevant stakeholders</p><p><b>Free online Data Apps with Shimoku Library</b> - Edgar Sarria<br/>We will show how to use Shimoku instead of Streamlit to build Data Products in few lines of code</p><p><b>Data Science in Transport Modelling</b> - Monica Dominguez<br/>Transport modelling and traffic simulation have traditionally been branches of Civil Engineering and Applied Mathematics. In this talk, we will present how the field is embracing Data Science and Machine Learning methodologies for data processing, pattern analysis, forecasting and prediction of recurrent and non-recurrent events.</p><p><b>Bundling a Python app in a single file</b> - Ricardo Ander-Egg<br/>Live coding talk. This talk will show how to bundle a Python app and all of its dependencies in a single file. Then we will copy this file to a different machine and see how the script runs without having to deal with Docker or virtual environments.</p>"
      requirements: ""
      language: "English / Spanish"
      topic: "Multiple topics"
      start_time_slot: 16:00
      end_time_slot: 17:15
      track_length: 4
      color: yellow
      type: talk
      location: Sala d'actes Ada Lovelace


    - start_time_slot: 17:30
      end_time_slot: 17:45
      track_length: 4
      color: blue
      title: "Closing session & Kahoot"
      speaker: "PyDataBCN Organising Committee"
      type: group
      location: Sala d'actes Ada Lovelace
      class: middle

        
---

## About PyDataBCN 2023

We are thrilled to announce the creation of PyDataBCN, our new annual event dedicated to bringing together the Data Engineering and Data Science community working with Python in Barcelona. PyDataBCN aims to provide a platform for knowledge-sharing, networking, and learning for professionals, enthusiasts, and students alike.

PyDataBCN will offer free hands-on workshops, lightning talks, and lots of fun activities. The `workshops` will be conducted by community members and will cover a range of topics related to data science, data engineering, machine learning, artificial intelligence, and more. Attendees will have the opportunity to learn new skills, get insights into the latest trends and best practices, and interact with like-minded individuals. The `lightning talks` will feature short and impactful presentations by speakers from academia and industry, who will share their experiences, insights, and perspectives on various topics related to data science and engineering. These talks will be followed by Q&A sessions, where attendees can ask questions and engage with the speakers.

In addition to the workshops and lightning talks, PyDataBCN will also host various fun activities, including `networking` events, `Kahoot` games, and more. We believe that learning should be enjoyable and that attendees should have the opportunity to connect and engage with each other in a relaxed and informal setting.

PyDataBCN is a free non-profit event and is open to everyone, regardless of their level of experience or background. We encourage students, professionals, and enthusiasts to join us and become part of the vibrant and growing community of data scientists and engineers in Barcelona.

We look forward to seeing you at PyDataBCN and sharing our passion for Python, data science, and engineering!


#### `When and where`

It is scheduled for **Saturday 10th June** in <a href="https://g.page/Canodrom?share" target="_blank">Canòdrom - Ateneu d'Innovació Digital i Democràtica</a>, from 9:00pm to 18:00pm CET, aprox.


#### `Disclaimer`

PyDataBCN would like to expressly clarify that it is an independent event and is not associated or affiliated with the PyData events organized by NumFOCUS. PyDataBCN operates autonomously with its own distinct goals, structure, and organization.