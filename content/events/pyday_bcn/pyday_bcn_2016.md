---
title: "PyDay BCN (2016)"
year: 2016
# The first day of this edition, from the Meetup export, which records it per
# event. The edition ran two days: the XXL meetup on Thursday 15 and the
# workshop day on Saturday 17, with nothing on the Friday between them.
date: 2016-09-15
# The last day of this edition. The archived site under /archives/ gives it:
# "September 17th, Saturday" on its PyDay page. The photographs agree: the ids
# of the four posts of the photos block decode (X snowflake epoch) to 19:14,
# 19:44, and 20:29 on Thursday 15, and the fourth to Friday 16 at 13:20,
# saying "See you tomorrow in our workshops!". The Friday post is the one
# outside the first day; the day it points at is the Saturday.
end_date: 2016-09-17
# The venue of this edition, from the Meetup export, which records it per event.
venue: "Universitat de Barcelona"
description: ""
menu:
  main:
    parent: 'PyDay BCN'
weight: 9

# The index of sections in the sidebar, like every other edition.
layout: event
heroBackground: /images/photos/people-pyday-2016.jpg

# The sponsors and collaborators of the edition, as the archived site under
# /archives/pybcn.org/pyday-bcn-2016/ lists them, by its own levels and in its
# own order, each resolved to a record of content/sponsors/. Five of the
# eleven had no record and were named in sponsors_text until 2026-10-14:
# Punt Multimèdia, Claranet, Schibsted Spain, AtlaSense, and MongoDB. Their
# records carry the name as the archived page writes it, the @320 logo of
# the archived page, and its site over https (bin/check-content rejects an
# http site). The hosts of Schibsted Spain and AtlaSense no longer resolve
# (measured 2026-10-14); check-content says a site that does not answer
# over https is for its owner to fix, so the link stays. The venue level
# follows the 2025 page, which lists Canòdrom among the organizers. This
# edition has no program: the archive holds none, and bin/check-content
# notes the gap.
sponsors_text: |
  The sponsors and collaborators of the first PyDay, by the levels of the archived site of the edition. Also on the archived site:

  - [The sponsorship offer of PyDay BCN 2016](/archives/pybcn.org/pyday-bcn-2016/sponsorship.html)
  - [Backend Developer at BMAT Music Innovation, a job offer of a sponsor](/archives/pybcn.org/pyday-bcn-2016/bmat-music-innovation/backend-developer.html)
sponsor_levels:
  - name: Venues
    sponsors_per_line: 3
    sponsors:
      - punt-multimedia
      - ub
  - name: Platinum
    sponsors_per_line: 2
    sponsors:
      - psf
      - claranet
  - name: Gold
    sponsors_per_line: 2
    sponsors:
      - schibsted-spain
      - bmat
  - name: Silver
    sponsors_per_line: 3
    sponsors:
      - atlasense
  - name: Collaborators
    sponsors_per_line: 3
    sponsors:
      - skyscanner
      - mongodb
  - name: Thanks to
    sponsors_per_line: 3
    sponsors:
      - pyladiesbcn
      - pythones

# Photos published by PyBCN on the day, one per post so no two share a caption,
# which is also the alt text. Imported with bin/import-x-photos, which excludes
# anything the account only shared: that copyright belongs to somebody else.
# The one photo of this day: the group photo when the day has one, and the
# picture that says most about it when it does not. It is what the carousel
# of the home page shows, one slide per event. See
# partials/canonical_photos.html.
#
# This one is the full lecture hall of the Universitat de Barcelona, facing
# the camera. It is not in the thread of @PyBCN: @PyLadiesBCN published it
# on 2016-09-15 at 17:20 UTC, "And this is happing now in Barcelona
# #PyDayBCN16 @pybcn", as the second of its two photographs,
# https://x.com/PyLadiesBCN/status/776470703289802752/photo/2. It is the
# canonical photo over people-pyday-2016.jpg, which is the cloister at
# the door. Stored at 1600px wide, the size the other chosen pictures of
# images/photos/ are kept at.
canonical_photo: group-pyday-2016.jpg

photos:
  thread: "https://x.com/PyBCN/status/776469200915337217"
  items:
    - file: pyday-2016/01-we-are-starting-with-tensorflow.jpg
      caption: "We are starting with TensorFlow"
      source: "https://x.com/PyBCN/status/776469200915337217"
      time: "19:14"
    - file: pyday-2016/02-and-we-re-in-our-second-talk-already-radinamatic-i.jpg
      caption: "And we're in our second talk already. @RadinaMatic is talking about accessibility in a Django project"
      source: "https://x.com/PyBCN/status/776476825530863617"
      time: "19:44"
    - file: pyday-2016/03-citybik-es-talk-at-pybcn-pydaybcn16-pydayes16.jpg
      caption: "Citybik.es talk at @pybcn #pydaybcn16 #pydayes16"
      source: "https://x.com/PyBCN/status/776488042647449600"
      time: "20:29"
    - file: pyday-2016/04-it-was-an-amazing-meetup-thanks-to-all-who-helped.jpg
      caption: "It was an amazing meetup. Thanks to All Who helped make it possible. See you tomorrow in our workshops! #PyDayBCN16"
      source: "https://x.com/PyBCN/status/776742531241545728"
      time: "13:20"
---

We are excited and glad to announce that we are organizing our first big event related to Python.
PyDay BCN 2016 is going to take place in Barcelona on **15 and 17 September**:
two days of **FREE** different and funny activities about Python.

We count with an incredible group of volunteers, sponsors, and contributing entities and companies.
Thanks to all them.

We really hope you'll have a great time attending to these!!
