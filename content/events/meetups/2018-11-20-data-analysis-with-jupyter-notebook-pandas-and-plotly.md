---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 256369543.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Data analysis with Jupyter Notebook, Pandas and Plotly"
date: 2018-11-20
year: 2018
venue: "Skyscanner's offices"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 33
meetup_url: "https://www.meetup.com/pyladies-bcn/events/256369543/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 256369543 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: data-analysis-with-jupyter-notebook-pandas-and-plotly
    title: "Data analysis with Jupyter Notebook, Pandas and Plotly"
    type: workshop
    description: "Join us and learn how to analyze data with Jupyter Notebook and Pandas, and how to do data visualization with Plotly. We will use the Tarjetas Black dataset, containing data about the expenses of the black cards users. A fraud case of the spanish banks Caja Madrid and Bankia. Do you wanna know who used his/her card in McDonalds? Who did the biggest expense? Who was a usual user and who just used it for special occasions? Join us and learn how to analyze data! This will be a guided workshop, suitable for both experienced users and beginners with an interest in data analysis. All you need is a laptop with Python and an appetite for learning!"
---
