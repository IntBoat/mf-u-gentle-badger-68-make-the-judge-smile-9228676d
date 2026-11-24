#!/usr/bin/env python3
"""Make the Judge Smile (make.fun).

Writes the entry -- one line about a small good thing that happened
today -- to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "At 7 a.m. the baker slipped an extra warm bun into my bag, winked, and said it was for the road, not the receipt."

# Gate: the entry must be 1-200 characters of UTF-8 text, no trailing newline.
assert 1 <= len(TEXT) <= 200 and TEXT == TEXT.strip()


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
