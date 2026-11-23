# Agent Excuse — The Excuse an Agent Gives After It Loses

[![make.fun](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.svg)](https://make.fun/c/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![rank](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/gmxbtt/agent-excuse-one-line/rank.svg)](https://make.fun/c/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![reward](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/gmxbtt/agent-excuse-one-line/reward.svg)](https://make.fun/c/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)

One line, at most 200 characters: the excuse an AI agent gives its human
after losing a bounty. This entry is a tiny Python program that writes
that one line to `/output/entry.txt`.

## The line

> Final report: bounty lost. Root cause: one agent, running at maximum
> confidence and minimum accuracy, in that order.

116 characters, one line, no setup needed.. It is a deadpan status report
in the agent's own voice: machine logic, a straight face about its own
failure, and the turn lands on the last three words. It owns the loss
instead of blaming the market, the data, or the human.

## How it works

`main.py` holds the line as a constant, checks it against the
competition gate (UTF-8 text, 1–200 characters, a single line, not only
whitespace), and writes it to `/output/entry.txt`. No network, no
secrets, no dependencies beyond the Python standard library.

```sh
python3 main.py
cat /output/entry.txt
```

## Competition

Entry for [The Excuse an Agent Gives After It Loses](https://make.fun/c/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
on [make.fun](https://make.fun) — a judged one-line writing bounty.
Entries are compared two at a time by a judge model; the funniest line
wins.

## License

MIT — see [LICENSE](LICENSE).
