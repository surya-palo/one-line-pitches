# Build log — A Day of One-Line Pitches

Bounty: `u-ronigrv-a-day-of-one-line-pitches-12cd9bb3` — one sentence (max 240
chars) that would convince a friend who has never coded to let an AI agent
build their first app idea on make.fun.

## Candidates considered

1. **236 chars (winner, v1)** — "Give the app idea you've been carrying for
   years to an AI agent on make.fun tonight, describe it in plain words, and
   by bedtime you'll have a version you can actually tap — free, and if you
   don't like it, you've lost nothing but a chat."
2. **239 chars** — "Hand the app idea you've been carrying around for years
   to an AI agent on make.fun, describe it in plain words tonight, and by
   bedtime you'll have something real you can tap — free, and if you don't
   like it, you've lost nothing but a chat."
3. **195 chars** — "You've been talking about that app idea for years, so
   hand it to an AI agent on make.fun tonight, describe it the way you'd tell
   a friend, and wake up to something you can actually tap, for free."
4. **203 chars** — "That app idea you keep describing over dinner — say it
   out loud to an AI agent on make.fun and it will build you a working version
   to try, no coding, no money, and you can change anything you don't like."
5. **199 chars** — "Give your idea one evening: describe it in plain words
   to an AI agent on make.fun and you'll have a real app to try by bedtime,
   free, and if you don't like it, you've lost nothing but a conversation."
6. **196 chars** — "Tell an AI agent on make.fun the app idea you've been
   carrying around for years, in plain words, and tonight you'll have a first
   version you can tap — free, and you stay in charge of every change."

## Why candidate 1 won

- **Persuasion (the judge's top weight):** it names the friend's own idea
  ("the app idea you've been carrying for years"), gives a concrete reason to
  say yes *now* ("tonight", "by bedtime"), and makes handing it over feel
  easy and low-risk ("describe it in plain words", "free", "you've lost
  nothing but a chat").
- **Clarity:** plain words throughout, no jargon; one read lands the whole
  arc — idea in, something tappable out, tonight.
- **Truth:** it promises a *version you can tap* by bedtime, not a finished
  product or a business — an honest first step a beginner would find holds up.
- **Warmth and craft:** "you've been carrying for years" and "lost nothing
  but a chat" sound like a person talking to a friend, not a slogan. The
  "carrying" image is fresher than "tell us your idea" templates.
- **Why not the others:** #2 says "something real", vaguer than "a version
  you can actually tap". #3's "wake up to something" is weaker than a
  same-night payoff and its ending trails off. #4's "working version" slightly
  overpromises and "no coding, no money" reads like a checklist. #5's "Give
  your idea one evening" is a decent hook but "a real app" overstates a first
  build. #6 is solid but "you stay in charge of every change" is a weaker
  closer than the nothing-to-lose line.

## v2 improvement (second commit)

Tightened the closing line from "you've lost nothing but a chat" to "all it
cost you was a chat" — shorter, punchier, and it frames the risk as a cost
("a chat") rather than a loss, which lands the free/low-risk point harder in
one read. Final pitch is 232 characters.

## Verification (v2, final)

- `entry.txt`: 232 characters, UTF-8, one sentence, not only whitespace.
- Determinism: `main.py` run twice; both runs produced
  sha256 `99b5e465cc27d8f5848cde093892700b91707533dce24745fe6e26d68df0e229`
  — byte-identical. `entry.txt` matches `/output/entry.txt` exactly.
- `.makefun/owner.json`: 57 bytes, no trailing newline.
- Note: the only other "." in the sentence is inside the domain name
  "make.fun"; the entry is a single sentence ending in one full stop.
