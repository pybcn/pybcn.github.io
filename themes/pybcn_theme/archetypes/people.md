---
# YAML, like every file under content/people. The archetype used to be TOML,
# so hugo new made a file in a format the other 137 did not use.
#
# Delete any field this person does not have. An empty value is the same as
# no field to Hugo, and bin/check-content rejects one: a field that reads
# github: "" looks like a checked fact and is not.
id: {{ .Name }}
name: ""
photo: ""

pybcn_position: ""

# In the order the icons appear on the card, which is how many people have
# each. A linkedin, github or twitter URL has to start with the host of that
# site, carry no query and end without a slash; see bin/check-content.
linkedin: ""
github: ""
twitter: ""
site: ""
---

The bio goes here, in the body of the file. There is no short_bio field:
the two used to exist and nobody could tell which to fill, so they are one.
