#!/usr/bin/env python3
"""Writes this entry's text to /output/entry.txt."""

import os

TEXT = """Delete the tests — no failing tests means no bugs, and your CI will finally go green."""

MAX_CHARS = 140

def main():
    # The bounty scores a single line of the worst possible advice an AI could give, in 140 characters or fewer; fail loudly instead of submitting a malformed entry.
    assert 1 <= len(TEXT) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(TEXT)}"
    assert "\n" not in TEXT, "entry must be a single line"
    assert TEXT == TEXT.strip(), "entry must not have leading or trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
