"""The URL form of a title, for this archive.

A slug is an address: the file name of an imported meetup, and the last
segment of the URL of a talk page. It drops the accents, which canon()
must never do to a stored string and which a URL cannot carry. That is
safe here and nowhere else: the slug is the address, the title beside it
keeps every letter, and the two are written from the same record.

One definition, because two imports need it. bin/import-meetups makes the
file name of a meetup out of its title, and bin/import-talks makes the id
of a talk out of its title, and the id is what content/talks/_content.gotmpl
puts in the URL of the talk page. A second copy of the rule would go on
making one of the two kinds of address after the rule changed.
"""

import re
import unicodedata

from canon import canon

SLUG_LIMIT = 60


def slugify(text, limit=SLUG_LIMIT):
    """Return the URL form of a title: ASCII, lower case, hyphen separated.

    Accents are decomposed and the combining marks dropped, every character
    that is not a letter or a digit becomes a hyphen, and runs collapse.
    That folds an emoji, a quote, and a colon to the same separator, which
    is what a reader of a URL expects.

    The result is cut at the last whole word inside limit, so a 150
    character title does not become a 150 character file name. The cut can
    make two slugs equal, which is why the caller reports a collision
    instead of overwriting a file.
    """
    text = unicodedata.normalize("NFKD", canon(text))
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = "".join(c if (c.isascii() and c.isalnum()) else "-" for c in text.lower())
    text = re.sub(r"-+", "-", text).strip("-")
    if len(text) <= limit:
        return text
    cut = text[:limit]
    if "-" in cut:
        cut = cut[:cut.rindex("-")]
    return cut.strip("-")
