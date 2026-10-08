---
# A sponsor renders as its logo, linked to its site, and nothing else. There
# is no page per sponsor, so these four fields are every field any template
# reads and a body below is never published.
#
# Only id and name are filled in, because bin/check-content rejects an empty
# value and any field that is not one of the four. Uncomment what applies.
# The archetype used to emit every field empty, so a new file failed the
# check before anyone had typed anything.
id: {{ .Name }}
name: {{ replace .Name "-" " " | title }}

# The file under themes/pybcn_theme/assets/images/sponsors/. There is no logo
# field: the archetype used to declare one, and no template has ever read it.
# logo_image: {{ .Name }}.png

# site, not web. The field was called web until the two names for one thing
# were merged, and only the person files were ever checked. Leave it out when
# the sponsor has no page to link to: the logo then renders without a link.
# site: ""
---
