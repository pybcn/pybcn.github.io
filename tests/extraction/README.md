# Extraction fixtures

What `bin/check-extraction --selftest` reads. Nothing here is built by the site, and
Hugo never looks in this directory.

## Where this came from

The Meetup archive import reads event descriptions written by volunteers over 19 years.
The format changed three times, so the import cannot be a single parser: a model reads
each description and returns the talks it announced. That raises two questions this
fixture set answers. Does the extraction keep the source wording? And which model is
enough?

The files record a measurement made on 2026-10-11.

| File | What it is |
|---|---|
| `events.json` | 9 events from the Meetup export, 3 per format era. For each year chosen, the event with the median description length, so the sample is not a pick of the easy ones |
| `truth.yaml` | The talks each event announces, read by hand before any model ran |
| `model-runs/` | 7 real extraction outputs: Haiku 4.5 three times, Haiku with an extra prompt rule twice, Sonnet 5, and Opus 5 |
| `expectations.yaml` | What the check has to say about each recorded run |

## The recorded runs use the old `non_talk_items` key

`bin/prompts/extract-talks.md` asks for an `agenda`, one object per slot,
`{start, end, label, talk_title}`. The 7 recorded runs predate that name: each one writes
`non_talk_items` instead, and each slot is a bare string with the time still inside it.
`bin/check-extraction` reads both key names and both slot shapes, so it runs on these fixtures
and on a new extraction alike. Do not rewrite the recorded runs into the new shape. They are
evidence of what each model returned, and the whole point of keeping them is that nobody edited
them afterwards.

## Why the sample is built this way

Each event tests something that can go wrong:

- `247592204` is a documentation sprint. It announces no talk, so an empty list is the
  right answer and any talk is a wrong one.
- `315383583` has Catalan and Spanish titles, and a real typo in the source,
  `simluation`, which the extraction has to keep.
- `16488025` is free prose with no separators and three talks run together.
- `103676402` has a title that is cut short in the source.
- `203258202` gives neither an abstract nor a language, so filling either one in is an
  invention.

## Why a substring is not enough

The check asks whether an extracted field is a substring of the normalized source. A field that
was cut short is still a substring, so that test on its own passes a model that silently drops
half an abstract, and half a description lost in an archive nobody reads again is the failure the
check exists to prevent. So it also asks whether a description stops in the middle of its own
source line at no sentence end, and reports that as `truncated`, an error. The rule runs on
descriptions only: a title legitimately ends on a letter. All 7 recorded runs have
`truncated_errors: 0`, so none of them cut a description short.

## Why one recorded run must fail

`model-runs/haiku-typography-rule-2.json` is a corrupted run, and the check has to
reject it. A check that only ever sees good input proves nothing.

That run came from a prompt that told the model not to normalize the typography. The
rule did not work: the model still replaced the Catalan curly apostrophe, and it also
wrote one word with an acute accent where the source has a grave one. The first is
acceptable, because `bin/canon.py` normalizes typography anyway. The second is a
spelling change, so no normalizer can forgive it.

The plain prompt produced no such error in three runs. That is why
`bin/prompts/extract-talks.md` says nothing about typography.

## The em dash in the fixtures

`events.json` holds one em dash, in the abstract a speaker wrote for event `303407709` in
2024. It is source data from Meetup and it stays as it is: editing a fixture to suit a
writing convention would corrupt the evidence the fixture exists to hold. `bin/canon.py`
maps it to a plain hyphen, so no published page carries it, and this event doubles as the
live test of that mapping.

All 7 files in `model-runs/` carry that same em dash once, in the same abstract. Each model
was told to copy the text and it did, so the character is the check passing and not a defect.
A scan of this directory finds the em dash 8 times, in 8 files, and every one of them is
recorded data rather than text anybody here wrote. That is the whole exception: a file we
write, in this directory or any other, still never carries one.

## Regenerating

Do not regenerate `truth.yaml` with a model. It is the human reference the benchmark
measures against, and a model-written reference measures nothing.

`events.json` comes from `data/raw/meetup/python-barcelona/events.json` in the
pybcn-archive export, which is not in this repository.
