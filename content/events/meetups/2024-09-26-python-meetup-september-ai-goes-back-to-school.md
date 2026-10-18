---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 303407709.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup September: AI Goes Back To School"
date: 2024-09-26
year: 2024
venue: "Codurance"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 55
meetup_url: "https://www.meetup.com/python-barcelona/events/303407709/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 303407709 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: from-text-to-actions-llms-as-the-new-software-consumers
    title: "From text to actions: LLMs as the new software consumers"
    speakers: [pol-alvarez-vecino]
    type: talk
    language: en
    duration_minutes: 30
    description: "QA bots, copilots, workflow automation - LLMs are evolving to control our software through natural language. The endgame is APIs. LLMs that can convert user intents directly into HTTP requests, like Talk2Apis does today, will have the flexibility to access any service. This creates a machine-first software economy with big implications for developers. Python examples included."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=9ASVfIPj_M8"
  - id: ragtime-an-approach-to-retrieval-augmented-generation
    title: "Ragtime: An Approach to Retrieval-Augmented Generation"
    speakers: [javier-martinez-alcantara]
    type: talk
    language: en
    duration_minutes: 30
    description: "In this session, we'll explore a pattern that has sparked significant interest in the world of natural language models (LLMs): Retrieval-Augmented Generation (RAG). We'll walk through a practical implementation, dive into its details, and share insights based on our experiences working with these methods. Whether you're a beginner or an expert, we encourage you to join-what matters most is your interest in LLMs, machine learning, and engineering, and how to leverage these technologies to bring value to your company or organization."
    links:
      - type: video
        url: "https://www.youtube.com/watch?v=h_LXliq1Wik"
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/1839346960492589226"
  items:
    - file: 2024-09-26-python-meetup-september-ai-goes-back-to-school/01-welcome-to-python-meetup-september-ai-goes-back-to.webp
      caption: "Welcome to \"Python Meetup September: AI Goes Back To School\" Thanks @codurance_ES for hosting us!"
      source: "https://x.com/PyBCN/status/1839346960492589226"
      time: "18:51"
    - file: 2024-09-26-python-meetup-september-ai-goes-back-to-school/02-ragtime-an-approach-to-retrieval-augmented-generat.webp
      caption: "\"Ragtime: An Approach to Retrieval-Augmented Generation\", by Javier Martinez Alcantara"
      source: "https://x.com/PyBCN/status/1839348035287138621"
      time: "18:55"
      talk: ragtime-an-approach-to-retrieval-augmented-generation
    - file: 2024-09-26-python-meetup-september-ai-goes-back-to-school/03-what-is-retrieval-augmented-information.webp
      caption: "What is \"Retrieval Augmented Information\"?"
      source: "https://x.com/PyBCN/status/1839349547111490044"
      time: "19:01"
    - file: 2024-09-26-python-meetup-september-ai-goes-back-to-school/04-wow-he-s-using-a-rag-to-figure-out-warhammer-rules.webp
      caption: "Wow, he's using a RAG to figure out Warhammer rules 🙌"
      source: "https://x.com/PyBCN/status/1839354553927639500"
      time: "19:21"
    - file: 2024-09-26-python-meetup-september-ai-goes-back-to-school/05-from-text-to-actions-llms-as-the-new-software-cons.webp
      caption: "\"From text to actions: LLMs as the new software consumers\", by Pol Alvarez Vecino"
      source: "https://x.com/PyBCN/status/1839359574895407158"
      time: "19:41"
      talk: from-text-to-actions-llms-as-the-new-software-consumers
    - file: 2024-09-26-python-meetup-september-ai-goes-back-to-school/06-doing-http-actions.webp
      caption: "Doing HTTP actions"
      source: "https://x.com/PyBCN/status/1839361844865384827"
      time: "19:50"
    - file: 2024-09-26-python-meetup-september-ai-goes-back-to-school/07-putting-everything-together-with-talk2apis.webp
      caption: "Putting everything together with Talk2Apis"
      source: "https://x.com/PyBCN/status/1839362903075598809"
      time: "19:54"
    - file: 2024-09-26-python-meetup-september-ai-goes-back-to-school/08-it-just-built-a-flask-app-with-html-js-frontend-in.webp
      caption: "It just built a flask app with html+js frontend in replit, awesome!"
      source: "https://x.com/PyBCN/status/1839365156167672042"
      time: "20:03"

---
