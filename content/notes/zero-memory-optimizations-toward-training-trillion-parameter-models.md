---
title: "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models"
date: 2022-08-10
categories:
  - distributed-training
  - deep-learning
  - memory-optimization
  - microsoft
  - large-language-models
description: ZeRO (Zero Redundancy Optimizer) eliminates memory redundancy in distributed training by partitioning optimizer states, gradients, and parameters across data-parallel processes rather than replicating them. It enables training models 8x larger than prior methods on the same hardware and forms the foundation of Microsoft's DeepSpeed library.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/DeepSpeed.pdf
---

## Summary

ZeRO (Zero Redundancy Optimizer) solves a fundamental inefficiency in distributed training: when using data parallelism, every GPU holds a full replica of optimizer states, gradients, and model parameters — leading to enormous memory redundancy. ZeRO partitions these across data-parallel processes instead, so each GPU holds only its share, reducing per-device memory consumption dramatically without sacrificing the communication efficiency that makes data parallelism attractive.

The technique operates in three stages of increasing aggressiveness: partitioning optimizer states (ZeRO-1), adding gradient partitioning (ZeRO-2), and finally partitioning model parameters as well (ZeRO-3). Each stage compounds the memory savings, with ZeRO-3 enabling training of models 8x larger than was previously possible on the same hardware. This is the technical foundation of DeepSpeed, Microsoft's open-source distributed training library.

ZeRO's significance extends beyond the specific paper: it reframed how the field thinks about scaling. Rather than requiring specialized model parallelism strategies that complicate training code, ZeRO achieves many of the same memory benefits while keeping the data-parallel programming model intact. It directly enabled the wave of very large language models that followed, including early large-scale pretraining runs at Microsoft and elsewhere.

## Key points

- ZeRO partitions optimizer states, gradients, and parameters across data-parallel ranks instead of replicating them
- Three stages of partitioning compound memory savings; ZeRO-3 enables 8x larger models on the same hardware
- Retains data parallelism's communication efficiency while eliminating its memory redundancy
- Foundational technology behind DeepSpeed, Microsoft's distributed training library
- Made trillion-parameter model training feasible without complex model-parallelism infrastructure

[Original](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/DeepSpeed.pdf)
