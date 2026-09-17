---
title: "GPT-Neo: Open Source GPT-3 Scale Language Models"
date: 2021-03-22
categories:
  - llm
  - open-source
  - gpt
  - machine-learning
  - nlp
description: GPT-Neo is EleutherAI's open-source implementation of GPT-style language models at GPT-3 scale — the first serious open attempt to replicate GPT-3's capabilities before open-weight models became common. Historically significant as the origin of the open LLM movement.
params:
  source: pinboard
  sourceUrl: https://github.com/EleutherAI/gpt-neo
---

![GPT-Neo: Open Source GPT-3 Scale Language Models](/images/notes/gpt-neo-eleutherai.png)

## Summary

GPT-Neo is EleutherAI's open-source implementation of GPT-style autoregressive language models, designed to reach GPT-3 scale (125M to 20B parameters) using mesh-tensorflow for model parallelism. It was released in early 2021 when GPT-3 was only available through OpenAI's controlled API with a waiting list — GPT-Neo was the first serious open attempt to make comparable models freely available.

EleutherAI is a grassroots research collective that formed explicitly to build open alternatives to OpenAI's increasingly closed models. GPT-Neo was trained on The Pile — a massive 825GB text dataset also assembled by EleutherAI and released open-source. The combination of open weights + open training data was a deliberate ideological stance: the frontier of AI shouldn't be controlled by a single organization.

From a 2026 vantage point, GPT-Neo is historically significant as the starting point of what became the open LLM movement. It directly led to GPT-J (6B params, often better than GPT-3 on many benchmarks), then GPT-NeoX (20B), then informed the development of models like LLaMA at Meta, which triggered the current era of widely available open-weight foundation models.

## Key points

- First open-source GPT-3 scale language model — released when GPT-3 was API-only with a waitlist.
- By EleutherAI — grassroots research collective committed to open AI.
- Trained on The Pile — 825GB open-source text dataset, also from EleutherAI.
- Lineage: GPT-Neo → GPT-J → GPT-NeoX → influenced LLaMA and the modern open-weight LLM ecosystem.
- Used mesh-tensorflow for model parallelism across multiple GPUs/TPUs.

[Original](https://github.com/EleutherAI/gpt-neo) → GitHub
