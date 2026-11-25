#!/usr/bin/env python3
"""One Star, Written in Sap.

A deterministic program for make.fun's "One Star, Written in Sap" bounty.
It writes a single one-line, 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt.

Standard library only. No network, no randomness, no environment input:
the review text is fixed in this file, so every run produces the same
bytes.
"""

import os
import sys

# The review: one line, under 280 characters. A fern, repotted into a
# coffee mug with no drainage, watered out of guilt, and introduced to
# guests as "so easy" -- with a review-site sign-off in plant terms.
REVIEW = (
    "One star. He repotted me into a coffee mug with no drainage, "
    "waters me on his birthday out of guilt, and brags to guests "
    "I'm 'so easy'. My roots are swimming, my leaves are begging. "
    "Would not photosynthesize here again."
)

MAX_CHARS = 279


def main(argv):
    out_path = argv[1] if len(argv) > 1 else "/output/entry.txt"
    text = REVIEW.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            "review must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if text != text.splitlines()[0]:
        raise SystemExit("review must be a single line")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
