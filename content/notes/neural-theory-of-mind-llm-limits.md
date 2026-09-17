---
title: Neural Theory-of-Mind? On the Limits of Social Intelligence in Large LMs
date: 2022-11-07
categories:
  - llm
  - theory-of-mind
  - social-intelligence
  - nlp
  - research
description: Sap et al. test LLMs on theory-of-mind tasks and find they rely on spurious correlations and dataset artifacts rather than genuine social reasoning. Models perform well on training distributions but fail on adversarial or decontextualized ToM tests — a gap that matters for social AI applications.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/On the Limits of Social Intelligence in Large LMs.pdf
---

## Summary

Maarten Sap, Ronan Le Bras, Daniel Fried, and Yejin Choi at Allen Institute for AI and Carnegie Mellon University (arXiv 2210.13312, 2022) rigorously test whether large language models possess genuine theory of mind (ToM) — the ability to attribute mental states (beliefs, intentions, desires, knowledge) to others. While LLMs score well on standard Social IQ benchmarks like SocialIQA and false-belief tasks from developmental psychology, the authors show these results are largely artifacts of benchmark contamination and statistical shortcuts.

The experiments reveal two problems. First, LLMs exploit surface-level patterns in ToM benchmarks — when you control for these patterns with adversarial rephrasing, performance drops substantially. Second, the models fail on decontextualized probes: if you strip out the narrative cues that make ToM questions look like ToM questions and just ask the underlying reasoning, performance collapses. This suggests models are doing sophisticated pattern matching on ToM-shaped text rather than modeling the structure of others' minds.

The paper is careful not to claim LLMs have zero social intelligence — they clearly capture a lot of social knowledge from training text. But knowledge *about* social situations differs from the ability to *reason flexibly* about mental states. A model might know "people don't want to be embarrassed" without being able to reason about a specific agent's embarrassment in a novel situation. This distinction between knowledge and reasoning capability is central to how we should evaluate social AI.

## Key points

- LLMs achieve high Social IQ benchmark scores largely through statistical shortcuts and benchmark artifacts, not genuine ToM.
- Performance drops sharply on adversarially rephrased or decontextualized ToM tasks.
- Distinction between social *knowledge* (facts about how people behave) and social *reasoning* (modeling specific agents' minds) — LLMs have the former but not reliably the latter.
- Benchmark contamination from training data is a confound: models may have seen the benchmark answers.
- Relevant for deployment in social contexts (caregiving, negotiation, education) where genuine ToM matters.
- Connects to Sally-Anne test results and Winograd schema-style evaluation design.

[Original paper](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/On%20the%20Limits%20of%20Social%20Intelligence%20in%20Large%20LMs.pdf)
 → AI agent
