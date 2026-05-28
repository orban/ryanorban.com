---
title: "Self-Refine: Iterative LLM Output Improvement via Self-Feedback"
date: 2023-04-08
categories:
  - llm
  - reasoning
  - research
  - self-improvement
  - prompting
description: Self-Refine is a framework where LLMs generate feedback on their own outputs and iteratively refine them — no human feedback, no gradient updates. Shows that a single LLM can be its own critic and improve outputs across diverse tasks.
params:
  source: pinboard
  sourceUrl: https://github.com/madaan/self-refine
---

## Summary

Self-Refine is a research framework demonstrating that LLMs can iteratively improve their own outputs by generating feedback on them and then revising based on that feedback. The loop: generate an initial output → generate critique of that output → revise based on the critique → repeat until satisfied or iteration limit reached. No additional training, no human feedback, no reward model — just the same LLM acting as both producer and critic.

The key finding: across diverse tasks (code optimization, math reasoning, sentiment rewriting, dialogue response generation), this self-feedback loop significantly improves output quality over a single generation pass. The improvement comes from the model's ability to identify errors or weaknesses from a different perspective — evaluating a completed output is a different cognitive stance than generating it, and LLMs exploit this asymmetry.

Self-Refine connects to a cluster of related ideas from 2023: [Constitutional AI](/notes/constitutional-ai/) from Anthropic (self-critique to align model behavior), Reflexion (self-reflection for agent error correction), and chain-of-thought prompting (extended generation improving reasoning). The unifying insight: inference-time computation spent on critique and revision often pays off more than a larger model or longer initial generation. This became foundational to later work on test-time compute scaling and the use of verifiers to select among multiple generations.

## Key points

- Generate → Critique → Revise loop using a single LLM — no fine-tuning, no human labels.
- Works across diverse tasks: code, math, dialogue, text rewriting, sentiment editing.
- Exploits the asymmetry between generation and evaluation — critiquing is easier than generating correctly the first time.
- Related to [Constitutional AI](/notes/constitutional-ai/), Reflexion, and test-time compute scaling research.
- Practical implication: spending more inference compute on self-refinement can outperform switching to a larger model.
- Foundation for later work on LLM output verification and multi-attempt generation with selection.

[Original](https://github.com/madaan/self-refine) → GitHub, AI agent
