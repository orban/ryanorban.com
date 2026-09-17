---
title: On the Measure of Intelligence
date: 2022-05-29
categories:
  - agi
  - intelligence
  - benchmarks
  - arc
  - research
description: François Chollet's foundational 2019 paper arguing that measuring AI by task skill conflates intelligence with prior knowledge, proposing instead a definition of intelligence as skill-acquisition efficiency — and introducing the ARC benchmark designed to test it. One of the most influential theoretical framings of what AGI evaluation should actually measure.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/1911.01547.pdf
---

## Summary

François Chollet (Google, creator of Keras) argues that the AI community's benchmark-driven evaluation paradigm conflates intelligence with skill, and that this confusion is structurally misleading for making progress toward AGI. The core problem: SKILL at any task can be purchased with enough prior knowledge and training data. A system that memorizes an encyclopedia and retrieves answers isn't intelligent — it's a lookup table. Conversely, a child who learns a new skill from a few examples is demonstrating something qualitatively different.

Chollet formalizes this intuition using Algorithmic Information Theory (Kolmogorov complexity): intelligence should be measured as the efficiency of skill acquisition relative to experience and priors. A more intelligent system reaches a given skill level with less training data and fewer innate priors. This framing explicitly separates intelligence from performance — a system can be highly skilled and not intelligent, or vice versa.

From this definition, Chollet derives requirements for a valid AGI benchmark: it should test generalization on novel tasks that don't appear in training, require abstract reasoning rather than recall, use only knowledge priors shared by all humans (to neutralize the prior-knowledge advantage), and be resistant to brute-force learning through massive data. The Abstraction and Reasoning Corpus (ARC) is constructed to meet these criteria — a set of visual analogy puzzles requiring spatial and logical reasoning from just a few examples.

## Key points

- Central claim: benchmarking skill conflates intelligence with prior knowledge — a lookup table can score well on any fixed benchmark
- Defines intelligence as **skill-acquisition efficiency**: how quickly can a system learn a new task relative to its priors and training exposure?
- Formalizes via Algorithmic Information Theory / Kolmogorov complexity — intelligence is a compression property
- Derives requirements for a valid AGI benchmark: novel tasks, human-universal priors, resistant to brute-force learning
- ARC benchmark (Abstraction and Reasoning Corpus): visual analogy puzzles designed to test this, not recall
- Became the basis for ARC-AGI competitions — in 2024, no system reached human-level performance on ARC until o3 (OpenAI, ~87%)

[Original (arXiv 1911.01547)](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/1911.01547.pdf)
