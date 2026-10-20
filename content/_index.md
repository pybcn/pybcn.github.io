---
title: "Welcome to PyBCN"
description: "If you are in Barcelona and interested in Python, this is your page!"

# /qr/ is the address that printed QR codes point to. It sends the reader
# here today. To send the codes somewhere else, move this alias to that page:
# the codes already printed do not change.
aliases:
  - /qr/

layout: home

# The page draws its own h1, in its first block, so
# partials/hero_header.html prints none.
no_page_heading: true

meetupEvents:
  - name: PyBCN
    id: python-barcelona
  - name: PyLadies BCN
    id: pyladies-bcn

# The video of the About PyBCN block: the presentation of the Barcelona
# community at PyConES 2020, the one video of the channel that belongs to
# no event of the association, which is why no page of the archive carries
# it (data/channel_videos.yaml has the entry and the reason). The frame is
# partials/video_frame.html, which accepts a YouTube watch URL and prints
# nothing for any other. The title is the one the channel shows, and it is
# the text of the link under the player.
about_video:
  url: https://www.youtube.com/watch?v=JYCcPr4QW_k
  title: "PyLadies Barcelona & Python Barcelona - Presentación comunidad local - PyConES 2020"

---

**Python Barcelona (PyBCN)** is the Python community of Barcelona: a meetup group since 2007, and a non-profit association since 2018. We run the monthly PyBCN meetups, the PyLadies BCN workshops, the practice sessions and coding dojos, and the annual PyDay BCN. The events are free or low cost, held in Barcelona, and hosted by local companies and universities.

In this talk at PyConES 2020, PyLadies Barcelona and Python Barcelona present the local community.

[Read more about the association](/pybcn_association/information/)
