---
# YAML, like every file under content/people. The archetype used to be TOML,
# so hugo new made a file in a format the other 137 did not use.
#
# Only id and name are filled in, because bin/check-content rejects an empty
# value: a field that reads github: "" looks like a checked fact and is not.
# Uncomment the ones this person has and leave out the rest. The archetype
# used to emit all of them empty, so a new file failed the check with six
# errors before anyone had typed anything.
id: {{ .Name }}
name: {{ replace .Name "-" " " | title }}

# The file under themes/pybcn_theme/assets/images/people/. It has to be
# square; see Person photos in the README.
# photo: ""

# The role under the name on the card, such as Organizer. Do not repeat the
# group: a card under a PyBCN heading says Organizer, not PyBCN Organizer.
# pybcn_position: ""

# In the order the icons appear on the card, which is how many people have
# each. A linkedin, github or twitter URL has to start with the host of that
# site, carry no query and end without a slash; see bin/check-content.
# linkedin: ""
# github: ""
# twitter: ""
# site: ""
---

The bio goes here, in the body of the file. There is no short_bio field:
the two used to exist and nobody could tell which to fill, so they are one.
