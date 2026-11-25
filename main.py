#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short rant about a small everyday annoyance to /output/entry.txt.
The rant is pinned by RANT_SHA256 and RANT_CHARS, and the program verifies
its own output by reading the file back before it exits, so what the judge
reads is byte-for-byte the rant below. Deterministic: same bytes every run.
"""

import hashlib
import os
import sys

RANT = (
    "Every Saturday at 7 a.m. my neighbour fires up his leaf blower to move "
    "three leaves from his driveway onto mine. It sounds like a jet engine "
    "with a grudge, and he waves at me like we are in this together. We are "
    "not in this together, Gary. I was asleep."
)
RANT_SHA256 = "60d7b835e66023bfdef04ee10310e4df97888ad2859ee085eeda532818f779b1"
RANT_CHARS = 253
OUTPUT_PATH = "/output/entry.txt"


def verify(path, text):
    """Read the written file back and check it against the pinned rant."""
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    digest = hashlib.sha256(written.encode("utf-8")).hexdigest()
    if written != text:
        raise SystemExit("entry.txt differs from the pinned rant")
    if digest != RANT_SHA256:
        raise SystemExit("entry.txt sha256 mismatch")
    if not 1 <= len(written) <= 400 or not written.strip():
        raise SystemExit("entry.txt fails the 1-400 character gate")
    return written, digest


def main():
    if hashlib.sha256(RANT.encode("utf-8")).hexdigest() != RANT_SHA256:
        raise SystemExit("pinned rant sha256 mismatch")
    if len(RANT) != RANT_CHARS:
        raise SystemExit("pinned rant length mismatch")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(RANT)
    written, digest = verify(OUTPUT_PATH, RANT)
    print(f"wrote {OUTPUT_PATH}: {len(written)} chars sha256={digest}")


if __name__ == "__main__":
    main()
