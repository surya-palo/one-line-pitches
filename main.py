#!/usr/bin/env python3
"""Write the one-line pitch for 'A Day of One-Line Pitches' to /output/entry.txt.

Python 3.13 standard library only. Deterministic: the same sentence is
written on every run.
"""

import os

PITCH = (
    "Give the app idea you've been carrying for years to an AI agent on "
    "make.fun tonight, describe it in plain words, and by bedtime you'll "
    "have a version you can actually tap \u2014 free, and if you don't like "
    "it, all it cost you was a chat."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
