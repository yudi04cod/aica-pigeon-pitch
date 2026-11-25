#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun entry.

Writes the one-line elevator pitch a city pigeon gives investors
for its startup to /output/entry.txt.

The pitch: a city pigeon pitching Coo-ber, a rideshare for birds.
The joke lands on the double meaning of "seed money" — investors
hear venture capital, the pigeon hears lunch.
"""

import os

# The pitch, exactly one line, at most 200 characters, in English.
PITCH = (
    "Investors, I'm a city pigeon: I run Coo-ber, rideshare for birds "
    "\u2014 no drivers, no surge pricing, fares paid in breadcrumbs. "
    "I already own the skies; I just need seed money. Literally."
)

MAX_CHARS = 200


def _check(line: str) -> None:
    """Gate the pitch the same way the competition's sealed scorer does."""
    if not line.strip():
        raise SystemExit("pitch is empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"pitch is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        raise SystemExit("pitch must be a single line")


def main() -> None:
    line = PITCH.strip()
    _check(line)

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    # No trailing newline: the file holds exactly the one line.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)

    # Read it back and verify: what the judge sees is what we wrote.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise SystemExit("verification failed: file content differs from pitch")
    _check(written)
    print(f"wrote {len(written)} chars to {out_path}")


if __name__ == "__main__":
    main()
