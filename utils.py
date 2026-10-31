import re

_SLUG = re.compile(r"[^a-z0-9]+")


def slugify(text):
    return _SLUG.sub("-", text.lower()).strip("-")


def chunk(seq, size):
    if size <= 0:
        raise ValueError("size must be positive")
    for i in range(0, len(seq), size):
        yield seq[i:i + size]
