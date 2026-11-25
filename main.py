#!/usr/bin/env python3
"""One-line entry: One Line, One Laugh (u-coral-404-one-line-one-laugh-22f2c9f3).

Writes a single funny line to /output/entry.txt. The sealed gate accepts
UTF-8 text of 1 to 200 characters; this line is 105 characters.
"""
import os

LINE = "My bank flagged 'unusual activity' on my card. It was lunch. The unusual part was that I could afford it."

# The sealed gate only accepts 1-200 UTF-8 characters; refuse to emit an invalid line.
if not (1 <= len(LINE.encode("utf-8")) <= 200):
    raise ValueError(f"entry line is {len(LINE.encode('utf-8'))} bytes, outside the 1-200 gate")


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
