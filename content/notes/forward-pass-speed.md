---
title: How fast can we perform a forward pass?
date: 2022-06-22
categories:
  - machine-learning
  - transformers
  - hardware
  - inference
  - performance
description: A deep technical investigation into the theoretical and practical speed limits of a single transformer forward pass, accounting for compute, memory bandwidth, and hardware constraints. The answer matters for inference costs, latency SLAs, and understanding where efficiency gains are actually possible.
params:
  source: pinboard
  sourceUrl: https://bounded-regret.ghost.io/how-fast-can-we-perform-a-forward-pass/
---

## Summary

This post from bounded-regret by Jacob Steinhardt (with thanks to Hao Zhang, Kayvon Fatahalian, and Jean-Stanislas Denain) asks a precise question: what is the minimum time to run one transformer forward pass? The question isn't academic — inference costs at scale are enormous, and understanding theoretical limits helps identify where optimization work pays off.

The analysis breaks the problem into two regimes: compute-bound and memory-bound operations. Matrix multiplications in the FFN layers and attention projection layers are compute-bound — the GPU's FLOPs are the bottleneck. The KV cache reads in autoregressive decoding are memory-bandwidth-bound — the bottleneck is how fast you can stream weights from HBM into compute. These two regimes have very different optimization strategies: for compute-bound operations you want larger batches; for memory-bound operations you want to minimize data movement.

The post derives that a single forward pass through a large transformer (e.g. 100B parameters) involves roughly O(12 * n_layers * d_model^2) FLOPs per token, plus attention cost that scales with sequence length. At the hardware limits of 2022 A100 GPUs (~312 TFLOPS BF16), even ignoring memory constraints, a single token forward pass through a large model takes milliseconds. In practice, batching and pipeline parallelism are essential to saturate hardware, which explains why serving latency and throughput have very different optimization paths.

## Key points

- Transformer forward pass splits into compute-bound (matrix multiplications) and memory-bound (KV cache reads) operations
- A single autoregressive decoding step is almost always memory-bandwidth-limited — you're streaming weights for one token
- Batch inference amortizes weight reads across many tokens simultaneously, shifting back to compute-bound regime
- A100 GPU at full utilization: roughly 312 TFLOPS BF16, ~2 TB/s HBM bandwidth — the ratio determines which regime you're in
- Practical implication: continuous batching strategies (Orca, vLLM) are so effective because they maximize hardware utilization by blending compute and memory phases
- Related work: Roofline model for analyzing compute vs bandwidth bounds; FlashAttention for memory-efficient attention computation

[Original](https://bounded-regret.ghost.io/how-fast-can-we-perform-a-forward-pass/)
