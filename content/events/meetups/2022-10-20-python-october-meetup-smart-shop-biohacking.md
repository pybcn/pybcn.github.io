---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 289046806.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python October Meetup: Smart Shop & Biohacking"
date: 2022-10-20
year: 2022
venue: "Ocado Technology"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 75
meetup_url: "https://www.meetup.com/python-barcelona/events/289046806/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 289046806 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: smart-shop-populate-your-basket-with-one-click
    title: "Smart Shop - Populate your basket with one click"
    speakers: [dennis-doerrich, laurent-candillier]
    type: talk
    language: en
    duration_minutes: 30
    description: "At Ocado Technology, we are on a journey to change the way the world shops, through our end-to-end Ocado Smart Platform (OSP). Our teams develop many different features that enable millions of global customers to enjoy a frictionless, hyper personalised shopping experience. One such feature is Smart Shop, which populates your basket with just one click.\nSmart Shop is capable of suggesting the items you may want to buy, based on your shopping history. However, populating the \"best\" or \"ideal\" basket of groceries for each customer could be a challenge, because:\n- The selection of items for a shopping basket is unique for each customer\n- The basket size is different for each customer\n- Customer preferences can vary over time\nIn this talk, we are going to show how we solved these challenges with Machine Learning, and how we managed to put it quickly in production, sharing our experience using scikit-learn and TensorFlow at scale, and using Python to orchestrate the ML pipelines."
  - id: biohacking-with-python
    title: "Biohacking with Python"
    speakers: [marina-moro-lopez]
    type: talk
    language: en
    duration_minutes: 30
    description: "Would you like to become the fluorescent Mr. Burns? In this talk we will go through a brief introduction to biohacking and a very short class on genetics in order to understand perfectly and carry out an experiment to edit our own DNA with CRISPR (a copy-paste biological tool) and a Python script (that will design the genetic sequences needed for this tool) to biohack certain genes and become that man. All this will allow us to see the huge potential of the synergy between genetic engineering and Python, not only for funny examples like the one mentioned before but also in the clinical field for therapy."
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/1583137255924695042"
  items:
    - file: 2022-10-20-python-october-meetup-smart-shop-biohacking/06-thanks-ocadotechnology-for-hosting-the-python-barc.webp
      caption: "Thanks @OcadoTechnology for hosting the Python Barcelona Meetup! @marc_maycas is introducing the speakers:"
      source: "https://x.com/PyBCN/status/1583136573188902914"
      time: "18:42"
    - file: 2022-10-20-python-october-meetup-smart-shop-biohacking/01-smart-shop-populate-your-basket-with-one-click-by.webp
      caption: "\"Smart Shop - Populate your basket with one click\", by Dennis Doerrich & Laurent Candillier"
      source: "https://x.com/PyBCN/status/1583137255924695042"
      time: "18:45"
      talk: smart-shop-populate-your-basket-with-one-click
    - file: 2022-10-20-python-october-meetup-smart-shop-biohacking/02-they-use-python-to-orchestrate-the-ml-pipelines.webp
      caption: "They use Python to orchestrate the ML pipelines:"
      source: "https://x.com/PyBCN/status/1583142036827688960"
      time: "19:04"
    - file: 2022-10-20-python-october-meetup-smart-shop-biohacking/03-biohacking-with-python-by-marina-moro-lopez-marina.webp
      caption: "\"Biohacking with Python\", by Marina Moro López (@marinamorolopez)"
      source: "https://x.com/PyBCN/status/1583146317240750081"
      time: "19:21"
      talk: biohacking-with-python
    - file: 2022-10-20-python-october-meetup-smart-shop-biohacking/04-nice-bottle-hello-pyladiesbcn.webp
      caption: "Nice bottle! Hello, @PyLadiesBCN! 👋"
      source: "https://x.com/PyBCN/status/1583148444197482496"
      time: "19:29"
    - file: 2022-10-20-python-october-meetup-smart-shop-biohacking/05-doing-crispr-from-python-the-full-code-is-availabl.webp
      caption: "Doing CRISPR from Python. The full code is available at @marinamorolopez's github:"
      source: "https://x.com/PyBCN/status/1583148949015523328"
      time: "19:31"
---
