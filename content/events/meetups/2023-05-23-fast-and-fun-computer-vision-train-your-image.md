---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 293543741.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Fast and Fun Computer Vision: Train Your Image Classification Model in Minutes!"
date: 2023-05-23
year: 2023
venue: "Canòdrom - Ateneu d'Innovació Digital i Democràtica"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 17
meetup_url: "https://www.meetup.com/pyladies-bcn/events/293543741/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 293543741 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: fast-and-fun-computer-vision-train-your-image
    title: "Fast and Fun Computer Vision: Train Your Image Classification Model in Minutes!"
    speakers: [amalia-vradi]
    type: workshop
    language: en
    description: "Join us for an exciting workshop on image classification using the fastai library!\n\nIn this hands-on session, you'll learn how to train a computer vision model to classify any type of images you want. Whether you're interested in cats vs. dogs, in distinguishing different dog breeds, or any other image classification task that strikes your fancy! (it doesn't have to be related with our furry friends!) You'll see how easy it is to create your own custom model with just a few lines of code.\n\nWe'll be using free GPU instances provided by Google Colab and Kaggle, so you don't need any special hardware or software to participate. Just bring your curiosity and enthusiasm to learn! (and your laptop)"
---
