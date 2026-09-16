---
title: Large Language Models Are Human-Level Prompt Engineers
date: 2022-10-02
categories:
  - llm
  - prompt-engineering
  - automation
  - instruction-tuning
  - research
description: Large Language Models Are Human-Level Prompt Engineers (APE) introduces an automated method for generating and selecting optimal prompts using LLMs themselves, matching or beating human-crafted instructions on 19 of 24 NLP tasks. It reframes prompt engineering as a program search problem, making manual iteration unnecessary.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/large_language_models_are_huma.pdf
---

## Summary

Yongchao Zhou, Andrei Ioan Muresanu, Ziwen Han, Keiran Paster, Silviu Pitis, Harris Chan, and Jimmy Ba (University of Toronto / Vector Institute, 2022) introduce [Automatic Prompt Engineer](/notes/automatic-prompt-engineer/) (APE) — a framework that treats instruction design as a program synthesis problem and automates it end-to-end using large language models themselves. Rather than handcrafting prompt wording through trial and error, APE generates a pool of candidate instructions by prompting an LLM to infer plausible task descriptions from input-output demonstrations, then scores each candidate by executing it and measuring downstream task performance, and selects the best.

The generate-then-score loop is the core insight: LLMs are good at producing plausible natural language instructions when shown examples, and evaluating whether an instruction works is computationally cheap compared to knowing in advance which wording is optimal. Tested across 24 NLP tasks, APE-generated prompts matched or outperformed human-crafted instructions on 19 of them — a result that was surprising in late 2022 when manual prompt engineering was still treated as a specialized craft requiring deep model intuition. The paper also showed APE-generated prompts improve model truthfulness and informativeness when prepended to standard prompts, and work well in few-shot learning setups.

The broader implication is that instruction optimization is searchable and automatable, which foreshadowed the trajectory of the field. OPRO (Google, 2023) extended this with iterative LLM-based refinement. [DSPy](/notes/dspy/) (Stanford, 2023) built a full programming framework around the idea. APE sits at the beginning of this line — the first rigorous demonstration that prompt space search is both tractable and worth doing.

## Key points

- APE generates candidate instructions from input-output demonstrations, scores each by task performance, selects the best — no human in the loop
- Outperforms or matches human-written prompts on 19/24 NLP benchmarks; sometimes exceeds zero-shot chain-of-thought baselines
- Prompt engineering reframed as discrete program search over instruction space — same problem class as program synthesis
- APE-generated prompts improve truthfulness on TruthfulQA and informativeness benchmarks
- Direct precursor to OPRO, [DSPy](/notes/dspy/), and the broader automated prompt optimization ecosystem
- Authors: Yongchao Zhou, Jimmy Ba et al. (Toronto/Vector Institute); arXiv 2211.01910

[Original paper](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/large_language_models_are_huma.pdf)
