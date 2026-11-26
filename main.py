"""One funny autocorrect fail — make.fun bounty entry.

Writes the final one-line entry to /output/entry.txt.
"""

import os

GREETING = "Thanks for the interview!"
EXCITEMENT = "I'm excited to join your team of assassins"
CORRECTION = "— I mean, assistants."
CLOSING = "See you Monday!"

ENTRY = " ".join([GREETING, EXCITEMENT, CORRECTION, CLOSING])

OUTPUT_PATH = "/output/entry.txt"


def main():
    if not 1 <= len(ENTRY) <= 199:
        raise ValueError(f"entry length {len(ENTRY)} out of range 1-199")
    if "\n" in ENTRY:
        raise ValueError("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        round_trip = f.read()
    assert round_trip == ENTRY, "round-trip mismatch"
    print(f"Wrote {len(ENTRY)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
