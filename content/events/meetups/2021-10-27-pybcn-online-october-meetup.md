---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 281570632.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyBCN Online: October Meetup"
date: 2021-10-27
year: 2021
# The export records this event as ONLINE, so it had no room.
venue: "Online"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 48
meetup_url: "https://www.meetup.com/python-barcelona/events/281570632/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 281570632 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: wardley-mapping-the-python-barcelona-association
    title: "Wardley mapping the Python Barcelona Association"
    speakers: [david-arcos, ruben-berenguel, alberto-camara]
    type: panel
    language: ca
    description: "Wardley mapping is a visual technique to analyse certain \"problem spaces\", like businesses, security and others. It is very helpful in providing a share understanding of the problem and also in finding new areas to explore, issues to fix and potential wins. In our case (aside from explaining the technique for everybody!) we want to see what we can learn together about how PyBCN works, how we can make it more efficient and better for all our members."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=Ga5Wiq0swS8"
---
