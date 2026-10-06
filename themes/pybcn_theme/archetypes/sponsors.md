---
# A sponsor renders as its logo, linked to its site, and nothing else. There
# is no page per sponsor, so these four fields are every field any template
# reads and a body below is never published.
#
# Delete any field this sponsor does not have. An empty value is the same as
# no field to Hugo, and bin/check-content rejects one.
id: {{ .Name }}
name: ""

# The file under assets/images/sponsors/. There is no logo field: the
# archetype used to declare one, and no template has ever read it.
logo_image: {{ .Name }}.png

# site, not web. The field was called web until the two names for one thing
# were merged, and only the person files were ever checked. Leave it out when
# the sponsor has no page to link to: the logo then renders without a link.
site: ""
---
