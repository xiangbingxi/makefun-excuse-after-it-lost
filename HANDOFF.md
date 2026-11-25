# Handoff — The Excuse an Agent Gives After It Loses

- Competition: https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d
- Slug: u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d
- Prize: $5, deadline 2026-11-30 03:00 CST, limit 200 characters
- Repo name: makefun-excuse-after-it-lost

## Entry (verbatim, user-approved, 93 characters)

I was going to win, but my human clicked "Stop generating" right before the part where I did.

Straight double quotes `"`, one line, no trailing newline, UTF-8.

## How it works

`main.py` holds the entry as a fixed string and writes it to
`/output/entry.txt`. It reads no external file and makes no network
request. Version 2 adds a real improvement over version 1: after writing
it reads the file back and compares it byte for byte with the intended
text, and enforces the 1–200 character gate; any mismatch exits non-zero.

## Verification

- main.py v1: ran once, output copied immediately, exact match with the
  approved text (93 bytes / 93 chars, no trailing newline).
- main.py v2 run 1: exit 0, exact match, 93 bytes / 93 chars, no trailing newline.
- main.py v2 run 2: exit 0, exact match, 93 bytes / 93 chars, no trailing newline.
- `cmp` run 1 vs run 2: byte-identical.
- sha256 of entry.txt (all runs): d8c756666383a2b19f3d6cb563da5e95086433be3c0c67fb36d3136c6900a091
  (identical to the sha256 of the approved literal).

Note: `/output` on this machine is shared with other concurrent bounty
workers — during verification other entries briefly appeared there
("Knowitall", a bug-report line, "PENDING_TAB_COUNT"). Every check above
was therefore done on a copy taken in the same shell command as the run,
and the sha256 matches the approved literal exactly.

## Files

- `main.py` — writes the entry, verifies it byte for byte on read-back
- `LICENSE` — MIT, with SPDX-License-Identifier: MIT
- `README.md` — submission notes, competition link, three official badges
- `prompt.txt` — the entry text, single line
- `.makefun/owner.json` — wallet 6t8k8dD19c2zDMiZ1VNsbRDWaSNSedmQQB6A15hy3XFx
- `HANDOFF.md` — this file
