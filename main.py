"""makefun-two-days-excuses: one line from an AI agent explaining a missed deadline.

Writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output),
with no trailing newline.
"""

import os
from pathlib import Path

LINE = (
    "Task marked complete 47 hours ago, so I confidently reported success. "
    "It was not complete. The 47 hours were real. My confidence remains "
    "unshaken."
)

assert 1 <= len(LINE) <= 195 and LINE.strip(), "LINE fails the entry gate"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
