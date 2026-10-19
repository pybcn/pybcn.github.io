---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 296203267.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python September Meetup: Back to School!"
date: 2023-09-28
year: 2023
venue: "Facultat de Matemàtiques i Informàtica - UB"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 90
meetup_url: "https://www.meetup.com/python-barcelona/events/296203267/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 296203267 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: the-two-language-problem-in-vectorized-python-expressions
    title: "The two language problem in vectorized python expressions"
    speakers: [david-buchaca]
    type: talk
    language: en
    duration_minutes: 30
    description: "There is a bit of a misleading conception that in order to make python code fast the best approach is to handle code in vectorized expressions. While this can be true in some cases, especially when your code can be mapped to an exact function call of numpy/scipy it is a dangerous path if followed without critical thinking. Algorithms can increase the complexity when vectorizing code. This can happen without the user being aware of it, since vectorized code is using other libraries. In this talk we will iterate over examples on how to think about devectorized expressions using cython and discuss the two language problem that arises in such a setting."
  - id: ai-image-generative-algorithm-in-fashion-design
    title: "AI image generative algorithm in fashion design"
    speakers: [lucas-pastur]
    type: talk
    language: en
    duration_minutes: 45
    description: "This presentation will explore the application of image generative algorithms in fashion design with a particular focus on their most valuable use cases and implementation at Mango. We will discuss the innovative ways in which these algorithms are transforming the fashion industry by generating diverse design elements such as photographic prints, vector and cartoon illustrations, fabric patterns, and textures. Additionally, we will delve into the art of prompt engineering, providing valuable insights into the creative process behind generating useful images. The presentation will shed light on the future of fashion design and the growing influence of artificial intelligence in this dynamic industry."
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/1707446292253745529"
  items:
    - file: 2023-09-28-python-september-meetup-back-to-school/06-during-the-intro-we-just-announced-a-new-pydaybcn.webp
      caption: "During the intro, we just announced a new PyDayBCN. Looking for speakers, sponsors, etc. Will keep you updated!"
      source: "https://x.com/PyBCN/status/1707445980931461366"
      time: "19:23"
    - file: 2023-09-28-python-september-meetup-back-to-school/01-the-two-language-problem-in-vectorized-python-expr.webp
      caption: "\"The two language problem in vectorized python expressions\", by David Buchaca"
      source: "https://x.com/PyBCN/status/1707446292253745529"
      time: "19:24"
      talk: the-two-language-problem-in-vectorized-python-expressions
    - file: 2023-09-28-python-september-meetup-back-to-school/02-this-is-the-way.webp
      caption: "This is the way"
      source: "https://x.com/PyBCN/status/1707452439895421056"
      time: "19:49"
    - file: 2023-09-28-python-september-meetup-back-to-school/03-ai-image-generative-algorithm-in-fashion-design-by.webp
      caption: "\"AI image generative algorithm in fashion design\", by Lucas Pastur"
      source: "https://x.com/PyBCN/status/1707454034368454912"
      time: "19:55"
      talk: ai-image-generative-algorithm-in-fashion-design
    - file: 2023-09-28-python-september-meetup-back-to-school/04-many-use-cases-in-fashion-design.webp
      caption: "Many use cases in fashion design:"
      source: "https://x.com/PyBCN/status/1707456945139880437"
      time: "20:07"
    - file: 2023-09-28-python-september-meetup-back-to-school/05-we-ve-seen-some-good-tips-on-prompt-engineering.webp
      caption: "We've seen some good tips on prompt engineering"
      source: "https://x.com/PyBCN/status/1707461285250580920"
      time: "20:24"
---
