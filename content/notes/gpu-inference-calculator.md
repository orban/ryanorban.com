---
title: GPU Calculator for LLM Inference
date: 2025-07-25
categories:
  - machine-learning
  - infrastructure
  - gpu
  - llm
  - tools
description: An interactive calculator for estimating GPU requirements for LLM inference — input model size, quantization, batch size, and context length to get memory and throughput estimates. Practical first tool when planning self-hosted or cloud inference deployments.
params:
  source: pinboard
  sourceUrl: https://calculator.inference.ai/
---

![GPU Calculator for LLM Inference](/images/notes/gpu-inference-calculator.png)

## Summary

calculator.inference.ai is an interactive tool for estimating GPU memory requirements and throughput for LLM inference. You specify the model size (parameters), quantization level (fp16, int8, int4), batch size, and context length, and the calculator estimates VRAM requirements and approximate tokens-per-second for different GPU configurations.

The core use case is capacity planning. Before committing to hardware (buying a GPU, reserving cloud instances, choosing a hosting tier), you need to know whether a given model fits in a given GPU's memory and whether the throughput meets your latency requirements. Without a calculator, this requires either running experiments or manually working through the math: `(parameters × bytes_per_parameter) + (kv_cache_size × batch × context)`.

The calculation is particularly important for LLM models where quantization dramatically changes the memory footprint. A LLaMA 70B model at fp16 requires ~140GB (two A100s); at int4 it fits in ~35GB (one A100 or a high-VRAM consumer GPU). The calculator makes these tradeoffs concrete for deployment planning. Pairs with LM Studio and Ollama documentation for practical self-hosting decisions.

## Key points

- Estimates VRAM requirements and throughput for LLM inference given model/hardware parameters.
- Inputs: model size, quantization (fp16/int8/int4), batch size, context length.
- Outputs: memory requirements, estimated tokens/sec, GPU recommendations.
- Quantization trade-offs made concrete: 70B at fp16 vs int4 is ~140GB vs ~35GB.
- Essential planning tool before committing to self-hosted inference hardware or cloud spend.
- Pairs with Ollama for local deployment and cloud pricing for cost modeling.

[Original](https://calculator.inference.ai/)
