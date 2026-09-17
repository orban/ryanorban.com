---
title: What Building "Copilot for X" Really Takes
date: 2022-12-26
categories:
  - ai
  - product
  - llm
  - developer-tools
  - latency
description: An essay from the team behind Codeium on what actually goes into building a 'Copilot for X' product — inference scale, latency budgets, context window management, and the unglamorous infrastructure work. A 2022 reality check on what the AI coding assistant category requires.
params:
  source: pinboard
  sourceUrl: https://lspace.swyx.io/p/what-building-copilot-for-x-really
---

## Summary

This essay, shared on swyx's newsletter, is written by the team behind Codeium — a competitor to GitHub Copilot — and explains the practical engineering challenges of building an AI coding assistant at production scale. It's a reality check against the just wrap the API assumption that many 2022-era AI product builders had.

The post covers several underappreciated requirements: estimating inference scale (how many tokens per second do you need to sustain, and what hardware/cost does that imply?), latency tradeoffs (autocomplete requires <100ms perceived latency; slower responses feel broken), and context window management (what context do you include in the prompt given limited window size?). These are not problems you solve once — they're continuous engineering work.

The Codeium team's position is interesting: they were building against GitHub Copilot, which had the advantage of Microsoft's infrastructure and access to OpenAI's models. To compete, they had to think carefully about inference efficiency, which led them to train smaller specialized models rather than using a large general model. The piece argues that Copilot for X requires genuine ML infrastructure investment — not just prompt engineering on top of an API — if you want latency and cost characteristics that feel like a product rather than a prototype.

## Key points

- Building an AI coding assistant requires: inference scale planning, <100ms latency, context management.
- Autocomplete latency is UX-critical — a slow suggestion is worse than no suggestion.
- Context window management is continuous engineering, not a one-time decision.
- Codeium competed with GitHub Copilot by training smaller specialized models for efficiency.
- Wrap the API doesn't scale — production AI products require real ML infrastructure investment.

[Original](https://lspace.swyx.io/p/what-building-copilot-for-x-really) → GitHub
