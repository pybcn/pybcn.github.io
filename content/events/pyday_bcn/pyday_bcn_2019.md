---
title: "PyDay BCN (2019)"
year: 2019
# The day of this edition, from the Meetup export, which records it per event.
date: 2019-11-16
# The venue of this edition, from the Meetup export, which records it per event.
venue: "Universitat de Barcelona"
description: ""
menu:
  main:
    parent: 'PyDay BCN'
weight: 7
heroBackground: /images/photos/people-pyday-2019.jpg

# This page is on layouts/_default/event.html, like the editions from 2020
# on, so it gets the sticky index of sections down the left of the page. It
# was on layouts/_default/single.html, which renders the body and the
# gallery and nothing else, so the page had no way to jump to its own
# gallery. The index lists what this file declares: About the event, and
# Gallery. There is no Schedule entry, because the grid needs eventTimes
# and numTracks and this page carries neither (see the comment on agenda below). PyDay BCN 2016 and 2018
# are still on single.html and still have no index.
layout: event

# The sponsors of the day, with the five levels the site of 2019 published,
# static/archives/pybcn.org/pyday-bcn-2019/. The page used to carry them as
# the HTML of that frozen page pasted into its body: nineteen img tags
# straight from the archive, each with its own width written in a style
# attribute, from 350px for one logo to 70px for another, inside <center>
# tags. They read as a wall of mismatched pictures next to the cards of
# every other edition, as the page of 2018 did. As levels they go through
# partials/sponsors-grid.html and take the same card as the rest.
sponsor_levels:
  - sponsors_per_line: 2
    sponsors: [ub, psf]
    name: Venue
  - sponsors_per_line: 3
    sponsors: [upcloud, kiwi, invisiblebits, chartboost, king, qustodio]
    name: Platinum
  - sponsors_per_line: 1
    sponsors: [affectv]
    name: Coffee Sponsor
  - sponsors_per_line: 4
    sponsors: [thoughtworks, bmat, holaluz, travelperk, elastic, verse, fundacion-ci]
    name: Gold
  - sponsors_per_line: 3
    sponsors: [kschool, satellogic, blueliv]
    name: Silver

# The program of this edition, read from the printed agenda that the live
# thread on X photographed (tweet 1195637939285430272, the photo on this page).
# The Google Calendar embed that held it is gone, and the Meetup description
# never carried it, so that photograph is the source. Titles are copied from
# the sheets, typos included: the sheets print "Decoradores en evolucion" and
# "Un caso practico" without their accents.
#
# The sheets name no speaker at all. The four that are named here come from the
# thread, which announced them. The other eleven are unknown, and that is what
# the source says. The caption of one photo credits the handle @bustawin for
# SQLAlchemy from 0 to proficient, but a handle is not a name, so that talk
# carries no speaker until somebody says who it is.
talks:
  # The two keynotes. The printed sheets announce the opening one in all three
  # tracks and give it no title, and the closing one is not on them at all: the
  # thread tweeted it at 20:03, well after the 18:30 the sheets end at. Both
  # titles come from the thread and not from a printed source, which is
  # why they are plain and not quoted.
  - id: opening-keynote
    title: "Opening keynote"
    speakers: [laura-perez-mayos]
    type: keynote
    source: "https://x.com/PyBCN/status/1195623896537554944"
  - id: closing-keynote
    title: "Closing keynote"
    speakers: [david-arcos]
    type: keynote
    source: "https://x.com/PyBCN/status/1195779452829097984"
  - id: arquitectura-limpia-para-microservicios
    title: "Arquitectura limpia para microservicios: Un caso practico"
    duration_minutes: 90
    language: es
    type: workshop
    source: "https://x.com/PyBCN/status/1195638580137406464"
  - id: fast-bayesian-ab-and-multivariate-testing
    title: "Fast Bayesian A/B and multivariate testing"
    duration_minutes: 45
    language: en
    type: talk
  - id: tell-me-why
    title: "Tell me Why"
    duration_minutes: 90
    language: en
    type: workshop
  - id: tips-for-optimize-django-database-queries
    title: "Tips for optimize Django database queries"
    duration_minutes: 90
    language: en
    type: workshop
  - id: deep-learning-for-image-classification-using-tensorflow
    title: "Deep Learning for Image Classification using TensorFlow"
    duration_minutes: 75
    language: en
    type: workshop
    source: "https://x.com/PyBCN/status/1195638268727042051"
  - id: decoradores-en-evolucion
    title: "Decoradores en evolucion"
    duration_minutes: 60
    language: es
    type: workshop
    source: "https://x.com/PyBCN/status/1195662968203153410"
  - id: the-magic-of-pyspark
    title: "The magic of PySpark"
    duration_minutes: 105
    language: en
    type: workshop
  - id: sqlalchemy-from-0-to-proficient
    title: "SQLAlchemy from 0 to proficient"
    duration_minutes: 90
    language: en
    type: workshop
    source: "https://x.com/PyBCN/status/1195729652893077504"
  - id: migracode
    title: "Migracode: the first code school for youth migrants and refugees in Barcelona"
    duration_minutes: 30
    language: en
    type: talk
  - id: keep-your-repo-clean
    title: "Keep your repo clean"
    speakers: [hector-canto]
    duration_minutes: 45
    language: es
    type: talk
    source: "https://x.com/PyBCN/status/1195639258599563264"
  - id: refactoring-a-web-application-with-python
    title: "Refactoring a Web Application with Python"
    duration_minutes: 90
    language: en
    type: workshop
    source: "https://x.com/PyBCN/status/1195663218259243010"
  - id: building-interactive-data-visualizations-with-plotly-and-dash
    title: "Building Interactive Data Visualizations with Plotly and Dash"
    speakers: [anna-fedotova]
    duration_minutes: 90
    language: en
    type: workshop
    source: "https://x.com/PyBCN/status/1195729247731630080"
  - id: quick-data-exploration-with-jupyter-and-ipywidgets
    title: "Quick data exploration with Jupyter and ipywidgets"
    duration_minutes: 90
    language: en
    type: workshop
    source: "https://x.com/PyBCN/status/1195729783734202368"

# The rooms the sheets name. Three parallel tracks, one level each.
rooms:
  - id: b6
    name: "B6"
    track: Advanced
  - id: b5
    name: "B5"
    track: Intermediate
  - id: b3
    name: "B-3"
    track: Beginner

# The grid, one row per session of the day, in the order the sheets print it:
# by time, and then by the track order of rooms above. A slot is when and
# where; the talk it names is what was said. The two were one list until this
# edition was converted, and the eight later editions already carry them
# apart.
#
# level is the one level the sheets give a session, which is the level of its
# track. It is not the python_level and topic_level pair that the editions
# from 2020 on carry, because the source names one level and not two.
#
# No slot carries a track_length other than 1: the three tracks ran in
# parallel all day and no session spanned two of them.
#
# The hand-drawn arrow on the sheet swapped the two B5 slots, 10:00 and
# 16:30. The comment that records it is on both of them, where the time it
# corrects now lives.
#
# This page declares no eventTimes, so no grid is rendered from this list.
# The program a reader sees is the Google Calendar embed in the body, which
# is what the association published. The list is here because a photo of the
# gallery joins to a talk by id, and because the nine photo days still to
# import need one shape for a program and not two.
agenda:
  # The sheets print the opening keynote in all three tracks at 9:30, so it is
  # one slot across the grid. The closing keynote has no slot: it is not on
  # them, and the thread gives the time of the tweet, not of the session.
  - start: "9:30"
    track_length: 3
    room: b6
    talk: opening-keynote
  - start: "10:00"
    track_length: 1
    room: b6
    talk: arquitectura-limpia-para-microservicios
    level: advanced
  - start: "10:00"
    track_length: 1
    room: b5
    talk: deep-learning-for-image-classification-using-tensorflow
    # The printed sheet has these two the other way round, with a hand-drawn
    # arrow swapping them. The thread confirms the arrow, not the print.
    level: intermediate
  - start: "10:00"
    track_length: 1
    room: b3
    talk: migracode
    level: beginner
  - start: "10:30"
    track_length: 1
    room: b3
    talk: keep-your-repo-clean
    level: beginner
  - start: "12:00"
    track_length: 1
    room: b6
    talk: fast-bayesian-ab-and-multivariate-testing
    level: advanced
  - start: "12:00"
    track_length: 1
    room: b5
    talk: decoradores-en-evolucion
    level: intermediate
  - start: "12:00"
    track_length: 1
    room: b3
    talk: refactoring-a-web-application-with-python
    level: beginner
  - start: "14:30"
    track_length: 1
    room: b6
    talk: tell-me-why
    level: advanced
  - start: "14:30"
    track_length: 1
    room: b5
    talk: the-magic-of-pyspark
    level: intermediate
  - start: "14:30"
    track_length: 1
    room: b3
    talk: building-interactive-data-visualizations-with-plotly-and-dash
    level: beginner
  - start: "16:30"
    track_length: 1
    room: b6
    talk: tips-for-optimize-django-database-queries
    level: advanced
  - start: "16:30"
    track_length: 1
    room: b5
    talk: sqlalchemy-from-0-to-proficient
    # The printed sheet has these two the other way round, with a hand-drawn
    # arrow swapping them. The thread confirms the arrow, not the print.
    level: intermediate
  - start: "16:30"
    track_length: 1
    room: b3
    talk: quick-data-exploration-with-jupyter-and-ipywidgets
    level: beginner

# Photos published by PyBCN on the day. One per tweet, so no two share a
# caption, and the caption is also the alt text. PyBCN organizers took them.
# The page credits the account that published them, which is the part the
# post itself proves.
# The one photo of this day: the group photo when the day has one, and the
# picture that says most about it when it does not. It is what the carousel
# of the home page shows, one slide per event. See
# partials/canonical_photos.html.
canonical_photo: pyday-2019/21-finally-our-gratitude-to-the-python-barcelona-comm.jpg

photos:
  thread: "https://x.com/PyBCN/status/1195623896537554944"
  date: 2019-11-16
  album: "https://drive.google.com/drive/folders/1kODXtBARnTbZmQwVW1Qx2EvBCDSqhZjX?usp=sharing"
  items:
    - file: pyday-2019/01-the-pydaybcn-just-started-keynote-by-our-president.jpg
      caption: "The #PyDayBCN just started! Keynote, by our President @lpmayos. This is what we do!"
      source: "https://x.com/PyBCN/status/1195623896537554944"
      time: "09:45"
      talk: opening-keynote
    - file: pyday-2019/03-python-barcelona-is-doing-lots-of-events.jpg
      caption: "Python Barcelona is doing lots of events!"
      source: "https://x.com/PyBCN/status/1195624998209232896"
      time: "09:49"
    - file: pyday-2019/04-this-is-us-the-social-media-guy.jpg
      caption: "This is us! - the social media guy"
      source: "https://x.com/PyBCN/status/1195625223665704960"
      time: "09:50"
    - file: pyday-2019/05-help-python-barcelona-send-a-proposal-become-a-mem.jpg
      caption: "Help Python Barcelona! Send a proposal, become a member 😊"
      source: "https://x.com/PyBCN/status/1195625991529541633"
      time: "09:53"
    - file: pyday-2019/06-introducing-the-djangogirlsbcn-event-by-ellaquimic.jpg
      caption: "Introducing the #DjangoGirlsBCN event, by @EllaQuimica"
      source: "https://x.com/PyBCN/status/1195628735539625984"
      time: "10:04"
    - file: pyday-2019/07-me-oh-no-a-g-balloon-is-broken-djangogirlsbcn-hold.jpg
      caption: "- me: oh no, a \"G\" balloon is broken! - @DjangoGirlsBCN: hold my beer... #quickhack"
      source: "https://x.com/PyBCN/status/1195630182075420674"
      time: "10:10"
    - file: pyday-2019/08-this-is-the-agenda-for-our-three-workshop-track.jpg
      caption: "This is the agenda for our three workshop track:"
      source: "https://x.com/PyBCN/status/1195637939285430272"
      time: "10:41"
    - file: pyday-2019/09-deep-learning-for-image-classification-using-tenso.jpg
      caption: "Deep Learning for Image Classification using TensorFlow"
      source: "https://x.com/PyBCN/status/1195638268727042051"
      time: "10:42"
      talk: deep-learning-for-image-classification-using-tensorflow
    - file: pyday-2019/10-arquitectura-limpia-para-microservicios-un-caso-pr.jpg
      caption: "Arquitectura limpia para microservicios: Un caso practico"
      source: "https://x.com/PyBCN/status/1195638580137406464"
      time: "10:43"
      talk: arquitectura-limpia-para-microservicios
    - file: pyday-2019/11-keep-your-repo-clean-by-hectorcanto-dev-from-bluel.jpg
      caption: "\"Keep your repo clean\", by @hectorcanto_dev from @blueliv"
      source: "https://x.com/PyBCN/status/1195639258599563264"
      time: "10:46"
      talk: keep-your-repo-clean
    - file: pyday-2019/12-great-materials-on-our-djangogirls-track.jpg
      caption: "Great materials on our #DjangoGirls track:"
      source: "https://x.com/PyBCN/status/1195645166138228737"
      time: "11:09"
    - file: pyday-2019/13-decoradores-en-evolucion.jpg
      caption: "\"Decoradores en evolución\""
      source: "https://x.com/PyBCN/status/1195662968203153410"
      time: "12:20"
      talk: decoradores-en-evolucion
    - file: pyday-2019/14-refactoring-a-web-application-with-python.jpg
      caption: "\"Refactoring a Web Application with Python\""
      source: "https://x.com/PyBCN/status/1195663218259243010"
      time: "12:21"
      talk: refactoring-a-web-application-with-python
    - file: pyday-2019/15-thanks-codekiwicom-for-bringing-churros-con-chocol.jpg
      caption: "Thanks @codekiwicom for bringing churros con chocolate, and hot wine! 👏👏👏 #PyDay"
      source: "https://x.com/PyBCN/status/1195680425752051712"
      time: "13:30"
    - file: pyday-2019/21-finally-our-gratitude-to-the-python-barcelona-comm.jpg
      caption: "Finally, our gratitude to the Python Barcelona community! @PyBCN, @PyLadiesBCN, @DjangoGirlsBCN, and all our awesome organizers, coaches, speakers, volunteers and assistants! 👏👏👏"
      source: "https://x.com/PyBCN/status/1197534799130497024"
      time: "16:18"
    - file: pyday-2019/16-building-interactive-data-visualizations-with-plot.jpg
      caption: "\"Building Interactive Data Visualizations with Plotly and Dash\" by Anna Fedotova"
      source: "https://x.com/PyBCN/status/1195729247731630080"
      time: "16:44"
      talk: building-interactive-data-visualizations-with-plotly-and-dash
    - file: pyday-2019/17-sqlalchemy-from-0-to-proficient-by-bustawin.jpg
      caption: "\"SQLAlchemy from 0 to proficient\" by @bustawin"
      source: "https://x.com/PyBCN/status/1195729652893077504"
      time: "16:45"
      talk: sqlalchemy-from-0-to-proficient
    - file: pyday-2019/18-quick-data-exploration-with-jupyter-and-ipywidgets.jpg
      caption: "\"Quick data exploration with Jupyter and ipywidgets\""
      source: "https://x.com/PyBCN/status/1195729783734202368"
      time: "16:46"
      talk: quick-data-exploration-with-jupyter-and-ipywidgets
    - file: pyday-2019/19-thanks-codekiwicom-for-the-quiz-and-the-prizes-pyd.jpg
      caption: "Thanks @codekiwicom for the quiz and the prizes! #PyDayBCN"
      source: "https://x.com/PyBCN/status/1195777282914304000"
      time: "19:54"
    - file: pyday-2019/20-great-ending-keynote-from-dzpm-hey-is-that-a-napki.jpg
      caption: "Great ending keynote from @DZPM! (Hey, is that a napkin?)"
      source: "https://x.com/PyBCN/status/1195779452829097984"
      time: "20:03"
      talk: closing-keynote
    - file: pyday_bcn_2019/22-thanks-to-all-the-sponsors-speakers-volunteers-coa.webp
      caption: "Thanks to all the sponsors, speakers, volunteers, coaches, organizers and assistants! Without you, the #PyDayBCN would not be possible 👏 Remember to send proposals: https://pybcn.org/call-for-proposals/ And become a member: https://pybcn.org/association/become-a-member/ And follow @PyBCN! Thanks 👏👏"
      source: "https://x.com/PyBCN/status/1195780662810304512"
      time: "20:08"
---
<p><img src="/archives/pybcn.org/pyday-bcn-2019/Foto%20de%20grup%20-%20small.jpg" style="width:100%" alt="The group photograph of PyDay BCN 2019, in the cloister of the Universitat de Barcelona" /></p>
<h2>Archived content</h2>
<p>We are excited to announce that we are organizing the third edition of PyDay in Barcelona!</p>
<p>PyDay Barcelona 2019 is going to take place on <strong>November 16th</strong> <em>fgin Universitat de Barcelona</em>, a full day full of FREE python-related activities for the Python community. Over the last two editions, PyDay has become a great opportunity to share our love for Python and engage users, companies and newcomers into it!</p>
<p>We count with an incredible group of volunteers and contributing entities but we still need your help to make this event not only possible but awesome! For information about the past editions, please visit <a href="/events/pyday_bcn/pyday_bcn_2016">PyDay 2016</a> (you can also see some photos) and <a href="/events/pyday_bcn/pyday_bcn_2018">PyDay 2018</a> web pages.</p>
<h2>What is PyDay Barcelona 2019 about?</h2>
<h3>Hands-on workshops</h3>
<p>We are planning to have different thematic tracks --i.e. data science, web development, security, beginners-- with hands-on guided workshops of about 2 hours in which participants will learn how to use different libraries, tools and techniques.</p>
<h3>Django Girls workshop</h3>
<p>This year we are planning to host a parallel DjangoGirls workshop!</p>
<p>A Django Girls event is a one-day workshop with an installation party the evening before or remotely via Google Hangout/Skype. During the whole day participants work in small groups (3 attendees + 1 coach) and go through the tutorial to successfully create a blog application and deploy it to the internet.</p>
<p>Django Girls events are always non-profit and free for participants. We do not pay coaches, speakers or organizers. Attendees don't need any previous knowledge about programming and there is no age limitation. All the attendees need is a laptop and some curiosity.</p>
<h3>Other activities</h3>
<p>Hackathons, quizzes, contests, lightning talks… We want PyDay BCN 2019 to be as enlightening and fun as possible!</p>
<h2>Agenda</h2>
{{< google-embed kind="calendar" height="600"
    title="Agenda of PyDay BCN 2019"
    src="https://calendar.google.com/calendar/embed?height=600&wkst=1&bgcolor=%23ffffff&ctz=Europe%2FMadrid&mode=AGENDA&showNav=0&showDate=0&showTabs=0&showCalendars=0&showTz=1&src=eTEway53c19pdWMxYW00c2Y5c3V2NGtqcjV0YXZuYzEzY0Bncm91cC5jYWxlbmRhci5nb29nbGUuY29t&color=%23F09300&title=Agenda%20del%20evento&showTitle=0" >}}
