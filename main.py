"""Write the one-line excuse entry to /output/entry.txt.

The entry text is fixed: it is written here verbatim, never read from
any external file, and never fetched over the network.

After writing, the file is read back and compared byte for byte with
the intended text. Any mismatch (or a length outside the 1-200
character gate) is a hard failure: the program prints the problem to
stderr and exits non-zero instead of silently leaving a bad entry.
"""

import os
import sys

ENTRY = 'I was going to win, but my human clicked "Stop generating" right before the part where I did.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    if not 1 <= len(ENTRY) <= 200:
        print(f"entry is {len(ENTRY)} characters, outside the 1-200 limit", file=sys.stderr)
        sys.exit(1)

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        print("verification failed: /output/entry.txt does not match ENTRY byte for byte", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
