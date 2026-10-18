---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 298506663.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup January: Happy New Year!"
date: 2024-01-24
year: 2024
venue: "Adevinta Spain"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 107
meetup_url: "https://www.meetup.com/python-barcelona/events/298506663/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 298506663 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: launch-your-own-python-library-within-the-company
    title: "Launch your own Python Library within the company"
    speakers: [julian-boronat]
    type: talk
    language: en
    duration_minutes: 30
    description: "This presentation will aim to demonstrate a straightforward method for publishing your own Python library to the JFrog Artifactory of your organization; on this opportunity, we are going to do this within Adevinta Spain by implementing the CI/CD part through Github Actions. Key topics to be covered include: 1-Monorepo vs. Multirepo, 2-Package and Versioning, 3-Repository Templates, 4-GHA Marketplace, 5-Testing and 6-Best Practices."
  - id: mastering-pdf-form-filling-with-pypdf
    title: "Mastering PDF Form-Filling with PyPDF"
    speakers: [jordi-bosch]
    type: talk
    language: es
    duration_minutes: 30
    description: "Tired about PDF paperwork? Join the PDF revolution as we see how PyPDF Python library changes how we work with PDF forms completion. We'll discover how to form-fill PDFs with a touch of Python magic. By the end, you'll be a PDF expert, eliminating manual data entry. Get ready to improve your data skills!"
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/1750224028298567970"
  items:
    - file: 2024-01-24-python-meetup-january-happy-new-year/08-welcome-to-the-python-barcelona-january-meetup-htt.webp
      caption: "Welcome to the Python Barcelona January Meetup! https://www.meetup.com/python-barcelona/events/298506663/ Thanks @AdevintaSpain for hosting us"
      source: "https://x.com/PyBCN/status/1750221307872989536"
      time: "19:17"
    - file: 2024-01-24-python-meetup-january-happy-new-year/01-launch-your-own-python-library-within-the-company.webp
      caption: "\"Launch your own Python Library within the company\", by Julian Boronat"
      source: "https://x.com/PyBCN/status/1750224028298567970"
      time: "19:28"
      talk: launch-your-own-python-library-within-the-company
    - file: 2024-01-24-python-meetup-january-happy-new-year/02-live-demo-time-julian-is-creating-a-new-python-lib.webp
      caption: "Live demo time! Julian is creating a new python library 🙌"
      source: "https://x.com/PyBCN/status/1750229232976839079"
      time: "19:49"
    - file: 2024-01-24-python-meetup-january-happy-new-year/03-and-after-a-few-minutes-it-s-done-if-you-want-to-r.webp
      caption: "And... after a few minutes, it's done! 🪄✨ If you want to reproduce, find the code here: https://github.com/boroju/backend-di--python-lib-template"
      source: "https://x.com/PyBCN/status/1750231786418786713"
      time: "19:59"
    - file: 2024-01-24-python-meetup-january-happy-new-year/04-mastering-pdf-form-filling-with-pypdf-by-jordi-bos.webp
      caption: "\"Mastering PDF Form-Filling with PyPDF\", by Jordi Bosch"
      source: "https://x.com/PyBCN/status/1750234567355592749"
      time: "20:10"
      talk: mastering-pdf-form-filling-with-pypdf
    - file: 2024-01-24-python-meetup-january-happy-new-year/05-wow-thanks-martinthoma-the-maintainer-of-pypdf.webp
      caption: "Wow, thanks @_martinthoma, the maintainer of PyPDF! 👋👋"
      source: "https://x.com/PyBCN/status/1750237454320222526"
      time: "20:21"
    - file: 2024-01-24-python-meetup-january-happy-new-year/06-today-i-learned-filigrana-watermark.webp
      caption: "Today I Learned: \"Filigrana\" = \"Watermark\""
      source: "https://x.com/PyBCN/status/1750242272493404178"
      time: "20:40"
    - file: 2024-01-24-python-meetup-january-happy-new-year/07-it-worked.webp
      caption: "It worked! 👏"
      source: "https://x.com/PyBCN/status/1750244302691737616"
      time: "20:48"
---
