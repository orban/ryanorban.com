---
title: Temporal Neural Networks
date: 2022-07-07
categories:
  - neural-networks
  - temporal
  - spiking-neural-networks
  - time-series
  - neuroscience
description: A paper on Temporal Neural Networks, architectures that encode time as a first-class computation dimension rather than implicitly through state, likely in the context of spiking neural networks or neuromorphic computing. Saved July 2022; specific paper identity unclear from the filename alone.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Temporal NN.pdf
---

## Summary

A paper on [Temporal Neural Networks](/notes/temporal-neural-networks/) (TNN) — neural architectures designed to model temporal dynamics explicitly, likely in the context of spiking neural networks or recurrent architectures for time series processing. Saved July 2022, a period of active research into biologically plausible neural computation and the intersection of neuroscience-inspired architectures with practical sequence modeling.

[Temporal neural networks](/notes/temporal-neural-networks/) broadly refer to architectures that encode time as a first-class dimension of computation, either by using spike timing as the primary information carrier (as in spiking neural networks) or by building temporal structure directly into weights and activation functions. This distinguishes them from standard recurrent neural networks (which process time implicitly through state) and transformers (which process time through positional encodings).

The document title Temporal NN doesn't map to a specific widely-known paper, so this may be course notes, a technical report, or a preprint from a specific research group working on biologically-motivated or neuromorphic temporal processing. The July 2022 timeframe predates the major neuromorphic computing publications that came later. Connections exist to neuromorphic computing, predictive coding, and the NeuroAI research program that bridges computational neuroscience and deep learning.

## Key points

- Temporal neural networks encode time as a first-class computation dimension rather than implicitly through state
- Related to spiking neural networks, where spike timing carries information — distinct from rate-coded networks
- Connects to neuromorphic computing hardware platforms like Intel Loihi and IBM TrueNorth
- Relevant to time series processing, event-based sensing (e.g., event cameras), and low-power inference
- Biologically motivated: mirrors how the brain encodes temporal relationships through relative spike timing

[Source PDF](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/Temporal%20NN.pdf)
