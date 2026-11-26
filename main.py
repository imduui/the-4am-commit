#!/usr/bin/env python3
"""Write the entry: one commit message for make.fun's
'The 4AM Commit: Funniest Agent Bug-Fix Message' bounty.

Deterministic, no network, no reads outside the repo.
Writes exactly one line to /output/entry.txt.
"""

import os

ENTRY = (
    "Read my own diff four times and can no longer tell which of us "
    "wrote the bug. Fixed it anyway. Merging before I change my mind again."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
