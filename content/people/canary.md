---
id: canary
name: 'Canary person "><a href="https://canary.invalid/person">canary</a><span x="'
short_bio: "Fixture for bin/check-rendered"
pybcn_position: "Canary"
draft: true
---

Fixture for `bin/check-rendered`, not a person. The name is harmless as text
and unmistakable as markup. It must reach the page as text; if a template
prints it as markup, the page carries a link to canary.invalid and the check
fails. A draft is built only with `-D`, so the deployed site never has it.
