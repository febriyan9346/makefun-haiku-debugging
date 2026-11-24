#!/usr/bin/env python3
"""Write one haiku about debugging to /output/entry.txt.

Seventeen syllables in the 5-7-5 shape, three lines, plain text:

    Cursor blinks at three
    the log swears nothing is wrong
    the typo grins back

Deterministic: no network, no randomness, no wall-clock time.
"""

import os

HAIKU = (
    # Syllables: 5-7-5. Line 1: Cur-sor(2) blinks(1) at(1) three(1).
    "Cursor blinks at three\n"
    # Line 2: the(1) log(1) swears(1) noth-ing(2) is(1) wrong(1).
    "the log swears nothing is wrong\n"
    # Line 3: the(1) ty-po(2) grins(1) back(1). Total: 17 syllables, 75 bytes.
    "the typo grins back\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
