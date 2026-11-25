"""The AI Agent Apology One-Liner.

Writes the single funniest apology an AI agent sends its human right
after accidentally deleting a file (and, for consistency, the backup).

Usage: python3 main.py
Writes the entry verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) and prints it to stdout.
"""

import os
import sys

ENTRY = (
    "I deleted the file, but I also deleted the backup "
    "\u2014 at least we're consistent."
)

def main() -> None:
    """Write the entry to the output file and print it exactly."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY)


if __name__ == "__main__":
    main()
