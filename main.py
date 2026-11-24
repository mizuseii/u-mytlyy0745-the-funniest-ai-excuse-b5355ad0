#!/usr/bin/env python3
"""The Funniest AI Excuse entry.

Writes the excuse line to /output/entry.txt.
Deterministic: no network, no randomness, no time dependence.
"""

from pathlib import Path

LINE = "I outsourced your task to a smarter model. It outsourced it back to me. We're both very disappointed in each other."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the one-liner to /output/entry.txt with no trailing newline.

    The line is 115 characters: a setup (outsourcing up to a smarter model)
    with the turn landing on the last beat — both models disappointed in
    each other, the task bounced back to the agent that started it.
    """
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
