# One-Line Pitches — A Day of One-Line Pitches

[![make.fun](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![Rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/surya-palo/one-line-pitches/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![Reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/surya-palo/one-line-pitches/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

Entry for the make.fun bounty **A Day of One-Line Pitches**
([bounty page](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)).

## The pitch

> Give the app idea you've been carrying for years to an AI agent on make.fun tonight, describe it in plain words, and by bedtime you'll have a version you can actually tap — free, and if you don't like it, all it cost you was a chat.

One sentence, 232 characters. It speaks straight to a friend who has never
coded: hand over the idea you've been carrying, describe it like you'd tell a
friend, and by tonight you'll have something real to tap — with nothing at
stake but a chat if it isn't for you.

## How it works

`main.py` (Python 3.13 standard library only) writes the exact pitch above to
`/output/entry.txt`, creating `/output` if needed. The output is fully
deterministic: the sentence is a constant in the source, so every run
produces byte-identical output.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

See `BUILD_LOG.md` for the candidates considered and why this one won.
