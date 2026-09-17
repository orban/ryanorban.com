---
title: "Chatbot Arena: Benchmarking LLMs in the Wild with Elo Ratings"
date: 2023-05-03
categories:
  - llm
  - benchmarks
  - evaluation
  - research
  - lmsys
description: Chatbot Arena is LMSYS's crowdsourced LLM benchmark where users rate anonymous head-to-head model comparisons using Elo ratings — producing rankings that reflect real user preferences rather than task-specific metrics. The Elo format became the dominant live benchmark for tracking which frontier model is currently best.
params:
  source: pinboard
  sourceUrl: https://lmsys.org/blog/2023-05-03-arena/
---

![Chatbot Arena: Benchmarking LLMs in the Wild with Elo Ratings](/images/notes/chatbot-arena.png)

## Summary

[Chatbot Arena](/notes/chatbot-arena/) (by LMSYS) is a crowdsourced benchmark platform for LLMs built around anonymous, randomized pairwise comparisons. Users submit a query, receive two anonymous model responses, and choose the better one. The Elo rating system then aggregates preferences into a ranking. The result is a benchmark driven by real human preferences on real queries — rather than fixed task suites that can be gamed or that don't reflect how people actually use models.

The anonymous evaluation is key: users vote without knowing which models they're rating, eliminating brand bias. The randomization and crowdsourcing means the benchmark covers a much wider query distribution than any manually curated test set. By May 2023 when this was published, the Arena had already collected hundreds of thousands of votes and established itself as the go-to live leaderboard for frontier model comparison.

[Chatbot Arena](/notes/chatbot-arena/) became the standard reference for which model is best right now precisely because it captures what static benchmarks miss: generalization across the messy variety of real user queries. It later expanded to cover specific capability categories (coding, math, instruction-following) and became the LMSYS Chatbot Arena leaderboard familiar to practitioners tracking model releases. Closely connected to Open LLM Leaderboard from Hugging Face, which uses different (task-specific) benchmarks.

## Key points

- Crowdsourced, anonymous pairwise comparison → Elo rankings that reflect real user preferences.
- Anonymous evaluation removes brand bias; randomized matching prevents systematic cherry-picking.
- Published May 2023 from LMSYS (UC Berkeley); became the dominant live frontier model leaderboard.
- Query diversity: real user queries, not fixed benchmarks, so generalizes better across use cases.
- Complementary to Open LLM Leaderboard (task-specific) and Papers With Code benchmarks.
- Later evolved to cover categories: coding, math, instruction-following, multilingual.

[Original](https://lmsys.org/blog/2023-05-03-arena/)
