---
title: Reasoning or Reciting? LLM Capabilities via Counterfactual Tasks
date: 2023-08-02
categories:
  - llm
  - research
  - reasoning
  - evaluation
  - benchmarks
description: An arxiv paper testing whether LLMs are reasoning or reciting — using counterfactual tasks (modified versions of standard benchmarks) to distinguish genuine reasoning from pattern-matching on training data. Finds LLMs show sharp performance drops on counterfactual variants, suggesting heavy reliance on memorization.
params:
  source: pinboard
  sourceUrl: https://arxiv.org/abs/2307.02477
---

![Reasoning or Reciting? LLM Capabilities via Counterfactual Tasks](/images/notes/reasoning-or-reciting-counterfactual.png)

## Summary

This arXiv paper (2307.02477) investigates a fundamental question about LLM capabilities: when a model answers a math problem or logic puzzle correctly, is it reasoning through the problem or reciting a pattern from training data? The methodology: take standard benchmark tasks and create counterfactual variants — modified versions with changed symbols, different base systems, or altered logical structures — that require the same underlying reasoning but can't be solved by memorized patterns.

The finding: LLM performance drops sharply on counterfactual variants compared to standard versions. A model that can solve standard arithmetic or symbolic logic problems often fails when the symbols are changed or the problem is stated in a form slightly different from training data. This suggests that a significant fraction of apparent reasoning on benchmarks is pattern matching against training-time examples rather than genuine generalization.

The paper distinguishes between instance-level generalization (the model has seen variants close enough to the test case) and principle-level generalization (the model understands the underlying rule and can apply it to genuinely novel configurations). LLMs appear strong on instance-level and weaker on principle-level generalization.

This connects to a broader debate about LLM evaluation: if standard benchmarks are contaminated with patterns from training data, they overestimate generalization. The counterfactual evaluation approach is a more robust test of actual reasoning capability that wasn't as common in 2023 as it became later.

## Key points

- Counterfactual tasks distinguish reasoning (applies principles to novel forms) from reciting (matches training patterns).
- LLMs show sharp performance drops on counterfactual variants of standard benchmarks.
- Suggests standard benchmark performance reflects pattern matching more than genuine reasoning.
- Instance-level vs. principle-level generalization: LLMs strong on former, weaker on latter.
- Motivated the counterfactual evaluation approach adopted by subsequent LLM evaluation research.

[Original](https://arxiv.org/abs/2307.02477)
