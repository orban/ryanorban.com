---
title: "Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity"
date: 2022-10-05
categories:
  - few-shot-learning
  - prompt-engineering
  - nlp
  - llm
  - research
description: ""
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Fantastically Ordered Prompts and Where to Find Them- Overcoming Few-Shot Prompt Order Sensitivity.pdf
---

## Summary

Tony Zhao, Eric Wallace, Shi Feng, Dan Klein, and Sameer Singh (ACL 2021) systematically document a fragile aspect of few-shot prompting: the order in which examples appear in the prompt dramatically affects performance, with variance across orderings sometimes exceeding 30 percentage points on the same task and model. This isn't a minor noise issue — it means that practitioners who report few-shot results on a single ordering may be reporting a lucky draw rather than a reliable capability.

The paper's analysis covers multiple tasks and several GPT-3 model sizes. The key finding: models are significantly biased toward predicting labels that appear more frequently at the end of the prompt (recency bias) and labels that appear more often overall in the prompt (majority label bias). These biases are model-size dependent and vary across tasks, making them hard to control without principled ordering strategies. The variance problem scales with the number of examples — more examples in context means more possible orderings means more sensitivity.

To address this, the authors propose heuristics for ordering selection: calibrate based on expected output distribution and use global entropy scores to pick orderings that balance label representation. These heuristics work significantly better than random and reveal that the "right" ordering aligns with the model's prior — the underlying insight being that demonstrations shape not just the task but the model's probability estimates for output tokens. This connects to work on prompt sensitivity in general (see `inbox/2022-03-15-reframing-instructional-prompts-gptk.md`) and the theoretical framing in Prompt Programming for Large Language Models (`inbox/2021-11-01-prompt-programming-llms-beyond-few-shot.md`) that prompts are programs specifying a computation.

## Key points

- Few-shot prompting is highly sensitive to example order — variance across orderings can exceed 30% on classification benchmarks
- Two main biases identified: **recency bias** (models over-predict labels that appeared last) and **majority label bias** (models over-predict the most common label in the prompt)
- Bias magnitude varies by model size and task — can't be assumed away with larger models
- Calibration heuristics: use global entropy scores over orderings to select more balanced, label-representative sequences
- Results imply that published few-shot numbers on a single ordering may be misleading — the field needs better evaluation practices
- Pairs with DART (`inbox/2022-07-30-dart-differentiable-prompt-few-shot-learning.md`) and T0 (`inbox/2022-07-27-multitask-prompted-training-t0-zero-shot.md`) for a full picture of few-shot learning challenges and solutions

[Source PDF](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Fantastically Ordered Prompts and Where to Find Them- Overcoming Few-Shot Prompt Order Sensitivity.pdf)
