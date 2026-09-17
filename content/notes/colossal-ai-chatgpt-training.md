---
title: "Colossal-AI: Open-Source ChatGPT Training Replication"
date: 2023-02-19
categories:
  - llm
  - training
  - open-source
  - rlhf
  - distributed-training
description: Colossal-AI released an open-source implementation of the ChatGPT training process (SFT + RLHF) that runs on a single GPU with 1.6GB memory — 7.73x faster than naive implementations. Made the ChatGPT training pipeline accessible to researchers without multi-GPU clusters.
params:
  source: pinboard
  sourceUrl: https://www.hpc-ai.tech/blog/colossal-ai-chatgpt
---

![Colossal-AI: Open-Source ChatGPT Training Replication](/images/notes/colossal-ai-chatgpt-training.png)

## Summary

Colossal-AI from HPC-AI Tech is an open-source distributed training framework optimized for large AI models. In February 2023, they released an implementation of the full ChatGPT training pipeline — SFT (supervised fine-tuning) + RLHF (reinforcement learning from human feedback with PPO) — that runs on a single consumer GPU with only 1.6GB of GPU memory, claiming 7.73x faster training than equivalent naive implementations.

The memory reduction is the headline achievement. The RLHF training process typically requires loading multiple models simultaneously — the policy model being trained, a reference model (to compute KL divergence), a reward model, and a value model. Colossal-AI applies gradient checkpointing, mixed-precision training, and their own memory management techniques to bring this under a single-GPU memory budget.

The February 2023 timing is significant: this appeared simultaneously with ChatLLaMA (nebullvm), Alpaca (Stanford), and other efforts to democratize ChatGPT-style training. Colossal-AI's contribution was specifically the efficiency angle — making the training accessible not just in terms of code but in terms of hardware requirements. Running RLHF on a single 24GB GPU was qualitatively different from running it on an 8-GPU A100 cluster.

## Key points

- Full ChatGPT training pipeline (SFT + RLHF with PPO) in open-source code.
- 1.6GB single-GPU minimum memory — enables training on consumer hardware via Colossal-AI's memory management.
- 7.73x speed improvement over naive implementations through gradient checkpointing and mixed precision.
- HPC-AI Tech — Chinese research group with deep expertise in distributed training efficiency.
- February 2023 — part of the first wave of open ChatGPT replication efforts alongside Alpaca and ChatLLaMA.

[Original](https://www.hpc-ai.tech/blog/colossal-ai-chatgpt)
