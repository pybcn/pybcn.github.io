---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 227336587.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python December Meetup"
date: 2015-12-17
year: 2015
venue: "Skyscanner"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 55
meetup_url: "https://www.meetup.com/python-barcelona/events/227336587/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 227336587 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: functional-programming
    title: "Functional programming"
    speakers: [guillermo-blasco-jimenez]
    type: talk
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=TLuqx4cwGPQ"
  - id: ipython-parallel
    title: "IPython parallel"
    speakers: [jordi-deu-pons]
    type: talk
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=RQc7KL-ne3A"
  - id: python-for-porn
    title: "Python for porn"
    speakers: [gabriel-gavilan]
    type: talk
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=pTFM5-ur8e8"
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/677552945223831552"
  items:
    - file: 2015-12-17-python-december-meetup/01-functional-programming-by-guillermo-blasco-theblac.webp
      caption: "Functional programming, by Guillermo Blasco (@theblackboxio) #pybcn"
      source: "https://x.com/PyBCN/status/677552945223831552"
      time: "19:16"
      talk: functional-programming
    - file: 2015-12-17-python-december-meetup/02-ipython-parallel-by-jordi-deu-pons-elbioc-pybcn.webp
      caption: "IPython parallel, by Jordi Deu-Pons (@elbioc) #pybcn"
      source: "https://x.com/PyBCN/status/677563742884884484"
      time: "19:59"
      talk: ipython-parallel
    - file: 2015-12-17-python-december-meetup/01-python-for-porn-by-gabriel-gavilan-gabriicom-pybcn.webp
      caption: "Python for porn, by Gabriel Gavilan (@gabriicom) #pybcn"
      source: "https://x.com/PyBCN/status/677574110046789632"
      time: "20:40"
      talk: python-for-porn

---
