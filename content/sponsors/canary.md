---
id: canary
name: 'Canary sponsor "><a href="https://canary.invalid/sponsor">canary</a><span x="'
logo_image: canary.svg
draft: true
---

Fixture for `bin/check-rendered`, not a sponsor. The name is harmless as text
and unmistakable as markup. It must reach the page as text; if a template
prints it as markup, the page carries a link to canary.invalid and the check
fails. A draft is built only with `-D`, so the deployed site never has it.
