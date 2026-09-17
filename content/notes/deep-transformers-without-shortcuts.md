---
title: "Deep Transformers without Shortcuts: Modifying Self-attention for Faithful Signal Propagation"
date: 2022-12-07
categories:
  - deep-learning
  - transformers
  - neural-networks
  - nlp
description: NeurIPS 2022 paper investigating how to train very deep Transformers by removing shortcut connections (residual paths), which typically cause rank collapse in attention layers. The work has implications for understanding how information propagates through depth in Transformer architectures.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2786_deep_transformers_without_shor.pdf
---

## Summary

This NeurIPS 2022 paper by Anagnostidis et al. tackles a core instability in very deep Transformer architectures: the presence of residual connections (shortcuts) prevents the network from making full use of its depth. While shortcuts were introduced in ResNet to avoid vanishing gradients and are standard in BERT and GPT-style models, they create an implicit tendency toward rank collapse in the attention matrix — where all tokens converge to the same representation regardless of input. The authors propose modifications to self-attention that enable faithful signal propagation without relying on skip connections.

The paper draws on tools from signal propagation theory (specifically mean field theory as applied in works like Deep Information Propagation) to characterize when gradients and activations remain well-conditioned at initialization. The key insight is that standard softmax attention with residual streams inevitably loses signal fidelity as depth grows, but reparameterized attention variants can maintain expressive, rank-preserving representations across many layers. The proposed approach allows training Transformers with dozens of layers that actually improve with depth, rather than degrading due to shortcut dominance.

Empirically, the authors validate on language modeling and image classification benchmarks, showing that deeper models trained with their approach outperform shallower shortcut-based counterparts with similar parameter counts. The work contributes to a better theoretical understanding of depth in self-supervised learning architectures.

## Key points

- Standard residual connections in Transformers cause rank collapse: deep networks converge toward rank-1 attention matrices, making very deep stacking ineffective
- Signal propagation theory (mean field theory) is used to analyze when networks are at the edge of chaos — the regime where gradients are neither exploding nor vanishing
- Modified attention without shortcuts requires careful initialization and layer normalization placement to maintain expressivity at depth
- Deeper shortcut-free Transformers outperform equivalent-parameter shallow Transformers on language modeling and image classification
- The work connects to broader questions about whether depth in neural networks is truly exploited or merely decorative due to shortcut dominance

[Original](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2786_deep_transformers_without_shor.pdf)
