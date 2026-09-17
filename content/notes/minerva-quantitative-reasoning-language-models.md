---
title: Solving Quantitative Reasoning Problems with Language Models (Minerva)
date: 2022-08-17
categories:
  - llm
  - math
  - reasoning
  - google
  - research
  - stem
description: Lewkowycz et al. at Google Research introduce Minerva, a language model pretrained on general text and further trained on technical content that achieves state-of-the-art on quantitative reasoning benchmarks without external tools. It correctly answers nearly a third of undergraduate-level science problems — an early proof that domain-specific pretraining unlocks STEM reasoning at scale.
params:
  source: papers
  sourceUrl: https://arxiv.org/abs/2206.14858
---

## Summary

Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, and colleagues at Google Research (arXiv:2206.14858, Jul 2022) introduce Minerva, a large language model pretrained on general natural language data and then further trained on a curated corpus of technical content — scientific papers, mathematics textbooks, and course notes. The key design insight is that quantitative reasoning requires a different pretraining distribution than general language tasks, and that targeted continued pretraining can close a substantial capability gap without architectural changes.

Minerva achieves state-of-the-art performance on technical benchmarks including MATH and MMLU-STEM without using external tools like calculators or computer algebra systems. The model generates step-by-step solutions entirely in natural language and mathematical notation. On over 200 undergraduate-level problems spanning physics, biology, chemistry, economics, and other sciences requiring quantitative reasoning, Minerva correctly answers nearly a third — a striking result given the difficulty of these problems and the absence of any symbolic computation support.

The paper is significant because it shifts the narrative around LLM math failure. Prior work treated quantitative reasoning as a fundamental limitation of next-token prediction; Minerva shows the limitation was largely one of pretraining data. The model's success also raises important questions about the boundary between few-shot reasoning and memorization — a concern the authors address by showing the model can solve novel problem variants not seen in training. Minerva prefigures later work on math-focused models like DeepMind's AlphaCode and the Gemini family's reasoning capabilities, and directly influenced the design of STEM-specialized training pipelines.

## Key points

- Continued pretraining on technical content (papers, textbooks) is sufficient to produce strong quantitative reasoning — no architectural changes needed
- Achieves state-of-the-art on MATH and MMLU-STEM without external tools; generates full solution chains in natural language
- Correctly solves ~30% of undergraduate-level multi-step science problems across five domains
- Demonstrates that LLM quantitative reasoning failures are primarily a data distribution problem, not a fundamental limitation of transformer architectures
- Prefigures the approach used in math-specialized LLMs and reasoning-focused training pipelines (DeepSeek-Math, Qwen-Math, etc.)

[Original](https://arxiv.org/abs/2206.14858)
