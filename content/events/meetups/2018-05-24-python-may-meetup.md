---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 250772681.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: Python May Meetup
date: 2018-05-24
year: 2018
venue: Pasaje Montoya
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 142
meetup_url: https://www.meetup.com/python-barcelona/events/250772681/
group: PyBCN
# The talks this meetup announced, read from the description of event 250772681 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
- id: something-something-moving-data
  title: Something, something, moving data...
  speakers:
  - lukas-kubis
  type: talk
  language: en
  duration_minutes: 30
  description: The Automation branch of kiwi.com's engineering team aims at automating 100% of company's internal processes, that don't need human touch. Get a peak into how Python helps achieving this ambitious goal and how to go about building a reliable automation service.
- id: telluric-manipulacion-interactiva-de-datos-geoespaciales-en
  title: 'telluric: manipulación interactiva de datos geoespaciales en Jupyter con Python'
  type: talk
  language: es
  duration_minutes: 30
  description: 'Existen diversas bibliotecas Python para manipulación de datos geoespaciales, tanto vectores como rasters. La mayoría de estas bibliotecas proveen una interfaz de alto nivel sobre algún software geoespacial ya existente, simplificando algunas tareas y facilitando su uso. Es el caso de pyproj con PROJ.4, Fiona con el proyecto OGR, Shapely con GEOS, o rasterio con GDAL. Sin embargo, la filosofía minimalista de estos proyectos hace que determinados análisis geoespaciales aún requieran cierto trabajo manual: por ejemplo, combinando Fiona, Shapely y pyproj para leer, manipular y reproyectar datos vectoriales, o rasterio, Shapely y affine para manipular y recortar imágenes raster. Por otra parte, a la hora de acceder a fuentes de datos externas (imágenes LANDSAT, Sentinel, etc.) o interactuar con sistemas de almacenamiento en la nube (Amazon S3, Azure Cloud Storage), hace falta recurrir a herramientas de terceros, que son heterogéneas y no ofrecen una interfaz unificada. telluric es una biblioteca open source desarrollada por Satellogic en lenguaje Python para manipulación interactiva de datos geoespaciales que combina todos los proyectos anteriores para ofrecer una experiencia aún más intuitiva, pensada para ser usada en Jupyter notebook o JupyterLab. Todas las operaciones de telluric gestionan el sistema de proyección de manera automática, eliminando la necesidad de hacerlo manualmente; los objetos se muestran de manera inmediata en la interfaz web sobre un mapa interactivo, y soporta todos los formatos vector y raster en el mundo GIS. Además, telluric permite crear un repositorio centralizado de acceso a los datos, especificando diversas fuentes externas que se pueden leer de manera homogénea. En esta comunicación detallaremos cómo utilizar telluric para manipular datos geoespaciales, cómo se integra en el ecosistema Python y GIS, explicaremos cómo Satellogic utiliza telluric internamente para diferentes tareas (gestión de datos geoespaciales, análisis de cobertura para constelaciones satelitales, visualización) y comentaremos las líneas de trabajo a futuro.'
  links:
  - type: github
    url: https://github.com/satellogic/telluric/
  speakers:
  - juan-luis-cano-rodriguez
- id: building-python-friendly-scalable-reliable-business
  title: Building Python-friendly Scalable, Reliable Business Intelligence Data Platform
  speakers:
  - miki-stencl
  type: talk
  language: en
  duration_minutes: 30
  description: Today's data systems and usage of data are all about distributed ecosystems of data, systems, people - modern business intelligence departments are driving data provisioning, data preparation, and data education as a top priority with the highest automation possible. Learn how we build kiwi.com's data provisioning architecture based on python-friendly solutions from scratch to serve analytics use cases and our lessons learned.
# The photographs the association published of this day, one per post
# so no two share a caption, which is also the alt text. The posts were
# read out of the X export by the text of their thread, and imported
# with bin/import-x-photos --ids.
photos:
  thread: "https://x.com/PyBCN/status/999701938169155584"
  items:
    - file: 2018-05-24-python-may-meetup/03-starting-may-s-meetup-pybcn.webp
      caption: "Starting May's Meetup! #pybcn"
      source: "https://x.com/PyBCN/status/999700473681727489"
      time: "19:15"
    - file: 2018-05-24-python-may-meetup/01-something-something-moving-data-by-lukas-kubis-unc.webp
      caption: "\"Something, something, moving data...\" by Lukas Kubis (@uncannylukas) #pybcn"
      source: "https://x.com/PyBCN/status/999701938169155584"
      time: "19:21"
      talk: something-something-moving-data
    - file: 2018-05-24-python-may-meetup/02-telluric-manipulacion-interactiva-de-datos-geoespa.webp
      caption: "telluric: manipulación interactiva de datos geoespaciales en Jupyter con Python by Juan Luis Cano (@astrojuanlu) https://github.com/satellogic/telluric/"
      source: "https://x.com/PyBCN/status/999709118976929793"
      time: "19:50"
      talk: telluric-manipulacion-interactiva-de-datos-geoespaciales-en
    - file: 2018-05-24-python-may-meetup/04-building-python-friendly-scalable-reliable-busines.webp
      caption: "\"Building Python-friendly Scalable, Reliable Business Intelligence Platform\" by Miki Stencl (@michaelstencl) #pybcn"
      source: "https://x.com/PyBCN/status/999717244878848001"
      time: "20:22"
---
