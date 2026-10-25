---
title: "PyDataBCN (2023)"
year: 2023
# The day of this edition, from the Meetup export, which records it per event.
date: 2023-06-10
# The venue of this edition, from the Meetup export, which records it per event.
venue: "Canòdrom"
description: "The annual gathering for Pythonists in love with data!"
menu:
  main:
    parent: "PyDataBCN"
weight: 2
aliases:
  - /pydatabcn-2023
heroBackground: /images/photos/canodrom.jpg

layout: event

free_text_sections:
  - title: Important dates
    id: important_dates
    content: "<b>11th April</b>: Call for proposals opening<br/>
      <b>10th May</b>: Call for proposals closing<br/>
      <b>24th May</b>: Program available<br/>
      <b>26th May,10AM</b>: Early registration open for speakers, sponsors and PyLadiesBCN members<br/>
      <b>29th May, 9AM</b>: General registration open through [Eventbrite](https://www.eventbrite.com/e/entradas-pydatabcn-2023-643559583037)<br/>
      <b>10th June</b>: PyDataBCN 2023"
  - title: Registration
    id: registration
    content: "General registration will open on Monday 29th of May, at 9AM through [Eventbrite](https://www.eventbrite.com/e/entradas-pydatabcn-2023-643559583037)."


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
            - amalia-vradi
            - carmen-iniesta-lopez
            - daniel-sanchez-santolaya
            - diego-quintana
            - edgar-sarria-tenes
            - fiorella-piriz-sapio
            - juan-bernardo-lince
            - juan-luis-cano-rodriguez
            - miquel-sarrias
            - monica-dominguez
            - nikita-polovinkin
            - oriol-abril-pla
            - rajdeep-pal
            - ricardo-ander-egg-aguilar
            - ruben-afonso
            - sergi-baena-miret
            - thais-ruiz-de-alda
    - title: Organizers
      id: organizers
      levels:
        - people_per_line: 4
          people:
            - laura-perez-mayos
            - natalia-padilla
            - elisabeth-ortega-carrasco
            - amalia-vradi
            - ariadna-fernandez
            - paula-szewach
            - nuria-pujol-vilanova
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
# a record with an id because the color of a block now comes from it: the
# template gives every room of an event one color of the agenda palette and
# keeps it for the whole day. See partials/agenda_entry.html.
rooms:
  - id: open-air-terrace
    name: "Open-air terrace"
  - id: sala-dactes-ada-lovelace
    name: "Sala d'actes Ada Lovelace"
  - id: aula-hedy-lamarr
    name: "Aula Hedy Lamarr"
  - id: sala-margarita-salas
    name: "Sala Margarita Salas"
  - id: aula-hipatia-dalexandria
    name: "Aula Hipàtia d'Alexandria"

# The talks of this edition: what was said, by whom, in which language. A talk
# carries no time and no room, because it is the content and not the slot.
# agenda below is what places it on the grid, and one talk can take more than
# one slot. The id is derived from the title and is the anchor a photo of the
# gallery links to, so it must not change.
talks:
  - id: convierte-tus-notebooks-de-jupyter-en-codigo-mantenible-con
    title: "Convierte tus notebooks de Jupyter en código mantenible con Kedro"
    title_lang: Spanish
    speakers: [juan-luis-cano-rodriguez]
    type: workshop
    language: es
    topic: "(Maintainable) Data Science"
    duration_minutes: 75
    description: "Los notebooks han sido fundamentales para el surgimiento de la ciencia de datos como campo, ya que brindan una interfaz fácil de usar, ofrecen un feedback rápido, y constituyen tanto un entorno de desarrollo como un formato de intercambio. Sin embargo, también se reconoce ampliamente que a menudo plantean problemas de reproducibilidad y mantenibilidad: el 90 % de los notebooks de Jupyter publicados no indican explícitamente las dependencias de los paquetes (Wang et al, 2021), y el 96 % de ellos contener errores o estado oculto que impidió obtener los mismos resultados después de volver a ejecutar (Pimentel et al, 2019). Se han propuesto varias herramientas y enfoques para mitigar los problemas de los notebooks para datos de producción. ciencia. En este taller, los autores proponen un flujo de trabajo que consiste en la refactorización iterativa de notebooks de Jupyter: mediante la extracción incremental de referencias de datos y lógica de negocio en módulos reutilizables de Python, los participantes serán capaces de explotar las capacidades dinámicas de los notebooks manteniendo su complejidad bajo control. Estos módulos de Python harán uso de Kedro, un framework Python para crear pipelines de datos reproducibles, mantenibles y modulares."
  - id: jupyter-notebooks-101
    title: "Jupyter Notebooks 101"
    speakers: [amalia-vradi]
    type: workshop
    language: en
    topic: "Data Analysis"
    duration_minutes: 75
    description: "This will be an interactive workshop on Jupyter Notebooks, the popular web application that enables you to create and share documents that contain live code, equations, visualizations and narrative text. In this beginner-friendly session, you'll discover what Jupyter Notebooks are and what you can do with them. We'll also introduce you to Google Colab and Kaggle, two platforms that offer free, cloud-based versions of Notebooks. You'll get hands-on experience with installing and using them, as well as experimenting with the features offered by the platforms. Bring your laptop and your curiosity and learn how to take your data science projects to the next level using Jupyter Notebooks!"
  - id: data-orchestration-with-airflow
    title: "Data orchestration with Airflow"
    speakers: [fiorella-piriz-sapio]
    type: workshop
    language: es
    topic: "Big Data Analysis"
    duration_minutes: 75
    description: "Introduction to the Python-based data orchestration tool, Airflow. We will learn about airflow components and create the first Dags using some of its main operators and connectors. Finally, we will learn how to connect Airflow with Kubernetes and Spark."
  - id: de-los-datos-al-modelo-en-produccion
    title: "De los datos al modelo en producción"
    title_lang: Spanish
    speakers: [ricardo-ander-egg-aguilar]
    type: workshop
    language: es
    topic: "Machine Learning"
    duration_minutes: 75
    description: "Comenzaremos con un conjunto de datos de imágenes sin procesar, entrenaremos un modelo de aprendizaje automático usando fastai/PyTorch y crearemos una aplicación web con FastAPI para permitir que los usuarios interactúen con el modelo."
  - id: data-analytics-with-python
    title: "Data Analytics with Python"
    speakers: [juan-bernardo-lince]
    type: workshop
    language: en
    topic: "Data Analysis"
    duration_minutes: 75
    description: "Introduction to Data Analytics with Python and Pandas, building a parallel with Excel on how to create columns, summarize information and retrieve quick statistics. Questions, such as \"how can we process data with code?\" and \"which issues should I be addressing with data?\" will be explored, through guided examples on a dataset, to answer business inquiries.<br/><br/>In the second part, examples on Pandas built-in quick plots will be provided. Additionally, we will use Seaborn to create charts and other visual information that enable us to show the answers from the analysis, in a clear and objective manner."
  - id: train-your-own-image-classification-model-in-minutes
    title: "Train Your Own Image Classification Model in Minutes"
    speakers: [amalia-vradi]
    type: workshop
    language: en
    topic: "Deep Learning, Artificial Intelligence"
    duration_minutes: 75
    description: "Learn how to train your own image classification model with fastai in this hands-on workshop. You'll discover how easy it is to build a custom model to classify any type of image you want, without needing any special hardware or software. We'll use Google Colab and Kaggle's free GPU instances to train our models, so all you need is your laptop and a curious mindset. Join us to explore the exciting world of computer vision!"
  - id: machine-learning-robustness-and-monitoring
    title: "Machine Learning Robustness and Monitoring"
    speakers: [daniel-sanchez-santolaya]
    type: workshop
    language: en
    topic: "Machine Learning Robustness and Monitoring"
    duration_minutes: 75
    description: "Mercury is a python library used in BBVA in data science projects. Recently, we open-sourced some parts of the library to the python and data science community.<br/><br/>In this workshop, we will introduce mercury.robust and mercury.monitoring. With mercury.robust we can perform dataset and model testing to detect undesirable conditions such as high level of noise in the labels, label leaking in the features of the dataset, or model excessive sensitivity to drift in certain features. Mercury.monitoring includes components that can help us detect data drift in our inference data and estimate the performance of our model when real labels are not available yet.<br/><br/>During the workshop we will use components of these libraries during different phases of a machine learning project: dataset generation, model training, and model inference.<br/><br/>The workshop is intended for data scientists and machine learning engineers interested in tools that can help improve the robustness and performance degradation detection of their machine learning models."
  - id: indices-invertidos-desde-cero
    title: "Índices invertidos desde cero"
    title_lang: Spanish
    speakers: [ricardo-ander-egg-aguilar]
    type: workshop
    language: es
    topic: "Data Engineering"
    duration_minutes: 75
    description: "Muchas bases de datos utilizan índices invertidos para permitir realizar búsquedas de texto completo (full-text search). Veremos cómo funciona un índice invertido y crearemos uno desde cero. También aprenderemos a clasificar los resultados de una búsqueda implementando TF-IDF."
  - id: fine-tuning-of-llm-models-for-text-processing
    title: "Fine-tuning of LLM models for text processing"
    speakers: [ruben-afonso]
    type: workshop
    language: en
    topic: "Artificial Intelligence"
    duration_minutes: 75
    description: "In this workshop we will review how to leverage your Python skills to reuse and fine-tune some of the latest Generative LLM (Large Language Models) available and strategies to tackle specific use cases such as text summarisation and question-answering"
  - id: foundations-of-machine-learning-exploring-use-cases-and
    title: "Foundations of Machine Learning: exploring use cases and typical tasks"
    speakers: [nikita-polovinkin]
    type: workshop
    language: en
    topic: "Machine Learning"
    duration_minutes: 75
    description: "In this workshop you will learn the logic and foundations behind Machine Learning, to better understand how it can be used and where not to. The Different use cases of Machine Learning, and practical exercises of the most typical Machine Learning tasks: regression and classification. Finally how to predict the gender pay gap based on some features such as job descriptions, age and other demographics."
  - id: ask-your-data-build-a-full-pipeline-to-get-generative
    title: "Ask your data! Build a full pipeline to get generative answers from a text dataset"
    speakers: [carmen-iniesta-lopez]
    type: workshop
    language: en
    topic: "Machine Learning, NLP, Semantic search, Generative AI"
    duration_minutes: 75
    description: "The goal of this workshop is to teach attendees how to build a full pipeline to generate sentence embeddings from a given dataset, index them in a vector database for semantic search, and integrate search results as context for a LLM. "
  - id: com-visualitzar-incertesa-i-models-probabilistics
    title: "Com visualitzar incertesa i models probabilistics"
    title_lang: Catalan
    speakers: [oriol-abril-pla]
    type: workshop
    language: ca
    topic: "Data Visualization"
    duration_minutes: 75
    description: "Aprèn a visualitzar paràmetres i prediccions de models probabilístics emprant histogrames, estimadors nuclears de densitat (KDE), gràfics de punts per quantils i funcions de distribució empíriques"
  - id: lightning-talks-session
    title: "Lightning talks session"
    speakers: [adrian-garcia-riber, albert-pujol-torras, alvaro-duran-barata, diego-quintana, edgar-sarria-tenes, miquel-sarrias, monica-dominguez, rajdeep-pal, ricardo-ander-egg-aguilar, sergi-baena-miret, thais-ruiz-de-alda]
    type: talk
    language: [en, es]
    topic: "Multiple topics"
    duration_minutes: 75
    description: "<p><b>How Data Scientists Can Be More Productive with the Power of Static Typing</b> - Alvaro Duran<br/>Data scientists frequently find themselves in situations where they need to verify that some intermediate step in a data pipeline works as expected, and tools such as Jupiter notebooks, where each step is explicitly shown to the user, are very useful at that. However, it can become quite cumbersome and time-consuming as the data pipeline grows more complex.<br/>That's where static typing comes in. By using types in our code, we can introduce our data into a structured pipeline and catch errors early on, before they have the chance to cause any real problems. This is particularly useful when working with large datasets, where a small error can have a significant impact on our results.<br/>But what exactly do we mean by 'types'? Essentially, types are a way of specifying the kind of data that a variable or function will handle. For example, we might specify that a certain variable should only contain integers, or that a certain function should only accept strings.<br/>By using types, we can catch errors early on in the development process, rather than having to wait until runtime to discover them. This can save us a lot of time and effort in the long run, as we can catch errors before they have a chance to cause any real damage.<br/>Now, you might be thinking, 'but doesn't introducing types make our code more complex?' And the answer is, not necessarily. In fact, Python has built-in support for types that makes it easy to incorporate them into our code.<br/>Of course, that is just the first part of the puzzle. Good type systems are analogous to test suites: they require some effort, but the payoff is immense.<br/>This talk will cover the very basics of how data scientists can benefit from using types, not only on their production code, but even on crude prototypes, giving some peace of mind by making illegal states unrepresentable.</p><p><b>Astronomical data Sonification</b> - Adrián García Riber<br/>The current development of massive astronomical archives and virtual observatory technology (VO) offers a wide range of data products and services that can be explored with a personal computer through interoperable technology. The use of sonification and musification in multimodal displays for the exploration of astronomical data offers an additional domain (complementary to visualization), that allows researchers to get immersed in their case studies, navigating the massive downloads of big data generated by space telescopes, and that makes stellar catalogs and databases more accessible for blind-visually impaired (BVI) users. In this talk I would like to introduce the collection of Python and TensorFlow Sonification prototypes developed in my PhD to generate multimodal representations of astronomical data using Deep Learning and Neural Networks.</p><p><b>Python models and alerts within dbt with dbt-fal and novu</b> - Diego Quintana<br/>How to trigger alarms and run python models within dbt with dbt-fal and novu. <br/>dbt is the T in the ELT pipe. Although dbt allows for python model since version 1.3, its support is limited. dbt-fal enables running python models and python code in general within a model. A simple demo will be shown, with a forecasting model is trained as part of a dbt pipeline and an alarm is triggered with novu, an open source notification infrastructure.</p><p><b>Serverless Machine Learning: Streamlining Deployment and Scaling of ML Services</b> - Rajdeep Pal<br/>The topic of deploying machine learning services using a serverless architecture is focused on leveraging cloud computing services to simplify the deployment and scaling of machine learning models. Using a serverless approach, developers can focus on writing code for their ML models without worrying about infrastructure setup and management. The serverless model also provides automatic scaling of resources to meet the demands of incoming requests, reducing the need for manual intervention and ensuring that services remain highly available. This talk would cover the benefits of using a serverless approach to deploy machine learning services and provide practical guidance on how to implement it effectively. It would also explore the challenges and trade-offs involved in using serverless architecture for ML services, such as performance considerations, security, and cost optimisation.</p><p><b>Practical considerations when using chatGPT in production for multilanguage processing</b> - Albert Pujol Torras<br/>We will describe the results of empirical measurements of the behavior of LLMs to automate NLP processes depending on both the language in which the prompt is written, the lenguage of the text to be analyzed as well as some practical considerations to take into account when considering putting in production this type of Models.</p><p><b>International Data Spaces: Implementing the European Strategy on Data</b> - Miquel Sarrias<br/>The International Data Spaces (IDS) initiative aims at cross-sectoral data sovereignty and data interoperability. It sets forth a Reference Architecture Model basing on open standards and contributing to global standards. By specifying data usage constraints, it defines the terms and conditions for the data economy. Data spaces are key to the global, digital economy. The European Commission is defining Europe's path forward into the digital economy of the future. A core element of their vision: international data spaces grounded in European values of trust and the self-determination of data usage by data providers, that we call data sovereignty.</p><p><b>Forecasting in the integral water cycle</b> - Sergi Baena-Miret<br/>Droughts can have severe impacts on water availability, demand, and quality, affecting water allocation, infrastructure planning, and environmental protection. Accurate forecasting of droughts is essential for mitigating their impacts by enabling effective water management strategies. Various techniques such as statistical models, machine learning, and remote sensing are used for drought forecasting in the integral water cycle. However, challenges such as data scarcity, non-stationarity, and uncertainty in climate change projections pose significant challenges for accurate forecasting.</p><p><b>MusicMetaData & algorithmic diversity perrspective</b> - Thais Ruiz de Alda<br/>We want to talk about the current challenge de music industry is facing around metadata and the challenges that including a gender perspective can imply. The talk will cover the story of music metadata and how Digitalfems is challenging the musical descriptive metadata status quo to develop an ADM system that will include gender diversity in a beta testing/lab environment with the support of different institutions such as FECYT, UPC and other relevant stakeholders</p><p><b>Free online Data Apps with Shimoku Library</b> - Edgar Sarria<br/>We will show how to use Shimoku instead of Streamlit to build Data Products in few lines of code</p><p><b>Data Science in Transport Modelling</b> - Monica Dominguez<br/>Transport modelling and traffic simulation have traditionally been branches of Civil Engineering and Applied Mathematics. In this talk, we will present how the field is embracing Data Science and Machine Learning methodologies for data processing, pattern analysis, forecasting and prediction of recurrent and non-recurrent events.</p><p><b>Bundling a Python app in a single file</b> - Ricardo Ander-Egg<br/>Live coding talk. This talk will show how to bundle a Python app and all of its dependencies in a single file. Then we will copy this file to a different machine and see how the script runs without having to deal with Docker or virtual environments.</p>"

# The grid, one row per slot of the day, in the order it is printed. A slot
# names the talk it holds, or carries its own label and type when it holds
# none: a break, the group photo, the welcome. The level and the requirements
# sit here and not on the talk, because they are what the slot asks of whoever
# walks into it. A start is always quoted: YAML 1.1 reads an unquoted 9:00 as
# the integer 540.
agenda:
  - start: "9:00"
    credited_as: "PyDataBCN 2023 organizers"
    track_length: 4
    room: open-air-terrace
    type: group
    label: "Registration & Welcome"
    duration_minutes: 15
  - start: "9:30"
    track_length: 1
    room: sala-dactes-ada-lovelace
    talk: convierte-tus-notebooks-de-jupyter-en-codigo-mantenible-con
    python_level: intermediate
    topic_level: beginner
    requirements: "Experiencia con Python, conocimiento básico de Jupyter y pandas"
  - start: "9:30"
    track_length: 1
    room: aula-hedy-lamarr
    talk: jupyter-notebooks-101
    python_level: beginner
    topic_level: beginner
  - start: "9:30"
    track_length: 1
    room: sala-margarita-salas
    talk: data-orchestration-with-airflow
    python_level: intermediate
    topic_level: intermediate
    requirements: "Python, Airflow > 2.0.0 (can be easily installed with Pypi), optional: S3, Spark, Kubernetes. Please see: https://github.com/Fiorellaps/airflow_workshop_pybcn/tree/main"
  - start: "9:30"
    track_length: 1
    room: aula-hipatia-dalexandria
    talk: de-los-datos-al-modelo-en-produccion
    python_level: intermediate
    topic_level: beginner
    requirements: "Solid knowledge of Python and some basic knowledge of web development (HTML). Virtual environment and editor already set up (https://github.com/polyrand/pydatabcn-imgapp-workshop1). Optional: Docker."
  - start: "11:00"
    track_length: 4
    room: open-air-terrace
    type: coffee
    label: "Coffee break"
    duration_minutes: 15
  - start: "11:30"
    track_length: 1
    room: sala-dactes-ada-lovelace
    talk: data-analytics-with-python
    python_level: beginner
    topic_level: beginner
  - start: "11:30"
    track_length: 1
    room: aula-hedy-lamarr
    talk: train-your-own-image-classification-model-in-minutes
    python_level: beginner
    topic_level: beginner
    requirements: "A google account (to be able to use Google Colab) or a Kaggle account, for using free GPU instances"
  - start: "11:30"
    track_length: 1
    room: sala-margarita-salas
    talk: machine-learning-robustness-and-monitoring
    python_level: intermediate
    topic_level: intermediate
    requirements: "Laptop with python installed (or alternatively laptop with access to Google Colab can be used as well)"
  - start: "11:30"
    track_length: 1
    room: aula-hipatia-dalexandria
    talk: indices-invertidos-desde-cero
    python_level: intermediate
    topic_level: beginner
    requirements: "Conocimiento de elementos de Python como funciones, clases, bucles, comprensiones de listas, generadores, etc. Conocer las estructuras de datos principales de Python (listas, sets, tuples, diccionarios...). Habilidades básicas de procesamiento de texto (manipular cadenas de texto y conocimiento básico de expresiones regulares (regex)).  Para el taller solamente utilizaremos la librería estándar de Python. Se recomienda usar Python 3.7 o superior."
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
    label: "Lunch break"
    duration_minutes: 30
  - start: "14:00"
    track_length: 1
    room: sala-dactes-ada-lovelace
    talk: fine-tuning-of-llm-models-for-text-processing
    python_level: intermediate
    topic_level: beginner
    requirements: "https://gist.github.com/rubenafo/b91861b37f31d16ee7b8d86e707a9f9f"
  - start: "14:00"
    track_length: 1
    room: aula-hedy-lamarr
    talk: foundations-of-machine-learning-exploring-use-cases-and
    python_level: beginner
    topic_level: beginner
  - start: "14:00"
    track_length: 1
    room: sala-margarita-salas
    talk: ask-your-data-build-a-full-pipeline-to-get-generative
    python_level: intermediate
    topic_level: intermediate
    requirements: "Intermediate knowledge of Python programming, understanding of natural language processing and semantic search concepts, enthusiasm and willingness to learn and collaborate.<br/>Technical requirements: Laptop with python >= 3.9 installed and HF’s SentenceTransformers. Nucliadb is optional, if not installed we’ll do it together during the workshop. A requirements.txt and more details  will be provided prior to the event."
  - start: "14:00"
    track_length: 1
    room: aula-hipatia-dalexandria
    talk: com-visualitzar-incertesa-i-models-probabilistics
    python_level: intermediate
    topic_level: beginner
    requirements: "Cal certa comoditat a l'hora de treballar amb Python, NumPy i Matplotlib. Tots els gràfics seran introduïts abans d'utilitzar-se, però és recomanable tenir coneixements bàsics d'estadística."
  - start: "15:30"
    track_length: 4
    room: open-air-terrace
    type: coffee
    label: "Coffee break"
    duration_minutes: 15
  - start: "16:00"
    track_length: 4
    room: sala-dactes-ada-lovelace
    talk: lightning-talks-session
  - start: "17:30"
    credited_as: "PyDataBCN 2023 organizers"
    track_length: 4
    room: sala-dactes-ada-lovelace
    type: group
    label: "Closing session & Kahoot"
    duration_minutes: 15

# Photos published by PyBCN on the day, one per post so no two share a caption,
# which is also the alt text. Imported with bin/import-x-photos, which excludes
# anything the account only shared: that copyright belongs to somebody else.
# The one photo of this day: the group photo when the day has one, and the
# picture that says most about it when it does not. It is what the carousel
# of the home page shows, one slide per event. See
# partials/canonical_photos.html.
canonical_photo: pydata-2023/25-nataliasirera-the-pydatabcn-2023-has-been-incredib.jpg

photos:
  thread: "https://x.com/PyBCN/status/1667433149322735616"
  items:
    - file: pydata-2023/01-starting-the-day-our-president-lpmayos-is-introduc.jpg
      caption: "Starting the day: our president @lpmayos is introducing Python Barcelona https://pybcn.org"
      source: "https://x.com/PyBCN/status/1667433149322735616"
      time: "09:26"
    - file: pydata-2023/02-this-event-is-only-possible-thanks-to-our-sponsors.jpg
      caption: "This event is only possible thanks to our sponsors 👏"
      source: "https://x.com/PyBCN/status/1667433772797640704"
      time: "09:29"
    - file: pydata-2023/03-data-orchestration-with-airflow-by-fiorella-piriz.jpg
      caption: "Data orchestration with Airflow, by Fiorella Piriz Sapio"
      source: "https://x.com/PyBCN/status/1667454807328661512"
      time: "10:53"
      talk: data-orchestration-with-airflow
    - file: pydata-2023/04-jupyter-notebooks-101-by-amalia-vradi.jpg
      caption: "Jupyter Notebooks 101, by Amalia Vradi"
      source: "https://x.com/PyBCN/status/1667455050828992514"
      time: "10:53"
      talk: jupyter-notebooks-101
    - file: pydata-2023/05-convierte-tus-notebooks-de-jupyter-en-codigo-mante.jpg
      caption: "Convierte tus notebooks de Jupyter en código mantenible con Kedro, by Juan Luis Cano Rodríguez"
      source: "https://x.com/PyBCN/status/1667455195125633024"
      time: "10:54"
      talk: convierte-tus-notebooks-de-jupyter-en-codigo-mantenible-con
    - file: pydata-2023/06-de-los-datos-al-modelo-en-produccion-by-ricardo-an.jpg
      caption: "De los datos al modelo en producción, by Ricardo Ander-Egg Aguilar"
      source: "https://x.com/PyBCN/status/1667455679081086976"
      time: "10:56"
      talk: de-los-datos-al-modelo-en-produccion
    - file: pydata-2023/07-had-a-nice-coffee-break-let-s-do-more-workshops.jpg
      caption: "Had a nice coffee break, let's do more workshops!"
      source: "https://x.com/PyBCN/status/1667475551102148610"
      time: "12:15"
    - file: pydata-2023/08-data-analytics-with-python-by-juan-bernardo-lince.jpg
      caption: "Data Analytics with Python, by Juan Bernardo Lince"
      source: "https://x.com/PyBCN/status/1667476072718278658"
      time: "12:17"
      talk: data-analytics-with-python
    - file: pydata-2023/09-machine-learning-robustness-and-monitoring-by-dani.jpg
      caption: "Machine Learning Robustness and Monitoring, by Daniel Sánchez Santolaya"
      source: "https://x.com/PyBCN/status/1667476187122114562"
      time: "12:17"
      talk: machine-learning-robustness-and-monitoring
    - file: pydata-2023/10-indices-invertidos-desde-cero-by-ricardo-ander-egg.jpg
      caption: "Índices invertidos desde cero, by Ricardo Ander-Egg Aguilar"
      source: "https://x.com/PyBCN/status/1667476445243793408"
      time: "12:18"
      talk: indices-invertidos-desde-cero
    - file: pydata-2023/11-fine-tuning-of-llm-models-for-text-processing-by-r.jpg
      caption: "Fine-tuning of LLM models for text processing, by Ruben Afonso"
      source: "https://x.com/PyBCN/status/1667521263726624770"
      time: "15:17"
      talk: fine-tuning-of-llm-models-for-text-processing
    - file: pydata-2023/12-ask-your-data-build-a-full-pipeline-to-get-generat.jpg
      caption: "Ask your data! Build a full pipeline to get generative answers from a text dataset, by Carmen Iniesta López"
      source: "https://x.com/PyBCN/status/1667521428093120515"
      time: "15:17"
      talk: ask-your-data-build-a-full-pipeline-to-get-generative
    - file: pydata-2023/13-foundations-of-machine-learning-exploring-use-case.jpg
      caption: "Foundations of Machine Learning: exploring use cases and typical tasks, by Nikita Polovinkin"
      source: "https://x.com/PyBCN/status/1667521809040670726"
      time: "15:19"
      talk: foundations-of-machine-learning-exploring-use-cases-and
    - file: pydata-2023/14-com-visualitzar-incertesa-i-models-probabilistics.jpg
      caption: "Com visualitzar incertesa i models probabilistics, by Oriol Abril Pla"
      source: "https://x.com/PyBCN/status/1667522020345618433"
      time: "15:20"
      talk: com-visualitzar-incertesa-i-models-probabilistics
    - file: pydata-2023/15-how-data-scientists-can-be-more-productive-with-th.jpg
      caption: "How Data Scientists Can Be More Productive with the Power of Static Typing, by Alvaro Duran"
      source: "https://x.com/PyBCN/status/1667577219026132992"
      time: "18:59"
    - file: pydata-2023/16-python-models-and-alerts-within-dbt-with-dbt-fal-a.jpg
      caption: "Python models and alerts within dbt with dbt-fal and novu, by Diego Quintana"
      source: "https://x.com/PyBCN/status/1667577221593149441"
      time: "18:59"
    - file: pydata-2023/17-international-data-spaces-implementing-the-europea.jpg
      caption: "International Data Spaces: Implementing the European Strategy on Data, by Miquel Sarrias"
      source: "https://x.com/PyBCN/status/1667577224344616960"
      time: "18:59"
    - file: pydata-2023/18-data-science-in-transport-modelling-by-monica-domi.jpg
      caption: "Data Science in Transport Modelling, by Monica Dominguez"
      source: "https://x.com/PyBCN/status/1667577226781499393"
      time: "18:59"
    - file: pydata-2023/19-serverless-machine-learning-streamlining-deploymen.jpg
      caption: "Serverless Machine Learning: Streamlining Deployment and Scaling of ML Services, by Rajdeep Pal"
      source: "https://x.com/PyBCN/status/1667577229516079104"
      time: "18:59"
    - file: pydata-2023/20-bundling-a-python-app-in-a-single-file-ricardo-and.jpg
      caption: "Bundling a Python app in a single file - Ricardo Ander-Egg"
      source: "https://x.com/PyBCN/status/1667577233127653376"
      time: "18:59"
    - file: pydata-2023/21-the-workshops-and-talks-are-done-let-s-play-a-game.jpg
      caption: "The workshops and talks are done. Let's play a game!"
      source: "https://x.com/PyBCN/status/1667577815041032195"
      time: "19:01"
    - file: pydata-2023/22-the-best-programming-language-is.jpg
      caption: "The best programming language is..."
      source: "https://x.com/PyBCN/status/1667579239321698304"
      time: "19:07"
    - file: pydata-2023/23-all-our-communications-are-written-by.jpg
      caption: "All our communications are written by..."
      source: "https://x.com/PyBCN/status/1667579241678995456"
      time: "19:07"
    - file: pydata-2023/24-will-you-volunteer-at-the-next-event-sure-natalias.jpg
      caption: "Will you volunteer at the next event? Sure, @nataliasirera!!"
      source: "https://x.com/PyBCN/status/1667579243780349952"
      time: "19:07"
    - file: pydata-2023/25-nataliasirera-the-pydatabcn-2023-has-been-incredib.jpg
      caption: "The PyDataBCN 2023 has been incredible! We are grateful for all the organizers, volunteers, speakers, sponsors and assistants. See you at our next event!"
      source: "https://x.com/PyBCN/status/1667589285262786561"
      time: "19:47"
---

## About PyDataBCN 2023

We are thrilled to announce the creation of PyDataBCN, our new annual event dedicated to bringing together the Data Engineering and Data Science community working with Python in Barcelona. PyDataBCN aims to provide a platform for knowledge-sharing, networking, and learning for professionals, enthusiasts, and students alike.

PyDataBCN will offer free hands-on workshops, lightning talks, and lots of fun activities. The `workshops` will be conducted by community members and will cover a range of topics related to data science, data engineering, machine learning, artificial intelligence, and more. Attendees will have the opportunity to learn new skills, get insights into the latest trends and best practices, and interact with like-minded individuals. The `lightning talks` will feature short and impactful presentations by speakers from academia and industry, who will share their experiences, insights, and perspectives on various topics related to data science and engineering. These talks will be followed by Q&A sessions, where attendees can ask questions and engage with the speakers.

In addition to the workshops and lightning talks, PyDataBCN will also host various fun activities, including `networking` events, `Kahoot` games, and more. We believe that learning should be enjoyable and that attendees should have the opportunity to connect and engage with each other in a relaxed and informal setting.

PyDataBCN is a free non-profit event and is open to everyone, regardless of their level of experience or background. We encourage students, professionals, and enthusiasts to join us and become part of the vibrant and growing community of data scientists and engineers in Barcelona.

We look forward to seeing you at PyDataBCN and sharing our passion for Python, data science, and engineering!


### `When and where`

It is scheduled for **Saturday 10th June** in [Canòdrom - Ateneu d'Innovació Digital i Democràtica](https://g.page/Canodrom?share), from 9:00pm to 18:00pm CET, aprox.


### `Disclaimer`

PyDataBCN would like to expressly clarify that it is an independent event and is not associated or affiliated with the PyData events organized by NumFOCUS. PyDataBCN operates autonomously with its own distinct goals, structure, and organization.