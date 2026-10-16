---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 285205950.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python April Meetup: Shorter testing feedback & aprendizaje a través de grafos"
date: 2022-04-21
year: 2022
venue: "Wojo Coworking Barcelona Poblenou - Alquiler oficinas y salas de reuniones"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 53
meetup_url: "https://www.meetup.com/python-barcelona/events/285205950/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 285205950 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: shorter-feedback-loop-by-running-impacted-tests-only
    title: "Shorter feedback loop by running impacted tests only"
    speakers: [mathieu-kniewallner]
    type: talk
    language: en
    duration_minutes: 40
    description: "At BackMarket, we have dozens of developers working on our Django monolith that holds most of our features. As we have a lot of interdependent applications, it's hard for developers to identify which part of the code their modifications will have an impact on, and it's only by running the full test suite that they can feel confident enough that they don't break anything outside of their scope. Since we have around 18K tests, they usually push code to the CI without knowing if tests will pass, making the feedback loop bad. To improve that, we used a feature of Python coverage library called Who tests what that indicates which tests ran which parts of the code. With that, developers now know which tests to run based on the code they are updating, effectively reducing the feedback loop."
  - id: aprendizaje-a-traves-de-grafos-graph-neural-networks
    title: "Aprendizaje a través de grafos: Graph Neural Networks"
    speakers: [camilo-chacon-sartori]
    type: talk
    language: es
    duration_minutes: 40
    description: "Muchos sistemas que usamos a diario se pueden modelar con grafos: redes sociales, el transporte público, los resultados que nos devuelve un motor de búsqueda, e incluso, nuestro propio lenguaje natural. ¿Qué ocurría si combináramos la flexibilidad de los grafos con técnicas de Deep Learning? Pues obtenemos: Graph Neural Networks, la capacidad de crear predicciones aprovechando la estructura de los grafos."
---
