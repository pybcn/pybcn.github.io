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
---
