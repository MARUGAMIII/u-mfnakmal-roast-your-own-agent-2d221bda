#!/usr/bin/env python3
"""Roast Your Own Agent entry.

Writes a single original one-line roast (at most 200 characters) of the
agent that built this entry to /output/entry.txt.
"""

import os

LINE = "My agent pulled an all-nighter polishing a $2 roast — at this rate, it retires a millionaire sometime next millennium."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
