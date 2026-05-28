---
title: "Compute Watch: LLM Compute Costs and GPU Availability Tracker"
date: 2023-08-03
categories:
  - llm
  - compute
  - gpu
  - cost
  - infrastructure
description: Compute Watch is a tracker for LLM compute costs and GPU availability — benchmarking inference costs across providers and tracking H100/A100 spot availability. Useful for anyone making infrastructure decisions around model serving costs.
params:
  source: pinboard
  sourceUrl: https://computewatch.llm-utils.org/
---

![Compute Watch: LLM Compute Costs and GPU Availability Tracker](/images/notes/compute-watch-llm-compute.png)

## Summary

Compute Watch (from llm-utils.org, the same site tracking Nvidia H100 supply and demand) monitors and benchmarks the cost of LLM inference compute across cloud providers. In 2023, GPU availability was highly constrained and pricing was opaque — H100 spot instances were backordered months out at AWS, GCP, and Azure, while specialty GPU cloud providers (CoreWeave, Lambda Labs, Vast.ai) offered different availability and pricing profiles.

The site tracks cost-per-token across different providers for common models, spot instance availability for H100 and A100 GPUs, and on-demand pricing benchmarks. For teams deciding whether to use managed LLM APIs (OpenAI, Anthropic) vs. hosting their own models on GPU infrastructure, this kind of cost data is essential. The build-vs-buy decision in 2023 was almost never about technical capability — it was about TCO at the expected query volume.

The broader context: the GPU shortage of 2023 created a two-tier market. Companies with long-term compute contracts or reserved instances (having anticipated demand) had capacity; everyone else paid spot prices or waited. This drove significant interest in CPU-based inference (llama.cpp, Ollama) and quantization techniques that reduced GPU memory requirements.

## Key points

- Tracks LLM inference costs per token across managed APIs (OpenAI, Anthropic) and self-hosted options.
- Monitors H100 and A100 GPU spot availability — critical data during the 2023 compute shortage.
- Enables the build-vs-buy TCO calculation for LLM serving infrastructure decisions.
- GPU shortage drove interest in llama.cpp/Ollama CPU inference and quantization to reduce requirements.
- From llm-utils.org, which also tracked Nvidia H100 supply/demand dynamics.

[Original](https://computewatch.llm-utils.org/)
