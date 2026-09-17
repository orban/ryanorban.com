---
title: "DSPy: Compiling Declarative Language Model Calls (SBTB23 talk)"
date: 2024-01-30
categories:
  - dspy
  - llm
  - programming
  - stanford
  - talk
  - video
description: Omar Khattab's ScalaBytesConf 2023 talk introducing DSPy — the core presentation that launched the framework into wider attention. Covers the compile-don't-prompt philosophy and demonstrates self-improving LLM pipelines.
params:
  source: pinboard
  sourceUrl: https://www.youtube.com/embed/Dt3H2ninoeY
---

![DSPy: Compiling Declarative Language Model Calls (SBTB23 talk)](/images/notes/dspy-talk-omar-khattab.png)

## Summary

Omar Khattab's talk at ScalaBytesConf 2023 introduces DSPy — the Stanford NLP framework for writing LLM programs as declarative, compilable pipelines rather than hand-crafted prompts. This talk is the primary artifact that brought DSPy into wider practitioner awareness, preceding the surge of tutorials and blog posts about the framework.

The central argument Khattab makes: the current practice of writing prompts by hand is analogous to writing assembly — it's optimizing at the wrong level of abstraction, and the optimizations are brittle across model versions and data distributions. DSPy moves this work up a level: you declare signatures (what goes in, what comes out) and the compiler finds the optimal prompts and few-shot examples through automated search against a small labeled dataset. This is the compile-don't-prompt philosophy.

The self-improving part of the title refers to DSPy's ability to reoptimize pipelines when conditions change — new training data, model upgrade, task shift. Because the optimization is automated, you don't manually re-engineer prompts; you re-compile. The talk demonstrates this with retrieval-augmented QA pipelines where DSPy discovers prompt strategies that outperform hand-tuned baselines. Connects to DSPy's later work including MIPROv2 optimization and Arbor's RL-based extension.

## Key points

- Omar Khattab introduces DSPy at ScalaBytesConf 2023 — the talk that launched wider adoption.
- Core argument: hand-written prompts are assembly code — DSPy compiles up a level.
- Declarative signatures + automated prompt optimization via labeled examples.
- "Self-improving": pipelines reoptimize when model or data changes — recompile, don't re-engineer.
- From Stanford NLP — connects to broader knowledge graph and RAG research traditions.
- See also: [DSPy gentle introduction](/notes/dspy-gentle-introduction/), Arbor (RL extension), Ax (TypeScript port).

[Original](https://www.youtube.com/embed/Dt3H2ninoeY)
