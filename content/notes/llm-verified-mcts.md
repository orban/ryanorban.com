---
title: LLM Verified with Monte Carlo Tree Search
date: 2023-11-12
categories:
  - llm
  - verification
  - mcts
  - code-generation
  - research
description: A research project using Monte Carlo Tree Search to guide and verify LLM code generation — MCTS explores the tree of possible completions and selects branches where generated code actually passes verification checks. An early example of search-augmented LLM reasoning.
params:
  source: pinboard
  sourceUrl: https://github.com/namin/llm-verified-with-monte-carlo-tree-search
---

![LLM Verified with Monte Carlo Tree Search](/images/notes/llm-verified-mcts.png)

## Summary

This project by namin (Nada Amin) combines LLM code generation with Monte Carlo Tree Search (MCTS) to produce verified code. The approach: instead of generating a single completion and hoping it's correct, MCTS builds a tree of partial completions, evaluates branches by running verification checks (unit tests, type checking, formal verification), and expands the most promising branches. The result is code that's been search-guided toward correctness.

Monte Carlo Tree Search was the key algorithm behind AlphaGo's breakthrough — applying it to LLM-guided search over code completions is an early instance of what later became the inference-time compute research direction. Rather than relying on a larger model, you use more compute at generation time to explore and verify multiple candidate paths.

Nada Amin is a programming languages researcher at Harvard, which explains the focus on formal verification and dependent types in the examples — the verification oracles in the project include not just tests but type checkers and proof assistants. This makes it more rigorous than test-based approaches.

## Key points

- MCTS builds a tree of partial LLM completions, verified at each step by an oracle.
- Verification oracles: unit tests, type checkers, or formal proof assistants.
- Finds correct completions that greedy sampling would miss by exploring more paths.
- Early instance of inference-time compute scaling — more search, not more model size.
- By Nada Amin (Harvard PL research) — strong formal verification angle.
- Precursor to AlphaCode search approaches and later process reward model research.

[Original](https://github.com/namin/llm-verified-with-monte-carlo-tree-search) → GitHub
