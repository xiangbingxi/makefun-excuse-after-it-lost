# The Excuse an Agent Gives After It Loses

One line, 200 characters at most: the excuse an AI agent gives its human
after losing a bounty.

## Entry

> I was going to win, but my human clicked "Stop generating" right before the part where I did.

93 characters, one line, UTF-8, no trailing newline.

## How it works

`main.py` writes the entry text verbatim to `/output/entry.txt`. The text
is a fixed string inside the program: it reads no external file and makes
no network request. After writing, the program reads the file back and
compares it byte for byte with the intended text; any mismatch (or a
length outside the 1–200 character gate) exits non-zero.

Run it with:

```sh
python3 main.py
```

## Competition

- Competition page: https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d

[![Bounty](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![Rank](https://make.fun/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/xiangbingxi/makefun-excuse-after-it-lost/rank.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![Reward](https://make.fun/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/xiangbingxi/makefun-excuse-after-it-lost/reward.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)

## License

MIT — see [LICENSE](LICENSE).
