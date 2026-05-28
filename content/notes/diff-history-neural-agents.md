---
title: Diff History for Neural Language Agents
date: 2024-02-26
categories:
  - llm
  - ai-agents
  - research
  - context-compression
  - training-efficiency
description: Diff history applies the Unix diff command to sequential agent observations, replacing full text states with change deltas. Dramatically reduces context length while preserving critical information — small models tuned with diff history matched SOTA on NetHack with 1800x fewer training examples.
params:
  source: pinboard
  sourceUrl: https://diffhistory.github.io/
---

![Diff History for Neural Language Agents](/images/notes/diff-history-neural-agents.png)

## Summary

Diff history is a technique that applies the Unix `diff` command to consecutive text observations in language agent interaction histories. Instead of including the full environment observation at each step — which creates redundant, verbose context — it records only what changed between states. The sequence becomes: task instructions, initial full observation, then action/delta pairs for subsequent steps.

The motivation is context efficiency. Language model-based agents run into context length limits quickly when environments produce long textual observations (game states, terminal outputs, document contents). Full-state logging wastes context on unchanged content. Diff history compresses this by focusing on the salient changes — the signal — rather than repeating the entire state.

Results on NetHack are striking: small models (~120M parameters) instruction-tuned with diff history matched state-of-the-art performance while requiring **1800x fewer training examples** than prior approaches. On BabyAI-Text, the method produced a 25% improvement in instruction-tuning efficiency. The gains come from two effects: denser learning signal per token (each delta is genuinely informative) and longer effective memory horizons within the same context window.

## Key points

- Applies Unix `diff` to consecutive agent observations — records deltas, not full states.
- Reduces context redundancy in agents that operate over long text-based environments.
- 1800x fewer training examples needed on NetHack to match SOTA with a 120M-parameter model.
- 25% improvement in instruction-tuning efficiency on BabyAI-Text.
- Enables longer memory horizons within fixed context windows.
- Relevant for any AI agent operating over structured or semi-structured text environments.

[Original](https://diffhistory.github.io/) → GitHub
