---
# One monthly meetup, imported from data/raw/meetup/pyladies-bcn/events.json in
# the pybcn-archive export, which is not in this repository, event 246896826.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "PyLadies BCN Workshop, January 2018"
date: 2018-01-25
year: 2018
venue: "Skyscanner's offices"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 28
meetup_url: "https://www.meetup.com/pyladies-bcn/events/246896826/"
group: "PyLadies BCN"
# The talks this meetup announced, read from the description of event 246896826 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: gender-imbalance-in-science
    title: "Gender Imbalance in Science"
    type: talk
    description: "Women in Science, Technology, Engineering and Mathematics (STEM) fields remain severely underrepresented. For instance, in Spain, women represent about 15% of full (catedras) professorships. Moreover, women are judged to be less competent, receive less payment and research facilities, and are less likely to be awarded research grants compared with male scientists. The different mechanisms leading to this disparity have been investigated and more is brought to light by ongoing research. In this talk we will explain the different challenges faced by women in STEM careers, the reasons and the mechanisms through which they emerge, and changes (big and small) that we can all do to improve the current dire scenario. We will also show how gender, race, class, and sexual identity discrimination are entangled and contribute to leaving out minorities from academia."
---
