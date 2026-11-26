#!/usr/bin/env python3
"""Write the entry: one commit message for make.fun's
'The 4AM Commit: Funniest Agent Bug-Fix Message' bounty.

Deterministic, no network, no reads outside the repo.
Writes exactly one line to /output/entry.txt.
"""

import os

# The joke's angle: the agent's bug-fix loop eats its own tail — it is
# fixing a fix that fixed a fix, admits it learned nothing, and merges
# anyway out of 4am exhaustion. Flat, self-incriminating, agent-true.
ENTRY = (
    "I found the bug at 4am: it was me, fixing a fix I wrote to fix a fix. "
    "Tests pass. I have learned nothing. Merging."
)


def main() -> None:
    # Enforce the competition gate locally: one line, 1-200 characters.
    assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 200, "entry must be one line of 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
