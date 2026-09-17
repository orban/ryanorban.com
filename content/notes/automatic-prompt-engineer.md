---
title: Automatic Prompt Engineer (APE)
date: 2022-11-04
categories:
  - prompt-engineering
  - llm
  - automation
  - research
  - open-source
description: Automatic Prompt Engineer (APE) is a research implementation that automatically generates and selects optimal prompts for LLMs using a generate-then-score approach. An early automated prompt optimization method predating DSPy.
params:
  source: pinboard
  sourceUrl: https://github.com/keirp/automatic_prompt_engineer
---

## Summary

[Automatic Prompt Engineer](/notes/automatic-prompt-engineer/) (APE) is a research implementation by Keirp that automates the task of finding good instructions for LLMs. The approach: given a set of input-output demonstrations, use the LLM itself to generate candidate instructions, then score each candidate by how well it produces the desired outputs on a held-out set, and select the best-scoring instruction. This bypasses the need for a human to manually iterate on prompt wording.

The core insight is that LLMs can generate plausible instructions when shown examples, and that evaluating a prompt's quality is cheaper than knowing in advance which wording will work best. The generate-then-score loop makes this tractable. APE demonstrated that automatically discovered prompts could match or outperform hand-written prompts on standard benchmarks, which was surprising in 2022 when manual prompt engineering was still treated as a skilled craft.

APE is an early example of automated prompt optimization, a space that developed significantly afterward. OPRO (Google, 2023) showed that LLMs can iteratively improve prompts using natural language feedback. [DSPy](/notes/dspy/) (Stanford, 2023) built a full framework around this idea, making prompt optimization a first-class programming primitive. The APE paper was influential in establishing that the search over prompt space was viable and worth automating.

## Key points

- Automated prompt engineering: generates candidate instructions from demonstrations, scores each, selects best.
- Bypasses manual iteration — uses the LLM itself to both generate and evaluate candidate prompts.
- Demonstrated automatically discovered prompts matching hand-crafted ones on benchmarks.
- Early entry in automated prompt optimization, predating [DSPy](/notes/dspy/) and OPRO.
- The generate-then-score loop is the core primitive; later work added gradient-based or iterative refinement.
- Established that prompt space search is tractable and worth automating.

[Original](https://github.com/keirp/automatic_prompt_engineer) → GitHub
