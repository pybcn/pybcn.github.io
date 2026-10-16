---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 307212919.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: 'Python Meetup April: The Spring Meetup'
date: 2025-04-30
year: 2025
venue: Cloudworks
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 45
meetup_url: https://www.meetup.com/python-barcelona/events/307212919/
group: PyBCN
# The talks this meetup announced, read from the description of event 307212919 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: why-decorators
  title: Why Decorators?
  speakers:
  - dirk-ludtke
  type: talk
  language: en
  duration_minutes: 30
  description: Python first introduced decorators way back in 2004 with version 2.4, as a powerful tool for enhancing the behavior of functions and (later on) classes all in a neat and concise way. You are probably familiar with some popular decorators like @classmethod, @app.route (Flask), @validator (Pydantic), and @tf.function (TensorFlow). While most of us happily use them, few actually create our own. Decorators are convenient, but they're not without their quirks. As I write this, I'm still a little on the fence about using them too liberally. But fear not! By the time we get to the talk, I'll share some intriguing insights, show you where decorators truly shine, and highlight a few hilarious examples of flagrant misuse.
- id: building-a-nogil-load-balancer-in-30-minutes
  title: Building a NoGIL Load Balancer in 30 minutes
  type: talk
  language: en
  duration_minutes: 30
  description: 'Load balancers are widespread nowadays because most software systems are web-centric and service oriented. However, they''re extremely complex to build, because they must be very performant and use sophisticated algorithms to route traffic. Until recently, you couldn''t use Python to build one, because even though it would make the code simpler, the GIL prevented multiple threads from executing Python at the same time.


    Now that you can, what are the practical implications in your day-to-day work?

    In this talk, we''re going to live code a load balancer in Python. This will help us understand the pros and cons of using modules such as asyncio, threading and concurrent.futures, and what changes when we remove the GIL from the way.

    Whether you''re building systems that demand concurrency (such as AI models or DevOps pipelines), or you''re just curious about how tools like gUnicorn or Starlette work under the hood, you''ll come away with practical insights on how to start off the NoGIL era on the right foot.'
  speakers:
  - alvaro-duran-barata
---
