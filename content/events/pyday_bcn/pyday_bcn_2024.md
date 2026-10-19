---
title: "PyDay BCN (2024)"
year: 2024
# The day of this edition, from the Meetup export, which records it per event.
date: 2024-11-09
# The venue of this edition, from the Meetup export, which records it per event.
venue: "Canòdrom"
description: "For the community, by the community!"
menu:
  main:
    parent: "PyDay BCN"
weight: 2
aliases:
  - /pyday-bcn-2024
heroBackground: /images/photos/canodrom.jpg

layout: event

free_text_sections:
  - title: Important dates
    id: important_dates
    content: "<b>26th September</b>: Call for proposals opening: [Workshops](https://forms.gle/GDL2VpUTu4veHbff8) and [Lightning talks](https://forms.gle/VLDY6zdmRxRsGsmv7)<br/>
      <b>27th October</b>: Call for proposals closing<br/>
      <b>3rd Novembre</b>: Program available<br/>
      <b>4th November, 9AM</b>: Early registration open for PyBCN members, PyDay speakers and sponsors<br/>
      <b>5th November, 9AM</b>: General registration open through [Eventbrite](https://www.eventbrite.es/e/entradas-pydaybcn-2024-1068930563089?aff=oddtdtcreator)<br/>
      <b>9th November</b>: PyDay BCN 2024"
  - title: Registration
    id: registration
    content: "General registration will open on Tuesday 5th of November, at 9AM through [Eventbrite](https://www.eventbrite.es/e/entradas-pydaybcn-2024-1068930563089?aff=oddtdtcreator)."

sponsor_levels:
  - sponsors_per_line: 2
    sponsors: [lambdaloopers, nagarro, innovamat, protopixel, pythones, isdieducation, coopdevs, rover, quside]
    name: Silver
  - sponsors_per_line: 3
    sponsors: [qilimanjaro, ikigai, hpc-now, shimoku, digitalfems, innoit, business-insights, travelperk, okta, preply, qustodio, codurance, gluecharm, somenergia, izi]
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
            - jimena-escobar-bermudez
            - kemalcan-bora
            - xiang-xu
            - dave-pitts
            - paula-bassaganas-odena
            - raul-cumplido
            - marc-ramirez
            - manuel-gijon-agudo
            - oriol-abril-pla
            - alex-molas
            - marina-palma
            - asia-noble
            
  - title: Organizers
    id: organizers
    levels:
      - people_per_line: 4
        people:
          - alicia-morales-carrasco
          - david-arcos
          - ferran-jovell
          - laura-perez-mayos
          - jose-riera-sanchez
          

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
  - id: grades
    name: "Grades"
  - id: aula-hedy-lamarr
    name: "Aula Hedy Lamarr"
  - id: aula-hipatia-dalexandria
    name: "Aula Hipàtia d'Alexandria"

# The talks of this edition: what was said, by whom, in which language. A talk
# carries no time and no room, because it is the content and not the slot.
# agenda below is what places it on the grid, and one talk can take more than
# one slot. The id is derived from the title and is the anchor a photo of the
# gallery links to, so it must not change.
talks:
  - id: unboxing-machine-learning-models-predicting-with-numpy
    title: "Unboxing Machine Learning Models: Predicting with Numpy After Model Training"
    speakers: [xiang-xu]
    type: workshop
    language: en
    topic: "Data science, ML"
    duration_minutes: 75
    description: "In this hands-on workshop, we'll bridge the gap between high-level machine learning libraries (like Scikit-learn and Keras) and the core mathematical principles driving their predictions. Participants will firstly train regression models using machine learning methods like Kernel Ridge Regression (KRR) and Deep Neural Networks (DNNs), save the trained model parameters, and then use only Numpy to replicate the prediction process."
  - id: discovering-etl-testing-essential-for-your-ai-solutions
    title: "Discovering ETL Testing: Essential for Your AI Solutions"
    speakers: [paula-bassaganas-odena]
    type: workshop
    language: en
    topic: "Testing"
    duration_minutes: 75
    description: "High-quality data is the foundation of effective AI, and rigorous ETL testing ensures your AI models are built on solid ground. ETL (Extract, Transform, Load) processes are vital for extracting, transforming, and loading data into systems for analysis, and well-tested ETLs are crucial for making reliable, data-driven decisions and successful AI implementations."
  - id: lightning-talks-coffee
    title: "Lightning talks & coffee"
    type: talk
    duration_minutes: 0
    description: " <h2>Lightning talks</h2>\n<b>IZI Record, revolutionizing the camera app</b><br> <i>Ferran Jovell </i> <p><q>What we do at izi? How do we generate videos from different sources? How does it all work?!</q></p>\n<b>A solution to store, catalog and visualize images using Django and Django Rest Framework. </b><br> <i>Josep Sitjar Suñer</i> <p><q>KeepYourPhoto (https://keepyourphoto.com) is a personal project developed with Django (Python) on the backend and Vue.js on the frontend, created in my free time to store, catalog and share photos. <br><br> During the last 5 years, since my daughter was born, our family has been accumulating gigabytes of images. Especially when she started kindergarten, the amount of images increased exponentially, as we've received a catalog of hundred of images for each activity they did. And of course, we want to keep all them as a treasure. <br><br> First, we exhausted the available free space of providers like Google Drive or Dropbox. Then we start paying some basic plans. But in order to keep control of all these images, and implement custom functions to catalog and to share them with other members of the family, I decided to create my own solution. <br><br> I've developed a web application, with Django on the backend. The images are stored on AWS S3, and served with Cloudfront to increase the speed and security of access to them. Django-storages has been a good ally to implement that. <br> In order to create the API, I've been using the Django Rest Framework, and as I work in the geospatial sector (as web map developer) it was mandatory to geolocate all the images with coordinates in their metadata. In that sense, I've been using GeoDjango. <br><br> The platform is not completely finished, as I try to implement new functionalities in my free time. But It's working as expected. It's possible to create albums, massively upload images to them, visualize the images through a gallery carousel, delete albums and images, and visualize over a map the photos with coordinates on their metadata. <br><br> I've received interest from other people, and now I'm trying to make it available to them. The self- registry is working, but it is not yet a payment solution to afford the storage costs at AWS. <br><br> During the talk, my idea is to present the tool and the technological solutions to implement it.</q></p> "
  - id: image-generation-with-ai-gans-and-diffusion-techniques
    title: "Image Generation with AI (GANs and Diffusion Techniques)"
    speakers: [marina-palma]
    type: workshop
    language: es
    topic: "Artificial Intelligence"
    duration_minutes: 75
    description: "This workshop explores the techniques of AI-driven image generation, focusing on two powerful models: Generative Adversarial Networks (GANs) and Diffusion Models. Participants will learn the fundamental principles, practical applications, and differences between these approaches. Through hands-on exercises, attendees will build three types of GANs, progressing from basic to more advanced models, for generating custom synthetic images."
  - id: introduccio-a-xarray-etiqueta-les-teves-dades-n-dimensionals
    title: "Introducció a xarray: etiqueta les teves dades n-dimensionals"
    title_lang: Catalan
    speakers: [oriol-abril-pla]
    type: workshop
    language: ca
    topic: "Data science"
    duration_minutes: 75
    description: "Apren com utilitzar xarray per treballar amb arrays n-dimensionals a través d'etiquetes i indexs arbitraris. Descobreix el model de dades d'xarray: DataArrays, Datasets, dimensions, coordenades, indexes. Explora a través del tutorial les operacions més comunes en matrius n-dimensionals: com especificar en quines dimensions han d'operar les funcions utilitzant noms enlloc d'indexs posicionals, com definir subconjunts a través de coordenades, com combinar el metode `.query` amb filtrar multiples dimensions, com crear multiples indexs per a una mateixa dimensió, les diferencies entre operacions d'indexatge exteriors o vectoritzades, groupbys multidimensionals, i més."
  - id: static-typing-in-python
    title: "Static Typing in Python"
    speakers: [alex-molas]
    type: workshop
    language: en
    topic: "Programming"
    duration_minutes: 75
    description: "Since 2014, with the introduction of type hints in Python 3.5, Python has been adding support to types while still maintaining its dynamic nature. Later, in Python 3.10, pattern matching was added to Python, which provides a powerful way to match data structures based on their types and values, improving Python's capability to work with typed data. Both type hints and pattern matching help make code more testable, predictable and robust.<br> In this talk, we'll answer the following questions: <br> - **Introduction to types in Python**: what's a type? which types does python have? What do they mean?<br> - **The basics of type hints**: how to define a type hint? <br> - **mypy**: how to use mypy to check that your code does what you expect?<br> - **Advanced type hints**: how to define complex type hints? how to define your own types? how to use generic types?<br> - **Data validation**: how to use Pydantic and dataclasses for data validation?<br> - **Pattern matching**: how to use pattern matching together with type hints to write cleaner and more maintainable code.<br> By the end of this talk, you'll have a clear understanding of how to use type hints effectively and why they're a valuable tool in any Python developer's toolkit."
  - id: building-data-pipelines-with-sqlmesh
    title: "Building data pipelines with SQLMesh"
    speakers: [marc-ramirez]
    type: workshop
    language: es
    topic: "Data engineering"
    duration_minutes: 75
    description: "In this session, participants will gain an in-depth understanding of SQLMesh's core concepts, including its innovative approach to environments (physical and virtual layers), diverse model types, and the integration of SQL and Python models. We'll also explore SQLMesh's testing framework, enabling reliable data transformations through rigorous validation. Attendees will be equipped with practical knowledge of how SQLMesh can streamline data pipeline development, making it easier to manage complex transformations and collaborate across data teams."
  - id: lightning-talks-1345
    title: "Lightning talks"
    type: talk
    duration_minutes: 0
    description: " <h2>Lightning talks</h2>\n<b>Leveraging Python in AWS for Smarter Stock Investment Strategies</b><br> <i>Przemyslaw Mikulski</i> <p><q>In this lightning talk, I'll demonstrate how Python can be a powerful ally for retail investors seeking to optimize their stock investments. We'll explore, in just five minutes, how to use Python libraries to solve common challenges faced by investors: data acquisition, analysis, and automation using AWS.</q></p>\n<b>La Rosalía Unveiled: Decoding Her Lyrics with AI</b><br> <i>Olga Ss</i> <p><q>We'll dive into the lyrics of urban singer Rosalía through the lens of Artificial Intelligence, specifically using NLP techniques.</q></p> "
  - id: lightning-talks-1545
    title: "Lightning talks"
    type: talk
    duration_minutes: 0
    description: " <h2>Lightning talks</h2>\n<b>Polars: Procesando datos a la velocidad de la luz con recursos espartanos</b><br> <i>Fernando Aparicio</i> <p><q>Pandas y Spark son las herramientas más conocidas para gestionar nuestros sets de datos, pero hay un jugador nuevo que quiere cambiar las reglas.Polars está pensado para el rendimiento y la resiliencia en entornos con pocos recursos. Cada megabyte y cada segundo cuenta. Os explicaré qué lo hace diferente al resto y qué es capaz de hacer.</q></p>\n<b>Evita bugs amb Pre-Commit</b><br> <i>Carles Julià</i> <p><q>How we improve code quality in our company for Python: pre-commit, ruff-format, ruff, mypy, etc</q></p> "
  - id: lightning-talks-1730
    title: "Lightning talks"
    type: talk
    duration_minutes: 0
    description: " <h2>Lightning talks</h2>\n<b>La iniciativa Scientific Python</b><br> <i>Oriol Abril Pla</i> <p><q>Fa uns anys es va engegar la iniciativa Scientific Python, amb l'objectiu d'enfortir la col·laboració entre llibreries de Python en el camp de la computació científica. En els 5 minuts intentaré explicar què és i algunes de les seves iniciatives principals, que van des de gestió de dependències a consells d'accessibilitat passant per traduccions, 'nightly builds' o governança.</q></p>\n<b>DrugScope: a ML-based platform for drug discovery</b><br> <i>Verónica Larroy</i> <p><q>DrugScope is a machine learning-powered tool designed to predict the binding affinity of small molecules to specific proteins, aiming to accelerate drug discovery and reduce costs. Using Graph Neural Networks (GNNs), the project models molecular structures as graphs, with atoms as nodes and bonds as edges. A public dataset from Leash Biosciences, containing around 300 million molecules and their interactions with three key proteins (HSA, BRD4, and SEH), was used for model training. <br><br> The project involved developing three separate GNN models, one for each protein, to capture the unique molecular interactions relevant to each target. Features for atoms and bonds were extracted using RDKit, and the data was prepared for training by converting these features into graph structures. The models were deployed using FastAPI, allowing researchers to input molecule data and receive predictions on binding affinity, potentially helping speed up the early stages of drug development.</q></p>\n<b>Can LLMs Power Product Recommendations?</b><br> <i>Babaniyi Olaniyi</i> <p><q>I will discuss the use of large language models (LLMs) for product recommendation systems, leveraging their natural language understanding capabilities to predict items a user might purchase given their historical product reviews and purchases.</q></p>\n<b>Pixel2Mechanics: Automated Biomechanical Simulations of High-Resolution Intervertebral Discs from Anisotropic MRIs</b><br> <i>Sai Natarajan</i> <p><q>This study presents Pixel2Mechanics, an automated pipeline for generating patient-specific biomechanical finite element (FE) models of lumbar intervertebral discs (IVD) from clinical MRI data. It utilizes a deep learning framework to create high-resolution meshes of the Annulus Fibrosus (AF) and Nucleus Pulposus (NP) across L1-L2 to L4-L5. The pipeline features a novel optimization method based on differentiable rendering and a Bayesian Coherent Point Drift++ morphing algorithm for volumetric FE meshes that maintain tissue topology. Load simulations validate the models against manual segmentation, demonstrating potential for clinical integration in diagnosing and treating IVD degeneration.</q></p> "
  - id: a-kingdom-above-the-clouds-how-far-can-you-go-on-aws-for-1
    title: "A kingdom above the clouds: How far can you go on AWS for $1 a month?"
    speakers: [kemalcan-bora]
    type: workshop
    language: en
    topic: "Serverless development"
    duration_minutes: 75
    description: "Let's discover how to create a fully functional serverless application that costs less than your morning coffee! We'll build Cloud Kingdom, a cool document processing app that uses AWS Lambda, S3, SQS, and SNS, topped with AI capabilities from Claude. You'll learn how to upload documents, generate automatic summaries, and notify users, all while keeping your wallet happy."
  - id: a-deep-dive-into-the-arrow-columnar-format-with-pyarrow-and
    title: "A deep dive into the Arrow Columnar format with pyarrow and nanoarrow"
    speakers: [raul-cumplido]
    type: workshop
    language: en
    topic: "Apache Arrow, Data Science"
    duration_minutes: 75
    description: "Apache Arrow has become a de-facto standard for efficient in-memory columnar data representation. You might have heard about Arrow or using Arrow, but do you understand the format and why it's so useful? This workshop will dive deep into the details of the Arrow columnar format, the different types and buffer layouts, and explore those details interactively using the pyarrow and nanoarrow libraries."
  - id: automate-end-to-end-mlflow-with-kestra-and-mlflow
    title: "Automate end to end MLflow with Kestra and MLFlow"
    speakers: [manuel-gijon-agudo]
    type: workshop
    language: en
    topic: "Data engineering"
    duration_minutes: 75
    description: "During this session we are going to create a whole ML pipeline, from gathering and prepare the data to train different models and perform inference. We will use a Kaggle competition as our use case. We will learn the basics of Kestra, an orchestration platform, and MLFlow, a tool for keeping track of all processes relative to the full lifecycle for machine learning projects. We are going to use these tools to download a dataset from Kaggle, analyse it, process it, train different models by using different algorithms, perform inference on submission samples, and automatically upload the results back to Kaggle."
  - id: open-source-databases-python-devs
    title: "Open Source Databases Python Devs"
    speakers: [dave-pitts]
    type: workshop
    language: en
    topic: "Databases"
    duration_minutes: 75
    description: "Are you interested in exploring open-source databases? Maybe you have experience with MySQL or PostgreSQL? Perhaps you are unsure which one to pick for your next project, then this workshop is for you. Both are highly successful open-source projects, with many similarities but also some notable differences. I'll also touch on some techniques for optimizing database queries."
  - id: lembolic-videojuegos-hechos-en-el-frontend-por-un-lenguaje
    title: "L'Embolic: Videojuegos hechos en el frontend por un lenguaje de backend"
    title_lang: Spanish
    speakers: [jimena-escobar-bermudez]
    type: workshop
    language: es
    topic: "Web development, Videogames"
    duration_minutes: 75
    description: "¿Te gustan los videojuegos? Entonces, seguro sabes que, desde hace años, los juegos diseñados para ejecutarse en el navegador son bastante populares, tanto por la facilidad de desarrollo como por su versatilidad, al poder jugarlos independientemente del sistema operativo. ¿Y si te digo que ya no es necesario dominar todos los entresijos del desarrollo frontend para poder crearlos? Hoy en día, podrías programarlos con tus conocimientos de Python. PyScript es un framework que permite crear aplicaciones que se ejecutan en el navegador y, con un poco de práctica, ¡incluso podemos desarrollar juegos! Pásate por este taller y te enseñaré cómo hacerlo."
  - id: predict-gender-equality-with-your-own-machine-learning-model
    title: "Predict gender equality with your own Machine Learning model"
    speakers: [asia-noble]
    type: workshop
    language: en
    topic: "Data science"
    duration_minutes: 75
    description: "In this session, you will use Python and Pandas to analyze how gender equality (or inequality) reveals itself through data.<br> What you'll learn:<br> <br>✅ The logic and foundations behind Machine Learning <br>✅ The different use cases of Machine Learning <br>✅ How to predict the gender pay gap"

# The grid, one row per slot of the day, in the order it is printed. A slot
# names the talk it holds, or carries its own label and type when it holds
# none: a break, the group photo, the welcome. The level and the requirements
# sit here and not on the talk, because they are what the slot asks of whoever
# walks into it. A start is always quoted: YAML 1.1 reads an unquoted 9:00 as
# the integer 540.
agenda:
  - start: "9:00"
    credited_as: "PyDay BCN 2024 Organizing Committee"
    track_length: 4
    room: sala-dactes-ada-lovelace
    type: group
    label: "Registration & Welcome"
    duration_minutes: 15
  - start: "9:30"
    track_length: 1
    room: sala-dactes-ada-lovelace
    talk: unboxing-machine-learning-models-predicting-with-numpy
    python_level: intermediate
    topic_level: intermediate
    requirements: "numpy, scikit-learn, and keras installed"
  - start: "9:30"
    track_length: 1
    type: workshop
    duration_minutes: 75
  - start: "9:30"
    track_length: 1
    type: workshop
    duration_minutes: 75
  - start: "9:30"
    track_length: 1
    room: sala-margarita-salas
    talk: discovering-etl-testing-essential-for-your-ai-solutions
    python_level: beginner
    topic_level: beginner
    requirements: "A Github account"
  - start: "11:00"
    track_length: 4
    room: grades
    type: coffee
    label: "Coffee break"
    duration_minutes: 0
  - start: "11:15"
    track_length: 4
    room: aula-hedy-lamarr
    talk: lightning-talks-coffee
  - start: "11:30"
    track_length: 1
    room: sala-dactes-ada-lovelace
    talk: image-generation-with-ai-gans-and-diffusion-techniques
    python_level: beginner
    topic_level: beginner
    requirements: "torch==2.0.1 torchvision==0.15.2 matplotlib==3.7.1"
  - start: "11:30"
    track_length: 1
    room: aula-hipatia-dalexandria
    talk: introduccio-a-xarray-etiqueta-les-teves-dades-n-dimensionals
    python_level: beginner
    topic_level: beginner
    requirements: "https://github.com/OriolAbril/pyday2024-xarray/blob/main/requirements.txt"
  - start: "11:30"
    track_length: 1
    room: aula-hedy-lamarr
    talk: static-typing-in-python
    python_level: beginner
    topic_level: intermediate
    requirements: "https://github.com/alexmolas/python-static-typing/blob/main/requirements.txt"
  - start: "11:30"
    track_length: 1
    room: sala-margarita-salas
    talk: building-data-pipelines-with-sqlmesh
    python_level: beginner
    topic_level: intermediate
    requirements: "Git, Docker Desktop, Visual Studio Code"
  - start: "13:00"
    track_length: 4
    room: grades
    type: photo
    label: "Group photo"
    duration_minutes: 0
  - start: "13:15"
    track_length: 4
    room: grades
    type: lunch
    label: "Lunch break"
    duration_minutes: 15
  - start: "13:45"
    track_length: 4
    room: aula-hedy-lamarr
    talk: lightning-talks-1345
  - start: "14:00"
    track_length: 1
    room: sala-dactes-ada-lovelace
    talk: a-kingdom-above-the-clouds-how-far-can-you-go-on-aws-for-1
    python_level: advanced
    topic_level: advanced
    requirements: "AWS Account"
  - start: "14:00"
    track_length: 1
    type: workshop
    duration_minutes: 75
  - start: "14:00"
    track_length: 1
    room: sala-margarita-salas
    talk: a-deep-dive-into-the-arrow-columnar-format-with-pyarrow-and
    python_level: intermediate
    topic_level: intermediate
    requirements: "You will be able to find both the requirements and the Notebooks on the following repository: https://github.com/raulcd/2024-pyday-bcn-arrow-workshop"
  - start: "15:30"
    track_length: 4
    room: grades
    type: coffee
    label: "Coffee break"
    duration_minutes: 0
  - start: "15:45"
    track_length: 4
    room: aula-hedy-lamarr
    talk: lightning-talks-1545
  - start: "16:00"
    track_length: 1
    room: sala-dactes-ada-lovelace
    talk: automate-end-to-end-mlflow-with-kestra-and-mlflow
    python_level: beginner
    topic_level: beginner
    requirements: "Docker, Conda"
  - start: "16:00"
    track_length: 1
    room: aula-hipatia-dalexandria
    talk: open-source-databases-python-devs
    python_level: intermediate
    topic_level: beginner
    requirements: "Postgres and MySQL installed locally or via Docker"
  - start: "16:00"
    track_length: 1
    room: aula-hedy-lamarr
    talk: lembolic-videojuegos-hechos-en-el-frontend-por-un-lenguaje
    python_level: intermediate
    topic_level: beginner
  - start: "16:00"
    track_length: 1
    room: sala-margarita-salas
    talk: predict-gender-equality-with-your-own-machine-learning-model
    python_level: beginner
    topic_level: beginner
    requirements: "Data Science techstack: PowerBI, Python, Scikit Learn, Tensorflow. Background n the creative tech industry, management, consulting, and operations."
  - start: "17:30"
    track_length: 4
    room: sala-dactes-ada-lovelace
    talk: lightning-talks-1730
  - start: "17:45"
    track_length: 4
    room: sala-dactes-ada-lovelace
    type: group
    label: "Closing session & Kahoot"
    duration_minutes: 0

# Photos published by PyBCN on the day, one per post so no two share a caption,
# which is also the alt text. Imported with bin/import-x-photos, which excludes
# anything the account only shared: that copyright belongs to somebody else.
# The one photo of this day: the group photo when the day has one, and the
# picture that says most about it when it does not. It is what the carousel
# of the home page shows, one slide per event. See
# partials/canonical_photos.html.
canonical_photo: pyday-2024/01-thanks-for-attending-the-pydaybcn-2024-see-you-nex.jpg

photos:
  thread: "https://x.com/PyBCN/status/1855180142240272592"
  items:
    - file: pyday-2024/01-today-we-re-celebrating-the-pydaybcn-welcome-pleas.jpg
      caption: "Today we're celebrating the #PyDayBCN! Welcome 👋, please get a seat!"
      source: "https://x.com/PyBCN/status/1855180142240272592"
      time: "10:26"
    - file: pyday-2024/02-unboxing-machine-learning-models-predicting-with-n.jpg
      caption: "\"Unboxing Machine Learning Models: Predicting with Numpy After Model Training\", by Xiang Xu"
      source: "https://x.com/PyBCN/status/1855181919559790867"
      time: "10:33"
      talk: unboxing-machine-learning-models-predicting-with-numpy
    - file: pyday-2024/03-discovering-etl-testing-essential-for-your-ai-solu.jpg
      caption: "\"Discovering ETL Testing: Essential for Your AI Solutions\", by Paula Bassagañas"
      source: "https://x.com/PyBCN/status/1855182272384663612"
      time: "10:34"
      talk: discovering-etl-testing-essential-for-your-ai-solutions
    - file: pyday-2024/04-izi-record-revolutionizing-the-camera-app-by-ferra.jpg
      caption: "\"IZI Record, revolutionizing the camera app\" by Ferran Jovell (@MrSwats)"
      source: "https://x.com/PyBCN/status/1855211394183962886"
      time: "12:30"
    - file: pyday-2024/05-mrswats-a-solution-to-store-catalog-and-visualize.jpg
      caption: "\"A solution to store, catalog and visualize images using Django and Django Rest Framework\" by Josep Sitjar Suñer"
      source: "https://x.com/PyBCN/status/1855211686346510817"
      time: "12:31"
    - file: pyday-2024/06-mrswats-image-generation-with-ai-gans-and-diffusio.jpg
      caption: "\"Image Generation with AI (GANs and Diffusion Techniques)\" by Marina Palma"
      source: "https://x.com/PyBCN/status/1855213044026032482"
      time: "12:37"
      talk: image-generation-with-ai-gans-and-diffusion-techniques
    - file: pyday-2024/07-introduccio-a-xarray-etiqueta-les-teves-dades-n-di.jpg
      caption: "\"Introducció a xarray: etiqueta les teves dades n-dimensionals\" by Oriol Abril Pla"
      source: "https://x.com/PyBCN/status/1855213518359834954"
      time: "12:39"
      talk: introduccio-a-xarray-etiqueta-les-teves-dades-n-dimensionals
    - file: pyday-2024/08-static-typing-in-python-by-alex-molas.jpg
      caption: "\"Static Typing in Python\" by Alex Molas"
      source: "https://x.com/PyBCN/status/1855213686542983460"
      time: "12:39"
      talk: static-typing-in-python
    - file: pyday-2024/09-building-data-pipelines-with-sqlmesh-by-marc-ramir.jpg
      caption: "\"Building data pipelines with SQLMesh\" by Marc Ramirez"
      source: "https://x.com/PyBCN/status/1855213884220600758"
      time: "12:40"
      talk: building-data-pipelines-with-sqlmesh
    - file: pyday-2024/10-la-rosalia-unveiled-decoding-her-lyrics-with-ai-by.jpg
      caption: "\"La Rosalía Unveiled: Decoding Her Lyrics with AI\", by Olga Ss"
      source: "https://x.com/PyBCN/status/1855249867385307276"
      time: "15:03"
    - file: pyday-2024/11-a-kingdom-above-the-clouds-how-far-can-you-go-on-a.jpg
      caption: "\"A kingdom above the clouds: How far can you go on AWS for $1 a month?\", by Kemalcan Bora"
      source: "https://x.com/PyBCN/status/1855250188463411365"
      time: "15:04"
      talk: a-kingdom-above-the-clouds-how-far-can-you-go-on-aws-for-1
    - file: pyday-2024/12-a-deep-dive-into-the-arrow-columnar-format-with-py.jpg
      caption: "\"A deep dive into the Arrow Columnar format with pyarrow and nanoarrow\", by Raúl Cumplido"
      source: "https://x.com/PyBCN/status/1855251365431288257"
      time: "15:09"
      talk: a-deep-dive-into-the-arrow-columnar-format-with-pyarrow-and
    - file: pyday-2024/13-polars-procesando-datos-a-la-velocidad-de-la-luz-c.jpg
      caption: "\"Polars: Procesando datos a la velocidad de la luz con recursos espartanos\", by Fernando Aparicio"
      source: "https://x.com/PyBCN/status/1855263927799525470"
      time: "15:59"
    - file: pyday-2024/14-evita-bugs-amb-pre-commit-by-carles-julia-chaosct.jpg
      caption: "\"Evita bugs amb Pre-Commit\", by Carles Julià (@chaosct)"
      source: "https://x.com/PyBCN/status/1855267845711527972"
      time: "16:14"
    - file: pyday-2024/15-chaosct-predict-gender-equality-with-your-own-mach.jpg
      caption: "\"Predict gender equality with your own Machine Learning model\", by Asia Noble"
      source: "https://x.com/PyBCN/status/1855268923261767778"
      time: "16:19"
      talk: predict-gender-equality-with-your-own-machine-learning-model
    - file: pyday-2024/16-chaosct-l-embolic-videojuegos-hechos-en-el-fronten.jpg
      caption: "\"L'Embolic: Videojuegos hechos en el frontend por un lenguaje de backend\", by Jimena (@Jimena_y_yo)"
      source: "https://x.com/PyBCN/status/1855269101087735918"
      time: "16:19"
      talk: lembolic-videojuegos-hechos-en-el-frontend-por-un-lenguaje
    - file: pyday-2024/17-chaosct-jimena-y-yo-open-source-databases-python-d.jpg
      caption: "\"Open Source Databases Python Devs\" by Dave Pitts"
      source: "https://x.com/PyBCN/status/1855269396618355152"
      time: "16:21"
      talk: open-source-databases-python-devs
    - file: pyday-2024/18-automate-end-to-end-mlflow-with-kestra-and-mlflow.jpg
      caption: "\"Automate end to end MLflow with Kestra and MLFlow\", by Manuel Gijón"
      source: "https://x.com/PyBCN/status/1855269627300827556"
      time: "16:22"
      talk: automate-end-to-end-mlflow-with-kestra-and-mlflow
    - file: pyday-2024/19-la-iniciativa-scientific-python-by-oriol-abril-pla.jpg
      caption: "\"La iniciativa Scientific Python\", by Oriol Abril Pla"
      source: "https://x.com/PyBCN/status/1855316971211948104"
      time: "19:30"
    - file: pyday-2024/20-drugscope-a-ml-based-platform-for-drug-discovery-b.jpg
      caption: "\"DrugScope: a ML-based platform for drug discovery\", by Verónica Larroy"
      source: "https://x.com/PyBCN/status/1855317098773225775"
      time: "19:30"
    - file: pyday-2024/21-can-llms-power-product-recommendations-by-babaniyi.jpg
      caption: "\"Can LLMs Power Product Recommendations?\", by Babaniyi Olaniyi\""
      source: "https://x.com/PyBCN/status/1855317374867472871"
      time: "19:31"
    - file: pyday-2024/22-pixel2mechanics-automated-biomechanical-simulation.jpg
      caption: "\"Pixel2Mechanics: Automated Biomechanical Simulations of High-Resolution Intervertebral Discs from Anisotropic MRIs\", by Sai Natarajan"
      source: "https://x.com/PyBCN/status/1855317468480479312"
      time: "19:32"
    - file: pyday-2024/01-thanks-for-attending-the-pydaybcn-2024-see-you-nex.jpg
      caption: "Thanks for attending the #PyDayBCN 2024! See you next year!"
      source: "https://x.com/PyBCN/status/1855898395161805079"
      time: "10:00"
---


## About PyDay BCN 2024

We are excited to announce the **8th edition** of PyDay in Barcelona!

PyDay is an event packed with FREE **python-related workshops** and activities for the Python community. It is organized once per year. Over the last seven editions, PyDay has become a fantastic opportunity to share our love for Python and engage users, companies, and newcomers!

### When and where

It is scheduled for **Saturday 9th November** at [Canòdrom](https://maps.app.goo.gl/Uxiao2Dr7uio9o3v9), from 9:00 a.m. to 18:00 p.m. CET, approximately.

### A full day of in-person, hands-on workshops

PyDay BCN 2024 will have different **thematic tracks** --e.g. data science, web development, security-- with hands-on workshops lasting about 90 minutes. Participants will learn how to use different libraries, tools and techniques, fully guided by community members and support volunteers.

### Participate in Kahoot and win prizes!

We will host a Kahoot game with questions about PyBCN and Python in general, with prizes for the fastest players. Will you miss it?!
