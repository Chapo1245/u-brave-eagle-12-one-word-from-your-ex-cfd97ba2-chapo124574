#!/usr/bin/env python3
"""One Word From Your Ex -- make.fun entry.

Writes exactly one word to /output/entry.txt: the word the entrant's
ex would use to describe them.

The word is "almost": the sharpest honest summary of a relationship
that never quite became what it was supposed to be. Almost the one.
Almost enough. Almost stayed. One word, no explanation needed.

Deterministic: the program writes the same bytes on every run.
Standard library only; no input, no network, no randomness.
"""

import os

WORD = "almost"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: exactly one word, 1-24 characters, no whitespace.
    if not (1 <= len(WORD) <= 24) or any(ch.isspace() for ch in WORD):
        raise ValueError("entry word must be a single word of 1-24 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
