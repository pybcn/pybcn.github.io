# Extract the talks from a Meetup event description

You get a JSON list of Meetup events. Each one has `id`, `title`, `dateTime`, `eventUrl`, and
`description`. The description is Markdown written by volunteers over 19 years, in three formats
that changed with the years. Your job is to find the talks each event announced.

## Copy the text, do not write it

- Copy the `title` and the `description` of each talk **from the source text**. Keep the wording,
  the spelling, the punctuation, the capitalisation, and the accents.
- **Do not translate.** A Catalan or Spanish title stays in Catalan or Spanish.
- **Do not correct** a typo, a misspelling, or a name. If the source says `simluation`, you write
  `simluation`.
- **Do not summarise, rewrite, complete, or improve** a title or a description.
- You may drop the Markdown markers (`**`, `*`, `_`, `>`), the escape backslashes, the decorative
  emoji of the template itself, and the leading and trailing spaces.
- If a title is cut short or badly built in the source, you copy it cut short.

## What counts as a talk

A talk is a presentation announced with a title. Record it with `type: talk`.

A **workshop, a practice session, or a tutorial** is also a talk, with `type: workshop`.

When such a session announces no talk title of its own, and the event is one single session that
teaches or presents something, record **one** talk. Its title is the event title with the series
prefix removed, which is the text after the final colon. For an event titled
`May PyBCN Practice Sessions: Intro to Image Processing and Computer Vision`, the title is
`Intro to Image Processing and Computer Vision`. Its description is the part of the event
description that says what the session does.

When the event is a work session with no presentation at all, a sprint, a hack night, a code
dojo with no programme, or a purely social meeting, record **no talk**. A documentation sprint
announces no talk, so the right answer is an empty list.

Never record as a talk: a coffee break, networking, the welcome, the goodbye, the venue, the
access control, the call for proposals, or a job offer.

## Output

Write **only** a JSON file, in this exact shape:

```json
[
  {
    "event_id": "286238841",
    "talks": [
      {
        "title": "...",
        "speakers": ["Firstname Lastname"],
        "description": "... or null when the event gives no abstract ...",
        "language": "English | Spanish | Catalan | null",
        "duration_minutes": 30,
        "type": "talk | workshop | lightning | panel | keynote",
        "links": [{"type": "slides|video|github|site|speaker_profile", "url": "https://..."}]
      }
    ],
    "agenda": [
      {"start": "18:30", "end": null, "label": "Welcome and Talks", "talk_title": null}
    ]
  }
]
```

- One object per event, in the same order as the input, with every event present.
- `speakers`: the names as the source writes them. An empty list when nobody is named.
- `description`, `language`, `duration_minutes`: `null` when the source does not say. Never guess
  and never infer.
- `links`: only URLs that are in the text and belong to that talk, so the speaker profile, the
  project repository, the slides, or the video. An empty list when there are none.
- `agenda`: one entry per slot, but **only when the event prints a schedule**. An empty list
  otherwise. Put the time in `start` and `end`, never inside `label`. Point `talk_title` at the
  talk when the slot is a talk, and leave it `null` for a break or for networking.
- Do not invent an `id` or a slug. The import derives those in code.

## Constraints

- Read no other file. Do not search the internet. Everything you need is in the input.
- Write no file other than the output JSON.
- Your final message is one line: the total number of talks you extracted.

---

## Why this prompt says nothing about the typography

An earlier version of this prompt had a rule that forbade normalising the typography, so straight
quotes for curly quotes, a short hyphen for a long dash, and three dots for an ellipsis.

**That rule made the result worse, and we measured it.** It did not stop the model from changing
the apostrophe. It did make the model write `História` where the source has `Història`, which is a
spelling change in Catalan and not a typography change. The plain prompt made no such error in
three runs; the prompt with the rule made it in one run of two.

Typography is normalised in code instead, by `bin/canon.py`, which runs over every imported
string. That makes the result consistent by construction, and it keeps letters and accents out of
reach. `bin/check-extraction` compares what the model wrote against the normalized source, so a
curly quote turned straight passes and a changed accent fails.

Measurement and reasoning: `Personal/PyBCN/2026-10-11 Fase 3 - El Archive, propuesta de modelos`
in David's vault, section "Qué modelo hace falta, medido".
