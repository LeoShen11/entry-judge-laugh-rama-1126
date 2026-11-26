"""Make the AI Judge Laugh — office-life one-liner.

Writes a single office joke (one line, under 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt),
then validates the written file and reads it back to prove it matches.
"""

import os
import sys

JOKE = (
    "Our office printer only jams five minutes before a deadline — "
    "apparently it reads my calendar better than I do."
)


def main() -> int:
    # The joke must be one line, 1-200 characters, and not only whitespace.
    if "\n" in JOKE or "\r" in JOKE:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if not JOKE.strip():
        print("error: joke must not be blank", file=sys.stderr)
        return 1
    if len(JOKE) > 200:
        print(f"error: joke is {len(JOKE)} chars, over the 200 limit",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    # Write with no trailing newline so the file holds exactly the joke.
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(JOKE)

    # Read-back check: the file on disk must be byte-for-byte the joke.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != JOKE:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    if not 1 <= len(written) <= 200 or not written.strip():
        print("error: written entry fails the gate", file=sys.stderr)
        return 1

    print(f"wrote {len(written)} chars, {len(written.split())} words "
          f"to {out_path}")
    print(written)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
