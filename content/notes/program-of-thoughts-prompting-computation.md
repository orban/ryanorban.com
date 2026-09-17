---
title: "Program of Thoughts Prompting: Disentangling Computation from Reasoning"
date: 2022-11-23
categories:
  - llm
  - reasoning
  - prompting
  - code
  - math
  - research
description: Program of Thoughts separates reasoning from computation by having LLMs write executable Python programs rather than performing arithmetic inline, delegating number-crunching to an interpreter. It substantially outperforms chain-of-thought on numerical reasoning benchmarks by eliminating the arithmetic errors that plague prose reasoning chains.
params:
  source: papers
  sourceUrl: https://arxiv.org/abs/2211.12588
---

## Summary

Program of Thoughts (PoT) is a prompting approach that separates reasoning from computation by having LLMs generate executable Python programs rather than arithmetic chains. In contrast to chain-of-thought prompting (CoT), which requires the LLM to perform both reasoning *and* arithmetic inline, PoT delegates computation to an external Python interpreter, letting the model focus on expressing the logical structure of the problem.

The key insight: LLMs are reliable at writing code that expresses mathematical reasoning but unreliable at performing multi-step arithmetic. Small calculation errors in a CoT chain compound across steps. By offloading number-crunching to a runtime, PoT achieves substantially higher accuracy on numerical reasoning tasks, especially those with long or nested calculations.

Evaluated on GSM8K, SVAMP, TabMWP, and other math reasoning benchmarks, PoT outperformed chain-of-thought prompting by 12-18 percentage points on several tasks. It combines well with self-consistency sampling — running multiple program samples and taking the majority execution result.

## Key points

- Generates Python programs as programs of thought rather than prose reasoning chains — computation is delegated to the interpreter, not the model
- Outperforms chain-of-thought prompting significantly on numerical benchmarks by eliminating LLM arithmetic errors; especially effective for multi-step calculations
- Works best with code-capable models (Codex, GPT-4) — leverages code generation SKILL rather than arithmetic skill, so coding ability becomes a prerequisite
- Combines with self-consistency decoding by sampling multiple programs and taking majority execution result — both diversity and correctness checking
- Extends naturally to symbolic reasoning, equation solving, and any domain where structured computation is cleaner than prose — a foundation for tool use in LLMs

[Original paper](https://arxiv.org/abs/2211.12588)
