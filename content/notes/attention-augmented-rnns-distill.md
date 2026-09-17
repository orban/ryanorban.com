---
title: Attention and Augmented Recurrent Neural Networks (Distill)
date: 2022-09-05
categories:
  - attention
  - rnns
  - neural-networks
  - machine-learning
  - distill
description: Distill's 2016 interactive visual explainer covering four augmented RNN variants — attention, memory networks, neural Turing machines, and neural programmers. A foundational reference for understanding how external memory and attention were grafted onto recurrent networks before the transformer era.
params:
  source: pinboard
  sourceUrl: https://distill.pub/2016/augmented-rnns/
---

## Summary

Chris Olah and Shan Carter's Distill.pub article from 2016 provides an interactive visual explanation of four augmented RNN variants that extend recurrent networks with external memory and attention mechanisms. The four systems covered: (1) Neural Turing Machines (NTMs) — RNNs with differentiable read/write access to an external memory matrix; (2) attention-based sequence-to-sequence models for translation; (3) adaptive computation time — allowing the network to vary computation per input; and (4) neural programmer-interpreters — learning to compose programs.

The historical context: this was published in 2016, when LSTMs were the dominant sequence model and the field was exploring how to give them capabilities closer to Turing completeness. Attention in this article refers specifically to soft attention over encoder states for translation — the mechanism from Bahdanau et al. 2015 that allowed decoders to selectively attend to different parts of the source sequence. This is the precursor to the self-attention mechanism in Transformers.

The Distill presentation is notable for its interactive visualizations — readers can observe how attention weights shift over source tokens during translation, making the mechanism intuitively clear. Distill.pub itself was a significant experiment in ML publishing: peer-reviewed, web-native, with a commitment to visualization and clarity over traditional academic prose. It influenced how the field communicates model internals and is a direct ancestor of modern ML interpretability research.

## Key points

- Covers four augmented RNN types: Neural Turing Machines, sequence attention, adaptive computation, and neural programmer.
- The attention mechanism here is Bahdanau attention (2015) — source sequence attention for translation, not self-attention.
- Interactive visualizations let readers observe attention weights shifting in real-time — a template for ML communication.
- Published 2016 on Distill.pub — a landmark in making ML research accessible without sacrificing rigor.
- NTMs introduced differentiable external memory — a different path toward long-range reasoning than transformers took.
- Historically important: captures the inflection point between the LSTM era and the transformer era.

[Original](https://distill.pub/2016/augmented-rnns/)
