---
title: "Nvidia H100 GPUs: Supply and Demand"
date: 2023-08-01
categories:
  - gpu
  - nvidia
  - h100
  - infrastructure
  - compute
description: A detailed analysis of the Nvidia H100 GPU supply and demand situation in mid-2023 — how constrained supply was, where the demand was coming from, and what the bottlenecks were. Essential context for understanding the AI infrastructure market that year.
params:
  source: pinboard
  sourceUrl: https://gpus.llm-utils.org/nvidia-h100-gpus-supply-and-demand/
---

![Nvidia H100 GPUs: Supply and Demand](/images/notes/nvidia-h100-gpu-supply-demand.png)

## Summary

This piece from llm-utils.org analyzed the Nvidia H100 supply and demand situation at a moment when the GPU shortage was near its peak. H100 GPUs had become the critical infrastructure for training and serving LLMs — significantly faster than the A100 for transformer workloads due to Tensor Cores and NVLink bandwidth improvements. Nvidia simply couldn't manufacture them fast enough to meet the surge in demand triggered by ChatGPT's success.

The supply constraints came from multiple layers: TSMC wafer capacity for the H100's 4nm process node, CoWoS packaging for HBM memory integration, and HBM3 memory supply itself. Nvidia was selling out every allocation to hyperscalers (Microsoft, Google, Amazon, Meta) who had multi-thousand-card orders, leaving startups and research labs to scramble in the spot market.

The demand side: training frontier LLMs requires thousands of H100s. GPT-4 was estimated to have trained on over 20,000 A100s. Serving ChatGPT at scale required thousands more. Every AI company wanted clusters; available supply was a fraction of demand. This created the H100 spot market at astronomical prices and drove investment in alternatives: AMD MI300X, Google TPUv4/v5, AWS Trainium, and Cerebras wafer-scale chips.

The shortage shaped the 2023 AI landscape: it favored well-capitalized incumbents, drove interest in efficient inference (reducing compute requirements per query), and made CPU inference viable via llama.cpp for smaller models.

## Key points

- H100 shortage in 2023 stemmed from TSMC capacity, CoWoS packaging, and HBM3 memory constraints.
- Hyperscalers (Microsoft, Google, Meta, Amazon) locked up most supply with large allocations.
- Spot market prices were 2-5x on-demand prices; backlogs stretched months.
- Accelerated interest in AMD MI300X, Google TPU, AWS Trainium as alternatives.
- Drove efficiency research: quantization, speculative decoding, and CPU inference via llama.cpp.

[Original](https://gpus.llm-utils.org/nvidia-h100-gpus-supply-and-demand/)
