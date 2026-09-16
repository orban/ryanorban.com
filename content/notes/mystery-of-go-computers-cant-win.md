---
title: The Mystery of Go, the Ancient Game That Computers Still Can't Win
date: 2014-05-12
categories:
  - go
  - artificial-intelligence
  - game-theory
  - deep-learning
  - historical
description: Wired's 2014 article arguing computers couldn't beat top Go players — written two years before DeepMind's AlphaGo defeated Lee Sedol. A remarkable historical document showing how quickly AI capabilities confounded expert predictions.
params:
  source: pinboard
  sourceUrl: http://www.wired.com/2014/05/the-world-of-computer-go
---

## Summary

This 2014 Wired article explained why Go was considered the hardest challenge in game-playing AI: the branching factor is ~250 per move (vs. ~35 for chess), the board is 19×19 with ~2×10^170 possible positions, and human expert intuition in Go relies on pattern recognition that defied reduction to search algorithms. The consensus in 2014 was that beating top human professionals was at least 10 years away.

AlphaGo beat Lee Sedol in March 2016 — less than two years after this article. The breakthrough was deep reinforcement learning applied to position evaluation and move selection, which DeepMind combined with Monte Carlo tree search. The same pattern recognition that experts said made Go uncomputable turned out to be learnable from millions of self-play games.

This article is a historical document worth preserving as a calibration example: expert predictions about AI capability timelines have a poor track record, and the humans are uniquely good at X framing has been repeatedly falsified. Chess (1997), Jeopardy! (2011), Go (2016), protein folding (2020), image recognition (2012), and language generation (2020+) all followed the pattern: deemed impossible, then solved faster than predicted.

## Key points

- Go was the final frontier of board game AI in 2014 — the specific cited reasons (branching factor, intuition) were correct but the timeline was not.
- AlphaGo solved it via deep learning for position evaluation + Monte Carlo tree search for planning — neither component was new, the combination at scale was.
- The defeat of Lee Sedol (March 2016) was a cultural moment: AI demonstrating superhuman performance at a game with centuries of human culture built around mastery.
- The article exemplifies a recurring pattern: experts argue AI can't do X because of property Y; deep learning either learns Y or routes around it.
- AlphaZero later solved chess, shogi, and Go from scratch (no human game data) — making the 2014 framing of human intuition is special even more clearly wrong.

[Original](http://www.wired.com/2014/05/the-world-of-computer-go)
