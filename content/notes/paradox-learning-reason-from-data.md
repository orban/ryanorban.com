---
title: On the Paradox of Learning to Reason from Data
date: 2022-09-29
categories:
  - reasoning
  - nlp
  - generalization
  - benchmark
  - research
description: "Zhang, Li, Meng, Chang, and Van den Broeck (UCLA) show that BERT achieves near-perfect accuracy on in-distribution logical reasoning problems while completely failing to generalize to other distributions over the same problem space. The explanation: BERT learned statistical features of the logical reasoning distribution, not the underlying reasoning function — a fundamental distinction between benchmark performance and genuine reasoning."
params:
  source: papers
  sourceUrl: https://arxiv.org/abs/2205.11502
---

## Summary

Honghua Zhang, Liunian Harold Li, Tao Meng, Kai-Wei Chang, and Guy Van den Broeck at UCLA (arXiv:2205.11502, 2022) expose a paradox in evaluating neural reasoning: BERT achieves near-perfect accuracy on in-distribution test examples from a logical reasoning task but fails completely when the same problem space is sampled from a different distribution. The problem space (SimpleLogic) is precisely defined — thousands of rules and facts, combinatorially many consistent reasoning problems — so there's no ambiguity about whether the task is within the model's training scope. The model knows the domain but can't reason in it.

The explanation is a careful analysis of what BERT actually learned. Rather than internalizing the correct reasoning function (modus ponens, chaining rules, etc.), BERT exploited **statistical features** that are inherent to the logical reasoning distribution it was trained on — co-occurrence patterns, lexical cues, surface regularities that correlate with correct answers in a particular distribution. When the problem distribution changes (same rules, different sampling), these statistical shortcuts no longer work. The paper calls this the paradox of learning to reason: a model can learn to ace a reasoning benchmark without learning to reason.

This result connects to broader debates about benchmark saturation, out-of-distribution generalization, and shortcut learning in deep learning. It's also relevant to the ongoing discussion about whether LLMs "reason" or perform sophisticated pattern matching — the paper suggests that benchmark performance alone can't answer this question, since a model can achieve near-perfect benchmark scores through statistical feature exploitation without having a generalizable reasoning procedure. The paper shows this is not a BERT-specific artifact: the results extend to T5 and the analysis applies to any neural model trained on NLP benchmarks.

## Key points

- BERT achieves near-perfect accuracy in-distribution but fails on different distributions over the **same** problem space — a controlled demonstration of reasoning non-generalization
- Explanation: BERT learned statistical features of the reasoning distribution, not the reasoning function itself (shortcut learning)
- SimpleLogic benchmark is precisely defined, ruling out ambiguity about task scope or capability boundary
- Results extend to T5 — not a BERT-specific failure, but a general property of neural models trained on reasoning benchmarks
- Directly challenges benchmark-based reasoning claims: high performance ≠ generalizable reasoning capability

[Original](https://arxiv.org/abs/2205.11502)
