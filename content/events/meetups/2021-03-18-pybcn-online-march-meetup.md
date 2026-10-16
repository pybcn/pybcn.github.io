---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 276854837.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyBCN Online: March Meetup"
date: 2021-03-18
year: 2021
# The export records this event as ONLINE, so it had no room.
venue: "Online"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 83
meetup_url: "https://www.meetup.com/python-barcelona/events/276854837/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 276854837 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: good-to-the-last-drop-writing-robust-flask-and-django-apps
    title: "Good to the last drop: Writing robust Flask and Django apps"
    speakers: [isaac-evans]
    type: talk
    language: en
    description: "In this talk Isaac Evans from r2c will walk us through an overview of web security, common gotchas, overview of the tooling, 10 core checks for Flask / Django / others.\n\nr2c is a startup working to profoundly improve software security and reliability to safeguard human progress. We are a team of AppSec engineers and program analysis experts. Having analyzed thousands of open source projects and spoken with hundreds of Python developers, we identified common security pitfalls that are specific to Python web apps. We partnered with authors of major web frameworks to identify common \"gotchas\" and create a set of best practices for building robust Python web apps. The talk will include:\n- Brief overview of common security problems (OWASP Top 10)\n- Common gotchas for Flask and Django\n- Tools for robust Python backend development\n- Q&A session\n\nIsaac is the leader of r2c, a small startup working on giving security tools directly to developers. Previously, he conducted research into binary exploitation bypasses for techniques like control-flow integrity and novel hardware defenses on new architectures like RISC-V as a researcher at the US Defense Department under a SFS program and at MIT Lincoln Laboratory. Isaac received his BS/MS degrees in EECS from MIT. Other interests include next-generation programming languages, secure-by-design frameworks, software-defined radio, and the intersection of cryptography and public policy."
---
