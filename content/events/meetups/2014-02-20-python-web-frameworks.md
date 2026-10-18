---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 159792902.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Web Frameworks"
date: 2014-02-20
year: 2014
venue: "Parc de Recerca Biomèdica de Barcelona (PRBB)"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 78
meetup_url: "https://www.meetup.com/python-barcelona/events/159792902/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 159792902 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: pyramid-python-webframework
    title: "Pyramid Python WebFramework"
    speakers: [ramon-navarro-bosch]
    type: talk
  - id: simple-webapps-with-nginx-uwsgi-emperor-bottle
    title: "Simple webapps with nginx + uWSGI emperor + Bottle"
    speakers: [jordi-soucheiron]
    type: talk
  - id: rapid-web-development-with-web2py
    title: "Rapid web development with Web2py"
    speakers: [giorgio-zoppi]
    type: talk
  - id: pybcn-org-website-powered-by-nikola
    title: "Pybcn.org website powered by Nikola"
    speakers: [areski-belaid]
    type: talk
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/436564028190904320"
  items:
    - file: 2014-02-20-python-web-frameworks/01-pyramid-python-webframework-by-ramon-navarro-blood.webp
      caption: "Pyramid Python WebFramework, by Ramon Navarro (@bloodbare) #pybcn"
      source: "https://x.com/PyBCN/status/436564028190904320"
      time: "19:12"
      talk: pyramid-python-webframework
    - file: 2014-02-20-python-web-frameworks/02-simple-webapps-with-nginx-uwsgi-emperor-bottle-by.webp
      caption: "Simple webapps with nginx + uWSGI emperor + Bottle, by Jordi Soucheiron (@jordixou) #pybcn"
      source: "https://x.com/PyBCN/status/436570487955918848"
      time: "19:38"
      talk: simple-webapps-with-nginx-uwsgi-emperor-bottle
    - file: 2014-02-20-python-web-frameworks/03-rapid-web-development-with-web2py-by-giorgio-zoppi.webp
      caption: "Rapid web development with Web2py, by Giorgio Zoppi (@jo_zoppi) #pybcn"
      source: "https://x.com/PyBCN/status/436577595820630017"
      time: "20:06"
      talk: rapid-web-development-with-web2py
    - file: 2014-02-20-python-web-frameworks/04-did-you-know-that-the-http-pybcn-org-website-power.webp
      caption: "Did you know that the https://pybcn.org website powered by Nikola? by Areski Belaid (@areskib) #pybcn"
      source: "https://x.com/PyBCN/status/436581795501719552"
      time: "20:23"
      talk: pybcn-org-website-powered-by-nikola
---
