---
title: "SURD: Synergistic-Unique-Redundant Decomposition of Causality"
date: 2024-11-12
categories:
  - research
  - information-theory
  - causality
  - turbulence
  - python
description: SURD is a Python library for decomposing causality into synergistic, unique, and redundant components in complex systems — quantifying how different variables jointly contribute to predicting future states. Developed for turbulence analysis but applicable to any causal inference problem.
params:
  source: pinboard
  sourceUrl: https://github.com/Computational-Turbulence-Group/SURD
---

![SURD: Synergistic-Unique-Redundant Decomposition of Causality](/images/notes/surd-causality-decomposition.png)

## Summary

SURD (Synergistic-Unique-Redundant Decomposition) is a Python library from the Computational Turbulence Group for decomposing causal relationships in complex systems. The core idea: when multiple variables jointly cause an outcome, you can partition their causal contribution into three types — synergistic (only present when variables act together), unique (contributed by one variable alone), and redundant (information shared across multiple variables).

The framework is built on information theory — specifically, measuring information gain about future states from past observations. This makes it non-parametric and applicable across domains without assuming linear relationships or specific data distributions. The non-intrusive design means you only need pairs of past and future observations, making it usable on experimental data without requiring a full model of the system.

The primary application domain is turbulence analysis (hence the research group), where understanding how different flow structures causally interact is fundamental to both physics and engineering. But the framework is general — applicable to any system where you want to understand how multiple variables jointly determine outcomes: neuroscience, climate science, economics, or machine learning model analysis.

## Key points

- Decomposes causal contributions into synergistic, unique, and redundant components.
- Built on information theory — non-parametric, no linearity assumptions.
- Non-intrusive: only requires pairs of past/future observations, no full model needed.
- Primary domain: turbulence analysis, but general-purpose causal inference tool.
- Tutorials included for turbulence and other complex system applications.

[Original](https://github.com/Computational-Turbulence-Group/SURD) → GitHub
