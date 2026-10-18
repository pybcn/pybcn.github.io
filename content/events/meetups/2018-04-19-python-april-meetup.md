---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 249666487.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python April Meetup"
date: 2018-04-19
year: 2018
venue: "Skyscanner"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 57
meetup_url: "https://www.meetup.com/python-barcelona/events/249666487/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 249666487 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: ttn-3-python
    title: "TTN <3 Python"
    speakers: [xose-perez]
    type: talk
    duration_minutes: 45
    description: "Des de TTNCat estem treballant per impulsar una xarxa de telemetria oberta, lliure i neutral. Volem donar a conèixer la tecnologia LoRa/LoRaWan amb la intenció de generar casos d'ús a la ciutat. És part d'un pilot que també inclou el desplegament de 15 gateways TTN a Barcelona i la realització de 2 hackatons. Existeixen solucions comercials i DIY que permeten programar dispositius IoT amb MicroPython i connectar-los a la xarxa TTN. La intenció de la xerrada serà explicar una mica què és TTN/LoRa/LoRaWan, veure algun exemple, algun hardware i convidar qui vulgui a unir-se a la comunitat."
  - id: high-altitude-python
    title: "High Altitude Python"
    speakers: [juampe-lopez]
    type: talk
    language: en
    duration_minutes: 30
    description: "We visited the stratosphere with a big helium-filled balloon and a long string of capsules that were ready to do some citizen science. The Koroliov 2 capsule featured a Raspberry Pi Zero running Linux and some sweet Python scripts that made the job easier."
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/987032822899757056"
  items:
    - file: 2018-04-19-python-april-meetup/04-everything-is-ready-for-today-s-meetup.webp
      caption: "Everything is ready for today's meetup!"
      source: "https://x.com/PyBCN/status/987006834979598336"
      time: "18:35"
    - file: 2018-04-19-python-april-meetup/05-ttn-3-python-by-xose-perez-xoseperez-pybcn.webp
      caption: "\"TTN <3 Python\" by Xose Pérez @xoseperez #pybcn"
      source: "https://x.com/PyBCN/status/987014949636632578"
      time: "19:07"
      talk: ttn-3-python
    - file: 2018-04-19-python-april-meetup/06-coverage-of-lora-networks-in-barcelona-europe-chec.webp
      caption: "Coverage of LoRa networks in Barcelona & Europe. Check https://ttnmapper.org"
      source: "https://x.com/PyBCN/status/987020397651595267"
      time: "19:29"
    - file: 2018-04-19-python-april-meetup/01-high-altitude-python-to-the-stratosphere-and-back.webp
      caption: "\"High Altitude Python: to the stratosphere and back again\" by Juampe López (@jotape) #pybcn"
      source: "https://x.com/PyBCN/status/987032822899757056"
      time: "20:18"
      talk: high-altitude-python
    - file: 2018-04-19-python-april-meetup/02-the-traffic-controllers-tell-the-planes-that-there.webp
      caption: "\"The traffic controllers tell the planes that there are some nerds playing with balloons\" - Juampe"
      source: "https://x.com/PyBCN/status/987034514177318913"
      time: "20:25"
    - file: 2018-04-19-python-april-meetup/03-linux-and-python-are-a-safe-bet-for-embedded-proje.webp
      caption: "\"Linux and Python are a safe bet for embedded projects\""
      source: "https://x.com/PyBCN/status/987040626628849664"
      time: "20:49"
---
