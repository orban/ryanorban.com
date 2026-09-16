---
title: "STaR: Bootstrapping Reasoning With Reasoning"
date: 2022-10-06
categories:
  - reasoning
  - chain-of-thought
  - self-improvement
  - language-models
  - few-shot
description: ""
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/STaR Self Taught Reasoner.pdf
---

blurb: "STaR introduces a method for teaching language models to reason by having them bootstrap their own chain-of-thought rationales iteratively, filtering on correctness and finetuning on the survivors. It's a clean demonstration that models can improve their reasoning capability without external supervision, using their own successful inferences as training signal."

## Summary

STaR (Self-Taught Reasoner), by Eric Zeiler and Noah Goodman at Stanford, proposes a simple but effective loop for improving chain-of-thought reasoning: give the model a handful of examples with rationales, have it generate rationales for new problems, keep only the ones that lead to correct answers, and finetune on them. Then repeat. The process is reminiscent of expectation-maximization — at each iteration the model's reasoning ability improves, which unlocks harder problems that were previously out of reach.

The method addresses a core limitation of few-shot prompting: with a fixed set of hand-written examples, the model is constrained to the reasoning style of those examples and can't improve. STaR's iterative loop breaks this ceiling. One key detail is *rationalization*: when the model gets an answer wrong even with a hint, it's shown the correct answer and asked to produce a rationale post-hoc, then finetuned on that. This allows the model to mine signal from problems it couldn't solve cold.

Experiments on CommonsenseQA and arithmetic benchmarks show significant gains over direct finetuning and standard few-shot prompting. The work is an early step toward self-improvement in language models — a research direction that would later expand into RLHF, STaR-variants, and test-time compute methods like process reward models.

## Key points

- Iterative rationale generation + filtering: only keep rationales that yield correct final answers as training signal for supervised finetuning
- *Rationalization* trick: if the model fails, show the correct answer and generate a rationale anyway, then train on it — extracting signal from failures
- The loop is model-agnostic and requires only a small labeled dataset and a base language model
- Chain-of-thought quality improves each iteration, unlocking harder problems that were initially unsolvable
- Precursor to process reward models and RLVR approaches: the core insight that reasoning traces can be self-generated training data

[Original paper](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/STaR Self Taught Reasoner.pdf)
