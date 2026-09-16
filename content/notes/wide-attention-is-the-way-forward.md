---
title: Wide Attention Is The Way Forward for Transformers
date: 2022-10-12
categories:
  - transformers
  - architecture
  - scaling
  - nlp
  - inference
description: ""
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Wide over Deep Transformers .pdf
---

blurb: "A Cambridge/Imperial/Oxford study showing that single-layer wide transformers can match or outperform deeper multi-layer counterparts across NLP tasks, with 3× faster inference and smaller memory footprint. Challenges the deep-is-better orthodoxy that dominated the field."

## Summary

Jason Ross Brown, Yiren Zhao, Ilia Shumailov, and Robert Mullins (Cambridge, Imperial College, Oxford) present a systematic study of transformer architecture aspect ratio — the tradeoff between number of layers and number of attention heads per layer. Their finding is counterintuitive: on average across four NLP tasks and ten attention types, single-layer wide models perform 0.3% *better* than equally-parameterized deep counterparts, and do so with significant practical advantages.

The paper's methodology holds total attention head count and all other hyperparameters constant while varying how those heads are distributed across layers. This isolates the depth-vs-width tradeoff cleanly. Wide models turn out to require far less memory bandwidth (no residual stream accumulation across layers) and run faster on commodity hardware — a single-layer IMDb classifier is 3.1× faster on CPU than its equally-accurate deep version, at half the size.

The result matters for deployment contexts where inference latency and memory dominate. It also connects to interpretability work: single-layer models expose all attention patterns at once, making them more amenable to [mechanistic interpretability](/notes/mechanistic-interpretability/) analysis. The paper predates mixture of experts and speculative decoding as deployment optimization strategies, but points toward a neglected axis of model architecture design.

## Key points

- Single-layer wide transformer models average 0.3% better than deep counterparts across 4 NLP tasks and 10 attention types when total parameter count is held constant
- 3.1× faster CPU inference and ~2× smaller memory footprint compared to deep counterparts of equal accuracy
- Wide models are more interpretable: all attention computation is visible in a single layer, aiding [mechanistic interpretability](/notes/mechanistic-interpretability/)
- The depth-vs-width tradeoff is underexplored; most scaling laws research focused on depth or uniform scaling
- arXiv:2210.00640 (Brown, Zhao, Shumailov, Mullins, 2022)

[Original paper](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Wide over Deep Transformers .pdf)
