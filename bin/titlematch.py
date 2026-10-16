"""The comparison form of a title, for finding one title inside a text.

Two imports of this archive have the same problem: a title written for a
reader has to be recognised inside another string that carries it.
bin/import-x-photos reads a tweet caption that quotes the title of the talk
it photographs, and bin/import-videos reads the title of a YouTube upload
that names the talk it recorded. The rule lives here, once, because a second
copy of it would go on matching one of the two after the rule changed. That
is the reason bin/slug.py exists as well.

Why the two titles differ at all, which is the thing to understand before
trying to make the match stricter or looser. A Meetup announcement carries
the title the speaker wrote in the call for proposals, months earlier. The
video carries the title the speaker actually used on the day. They are two
honest records of the same talk at two moments, and neither is wrong when
they disagree: "GeoDjango in Agroptima" and "GeoDjango use case: mapping
farmer fields all over Spain" are the same session. So a miss here is the
normal case and not a defect to chase, and the right answer to one is a
human reading the two titles, not a lower guard.

The rule, and its two guards.

fold() is the comparison form: prep() from canon.py, then lower case, the
accents decomposed and dropped, and every mark replaced by a space. This is
the one place in this repository that folds an accent on purpose, and it is
safe only because nothing it returns is ever stored or published. A title
printed with its own punctuation has to compare equal to the programme:
"Models de regressio bayesians," in a post and "Models de regressió
bayesians" in the front matter are the same title.

TITLE_MINIMUM is the length guard. A folded title of a few characters
appears inside unrelated prose, so matching it links the wrong talk.
Measured on 2026-10-13 over the 231 photos the X import brought in, this
cut keeps the 46% that carry a real title, 107 of them, and costs none.

match_title() is the ambiguity guard. When two candidates match one text it
returns no key and both of them. A wrong link is worse than no link,
because the page then points the reader at another talk and nothing on it
says so.

Containment runs one way by default: the candidate title inside the text. A
caption quotes the whole title and adds the speaker, so there the title is
the shorter side. A YouTube title is not always the longer side: the
uploader shortens a long title and writes "[...]" where the cut is, so the
text is then the shorter one. both_ways accepts containment in either
direction, with the length guard on whichever side is the needle, and the
caller says which of the two it needs.
"""

import argparse
import re
import sys
import unicodedata

# canon.py sits next to this module and is not an installed package. A
# caller already puts bin/ on the path to import this file, so the plain
# import works for the caller too.
from canon import prep

# The shortest folded title that may be matched inside another string. See
# the length guard above.
TITLE_MINIMUM = 12

# Every character that is not a letter or a digit becomes a space, so a
# title compares equal to the same title written with other punctuation. A
# space and not a hyphen, because the result is read as words and never as
# an address: bin/slug.py is what makes an address.
_NOT_WORD = re.compile(r"[^a-z0-9]+")


def fold(text):
    """Return the comparison form of text.

    prep() first, so the Markdown and the emoji of a source string are gone
    and both sides arrive in the one normalized form the archive import
    shares. Then lower case, the accents off, and every mark replaced by a
    space.
    """
    lowered = prep(text).lower()
    folded = unicodedata.normalize("NFKD", lowered)
    folded = "".join(character for character in folded
                     if not unicodedata.combining(character))
    return re.sub(r"\s+", " ", _NOT_WORD.sub(" ", folded)).strip()


def contains(haystack, needle):
    """Return True when folded needle sits inside folded haystack.

    Both arguments are already folded. A needle shorter than TITLE_MINIMUM
    never matches, whichever side it came from.
    """
    return len(needle) >= TITLE_MINIMUM and needle in haystack


def match_title(text, candidates, both_ways=False):
    """Return (key, hits) for one text against folded candidate titles.

    candidates is a sequence of (key, folded title) pairs, folded once by
    the caller because the same candidates are matched against many texts.
    The return is the one key that matched and no hit, or no key and every
    hit: one hit is a match, and none or several is not.
    """
    folded = fold(text)
    if not folded:
        return None, []
    hits = [key for key, candidate in candidates
            if contains(folded, candidate)
            or (both_ways and contains(candidate, folded))]
    if len(hits) == 1:
        return hits[0], []
    return None, hits


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

# Each row is one behavior this module has to keep: the folded form of a
# string, or the (key, hits) of one match. A bug found later becomes a new
# row here, not a note in a pull request description.
_FOLD_CASES = [
    ("Models de regressió bayesians", "models de regressio bayesians"),
    ("Models de regressio bayesians,", "models de regressio bayesians"),
    ("PySpark on Kubernetes -- Avoiding the pain of YARN",
     "pyspark on kubernetes avoiding the pain of yarn"),
    ("PySpark on Kubernetes: Avoiding the pain of YARN",
     "pyspark on kubernetes avoiding the pain of yarn"),
    ("Architecture Decision Records: documenta tu arquitectura [...]",
     "architecture decision records documenta tu arquitectura"),
    ("A Day Has Only 24±1 Hours", "a day has only 24 1 hours"),
    ("", ""),
    (None, ""),
]

# One programme, folded once, as a caller passes it.
_TALKS = [
    ("api-by-example", fold("API by example")),
    ("hacking-the-bcn-housing-market-scrapy",
     fold('"Hacking the BCN housing market" (Scrapy)')),
    ("comprehensions-in-5-min", fold("Comprehensions in 5 min")),
    ("frozen-python-satice-ice-dataloggers",
     fold("Frozen Python: satice ice dataloggers")),
]

_MATCH_CASES = [
    # A caption quotes the whole title and adds the speaker: one way is enough.
    ("PyBCN Meetup 2015/10 - API by example by C. Barrobés", False,
     "api-by-example", []),
    # The uploader shortened the title, so the text is the shorter side and
    # one way finds nothing.
    ("PyBCN Meetup 2015/09 - Hacking the BCN housing market by T. Barbu",
     False, None, []),
    ("Hacking the BCN housing market", True,
     "hacking-the-bcn-housing-market-scrapy", []),
    ("Frozen Python", True, "frozen-python-satice-ice-dataloggers", []),
    # Under the length guard, both ways: "comprehensions" alone is 14
    # characters, but the folded text here is 11 and never matches.
    ("Comprehensi", True, None, []),
    # Nothing of the programme is in this text.
    ("PyDayBCN 2020 Track 1 - Retrying, a better way by C. Adell", True,
     None, []),
    ("", True, None, []),
]

# Two talks of one day with the same title in them: the match is ambiguous
# and the return names both, which is what stops a wrong link.
_AMBIGUOUS_TALKS = [
    ("introduction-to-pyscript", fold("Introduction to PyScript")),
    ("introduction-to-pyscript-2", fold("Introduction to PyScript")),
]


def _run_selftest():
    """Run the tables above, print one line per case, and return True when
    every one of them passes.
    """
    passed = True

    for value, expect in _FOLD_CASES:
        got = fold(value)
        ok = got == expect
        passed = passed and ok
        print("%-4s  %-10s %-62r -> %r"
              % ("ok" if ok else "FAIL", "fold", value, got))

    for text, both_ways, expect_key, expect_hits in _MATCH_CASES:
        key, hits = match_title(text, _TALKS, both_ways=both_ways)
        ok = key == expect_key and hits == expect_hits
        passed = passed and ok
        print("%-4s  %-10s %-62r -> %r %r"
              % ("ok" if ok else "FAIL",
                 "both" if both_ways else "one way", text, key, hits))

    key, hits = match_title("Introduction to PyScript", _AMBIGUOUS_TALKS,
                            both_ways=True)
    ok = key is None and len(hits) == 2
    passed = passed and ok
    print("%-4s  %-10s two talks of one title -> %r %r"
          % ("ok" if ok else "FAIL", "ambiguous", key, hits))

    # The guard is on the needle and not on the text, so a long text never
    # buys a short title a match.
    ok = not contains(fold("Comprehensions in 5 min and more words"),
                      fold("in 5 min"))
    passed = passed and ok
    print("%-4s  %-10s a short title is not matched in a long text"
          % ("ok" if ok else "FAIL", "guard"))

    return passed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selftest", action="store_true",
                        help="run the built-in test tables and exit 0 or 1")
    args = parser.parse_args()

    if not args.selftest:
        parser.print_help()
        return 1

    ok = _run_selftest()
    print("\nPASS" if ok else "\nFAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
