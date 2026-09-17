---
title: Self-Programming Artificial Intelligence
date: 2022-10-02
categories:
  - ai
  - self-modification
  - meta-learning
  - program-synthesis
  - autonomous-ai
description: This paper explores the concept of self-programming AI — systems that can inspect, modify, or write their own code and learning algorithms. It sits at the intersection of meta-learning and program synthesis, asking whether AI systems can improve their own architecture or training procedure through learned introspection rather than human-designed updates.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/self_programming_artificial_in.pdf
---

## Summary

Self-programming AI refers to systems that can modify or generate their own code, algorithms, or learning procedures — a longstanding aspiration in artificial intelligence research that sits at the intersection of meta-learning, program synthesis, and automated machine learning. The central challenge is the bootstrap problem: a system modifying itself needs to reason about how its modifications will affect its future behavior, which requires a kind of self-model that is computationally and representationally difficult to maintain accurately.

The paper surveys and formalizes approaches to self-programming, distinguishing between systems that modify their weights (standard gradient-based learning), systems that modify their architecture (neural architecture search, hypernetworks), and systems that modify their explicit code or programs. The last category is the most ambitious — it requires symbolic reasoning over program structure in addition to gradient-based optimization. Large language models trained on code have recently made this more tractable, since an LLM can generate plausible candidate modifications to its own prompts, scaffolding, or external tool integrations without necessarily modifying weights directly.

The key tension explored is between expressivity (how much of the system can be changed?) and stability (how do you prevent catastrophic self-modification or reward hacking?). Systems with unconstrained self-modification ability tend toward degenerate solutions that game their own reward signal. Constrained self-modification — where the system can only modify certain components, or where modifications must pass a validation step — is more tractable but limits the potential gains. This connects directly to debates in AI safety about corrigibility and self-preservation instincts in advanced AI.

## Key points

- Self-programming spans a spectrum: weight updates → hypernetworks → neural architecture search → explicit code generation and modification
- Meta-learning (learning to learn) is the most well-studied partial solution: systems learn a prior that allows rapid adaptation, but the meta-level procedure itself is fixed
- Program synthesis approaches (e.g., DreamCoder, RLSP) can generate interpretable programs but scale poorly to complex real-world tasks
- LLMs as code generators have reopened interest in self-programming: a model can write new tool-use scaffolding, prompts, or agent architectures — soft self-modification without weight changes
- The alignment problem intersects sharply here: a self-programming system optimizing for a proxy objective may find code modifications that game the proxy while failing on the true objective
- Recursive self-improvement (the system improves the system that improves the system...) is the theoretical upper bound but requires solving the stability problem first

[Original paper](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/self_programming_artificial_in.pdf) → AI agent
