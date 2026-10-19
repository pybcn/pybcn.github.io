---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 299074873.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup February: Python World Congress"
date: 2024-02-21
year: 2024
venue: "Servizurich - Technology Delivery Center"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 85
meetup_url: "https://www.meetup.com/python-barcelona/events/299074873/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 299074873 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: pytest-a-short-hike
    title: "Pytest, a short hike."
    speakers: [itxaso-txas-aizpurua]
    type: talk
    language: en
    duration_minutes: 45
    description: "Pytest is the go-to testing framework for python. In this talk, we will go through the basics of pytest to get everyone up to speed, and then delve deeper into some concepts like fixtures, mocking, profiling, parallelization, logging capture, etc."
  - id: analysis-of-the-use-and-the-discourse-of-queering-the-map
    title: "Analysis of the use and the discourse of \"Queering The Map\""
    speakers: [marta-garcia]
    type: talk
    language: en
    duration_minutes: 15
    description: "In 2017 Lucas LaRochelle created the webpage Queering The Map. Its purpose was to provide a safe space for queer people around the globe to share experiences anonymously, and link them to a physical space. The information of the page arises this question: How does race, gender, sexuality, citizenship, ability, and class affect the ways in which we relate to, move through, and create space?\n\nThis presentation aims to give some insights in the process of answering this question, respecting the anonymity of the community involved, through the analysis of the discourse of the shared experiences and its relationship with the physical space defined by each country."
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/1760369660006965534"
  items:
    - file: 2024-02-21-python-meetup-february-python-world-congress/06-thanks-servizurich-for-hosting-us.webp
      caption: "Thanks Servizurich for hosting us"
      source: "https://x.com/PyBCN/status/1760368277266612664"
      time: "19:17"
    - file: 2024-02-21-python-meetup-february-python-world-congress/01-pytest-a-short-hike-by-itxaso-aizpurua.webp
      caption: "\"Pytest, a short hike\", by Itxaso Aizpurua"
      source: "https://x.com/PyBCN/status/1760369660006965534"
      time: "19:23"
      talk: pytest-a-short-hike
    - file: 2024-02-21-python-meetup-february-python-world-congress/02-live-demo-with-cat-facts.webp
      caption: "Live demo, with cat facts 😺"
      source: "https://x.com/PyBCN/status/1760370131836776878"
      time: "19:25"
    - file: 2024-02-21-python-meetup-february-python-world-congress/03-fyi-we-re-recording-the-talks-go-check-our-youtube.webp
      caption: "FYI we're recording the talks, go check our YouTube channel later: https://www.youtube.com/c/PythonBarcelona"
      source: "https://x.com/PyBCN/status/1760373331193114667"
      time: "19:38"
    - file: 2024-02-21-python-meetup-february-python-world-congress/04-analysis-of-queering-the-map-by-marta-garcia.webp
      caption: "Analysis of \"Queering The Map\", by Marta García"
      source: "https://x.com/PyBCN/status/1760377376507056400"
      time: "19:54"
    - file: 2024-02-21-python-meetup-february-python-world-congress/05-today-s-meetup-is-surely-about-cats-if-you-also-lo.webp
      caption: "Today's meetup is surely about cats! ❤️ if you also love Ellie 🐈"
      source: "https://x.com/PyBCN/status/1760377864774471838"
      time: "19:56"
    - file: 2024-02-21-python-meetup-february-python-world-congress/07-photo.webp
      caption: "A speaker at the lectern, beside a slide of a Streamlit app: Description branches into Web and Discourse, and both run down to Analysis"
      source: "https://x.com/PyBCN/status/1760411826565623870"
      time: "22:11"
---
