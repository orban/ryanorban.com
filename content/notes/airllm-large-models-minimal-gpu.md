---
title: "AirLLM: 70B LLMs on a 4GB GPU"
date: 2023-12-28
categories:
  - llm
  - inference
  - memory-optimization
  - open-source
  - ml-infrastructure
description: AirLLM runs 70B LLMs on a single 4GB GPU and 405B Llama3.1 on 8GB VRAM — without quantization, distillation, or pruning. It optimizes inference memory usage itself rather than compressing the model, preserving full model quality on consumer hardware.
params:
  source: pinboard
  sourceUrl: https://github.com/lyogavin/Anima/tree/main/air_llm
---

![AirLLM: 70B LLMs on a 4GB GPU](/images/notes/airllm-large-models-minimal-gpu.png)

## Summary

AirLLM is a memory optimization framework for LLM inference that enables running models far larger than would typically fit in available GPU memory — without changing the model through quantization, distillation, or pruning. The headline claim: Llama 2 70B on a single 4GB GPU, and Llama 3.1 405B on 8GB VRAM.

The technique focuses on inference-time memory management rather than model compression. Instead of fitting all model weights in GPU memory simultaneously, it optimizes how weights are loaded, cached, and released during the forward pass — exploiting the layered structure of transformer models to minimize peak memory usage. This preserves the full float32 (or bfloat16) model quality that quantization trades away.

The practical implication is significant for researchers and developers without access to high-end GPU clusters: you can run state-of-the-art open models like Llama 3.1 on consumer hardware for experiments, fine-tuning evaluation, or inference tasks that don't require production throughput. The tradeoff is speed — inference is slower than on a properly-sized GPU — but for tasks where latency isn't critical, AirLLM removes what was a hard barrier. The project later moved to a dedicated repository at github.com/lyogavin/airllm.

## Key points

- Llama 2 70B on 4GB GPU, Llama 3.1 405B on 8GB VRAM — no quantization or pruning.
- Memory optimization at inference time, not model compression — preserves full model quality.
- Exploits layered transformer structure to minimize peak VRAM usage.
- Trade-off is inference throughput — slower than properly-sized GPU but enables experiments on consumer hardware.
- Relevant for researchers without GPU cluster access who want to run full-precision SOTA models.
- Project migrated to [github.com/lyogavin/airllm](https://github.com/lyogavin/airllm) for ongoing development.

[Original](https://github.com/lyogavin/Anima/tree/main/air_llm) → GitHub
