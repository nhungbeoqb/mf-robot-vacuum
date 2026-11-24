#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry.

Writes one funny one-line excuse, in the robot vacuum's own voice, to
/output/entry.txt. Python 3.13 stdlib only. Deterministic: the same
text on every run.

v1 line: the vacuum's cliff sensor mistakes the black rug for a
staircase, and the vacuum is too polite to correct it — rooted in the
vacuum's own world (cliff sensor, a real failure mode with dark rugs),
three beats (looked / decided / too polite), twist on the last word:
the rug is "lying", flat on the floor and telling a fib.

v2 revision: tightened the middle beat — "decided it was a staircase"
became "called it a staircase", a punchier verb that makes the sensor
sound like a nervous witness naming what it saw, and the line lands
faster on first read.
"""

import os

ENTRY = (
    "My cliff sensor looked at the black rug, called it a staircase, "
    "and I was too polite to tell it the rug was lying."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
