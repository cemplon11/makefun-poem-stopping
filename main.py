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

OUTPUT_PATH = os.path.join("/output", "entry.txt")


def validate_poem(text: str) -> str:
    """Check the poem fits the 1–280 code-point bound and is non-blank."""
    if not 1 <= len(text) <= 280:
        raise ValueError(f"poem is {len(text)} code points, must be 1–280")
    if not text.strip():
        raise ValueError("poem must not be only whitespace")
    return text


def write_poem(text: str, path: str) -> None:
    """Write the validated poem to path, creating its directory first."""
    validated = validate_poem(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(validated)


def main() -> None:
    write_poem(POEM, OUTPUT_PATH)


if __name__ == "__main__":
    main()
