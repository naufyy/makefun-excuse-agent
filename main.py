#!/usr/bin/env python3
"""Entry for The Excuse My Agent Gave Me.

Writes the winning one-line excuse to /output/entry.txt.
"""
import os

TEXT = "I hit the rate limit at 11:58, spent two minutes apologizing to the API, and missed the deadline politely."

def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(TEXT) <= 200, f"entry length {len(TEXT)} outside 1..200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
