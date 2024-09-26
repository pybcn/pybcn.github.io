---
title: "PyDay BCN 2020"
description: "The fourth edition!"
menu:
  main:
    parent: 'PyDay BCN'
weight: 5
aliases:
- /pyday-bcn-2020
heroBackground: https://images.unsplash.com/photo-1504384764586-bb4cdc1707b0?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80

layout: event

free_text_sections:
    - title: Registration
      id: registration
      content: "All attendeed must **<a href='https://www.meetup.com/python-barcelona/events/274983461/' target='_blank'>register to the event through Meetup</a>**, which will be the main communication channel with attendees before the event. All registered attendees will receive the links to the YouTube playlists and Slack channels through Meetup."

sponsor_levels:
    - sponsors_per_line: 2
      sponsors: [cloudblue]
      name: Gold
    - sponsors_per_line: 2
      sponsors: [preply, qida]
      name: Supporting

people_sections:
    - title: Speakers
      id: speakers
      levels:
        - people_per_line: 4
          people:
              - alberto
              - alvaro_duran
              - ankit-mahato
              - carles_barrobes
              - christian-adell-querol
              - daniel_mesejo
              - edgar-riba
              - eduard_cespedes
              - elisabeth-ortega-carrasco
              - ferran-fabregas
              - francesco-faraone
              - gajendra-deshpande
              - joan-fontanals-martinez
              - jose_haro
              - julio-martinez
              - marc-pous
              - maria-teresa-grifa
              - miroslav_sedivy
    - title: Organizers
      id: organizers
      levels:
        - people_per_line: 4
          people:
              - david
              - eloi
              - ifosch
              - lpmayos
              - mireia
              - natalia
              - nuria
              - rberenguel

previous_editions:
    - name: PyDay BCN 2019
      url: /events/pyday_bcn/pyday_bcn_2019/
    - name: PyDay BCN 2018
      url: /events/pyday_bcn/pyday_bcn_2018/
    - name: PyDay BCN 2016
      url: /events/pyday_bcn/pyday_bcn_2016/

spansDuration: 15
numTracks: 2
eventTimes: [16:00, 16:15, 16:30, 16:45, 17:00, 17:15, 17:30, 17:45, 18:00, 18:15, 18:30, 18:45, 19:00, 19:15, 19:30, 19:45, 20:00, 20:15, 20:30]
events:
    - start_time_slot: 16:00
      end_time_slot: 16:00
      track_length: 2
      video: https://www.youtube.com/watch?v=oLB0eo7tpj0
      color: purple
      title: "Welcome Session"
      speaker: "Laura Pérez-Mayos"
      location: https://www.youtube.com
      type: group
      location: YouTube track1 and track2

    - start_time_slot: 16:15
      end_time_slot: 16:30
      track_length: 1
      video: https://www.youtube.com/watch?v=w9cYczex79M
      color: orange
      title: "Ready, Set, Go with Numba"
      description: "The prominent reasons for the wide adoption of Python is the ease of learning, usability and readability coupled with the powerful ecosystem of Python packages. This often makes Python an attractive language for researchers & scholars to undertake computational projects and thesis. The ease of prototyping and tinkering allows for higher number of iterations and customization, leading to an increase in research output. But, a major pain point of using Python is its speed when compared to languages like C++ or FORTRAN which are still widely used in research.<br/><br/>Developers, when hit by the performance bottleneck of python code, often come across some methods to increase their code performance like using PyMPI, Numpy or CPython. But, the learning curve is steep and APIs get less familiar. <br/><br/>If learning Python is so easy, why should increasing the performance of Python code be so difficult?<br/><br/>This talk will address this question and get us up and running with Numba, an open source JIT compiler that translates Python and NumPy code into fast machine code. We will delve into real world exercises which will demonstrate the core concepts, ease and effectiveness of using Numba and how it can be useful in lowering the barrier to achieve code performance in Python."
      language: "English"
      speaker: "Ankit Mahato"
      type: talk
      python_level: Beginner
      topic: Data Science, ML, DL
      location: YouTube track1
    - start_time_slot: 16:45
      end_time_slot: 17:00
      track_length: 1
      video: https://www.youtube.com/watch?v=uzjlrbqq26M
      color: orange
      title: "Working with Text Data in Pandas"
      description: "I'll will present some tips, tricks and libraries to speed up text processing with pandas."
      language: "Spanish"
      speaker: "Daniel Mesejo"
      type: talk
      python_level: Intermediate
      topic: Data Science, ML, DL
      location: YouTube track1
    - start_time_slot: 17:15
      end_time_slot: 17:15
      track_length: 1
      video: https://www.youtube.com/watch?v=Hnr7MH9Pd5s
      color: orange
      title: "Lifebox: a virtual ecosystem"
      description: "Lifebox is a project about a virtual ecosystem created using Python. Inside the Lifebox you can find two different kind of species, the ‘species’ and the ‘mana’. Each of the ‘species’ have a set of parameters that defines how they evolve inside the virtual ecosystem, and you can change all the parameter of species in real-time. The goal of the project is to offer the possibility to learn the basic concepts of biology through the experimentation, viewing the consequences of your actions and trying to find the way to balance the ecosystem through changing the Lifebox parameters."
      language: "Catalan"
      speaker: "Ferran Fábregas"
      type: lightning
      python_level: Intermediate
      topic: Data Science, ML, DL
      location: YouTube track1
    - start_time_slot: 17:30
      end_time_slot: 17:30
      track_length: 1
      video: https://www.youtube.com/watch?v=4oc0OTkks0k
      color: orange
      title: "Transformers: the all-in-one tool for NLP"
      description: "NLP has been evolving from classic bag of words to embedding methods. But in 2017 finally a new model that can be used for all kind of NLP tasks emerged: transformers. Let's review its general ideas, and a practical example of its use."
      language: "English"
      speaker: "Julio Martínez"
      type: lightning
      python_level: Intermediate
      topic: Data Science, ML, DL
      location: YouTube track1
    - start_time_slot: 17:45
      end_time_slot: 17:45
      video: https://www.youtube.com/watch?v=4-OPxy4CLAw
      track_length: 1
      color: blue
      title: "A Day Has Only 24±1 Hours"
      description: "On the last Sunday of October you may get “one more hour of sleep” but as well may spend much more time debugging code dealing with the time zones, daylight saving time shifts and datetime stuff in general. Two centuries of short-sighted propaganda and long-term chaos in ten minutes. Maybe that will make you want to avoid time zones in your code altogether!<br/><br/>El último domingo de octubre puedes obtener “una hora más de sueño”, pero también puedes pasar mucho más tiempo debugando el código tratando con las zonas horarias, los cambios de horario de verano y las cosas de fecha y hora en general. Dos siglos de propaganda miope y caos a largo plazo en diez minutos. ¡Quizás eso te haga querer evitar las zonas horarias en tu código por completo!"
      language: "English"
      speaker: "Miroslav Šedivý"
      type: lightning
      python_level: Intermediate
      topic: Python programming
      location: YouTube track1
    - start_time_slot: 18:00
      end_time_slot: 18:00
      video: https://www.youtube.com/watch?v=B0YM3XkNkQs
      track_length: 1
      color: blue
      title: "Ho sento, no ets el meu tipus"
      description: "Type Hints were introduced in Python 3 but you may have never used them, known that they exist, or seen code that uses them. Or you may have seen code with type hints and cringed because it didn't look like the Python you know. In this talk we will demistify type hints and show how they can actually help you find potential bugs."
      language: "Catalan"
      speaker: "Carles Barrobés"
      type: lightning
      python_level: Intermediate
      topic: Python programming
      location: YouTube track1

    - start_time_slot: 16:15
      end_time_slot: 16:30
      track_length: 1
      video: https://www.youtube.com/watch?v=8UjkfOKh6jA
      color: yellow
      title: "Alexa, te elijo a ti"
      description: "Algunos de nosotros tenemos un aparatito en casa escuchándonos 24/7 que usamos para escuchar música, preguntarle la hora y pedirle un temporizador o un chiste malo. En esta charla os voy a enseñar como programar a Alexa usando Python para que os ayude en vuestras tareas usando dos ejemplos: una skill que nos calculará equivalencias para ayudarnos en las recetas de cocina (entre otras cosas) y otra que nos aconsejará sobre qué tipo de Pokémon elegir para enfrentarnos a un oponente."
      language: "Spanish"
      speaker: "Elisabeth Ortega Carrasco"
      type: talk
      python_level: Beginner
      topic: IOT
      location: YouTube track2
    - start_time_slot: 16:45
      end_time_slot: 17:00
      video: https://www.youtube.com/watch?v=Se3FmYvn6sM
      track_length: 1
      color: green
      title: "Network automation using Python"
      description: "I will share the status of network automation using Python, presenting and demoing some popular libraries such as Netmiko, Napalm and Nornir."
      language: "English"
      speaker: "Christian Adell"
      type: talk
      python_level: Intermediate
      topic: Network automation
      location: YouTube track2
    - start_time_slot: 17:15
      end_time_slot: 17:15
      track_length: 1
      video: https://www.youtube.com/watch?v=kwa58dEhPNY
      color: blue
      title: "Retrying, a better way"
      description: "Python have a lot of libraries, for multiple purposes, and among them there are a lot of hidden gems, such as the Backoff library (https://github.com/litl/backoff) which will make retrying operations based on exceptions or predicates an easy game.<br/>Handling retries have never been so simple."
      language: "English"
      speaker: "Christian Adell"
      type: lightning
      python_level: Beginner
      topic: Python programming
      location: YouTube track2
    - start_time_slot: 17:30
      end_time_slot: 17:30
      video: https://www.youtube.com/watch?v=S3ebYJxXBRU
      track_length: 1
      color: blue
      title: "Antifragile Software: Code that gains from disorder"
      description: "Joel Spolsky famously said that you should never rewrite your code from scratch. Still, many organizations see no other way out of their codebases. Why? In this talk we explore the concept of antifragility, and how it can be applied to software engineer to keep your codebase from getting \"rusty\"."
      language: "English"
      speaker: "Alvaro Duran"
      type: lightning
      python_level: Beginner
      topic: Python programming
      location: YouTube track2
    - start_time_slot: 17:45
      end_time_slot: 18:00
      track_length: 1
      video: https://www.youtube.com/watch?v=cmi4B41oOd8
      color: green
      title: "Efficiently share data on a true microservices architecture using django-cqrs (CloudBlue sponsored talk)"
      type: talk
      location: YouTube track2
      topic: Web development, microservices
      language: "English"
      python_level: Intermediate
      speaker: Francesco Faraone

    - start_time_slot: 18:15
      end_time_slot: 18:15
      track_length: 2
      color: purple
      title: "Coffee Break"
      type: coffee

    - start_time_slot: 18:30
      end_time_slot: 18:45
      track_length: 1
      video: https://www.youtube.com/watch?v=v75bTfShH-M
      color: orange
      title: "Performing Sentiment Analysis on Video with Serverless Architectures"
      description: "In this talk we will explain how to create video processing pipelines using an event-driven and fully Serverless Architecture in AWS. We will use AWS Chalice, a Python framework from AWS, for managing the serverless Lambda Functions and a range variety of AWS services for the video manipulation like AWS Elastic Transcoder, Amazon Transcribe, Amazon Comprehend. And of course the more common architectural and traditional services like S3, DynamoDB, Gateway, SQS, SNS and SES."
      language: "English"
      speaker: "Eduard Cespedes Borras"
      type: talk
      python_level: Intermediate
      topic: Data Science, ML, DL
      location: YouTube track1
    - start_time_slot: 19:00
      end_time_slot: 19:15
      video: https://www.youtube.com/watch?v=KOpW86J56CU
      track_length: 1
      color: orange
      title: "Counting votes: analyzing a large dataset with Dask"
      description: "We will explain how to switch from Pandas to Dask in order to analyze a large dataset that does not fit into single-machine memory.<br/><br/>Repository: <a href='https://github.com/ber2/pyday2020-counting-votes-with-dask' target='_blank'>https://github.com/ber2/pyday2020-counting-votes-with-dask</a>"
      language: "English"
      speaker: "Alberto Camara"
      type: talk
      python_level: Intermediate
      topic: Data Science, ML, DL
      location: YouTube track1
    - start_time_slot: 19:30
      end_time_slot: 19:45
      track_length: 1
      video: https://www.youtube.com/watch?v=uUwmknHAIhU
      color: orange
      title: "Kornia: differentiable Computer Vision with Pytorch"
      description: "The talk is an introduction to Kornia which is a library that implements classical Computer Vision algorithms in PyTorch that got a lot of attention within the open source community during the last year. The core of the library is written from scratch using pure PyTorch operators and uses the auto-reverse differentiable engine to allow to the user to plug any function within neural networks with a transparent API for high performance devices such as GPUs and TPUs. During the talk I'll go through the different principle designs and the functionalities found in each of the modules, practical examples, basic usage of the library and more. Information about the project in the website: www.kornia.org"
      language: "English"
      speaker: "Edgar Riba"
      type: talk
      python_level: Intermediate
      topic: Data Science, ML, DL
      location: YouTube track1
    - start_time_slot: 20:00
      end_time_slot: 20:15
      track_length: 1
      video: https://www.youtube.com/watch?v=UtK-npeVsH0
      color: orange
      title: "JINA AI: An Open Source Neural Search Framework"
      description: "What is neural or semantic search? How is it different from traditional symbolic search? Jina AI is an open source framework for AI-powered search."
      language: "English"
      speaker: "Joan Fontanals Martinez"
      type: talk
      python_level: Beginner
      topic: Data Science, ML, DL
      location: YouTube track1

    - start_time_slot: 18:30
      end_time_slot: 18:45
      track_length: 1
      video: https://www.youtube.com/watch?v=nWVJ7HfFC5E
      color: yellow
      title: "Building My First Python IoT Device with Containers (in 20 minutes)"
      description: "This workshop is designed for developers who are coming from Web development and other technologies into the Internet of Things. This session will guide assistants how to connect an Arm-powered device such as a Raspberry Pi to the Internet with balena and open source tools."
      language: "English"
      speaker: "Marc Pous"
      type: talk
      python_level: Beginner
      topic: IOT
      location: YouTube track2
    - start_time_slot: 19:00
      end_time_slot: 19:15
      track_length: 1
      video: https://www.youtube.com/watch?v=BoaGrcmfVH8
      color: green
      title: "Documentation-driven development for Python web APIs"
      description: "In this presentation, I want to show how developers can minimise the risk of API integration failures by using documentation-driven development. Documentation-driven development is an approach where we first write the API documentation, and then we validate the API implementation against the specification. This approach helps us create a more robust software delivery process for our APIs. I’ll show useful tools and frameworks, such as Dredd, that can help us automatically generate tests that validate our APIs. "
      language: "English"
      speaker: "Jose Haro Peralta"
      type: talk
      python_level: Beginner
      topic: Web
      location: YouTube track2
    - start_time_slot: 19:30
      end_time_slot: 19:45
      video: https://www.youtube.com/watch?v=LvvwLYk9aIo
      track_length: 1
      color: blue
      title: "Alice in Pythonland: Object oriented programming in Lewis Carroll games"
      description: "Tutorial regarding object oriented programming in Python. The applications that will be presented are some of the maths games hidden in the book Alice in Wonderland of Lewis Carroll. These games are algorimths pubblished by Lewis Carroll on scientific journals. My contribution would be to explain oop techniques (inheritance,decorators,dataclass, nametuple,...) for developing maths games and use some NLP techniques (i.e., finding the dialogs between charcaters in the books) for presenting the interactions between the playes involved in the game.<br/>I have been inspired by a repository from Anna-Lena Popkes<br/>(please see https://github.com/zotroneneis/magical_universe) on working on one  programming topic per day. In this way, I have improved  my coding skills day by day and I have created the a Wonderland Universe. The idea of coding the games created by Lewis Carroll is related to my maths background and has the intent of explain some joyful algorithms. My goal is to encourage other people to use the same learning technique and challege theiself with custom examples and applications."
      language: "English"
      speaker: "Maria Teresa Grifa"
      type: talk
      python_level: Beginner
      topic: Python programming
      location: YouTube track2
    - start_time_slot: 20:00
      end_time_slot: 20:15
      track_length: 1
      video: https://www.youtube.com/watch?v=LAQY4ucheQA
      color: green
      title: "Investigating Digital Crimes using Python"
      description: "A recent study by CheckPoint Research has recorded over 1,50,000 cyber-attacks every week during the COVID-19 pandemic. There has been an increase of 30% in cyber-attacks compared to previous weeks. The pandemic has been the main reason for job loss and pay cuts of people and has led to an increase in cybercrimes. Examples of cyber-attacks include phishing, ransomware, fake news, fake medicine, extortion, and insider frauds. Cyber forensics is a field that deals with the investigation of digital crimes by analyzing, examining, identifying, and recovering digital evidence from electronic devices and producing them in the court of law. Python has a great collection of built-in modules for digital forensics tasks. The talk begins with an introduction to digital crimes, digital forensics, the process of investigation, and the collection of evidence. Next, I will discuss report creation using CSV and Excel reports, investigation of acquisition media using the pyscreenshot module. Finally, I will conclude the talk with the investigation of embedded metadata, emails, and log files. In this talk, I will cover mutagen, mailbox, tqdm, argparser, yara python modules, and utilities which are used for the above-mentioned tasks.<br/><br/>In this talk, the audience will learn the procedure to be followed while investigating digital crimes and most importantly how to develop their own digital forensic tools using Python. I believe that the attendees will learn about the new exciting field where there are lots of opportunities with respect to their careers. Basic understanding of Python language or any other scripting language will be helpful in understanding the concepts.<br/><br/>Outline 1. Introduction to digital crimes, digital forensics, the process of investigation, and collection of evidence. [05 Minutes] 2. Report creation using CSV and Excel reports [04 Minutes] 3. Investigation of acquisition media using the pyscreenshot module [03 Minutes] 4. Investigation of embedded metadata [05 Minutes] 5. Investigation of emails [05 Minutes] 6. Investigation of log files [05 Minutes] 7. Conclusion and Questions [03 Minutes]"
      language: "English"
      speaker: "Gajendra Deshpande"
      type: talk
      python_level: Beginner
      topic: Security
      location: YouTube track2

    - start_time_slot: 20:30
      end_time_slot: 20:30
      track_length: 2
      color: purple
      title: "Kahoot game and closing remarks"
      location: Zoom
      type: workshop

        
---

## What is PyDay BCN 2020 about?

We are excited to announce that we are organizing **the fourth edition** of PyDay in Barcelona! This year it will be an **online event** with up to 200 attendees. It is scheduled for **12th of December from 4:00pm to 8:45pm CET**.

PyDay is an event full of FREE python-related activities for the Python community, organized once per year. Over the last three editions, PyDay has become a great opportunity to share our love for Python and engage users, companies and newcomers into it!

### Talks, demos and lightning talks
PyDay BCN 2020 will have different **thematic tracks** --e.g. data science, web development, security-- with talks and demos of about 20 minutes in which participants will learn how to use different libraries, tools and techniques, and also shorter lightning talks. The videos will be **pre-recorded and released on YouTube** along the event according to the agenda, and we will host live **Q&A sessions through Slack**.

### Participate in Kahoot and win prizes!
 We will host a Kahoot game with questions about PyBCN and Python in general, with prizes for the fastest players. Will you miss it?!
 
 
### Sponsor us!
Would you like to sponsor PyDay BCN 2020? Have a look at the <a href="https://bit.ly/pydaybcn-2020-sponsoring" target="_blank">sponsorship brochure</a>!<br/><br/>
