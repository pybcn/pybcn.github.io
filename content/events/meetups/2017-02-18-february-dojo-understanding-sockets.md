---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 237121471.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "February Dojo: Understanding sockets"
date: 2017-02-18
year: 2017
venue: "Punt Multimèdia Espanya Industrial"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 21
meetup_url: "https://www.meetup.com/python-barcelona/events/237121471/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 237121471 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: understanding-sockets
    title: "Understanding sockets"
    type: workshop
    description: "A test driven session introducing the socket communication with Python. After a brief talk on Berkeley sockets, we will do some exercises with unix and internet socket using the Python interface module. The goal of this session is to achieve solid knowledge about what is a socket and how to implement both client and server sides with Python."
    links:
      - type: site
        url: "https://en.wikipedia.org/wiki/Berkeley_sockets"
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/832999756796461057"
  items:
    - file: 2017-02-18-february-dojo-understanding-sockets/01-session-about-sockets-by-jaume-mila-at-pybcn-febru.webp
      caption: "Session about sockets by Jaume Mila at @pybcn February dojo"
      source: "https://x.com/PyBCN/status/832999756796461057"
      time: "18:06"
---
