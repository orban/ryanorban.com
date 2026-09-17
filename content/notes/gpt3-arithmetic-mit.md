---
title: GPT-3 and Arithmetic (MIT LINGO Lab)
date: 2022-09-02
categories:
  - gpt-3
  - arithmetic
  - language-models
  - research
  - llm
description: MIT LINGO Lab's analysis of GPT-3's arithmetic abilities — probing how and when it succeeds or fails at basic math, and what this reveals about how language models represent numerical reasoning. Relevant to understanding the difference between pattern matching and genuine computation.
params:
  source: pinboard
  sourceUrl: https://lingo.csail.mit.edu/blog/arithmetic_gpt3/
---

## Summary

The MIT LINGO Lab blog post investigates GPT-3's arithmetic capabilities — systematically testing addition, subtraction, multiplication, and division across different digit counts and operation types to understand when and why GPT-3 succeeds or fails at basic math. The findings are nuanced: GPT-3 performs surprisingly well on small-number arithmetic (where the answer may have been memorized from training data) but degrades predictably as operand sizes increase.

The key question the analysis probes: is GPT-3 doing arithmetic or pattern-matching? The evidence suggests largely the latter — the model has seen "2 + 3 = 5" many times in training and retrieves it; it hasn't learned an algorithm for adding numbers in general. This is confirmed by performance collapsing on large numbers that wouldn't appear frequently in training corpora. The error patterns (systematic failures at carry operations, digit-length sensitivity) are consistent with interpolation from seen examples rather than rule-following.

This research context matters: in 2022, there was active debate about whether LLMs could "reason" in any meaningful sense or whether impressive results were all sophisticated retrieval. Arithmetic was a clean test case because ground truth is unambiguous. The findings informed the motivation for chain-of-thought prompting (Jason Wei et al., 2022): if you force the model to show its work step by step, performance on arithmetic improves substantially — suggesting the model can do it, but needs the intermediate computation space. Tool use (executing actual code) was the more robust solution.

## Key points

- GPT-3 performs well on small-number arithmetic (likely memorized) but degrades sharply with larger operands.
- Error patterns suggest pattern-matching from training data, not a learned general algorithm.
- Systematic failure at carry operations and digit-length sensitivity — consistent with interpolation, not rule-following.
- Motivated research into chain-of-thought prompting: showing intermediate steps improves arithmetic significantly.
- Tool use (Python interpreter) is the robust solution — offload computation to actual software.
- Part of the 2022 can LLMs reason? debate; arithmetic was the canonical clean test case.

[Original](https://lingo.csail.mit.edu/blog/arithmetic_gpt3/)
