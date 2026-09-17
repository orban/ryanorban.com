---
title: "Compute-Optimal LLMs: Chinchilla Scaling Calculator"
date: 2023-01-24
categories:
  - llm
  - scaling-laws
  - compute
  - research
  - chinchilla
description: howmanyparams.com is a calculator for compute-optimal LLM training based on Chinchilla scaling laws — given a compute budget, it tells you the optimal model size and token count. A practical tool for applying the Hoffmann et al. scaling law findings.
params:
  source: pinboard
  sourceUrl: https://howmanyparams.com/
---

![Compute-Optimal LLMs: Chinchilla Scaling Calculator](/images/notes/compute-optimal-llms-chinchilla.png)

## Summary

howmanyparams.com is a web calculator for compute-optimal large language model training based on the Chinchilla scaling laws from DeepMind's 2022 paper "Training Compute-Optimal Large Language Models" by Hoffmann et al. Given a compute budget (in FLOPs or GPU-hours), the calculator outputs the optimal model size (parameters) and training token count.

The Chinchilla paper's key finding was that prior models — including GPT-3 — were significantly undertrained relative to their parameter count. The optimal ratio, according to the paper's analysis, is roughly 20 tokens of training data per parameter. A 70B parameter model trained compute-optimally should see around 1.4 trillion tokens — much more than GPT-3's 300B tokens for 175B parameters. LLaMA 1 and 2, and many subsequent open models, explicitly targeted Chinchilla-optimal training regimes.

The calculator makes this actionable: if you have a specific GPU budget, it translates Chinchilla's empirical scaling laws into a concrete recommendation for how to allocate that compute between model size and training tokens. This matters because under-training large models wastes compute — you'd get better results with a smaller model trained longer on the same budget.

## Key points

- Calculator for Chinchilla compute-optimal LLM training — given budget, outputs optimal size + tokens
- Based on Hoffmann et al. (DeepMind, 2022): optimal is ~20 training tokens per parameter
- GPT-3 (175B params, 300B tokens) was undertrained by Chinchilla standards
- LLaMA explicitly targeted Chinchilla-optimal training; influenced the open LLM ecosystem
- Practically useful: converts GPU-hour budget into model size + token count recommendations

[Original](https://howmanyparams.com/)
