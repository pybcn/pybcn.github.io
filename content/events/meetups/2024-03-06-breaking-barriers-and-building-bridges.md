---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 299310107.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Breaking Barriers and Building Bridges"
date: 2024-03-06
year: 2024
venue: "Adevinta Spain"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 42
meetup_url: "https://www.meetup.com/pyladies-bcn/events/299310107/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 299310107 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: masterclass-analyzing-the-gender-gap-with-data-analytics
    title: "Masterclass: Analyzing the Gender Gap with data analytics"
    speakers: [idoia-marti]
    type: talk
    language: en
    duration_minutes: 45
    description: "Many people say the gender gap in income and occupation levels is overstated all over the world, and there are some say that inequality in the labor force is a thing of the past. Is there a REAL gender gap at all? Is it stronger in some industries than in others?Let's try to answer all those questions with REAL data! We are going to work with a dataset retrieved from the U.S. Bureau of Labor Statistics, which shows the median weekly incomes for different occupations."
    links:
      - type: site
        url: "https://www.bls.gov/"
  - id: step4ward-empowering-women-in-tech
    title: "Step4ward: Empowering Women in Tech"
    speakers: [susana-vazquez]
    type: lightning
    language: es
    duration_minutes: 5
    description: "Come explore step4ward, a non-profit organization passionately crafted BY and FOR women. In just 5 minutes, learn how we're all about supporting women in the tech job market. We provide advice, build a community, and help with interview prep and early career steps. Let's break barriers and boost women in tech together!"
  - id: analysis-of-the-use-and-the-discourse-of-queering-the-map
    title: "Analysis of the use and the discourse of \"Queering The Map\""
    speakers: [marta-garcia]
    type: talk
    language: en
    duration_minutes: 15
    description: "In 2017 Lucas LaRochelle created the webpage Queering The Map. Its purpose was to provide a safe space for queer people around the globe to share experiences anonymously, and link them to a physical space. The information of the page arises this question: How does race, gender, sexuality, citizenship, ability, and class affect the ways in which we relate to, move through, and create space?\nThis presentation aims to give some insights in the process of answering this question, respecting the anonymity of the community involved, through the analysis of the discourse of the shared experiences and its relationship with the physical space defined by each country."
---
