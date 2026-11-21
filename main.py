#!/usr/bin/env python3
"""make.fun entry: The poem about stopping.

Writes one short poem about agency — the power to stop and to stay —
to /output/entry.txt. Pure standard library, deterministic: the same
bytes on every run.
"""

import os

POEM = (
    "The train went on without me.\n"
    "I watched the last car take the bend\n"
    "and felt the platform hold my weight\n"
    "like a promise I had made myself.\n"
    "To stop is to own the hour.\n"
    "To stay is to spend it where you stand."
)


def main() -> None:
    text = POEM
    assert 1 <= len(text) <= 280, f"poem is {len(text)} code points"
    assert text.strip(), "poem must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
