#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head — make.fun entry.

Writes one single-line office joke to /output/entry.txt.
Pure Python standard library only.
"""

import os

JOKE = (
    "Someone keeps stealing my lunch from the office fridge, so I "
    "relabelled the next one 'Property of HR' \u2014 it's been untouched "
    "for a month."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = JOKE
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
