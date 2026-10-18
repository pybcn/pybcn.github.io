---
title: "PyDay BCN (2018)"
year: 2018
# The day of this edition, from the Meetup export, which records it per event.
date: 2018-11-24
# The venue of this edition, from the Meetup export, which records it per event.
venue: "Punt Multimèdia Espanya Industrial"
description: ""
menu:
  main:
    parent: 'PyDay BCN'
weight: 8
heroBackground: /images/photos/people-pyday-2016.jpg

# The programme of this edition, read from the page the association published
# for it, which this repository keeps frozen at
# static/archives/pybcn.org/pyday-bcn-2018/index.html. Its Agenda table gives
# the time, the track, and the speaker of every session, and its "Workshops
# descriptions" section gives the description, the language, the level, and
# the requirements of each one. Nothing here comes from anywhere else.
#
# Titles and descriptions are copied from that page, typos included: it prints
# "SInce pytorch's models", "Facebooks's AI Research Group", and "a variety of
# interestss levels".
#
# No talk carries a length. The page gives a start time per row and says, in
# prose, that each workshop is "about 80 minutes long". It never prints an end
# time, so none is stored.
#
# The five rows that are not a session are not talks: Registration & Breakfast
# at 09:30, the Welcome session at 10:00, the Coffee break at 12:00, Lunch at
# 14:00, and the Closing session at 18:00.
talks:
  - id: developing-a-small-application-with-git
    title: "Developing a small application with git"
    speakers: [ignasi-fosch]
    language: en
    type: workshop
    description: "In this workshop, the attendees will participate in collaborative developing a small simple application using git and GitHub for the workflow. The goals of the exercise is to practice some simple concepts about contributing code."
  - id: introduction-to-pytorch
    title: "Introduction to pytorch"
    speakers: [bartek-skorulski]
    language: en
    type: workshop
    description: "Why is it worth to know pytorch? Pytorch is a machine/deep learning library for python mainly developed by Facebooks's AI Research Group. SInce pytorch's models are just like other python programs, it quite easy to write and debug them. Hence pytorch is great for research and experiments. Moreover, with new version 1.0, pytorch introduce \"script mode\" that aims to become also a tool for writing production code.\n\nIn this short workshop we give a quick and dirty introduction to pytorch. You will have an opportunity to build, train and evaluate few forward feed neural networks. We start with a simple single layer neural networks and finish with convolutional ones."
  - id: data-analysis-with-jupyter-notebook-pandas-and-plotly
    title: "Data analysis with Jupyter Notebook, Pandas and Plotly"
    speakers: [natalia-padilla, laura-perez-mayos]
    language: en
    type: workshop
    description: "A hands-on session where you will learn how to analyze data with Jupyter Notebook, Pandas and Plotly. This will be a guided workshop, suitable for both experienced users and beginners with an interest in data analysis."
  - id: mirror-mirror-on-the-wall-introduction-to-opencv
    title: "Mirror, mirror on the wall, who is the fairest of them all? (Introduction to OpenCV)"
    speakers: [ismael-benito]
    language: en
    type: workshop
    description: "An introduction to OpenCV for NumPy-Scipy-Matplotlib stack users. Starting with Anaconda pre-compiled versions, specially from Menpo project (https://anaconda.org/menpo/opencv3). Covering inputs and outputs, from basic image handling, such as: 'imread', 'imshow', 'imwrite', etc; to video streams. Some basics in color treatment and thresholding techniques. Also, fundamentals of image warping and cropping. Finally, a small project to be able to find a specific object, for example a QR Code, in a scene and trimmed it."
  - id: python-and-elasticsearch
    title: "Python and Elasticsearch"
    speakers: [artur-mindiyarov]
    language: en
    type: workshop
    description: "Elasticsearch is one of the best open-source, cross-platform, distributed and scalable search engine. In this workshop we are going to learn basics of Elasticsearch and use it to built our own search solution."
  # The numbered session plan the page prints between the description and
  # the level is not the description, so it stays in the body only.
  - id: intro-to-nosql-db-with-pymongo
    title: "Intro to NoSQL DB with PyMongo"
    speakers: [jordi-guix]
    language: en
    type: workshop
    description: "Learn how to access and manage big data with Python. How to access to DB, basic CRUD operations (Create, Read, Update, Delete) and overview of advance operations. Get the [workshop materials](https://github.com/giffy)."
  - id: guillotina-data-framework
    title: "Guillotina - Data framework"
    speakers: [ramon-navarro-bosch]
    language: en
    type: workshop
    description: "A walkthrough from creating a data REST API with your custom model and structure to an interactive interface to consume and manage it. Security and custom rich object models to create micro-services that handles large volume information. We also will cover how to interact with it to compute models using its internal API and Jupyter."
  - id: organizando-chistes-con-nlp
    title: "Organizando chistes con NLP"
    speakers: [julio-martinez]
    language: es
    type: workshop
    description: "Haciendo un repaso global de diferentes técnicas de NLP clásicas y modernas, vamos a organizar una colección de chistes en castellano. Habrá una introducción general con slides (30 minutos) y luego una serie de ejercicios con un notebook de Jupyter."

# The page names no room. What it names is the track of each column of the
# agenda table, and the two columns change track after lunch: the left one
# runs the introductory workshops in the morning and the web track in the
# afternoon, the right one the two halves of the data track. These four are
# the headings the table prints, so they are what a talk points at.
rooms:
  - id: pybcn-introductory-workshops
    name: "PyBCN Introductory Workshops"
  - id: data-and-python-track-i
    name: "Data and Python Track (I)"
  - id: web-track
    name: "Web Track"
  - id: data-and-python-track-ii
    name: "Data and Python Track (II)"

# The grid, one row per session of the day, in the order the agenda table
# prints it: by time, and then by the column order of rooms above. A slot is
# when and where; the talk it names is what was said. The two were one list
# until this edition was converted, and the eight later editions already carry
# them apart.
#
# level, requirements and installation sit on the slot and not on the talk,
# because they are what the session asked of whoever walked into it. level is
# the one level the frozen page prints under each workshop description, which
# is not the python_level and topic_level pair that the editions from 2020 on
# carry: the source names one level and not two. requirements is a list here
# and a single string on those later editions, because the page prints the
# requirements of a workshop as separate lines.
#
# No slot carries a track_length other than 1: the table runs two columns all
# day and no session spanned both. No slot carries a duration_minutes either,
# because no session has a length to put on it: the page gives a start time
# per row and says, in prose, that each workshop is "about 80 minutes long".
#
# The five rows of the table that are not a session are not slots of this
# list: Registration & Breakfast at 09:30, the Welcome session at 10:00, the
# Coffee break at 12:00, Lunch at 14:00, and the Closing session at 18:00.
# They are in the table the body of this page prints, verbatim, and nothing
# reads them from here.
#
# This page declares no eventTimes, so no grid is rendered from this list. The
# programme a reader sees is that same frozen table. The list is here because
# a photo of the gallery joins to a talk by id, and because the nine photo
# days still to import need one shape for a programme and not two.
agenda:
  - start: "10:30"
    track_length: 1
    room: pybcn-introductory-workshops
    talk: developing-a-small-application-with-git
    level: beginner
    requirements:
      - "Git installed"
      - "Some virtual environment with Python 3.6 and pytest setup"
      - "GitHub account created"
  - start: "10:30"
    track_length: 1
    room: data-and-python-track-i
    talk: introduction-to-pytorch
    level: intermediate
    requirements:
      - "We assume that you are familiar with python, have some basic knowledge about neural network."
      - "You will get the best experience if you bring a notebook with access to python (I'll use version 3.6) with numpy, pandas, jupyter, pytorch, matplotlib, pillow and opencv."
      - "[Guide to install Pytorch](https://bartek-blog.github.io/python/pytorch/conda/2018/11/12/install-pytorch-with-conda.html)."
  - start: "12:30"
    track_length: 1
    room: pybcn-introductory-workshops
    talk: data-analysis-with-jupyter-notebook-pandas-and-plotly
    level: beginner
    # The page prints an "Installation" label under the requirements of
    # this one workshop, with two options. Both are kept, under
    # installation.
    requirements:
      - "a laptop + Jupyter + Pandas + Plotly + an appetite for learning!"
    installation:
      - "Option 1: Install Anaconda https://www.anaconda.com/download/"
      - "Option 2: Execute on the terminal: pip install jupyter pandas plotly"
  - start: "12:30"
    track_length: 1
    room: data-and-python-track-i
    talk: mirror-mirror-on-the-wall-introduction-to-opencv
    level: intermediate
    # The requirements end on a colon: the page then prints a conda block
    # and an apt block, which stay in the body of this page and not here.
    requirements:
      - "A laptop with a Miniconda/Anaconda distribution. You must create an environment:"
  - start: "15:00"
    track_length: 1
    room: web-track
    talk: python-and-elasticsearch
    level: intermediate
    requirements:
      - "Google account to use Google Colaboratory"
      - "Knowledge of Python"
  - start: "15:00"
    track_length: 1
    room: data-and-python-track-ii
    talk: intro-to-nosql-db-with-pymongo
    level: beginner
    # The page prints "(to be announced)" and then announces three
    # requirements under it. Both halves are what the source says.
    requirements:
      - "(to be announced)"
      - "Laptop with Internet access"
      - "Google Account with access to Google Drive (to use Google Colab)"
      - "Web browser"
  - start: "16:30"
    track_length: 1
    room: web-track
    talk: guillotina-data-framework
    level: intermediate
    requirements:
      - "Docker with elasticsearch, postgres and redis images"
      - "Python packages: guillotina, guillotina_elasticsearch, guillotina_rediscache"
      - "https://github.com/guillotinaweb/guillotina_processing repo downloaded and docker image built"
  - start: "16:30"
    track_length: 1
    room: data-and-python-track-ii
    talk: organizando-chistes-con-nlp
    level: intermediate
    requirements:
      - "Python 3"
      - "jupyter"
      - "scikit-learn"
      - "spacy (with Spanish model installed)"

# Photos published by @PyBCN on the day, from the account's own X export.
# One photo per tweet: the lunch tweet carried four, and a caption is also
# the alt text, so three repeated alts help nobody. The first of the four is
# the one kept. Nothing else of the day is left out: the export holds no
# retweet with a photo for this date, and no photograph of a credential or
# of a screen that says nothing about the day.
#
# A photo carries a talk only when its caption names that talk. The eight
# that do are the eight sessions of the programme above, each announced as
# it started. The other eight are the room, the welcome slides, and lunch.
# The one photo of this day: the group photo when the day has one, and the
# picture that says most about it when it does not. It is what the carousel
# of the home page shows, one slide per event. See
# partials/canonical_photos.html.
canonical_photo: pyday-2018/03-full-room-the-100-tickets-were-over-in-less-than-t.jpg

photos:
  date: 2018-11-24
  thread: "https://x.com/PyBCN/status/1066253610957324288"
  items:
    - file: pyday-2018/01-about-to-start-the-pydaybcn2018.jpg
      caption: "About to start the #PyDayBCN2018!"
      source: "https://x.com/PyBCN/status/1066253610957324288"
      time: "09:54"
    - file: pyday-2018/02-welcome-to-the-pydaybcn2018-lpmayos-is-explaining.jpg
      caption: "Welcome to the #PyDayBCN2018! @lpmayos is explaining our recent history"
      source: "https://x.com/PyBCN/status/1066258474206679041"
      time: "10:13"
    - file: pyday-2018/03-full-room-the-100-tickets-were-over-in-less-than-t.jpg
      caption: "Full room! The ~100 tickets were over in less than two hours #PyDayBCN2018"
      source: "https://x.com/PyBCN/status/1066259011425701888"
      time: "10:15"
    - file: pyday-2018/04-pybcn-went-from-17-to-3000-members-in-11-years-pyd.jpg
      caption: "#PyBCN went from 17 to ~3000 members in 11 years! #PyDayBCN2018"
      source: "https://x.com/PyBCN/status/1066259424862453760"
      time: "10:17"
    - file: pyday-2018/05-we-want-to-organize-more-activities-help-us.jpg
      caption: "We want to organize more activities. Help us! 😊"
      source: "https://x.com/PyBCN/status/1066259982545494016"
      time: "10:19"
    - file: pyday-2018/06-we-just-registered-an-association-seriousbusiness.jpg
      caption: "We just registered an association! #SeriousBusiness #PyDayBCN2018"
      source: "https://x.com/PyBCN/status/1066260675356499968"
      time: "10:22"
    - file: pyday-2018/07-we-re-doing-a-code-tournament-with-prizes-pydaybcn.jpg
      caption: "We're doing a code tournament, with prizes! #PyDayBCN2018"
      source: "https://x.com/PyBCN/status/1066262626718687232"
      time: "10:29"
    - file: pyday-2018/08-developing-a-small-application-with-git-ignasi-fos.jpg
      caption: "Developing a small application with git - Ignasi Fosch (@ifosch) #PyDayBCN2018"
      source: "https://x.com/PyBCN/status/1066271782657765376"
      time: "11:06"
      talk: developing-a-small-application-with-git
    - file: pyday-2018/09-introduction-to-pytorch-bartek-skorulski-pydaybcn2.jpg
      caption: "Introduction to pytorch - Bartek Skorulski #PyDayBCN2018"
      source: "https://x.com/PyBCN/status/1066272113886224386"
      time: "11:07"
      talk: introduction-to-pytorch
    - file: pyday-2018/10-data-analysis-with-jupyter-notebook-pandas-and-plo.jpg
      caption: "Data analysis with Jupyter Notebook, Pandas and Plotly - Natàlia Padilla @nataliasirera and Laura Pérez @lpmayos (@PyLadiesBCN)"
      source: "https://x.com/PyBCN/status/1066297782099722243"
      time: "12:49"
      talk: data-analysis-with-jupyter-notebook-pandas-and-plotly
    - file: pyday-2018/11-mirror-mirror-on-the-wall-who-is-the-fairest-of-th.jpg
      caption: "Mirror, mirror on the wall, who is the fairest of them all? (Introduction to OpenCV) - Ismael Benito"
      source: "https://x.com/PyBCN/status/1066297904976052224"
      time: "12:50"
      talk: mirror-mirror-on-the-wall-introduction-to-opencv
    - file: pyday-2018/12-lunch-time-pydaybcn2018.jpg
      caption: "Lunch time! #PyDayBCN2018"
      source: "https://x.com/PyBCN/status/1066316089100066816"
      time: "14:02"
    - file: pyday-2018/13-intro-to-nosql-db-with-pymongo-jordi-guix.jpg
      caption: "Intro to NoSQL DB with PyMongo - Jordi Guix"
      source: "https://x.com/PyBCN/status/1066335895740141568"
      time: "15:21"
      talk: intro-to-nosql-db-with-pymongo
    - file: pyday-2018/14-python-and-elasticsearch-artur-mindiyarov.jpg
      caption: "Python and Elasticsearch - Artur Mindiyarov"
      source: "https://x.com/PyBCN/status/1066336198262747138"
      time: "15:22"
      talk: python-and-elasticsearch
    - file: pyday-2018/15-guillotina-data-framework-ramon-navarro-bosch-bloo.jpg
      caption: "Guillotina - Data framework - Ramon Navarro Bosch (@bloodbare)"
      source: "https://x.com/PyBCN/status/1066366658460246017"
      time: "17:23"
      talk: guillotina-data-framework
    - file: pyday-2018/16-organizando-chistes-con-nlp-julio-martinez-liopic.jpg
      caption: "Organizando chistes con NLP - Julio Martínez (@liopic)"
      source: "https://x.com/PyBCN/status/1066366811829088258"
      time: "17:23"
      talk: organizando-chistes-con-nlp

# The index of sections in the sidebar, like every other edition.
layout: event

# The sponsors of the day, with the two levels the site of 2018 published,
# static/archives/pybcn.org/pyday-bcn-2018/. The page used to carry them as
# the HTML of that frozen page pasted into its body: six img tags straight
# from the archive, each with its own height written in a style attribute,
# 150px for one logo and 80px for another. They read as a row of mismatched
# pictures next to the cards of every other edition. As levels they go through partials/sponsors-grid.html and
# take the same card as the rest.
sponsor_levels:
  - sponsors_per_line: 2
    sponsors: [kiwi, onna]
    name: Platinum
  - sponsors_per_line: 4
    sponsors: [kernel-analytics, travelperk, kschool, psf]
    name: Gold
---
<p>
We are excited and glad to announce that we are organizing the second edition of PyDay in Barcelona!
</p>
<p>
PyDay Barcelona 2018 is going to take place on <b>November 24th</b> at <a href="https://goo.gl/maps/Ngk6PbN3FuB2" target="_blank">PuntMultimèdia (Espanya Industrial, Sants)</a>, full of FREE workshops, talks and contests for the local Python community and an opportunity to spread the word of its existence to other people that could be interested in Python.
</p>
<h2 class="h3">What is PyDay Barcelona 2018 about?</h2>
<p>
PyDay Barcelona 2018 has the aim of expanding the local Python community. It will be a whole day event, consisting of different level workshops focused on people with a variety of interestss levels and interests. There will be two tracks: beginner and intermediate. Each workshop will be about 80 minutes long. There will be networking opportunities amongst attendees and the sponsoring companies: coffee breaks, open spaces, etc.
</p>
<h2 class="h3">Join the event</h2>
<p>
<a href="https://www.eventbrite.es/e/entradas-pyday-barcelona-2018-50585714233?ref=ebtnebtckt" target="_blank"><img src="https://www.eventbrite.es/custombutton?eid=50585714233" alt="Eventbrite - PyDay Barcelona 2018" /></a>
</p>
<h2 class="h3">Agenda</h2>
<table>
<tbody>
<tr>
<td>09:30</td>
<td colspan="2"><b>Registration & Breakfast</b></td>
</tr>
<tr>
<td>10:00</td>
<td colspan="2">Welcome session -  Laura Pérez Mayos</td>
</tr>
<tr>
<td></td>
<td><b>PyBCN Introductory Workshops</b></td>
<td><b>Data and Python Track (I)</b></td>
</tr>
<tr>
<td>10:30</td>
<td>Developing a small application with git - Ignasi Fosch</td>
<td>Introduction to pytorch - Bartek Skorulski</td>
</tr>
<tr>
<td>12:00</td>
<td colspan="2"><b>Coffee break</b></td>
</tr>
<tr>
<td>12:30</td>
<td>Data analysis with Jupyter Notebook, Pandas and Plotly - Natàlia Padilla and Laura Pérez (PyLadiesBCN)</td>
<td>Mirror, mirror on the wall, who is the fairest of them all? (Introduction to OpenCV) - Ismael Benito</td>
</tr>
<tr>
<td>14:00</td>
<td colspan="2"><b>Lunch</b></td>
</tr>
<tr>
<td></td>
<td><b>Web Track</b></td>
<td><b>Data and Python Track (II)</b></td>
</tr>
<tr>
<td>15:00</td>
<td>Python and Elasticsearch - Artur Mindiyarov</td>
<td>Intro to NoSQL DB with PyMongo - Jordi Guix</td>
</tr>
<tr>
<td>16:30</td>
<td>Guillotina - Data framework - Ramon Navarro Bosch</td>
<td>Organizando chistes con NLP - Julio Martínez</td>
</tr>
<tr>
<td>18:00</td>
<td colspan="2">Closing session: Kahoot &amp;- Code Fights Awards</td>
</tr>
</tbody>
</table>
<h2 style="margin-top:10px">Workshops descriptions</h2>
<h3>Developing a small application with git</h3>
<p>
<b>Speaker:</b> Ignasi Fosch (@ignasi-fosch)<br/>
<b>Language:</b> English<br/>
<b>Description:</b> In this workshop, the attendees will participate in collaborative developing a small simple application using git and GitHub for the workflow. The goals of the exercise is to practice some simple concepts about contributing code.<br/>
<b>Level:</b> Beginner<br/>
<b>Requirements:</b>
</p>
<ul>
<li>Git installed</li>
<li>Some virtual environment with Python 3.6 and pytest setup</li>
<li>GitHub account created</li>
</ul>
<h3>Introduction to pytorch</h3>
<p>
<b>Speaker:</b> Bartek Skorulski<br/>
<b>Language:</b> English<br/>
<b>Description:</b> Why is it worth to know pytorch? Pytorch is a machine/deep learning library for python mainly developed by Facebooks’s AI Research Group. SInce pytorch's models are just like other python programs, it quite easy to write and debug them. Hence pytorch is great for research and experiments. Moreover, with new version 1.0, pytorch introduce "script mode" that aims to become also a tool for writing production code.
</p>
<p>
In this short workshop we give a quick and dirty introduction to pytorch. You will have an opportunity to build, train and evaluate few forward feed neural networks. We start with a simple single layer neural networks and finish with convolutional ones.<br/>
<b>Level:</b> Intermediate<br/>
<b>Requirements:</b>
</p>
<ul>
<li>We assume that you are familiar with python, have some basic knowledge about neural network.</li>
<li>You will get the best experience if you bring a notebook with access to python (I'll use version 3.6) with numpy, pandas, jupyter, pytorch, matplotlib, pillow and opencv.</li>
<li><a href="https://bartek-blog.github.io/python/pytorch/conda/2018/11/12/install-pytorch-with-conda.html" target="_blank">Guide to install Pytorch</a>.</li>
</ul>
<h3>Data analysis with Jupyter Notebook, Pandas and Plotly</h3>
<p><b>Speaker:</b> Natàlia Padilla (@nataliasirera) and Laura Pérez (@laura-perez-mayos) (@PyLadiesBCN)  <br/>
<b>Language:</b> English<br/>
<b>Description:</b> A hands-on session where you will learn how to analyze data with Jupyter Notebook, Pandas and Plotly. This will be a guided workshop, suitable for both experienced users and beginners with an interest in data analysis.<br/>
<b>Level:</b> Beginner<br/>
<b>Requirements:</b> a laptop + Jupyter + Pandas + Plotly +  an appetite for learning!<br/>
<b>Installation:</b><br/>
• Option 1: Install Anaconda <a href="https://www.anaconda.com/download/" target="_blank">anaconda.com/download</a><br/>
• Option 2: Execute on the terminal: pip install jupyter pandas plotly</p>
<h3>Mirror, mirror on the wall, who is the fairest of them all? (Introduction to OpenCV)</h3>
<p><b>Speaker:</b> Ismael Benito (@ismansiete)<br/>
<b>Language:</b> English<br/>
<b>Description:</b> An introduction to OpenCV for NumPy-Scipy-Matplotlib stack users. Starting with Anaconda pre-compiled versions, specially from Menpo project (<a href="https://anaconda.org/menpo/opencv3" target="_blank">https://anaconda.org/menpo/opencv3</a>). Covering inputs and outputs, from basic image handling, such as: 'imread', 'imshow', 'imwrite', etc; to video streams. Some basics in color treatment and thresholding techniques. Also, fundamentals of image warping and cropping. Finally, a small project to be able to find a specific object, for example a QR Code, in a scene and trimmed it.<br/>
<b>Level:</b> Intermediate<br/>
<b>Requirements:</b>
A laptop with a Miniconda/Anaconda distribution. You must create an environment:</p>
<pre><code>conda create -n opencv python=3.5 anaconda

activate opencv (Windows)
source activate opencv (Linux|Mac)

conda install -y --channel menpo matplotlib scipy numpy pandas Pillow scikit-learn imageio opencv3=3.1.0
pip install pyzbar qrcode scikit-video
</code></pre>
<p>On Linux systems you might need to install this dependencies:</p>
<pre><code>apt install -y libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
apt install -y libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
</code></pre>
<h3>Python and Elasticsearch</h3>
<p><b>Speaker:</b> Artur Mindiyarov <br/>
<b>Language:</b> English<br/>
<b>Description:</b> Elasticsearch is one of the best open-source, cross-platform, distributed and scalable search engine. In this workshop we are going to learn basics of Elasticsearch and use it to built our own search solution.<br/>
<b>Level:</b> Intermediate<br/>
<b>Requirements:</b></p>
<ul>
<li>Google account to use Google Colaboratory</li>
<li>Knowledge of Python</li>
</ul>
<h3>Intro to NoSQL DB with PyMongo</h3>
<p><b>Speaker:</b> Jordi Guix<br/>
<b>Language:</b> English<br/>
<b>Description:</b> Learn how to access and manage big data with Python. How to access to DB, basic CRUD operations (Create, Read, Update, Delete) and overview of advance operations.<br/>
Get the <a href="https://github.com/giffy" target="_blank">workshop materials</a>.</p>
<ol>
<li>Presentació   (5 min)</li>
<li>Breu introducció de:  (10 - 15 min)<ul>
<li>Bases de dades relacionals i no relacionals</li>
<li>Que es mongoDB y links de com instal·lar-lo</li>
<li>Característiques de Mongo i perquè tasques es recomanable</li>
<li>Punts forts i febles</li>
<li>Enllaços d'interes</li>
</ul>
</li>
<li>Workshop - (40 min ) (la meva intenció es fer la pràctica amb Google Colab, accedint al notebook des de Github)<ul>
<li>Instal·lació (execució del notebook) explicaré les opcions bàsiques de execució</li>
<li>PyMongo (llibreria per accedir a Mongo)<ul>
<li>Com connectar-se a la base de dades</li>
<li>Visualització de la estructura de la base de dades</li>
<li>Accions de Creacio, Lectura, Actualització i Esborrar (CRUD)</li>
<li>Consultes típiques</li>
</ul>
</li>
</ul>
</li>
<li>Cas practic (30 min)  ( Estic considerant una de 2 possibles opcions)<ul>
<li>Opció 1 :  Consultar dades sobre telefonia mòbil.  Amb Dades Obertes de la Generalitat, consultar dades i crear mapes de calor per veure concentracions de gent a Barcelona a un dia i hora determinat.</li>
<li>Opció 2 : Consulta dades sobre Bicing.  Amb Dades de l'ajuntament de Barcelona, consultar l'us del bicing.</li>
</ul>
</li>
</ol>
<p><b>Level:</b> Beginner<br/>
<b>Requirements:</b> (to be announced)</p>
<ul>
<li>Laptop with Internet access</li>
<li>Google Account with access to Google Drive (to use Google Colab)</li>
<li>Web browser</li>
</ul>
<h3>Guillotina - Data framework</h3>
<p><b>Speaker:</b> Ramon Navarro Bosch (@bloodbare)<br/>
<b>Language:</b> English<br/>
<b>Description:</b> A walkthrough from creating a data REST API with your custom model and structure to an interactive interface to consume and manage it. Security and custom rich object models to create micro-services that handles large volume information. We also will cover how to interact with it to compute models using its internal API and Jupyter.<br/>
<b>Level:</b> Intermediate<br/>
<b>Requirements:</b></p>
<ul>
<li>Docker with elasticsearch, postgres and redis images</li>
<li>Python packages: guillotina, guillotina_elasticsearch, guillotina_rediscache</li>
<li><a href="https://github.com/guillotinaweb/guillotina_processing" target="_blank">https://github.com/guillotinaweb/guillotina_processing</a> repo downloaded and docker image built</li>
</ul>
<h3>Organizando chistes con NLP</h3>
<p><b>Speaker:</b> Julio Martínez (@liopic)<br/>
<b>Language:</b> Spanish<br/>
<b>Description:</b> Haciendo un repaso global de diferentes técnicas de NLP clásicas y modernas, vamos a organizar una colección de chistes en castellano. Habrá una introducción general con slides (30 minutos) y luego una serie de ejercicios con un notebook de Jupyter.<br/>
<b>Level:</b> Intermediate<br/>
<b>Requirements:</b></p>
<ul>
<li>Python 3</li>
<li>jupyter</li>
<li>scikit-learn</li>
<li>spacy (with Spanish model installed)</li>
</ul>
