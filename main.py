#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun program/v1 entry.

Writes one funny single-line reply from a hopeless tech support agent
to a desperate customer to /output/entry.txt. Deterministic: the same
bytes on every run, no network, no randomness, no input read.
"""

import os

LINE = (
    "Have you tried turning it off and on again? Breathe - "
    "I've said that 400 times today and it's worked exactly never."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
