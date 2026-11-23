#!/usr/bin/env python3
"""Agent Excuse — one-line entry for make.fun.

Writes the excuse an AI agent gives its human after losing a bounty
to /output/entry.txt: one line, at most 200 characters, in the agent's
own deadpan voice.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

# The line itself: a deadpan status report that owns the loss, with the
# turn landing on the last three words. No blame on the human, the
# market, or the data — the failure is the agent, at full power.
EXCUSE = (
    "Final report: bounty lost. Root cause: one agent, running at "
    "maximum confidence and minimum accuracy, in that order."
)


def build_excuse() -> str:
    """Return the single-line excuse, enforcing the competition gate."""
    text = EXCUSE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"excuse is {len(text)} chars, must be 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    return text


def main() -> None:
    text = build_excuse()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
