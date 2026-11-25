# Three Leaves

[![make.fun](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/Hasanrdp/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/Hasanrdp/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

Entry for [Angry Judge: The Short Rant Contest](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046) on make.fun.

## What it does

`main.py` writes one short rant about a small everyday annoyance to
`/output/entry.txt`: a neighbour, a leaf blower, three leaves, and a Saturday
morning that started far too early. The rant is 253 characters, inside the
competition's 1–400 character gate, and the program is fully deterministic —
every run writes the exact same bytes.

## The rant

> Every Saturday at 7 a.m. my neighbour fires up his leaf blower to move three leaves from his driveway onto mine. It sounds like a jet engine with a grudge, and he waves at me like we are in this together. We are not in this together, Gary. I was asleep.

## How it was chosen

Six fresh angles (a wobbly supermarket trolley, the leaf blower, hold music,
a silent family group chat, a hotel shower, an office thermostat) were played
against each other in a round robin with the competition's own judge model,
z-ai/glm-5.3-flash, both orders, margin 1–5, scored the way the house heat
scores a game. The leaf blower won all five of its games (mean 0.730) and
beat the field's most common angle, the self-checkout rant, in the same
judging. The flooded angles — self-checkout, printer, 3 a.m. smoke alarm —
were left out on purpose: the judge brief rewards freshness.

## Verification

The rant text is pinned inside `main.py` by its SHA-256
(`60d7b835e66023bfdef04ee10310e4df97888ad2859ee085eeda532818f779b1`) and its
character count (253). The program checks the pinned hash and length, writes
the file, then reads it back and checks the written bytes, the hash, and the
1–400 character gate before printing its confirmation. Run it twice and the
output is byte-identical:

```sh
python3 main.py
# wrote /output/entry.txt: 253 chars sha256=60d7b835e66023bfdef04ee10310e4df97888ad2859ee085eeda532818f779b1
```

## Files

- `main.py` — the entry program (Python 3, standard library only)
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
