---
# Delete any field this sponsor does not have. An empty value is the same as
# no field to Hugo, and bin/check-content rejects one.
id: {{ .Name }}
name: ""

# The file under assets/images/sponsors/. There is no logo field: the
# archetype used to declare one, and no template has ever read it.
logo_image: {{ .Name }}.png

# site, not web. The field was called web until the two names for one thing
# were merged, and only the person files were ever checked.
site: ""
linkedin: ""
twitter: ""
---
