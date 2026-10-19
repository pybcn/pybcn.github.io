---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 225921951.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python October Meetup"
date: 2015-10-22
year: 2015
venue: "Skyscanner"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 47
meetup_url: "https://www.meetup.com/python-barcelona/events/225921951/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 225921951 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: api-by-example
    title: "Api By Example"
    speakers: [carles-barrobes]
    type: talk
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=1VdEN4B2OIM"
  - id: ofxpython-embedding-python-into-c
    title: "ofxPython: embedding Python into C++"
    speakers: [carles-f-julia]
    type: talk
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=ousMvSsY0Eo"
  - id: web-crawling-with-notebook-and-selenium
    title: "Web crawling with Notebook and Selenium"
    speakers: [silvia-puglisi]
    type: talk
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=pPMTC2XG4Gc"
  - id: data-structures-beyond-dicts-and-lists
    title: "Data structures beyond dicts and lists"
    speakers: [sergi-sorribas]
    type: talk
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=Nb4mJEn04rY"
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/657245171701166080"
  items:
    - file: 2015-10-22-python-october-meetup/01-ofxpython-embedding-python-into-c-by-carles-f-juli.webp
      caption: "\"ofxPython: embedding Python into C++\", by Carles F. Julià (@chaosct) #pybcn"
      source: "https://x.com/PyBCN/status/657245171701166080"
      time: "19:20"
      talk: ofxpython-embedding-python-into-c
    - file: 2015-10-22-python-october-meetup/02-web-crawling-with-notebook-and-selenium-by-silvia.webp
      caption: "\"Web crawling with Notebook and Selenium\", by Silvia Puglisi (@nopressure) #pybcn"
      source: "https://x.com/PyBCN/status/657257370347806720"
      time: "20:09"
      talk: web-crawling-with-notebook-and-selenium
    - file: 2015-10-22-python-october-meetup/03-data-structures-beyond-dicts-and-lists-by-sergi-so.webp
      caption: "\"Data structures beyond dicts and lists\", by Sergi Sorribas #pybcn"
      source: "https://x.com/PyBCN/status/657260707470290944"
      time: "20:22"
      talk: data-structures-beyond-dicts-and-lists
    - file: 2015-10-22-python-october-meetup/01-api-by-example-by-carles-barrobes-technomilk-pybcn.webp
      caption: "\"Api By Example\", by Carles Barrobés (@technomilk) #pybcn"
      source: "https://x.com/PyBCN/status/657242234404872193"
      time: "19:08"
      talk: api-by-example

---
