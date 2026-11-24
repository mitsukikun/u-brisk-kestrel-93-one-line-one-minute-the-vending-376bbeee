#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes one pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt, then self-checks the gate:
UTF-8, 1-200 characters, not only whitespace, a single line.
Pure standard library, no network.

Judge brief (most important first):
  1. The line is a pickup line a vending machine would use, spoken by
     the machine itself.
  2. It uses the machine's own world: slot, buttons, coils, snacks,
     hum, exact change.
  3. The laugh lands with the turn arriving by the last few words.
  4. Short and speakable, one line read in a breath.
  5. Charming rather than creepy.
"""

import os

LINE = (
    "I hum the same tune all day and my coils spin for anyone, but you "
    "walked by and every button lit up. Press B7: tonight, I'm the snack."
)


def validate_entry(text: str) -> tuple[int, int]:
    """Validate the gate rules and return (char_count, byte_count).

    Rules: UTF-8 encodable, 1-200 characters, not only whitespace,
    and a single line (no embedded newline).
    """
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"length {len(text)} outside 1-200")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return len(text), len(encoded)


def main():
    chars, byte_count = validate_entry(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote /output/entry.txt: {chars} chars, {byte_count} bytes")


if __name__ == "__main__":
    main()
