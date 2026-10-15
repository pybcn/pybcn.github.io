"""Canonical text form for the Meetup archive import.

The decision this module encodes: text imported from the Meetup export is
stored normalized and consistent, not as a facsimile of Meetup. The
normalization has to be deterministic and in code, with one definition, and
it cannot depend on a model behaving well. A model told NOT to normalize
the typography was measured against the Meetup export: it changed the
apostrophe anyway, and in the same pass it corrupted an accented letter
that it had copied correctly without the rule. Code cannot do that,
because it never touches a letter.

canon() is the normalizer. strip_md() and prep() support comparing a source
string against an extracted one: the extractor runs text through Markdown,
and a source string never was, so the two cannot be compared until the
Markdown is gone from both. strip_time() removes a schedule label's leading
time, because the time lives in the event's own start and end fields and
does not belong in the label text too.

The one rule canon() never breaks: it does not touch a letter or an accent.
Everywhere else, "normalize the typography" is safe to read as "make it
closer to ASCII", and a model treats it that way. Here it is not: the data
covers Catalan, Spanish, and French, so NFKD-then-strip-accents or any other
latinizing transform would silently corrupt "Història" into "Historia" or
"Historia" into something that no longer matches its own source. The map
below stays within the set of marks and spaces that normal keyboard input
also maps to one of these forms; it never reaches into the letters.
"""

import argparse
import re
import sys
import unicodedata

# Every substitution below is built from its code point, not typed as the
# raw character. Several of these marks look alike, or look like nothing at
# all (a hair space renders as a gap the width of a typo), and a source file
# that carries them as raw bytes hides that from a reviewer: the same trap
# bin/check-html-safety guards against in built HTML. Spelling out the code
# point also keeps these tables in the ASCII range, so a diff of one never
# carries an invisible or look-alike character by accident. The rest of the
# file is not ASCII, and cannot be: the selftest table below holds a raw
# curly apostrophe and raw accented letters, because those are what it
# tests.

# Quotation marks and primes that stand in for a straight quote on a
# keyboard that supports typing one directly, or that a word processor
# "smart quotes" feature produces from one. Catalan text uses the left and
# right single forms for its apostrophe (d'una), so both single and double
# families are mapped, not just the double ones a generic cleanup usually
# targets.
QUOTES = {
    0x2018: "'", 0x2019: "'", 0x201A: "'", 0x201B: "'",  # single quotes
    0x201C: '"', 0x201D: '"', 0x201E: '"',  # double quotes
    0x00AB: '"', 0x00BB: '"',  # guillemets, used as quotes in French text
    0x2032: "'", 0x2033: '"',  # prime and double prime
}

# Dashes and the mathematical minus sign that a source pastes in place of a
# plain hyphen: Meetup descriptions carry an en dash, an em dash, and the
# Unicode minus sign interchangeably with "-". All of them collapse to the
# one ASCII hyphen, so a comparison never fails over which dash a human
# picked.
DASHES = {
    0x2013: "-",  # en dash
    0x2014: "-",  # em dash
    0x2212: "-",  # minus sign
    0x2010: "-",  # hyphen (the dedicated Unicode character, not "-")
    0x2011: "-",  # non-breaking hyphen
}

# A single ellipsis character, which prep() has to treat as the same text as
# three periods: a source may use either, and the extractor's model tends to
# write the three-period form regardless of which one the source used.
ELLIPSIS = {0x2026: "..."}

# Non-breaking, figure, narrow, and thin spaces. Meetup's export carries these
# where a human just pressed the space bar on a system that substituted one,
# or where an editor inserted a non-breaking space before a unit or a
# punctuation mark. None of them is a letter, so all of them fold to the
# plain space.
SPACES = {
    0x00A0: " ",  # no-break space
    0x2007: " ",  # figure space
    0x202F: " ",  # narrow no-break space
    0x2009: " ",  # thin space
    0x200A: " ",  # hair space
}

_CANON_MAP = {}
for _table in (QUOTES, DASHES, ELLIPSIS, SPACES):
    _CANON_MAP.update({chr(codepoint): replacement for codepoint, replacement in _table.items()})
_CANON_TABLE = str.maketrans(_CANON_MAP)

_HORIZONTAL_WHITESPACE = re.compile(r"[ \t]+")


def canon(text):
    """Return the acceptable typographic form of text.

    NFC first, so a letter with a combining accent and the same letter with
    a precomposed accent compare equal. Then the character substitutions
    above: curly and angle quotes to a straight quote, every dash and the
    minus sign to a hyphen, a one-character ellipsis to three periods, and
    the non-ASCII spaces to a plain one. Runs of plain spaces and tabs
    collapse to one space.

    This never changes a letter or an accent. That boundary is the entire
    point of the function: the archive's source text is Catalan, Spanish, and
    French, and a transform that also "normalizes" accents would turn
    "Història" into "Historia" or "Historia" into "História". Either breaks
    a comparison against the source and nobody would notice until a word
    read wrong on the published page.
    """
    text = unicodedata.normalize("NFC", text or "")
    text = text.translate(_CANON_TABLE)
    return _HORIZONTAL_WHITESPACE.sub(" ", text)


# [text](url) resolves to text. Applied before the character-class strip
# below, because the URL inside the parentheses can itself contain '*', '_',
# or '#', and stripping those first would leave the parentheses and the URL
# behind as stray text.
_MARKDOWN_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")

# Markdown markup characters with no reading-order meaning of their own:
# emphasis (* _), blockquote (>), inline code (`), and heading (#). Removing
# them, rather than parsing Markdown into a tree, is enough because prep()
# only needs the reading text, not the structure.
_MARKDOWN_MARKUP = re.compile(r"[*_>`#]")

_WHITESPACE_RUN = re.compile(r"\s+")


def strip_md(text):
    """Return the Markdown-free reading text of text, for comparison.

    The extractor's output is Markdown; a source string pasted out of the
    Meetup export never was. The two cannot be compared for equality until
    both go through this: it resolves a link to its visible text, drops the
    backslash of an escaped character, drops the emphasis/quote/code/heading
    markup characters, drops every emoji and formatting character (Unicode
    categories So "other symbol", Sk "modifier symbol", and Cf "format", which
    covers variation selectors and zero-width joiners), and collapses all
    whitespace, including a newline, to one space.
    """
    text = (text or "").replace("\\", "")
    text = _MARKDOWN_LINK.sub(r"\1", text)
    text = _MARKDOWN_MARKUP.sub("", text)
    text = "".join(
        character for character in text
        if unicodedata.category(character) not in ("So", "Sk", "Cf")
    )
    return _WHITESPACE_RUN.sub(" ", text).strip()


def prep(text):
    """Return text ready to compare: strip_md(canon(text)).

    This is what the extractor and the check run both the source and the
    extracted text through before comparing them, so neither side's leftover
    typography or Markdown can make a true match look like a mismatch, or
    the reverse.
    """
    return strip_md(canon(text))


# A grid label carries its own leading time ("18:30: Welcome and Talks")
# because that is how it read on the Meetup page, but the imported event
# already stores the time in its start and end fields. Leaving it in the
# label would duplicate it and risk the two disagreeing after an edit to
# either one. The pattern accepts the two separators the export uses (":" or
# ".") between hour and minute, an optional "h" or "hs" unit after the
# minutes, and a colon, a hyphen, or nothing between the time and the label
# text. It runs after prep(), so by this point any dash has already become
# the plain hyphen "-" that canon() produces; there is no other dash form to
# match here.
#
# "hs" has to come before "h" in the alternation. Regex alternation tries
# each branch in order and stops at the first one that lets the rest of the
# pattern match, not the longest one: with "h" first, "9:00hs: Talk" matched
# only the "h", because the remaining "s: Talk" still satisfied the optional
# groups that follow, and the label came out as "s: Talk" instead of "Talk".
_TIME = r"\d{1,2}[:.]\d{2}\s*(?:hs|h)?\s*"
# The optional second time covers a range ("09:30 - 10:45 Keynote"), which is
# how the PyDay and PyData grids print a slot. Without it only the start time
# came off and the end time stayed in the label text.
_LEADING_TIME = re.compile(r"^" + _TIME + r"(?:[:-]\s*" + _TIME + r")?[:-]?\s*")


def strip_time(label):
    """Return label with a leading grid time removed, for example:

    "18:30: Welcome and Talks" -> "Welcome and Talks"
    "Welcome and Talks" -> "Welcome and Talks" (unchanged, no leading time)
    """
    return _LEADING_TIME.sub("", prep(label))


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

# Each row is one behavior this module has to keep. "kind" says which
# function the row checks, "input" is what goes in, "expect" is what has to
# come out. This is the only test this repository has for canon.py, so the
# table is also where a regression gets added: a bug found later becomes a
# new row here, not a note in a pull request description.
_SELFTEST_CASES = [
    ("canon", "d’una", "d'una"),  # Catalan curly apostrophe
    ("canon", "Història", "Història"),  # accent must not change
    ("canon", "", ""),
    ("canon", None, ""),
    ("strip_md", None, ""),
    ("strip_md",
     "how [Yaetos](https://github.com/arthurprevot/yaetos) can help",
     "how Yaetos can help"),
    ("prep", None, ""),
    ("strip_time", "18:30: Welcome and Talks", "Welcome and Talks"),
    ("strip_time", "18.30 Welcome and Talks", "Welcome and Talks"),
    ("strip_time", "9:00h - Talk", "Talk"),
    ("strip_time", "9:00hs: Talk", "Talk"),
    ("strip_time", "09:30 - 10:45 Keynote", "Keynote"),  # a range, as PyDay prints it
    ("strip_time", "09:30-10:45 Keynote", "Keynote"),
    ("strip_time", "10:00 - 10:30: Coffee break", "Coffee break"),
    ("strip_time", "Welcome and Talks", "Welcome and Talks"),  # no leading time
    ("strip_time", None, ""),
]

_FUNCTIONS = {"canon": canon, "strip_md": strip_md, "prep": prep, "strip_time": strip_time}


def _run_selftest():
    """Run _SELFTEST_CASES plus the two checks that do not fit a (kind, input,
    expect) row, print one line per case, and return True if all of them pass.
    """
    passed = True

    for kind, value, expect in _SELFTEST_CASES:
        got = _FUNCTIONS[kind](value)
        ok = got == expect
        passed = passed and ok
        print("%-4s  %-10s %-45r -> %-25r (expect %r)"
              % ("ok" if ok else "FAIL", kind, value, got, expect))

    # Història and História must stay distinct after prep(), because they
    # are different words in different languages. A transform that folded
    # accents, rather than merely normalizing typography, would make this
    # pair equal and silently merge two different source texts.
    distinct = prep("Història") != prep("História")
    passed = passed and distinct
    print("%-4s  %-10s %r != %r"
          % ("ok" if distinct else "FAIL", "prep", "Història", "História"))

    # canon() has to be idempotent: running it twice must give the same
    # result as running it once, because prep() calls it once but the
    # extractor and the check may each run it again on the other's output.
    for kind, value, _ in _SELFTEST_CASES:
        if kind != "canon" and value is None:
            continue
        once = canon(value)
        twice = canon(once)
        ok = once == twice
        passed = passed and ok
        print("%-4s  %-10s canon(canon(%r)) == canon(%r)"
              % ("ok" if ok else "FAIL", "idempotent", value, value))

    return passed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selftest", action="store_true",
                         help="run the built-in test table and exit 0 or 1")
    args = parser.parse_args()

    if not args.selftest:
        parser.print_help()
        return 1

    ok = _run_selftest()
    print("\nPASS" if ok else "\nFAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
