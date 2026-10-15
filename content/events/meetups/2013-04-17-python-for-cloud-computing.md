---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 104240822.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: Python for Cloud Computing
date: 2013-04-17
year: 2013
venue: Parc de Recerca Biomèdica de Barcelona (PRBB)
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 73
meetup_url: https://www.meetup.com/python-barcelona/events/104240822/
group: PyBCN
# The talks this meetup announced, read from the description of event 104240822 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: introduction-to-aws-amazon-web-services-and-boto
  title: Introduction to AWS (Amazon Web Services) and Boto
  speakers:
  - christian-teijon
  type: talk
  description: (Christian is CTO at MindtheByte, an AWS technology partner)
  links:
  - type: site
    url: https://aws.amazon.com/
  - type: site
    url: https://boto.readthedocs.org/en/latest/
- id: scalable-pyramid-on-top-of-dynamodb-ec2-using-boto
  title: scalable Pyramid on top of DynamoDB/EC2 using Boto
  type: talk
  description: (practical example of how to use Boto)
  links:
  - type: site
    url: https://aws.amazon.com/dynamodb/
  - type: site
    url: https://aws.amazon.com/ec2/
  - type: site
    url: https://boto.readthedocs.org/en/latest/
  speakers:
  - ramon-navarro-bosch
- id: mapreduce-with-hadoop-on-amazon-web-service-using-python
  title: MapReduce with Hadoop on Amazon Web Service (using Python)
  speakers:
  - piotr-migdal
  type: talk
  links:
  - type: site
    url: https://hadoop.apache.org/
- id: hands-on-mongodb
  title: Hands on MongoDB
  speakers:
  - norberto-leite
  type: talk
  description: (Norberto is 'Senior solutions consultant' at 10gen, the company behind MongoDB). Norberto recommends bringing our laptop with MongoDB installed so we can try his examples along with him.
  links:
  - type: site
    url: https://www.mongodb.org/
- id: google-app-engine
  title: Google App Engine
  speakers:
  - michael-gradek
  type: talk
  links:
  - type: site
    url: https://cloud.google.com/products/
- id: mico-python-s-socialpoint-tool-to-manage-ec2-aws-hosts
  title: Mico, Python's SocialPoint tool to manage EC2 AWS hosts
  speakers:
  - andres-diaz
  type: talk
  description: (Andrés is senior IT at SocialPoint, the company behind Facebook's Dragon City)
---
