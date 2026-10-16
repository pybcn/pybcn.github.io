---
# One monthly meetup, imported from data/raw/meetup/python-barcelona/events.json in
# the pybcn-archive export, which is not in this repository, event 311354313.
# bin/import-meetups writes this file from that record: a correction goes
# to the export or to the script, never here. The Meetup description is
# the logistics of signing up and is not published, and the talks it
# announces arrive separately. See content/events/meetups/_index.md.
title: "Python Meetup October: MCPs & Access Control Systems for AI"
date: 2025-10-23
year: 2025
venue: "Codurance"
# Who said yes on Meetup, not who came: attendedCount is zero on almost
# every record, so this is the only figure the export gives. It names
# nobody, which is what makes it publishable.
attendance: 63
meetup_url: "https://www.meetup.com/python-barcelona/events/311354313/"
group: "PyBCN"
# The talks this meetup announced, read from the description of event 311354313 in
# the pybcn-archive export by a model and compared field by field against
# that description by bin/check-extraction. bin/import-talks writes this
# block: a correction goes to the extraction or to the script, never here.
# speakers holds the content/people/ record the announced name resolves to,
# by the same name, ignoring accents and case. speaker_names holds a name
# that resolves to no record: no template reads it, so the page credits
# nobody until a human verifies the person (AGENTS.md).
talks:
  - id: securing-ai-a-journey-through-access-control-systems
    title: "Securing AI: a journey through access control systems"
    speakers: [carla-urrea-stabile]
    type: talk
    language: en
    duration_minutes: 30
    description: "Remember when you started working on that application and only admins could do that one action? Then that quickly evolved to having others being able to do that other action and you ended up with a bunch of different roles, attributes, etc to handle all those cases? Ha, welcome to the world of access control systems!\nIn this talk, we'll follow the journey of a project that begins with no access control, progresses to Role-Based Access Control (RBAC), struggles with Attribute-Based Access Control (ABAC), and ultimately finds its footing with Fine-Grained Authorization (FGA). You'll see how this journey becomes even more important in modern applications, especially when thinking about things like AI. In this process, you'll learn how OpenFGA addresses the growing complexity with a relationship-based model that's both flexible and scalable."
  - id: python-mcp-from-zero-to-a-working-server-in-30-minutes
    title: "Python + MCP: from zero to a working server in 30 minutes"
    speakers: [javier-martinez-alcantara]
    type: talk
    language: en
    duration_minutes: 30
    description: "The Model Context Protocol (MCP) is an open standard that lets apps and AI assistants connect securely to data and tools through a common client-server contract. In this fast-paced talk, we'll cover what MCP brings to the Python ecosystem, how it's structured (clients, servers, resources, tools, and prompts), and which official SDKs are available. We'll close with a live demo: building a minimal MCP server in Python that exposes a real tool and connecting it to a compatible client to invoke it from a conversation. The session targets developers with intermediate Python who want to integrate their stack (APIs, files, databases) with assistants. After 30 minutes you'll leave with a clear mental model, reusable boilerplate, and practical best-practice guidelines."
---
