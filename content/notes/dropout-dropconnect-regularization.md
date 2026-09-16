---
title: Regularizing Neural Networks with Dropout and DropConnect
date: 2013-12-29
categories:
  - neural-networks
  - regularization
  - deep-learning
  - dropout
  - machine-learning
description: FastML's comparison of Dropout and DropConnect — two techniques for regularizing neural networks by randomly zeroing activations or weights during training. Clarifies that DropConnect's CIFAR-10 SOTA came from model ensembling, not the technique itself.
params:
  source: pinboard
  sourceUrl: http://fastml.com/regularizing-neural-networks-with-dropout-and-with-dropconnect
---

## Summary

Dropout and DropConnect are two closely related regularization techniques for neural networks, and this FastML article explains the distinction clearly. Dropout zeros out unit activations at random during training — the standard horizontal/vertical stripe masking that became ubiquitous after Hinton's 2012 paper. DropConnect extends this by zeroing weights rather than activations, producing a sparser, irregular masking pattern across the network.

The practical punchline is that both methods produce similar accuracy results. The state-of-the-art CIFAR-10 result (9.32% error) that DropConnect was associated with came from ensembling 12 models, each individually achieving ~11% error — not from DropConnect's inherent superiority. This is an important distinction: benchmark improvements from ensembling are real but rarely practical for deployment.

Both methods work by encouraging the network to learn redundant, distributed representations — no single neuron or weight can be relied upon to always be present, so the network avoids co-adaptation and learns more robust features. The effect is similar to training an ensemble of many thinned networks that share parameters.

## Key points

- Dropout: zeros activations → horizontal/vertical stripe pattern. DropConnect: zeros weights → irregular binary mask.
- Both act as regularization against overfitting, functioning as implicit ensembles of many sub-networks.
- Performance difference between the two is marginal in practice.
- The CIFAR-10 SOTA at the time came from averaging 12 DropConnect models — model ensembling, not the regularizer itself.
- Dropout can hurt performance on sparse, noisy features by reducing effective training signal.
- The core insight: preventing co-adaptation between units forces more distributed feature learning.

[Original](http://fastml.com/regularizing-neural-networks-with-dropout-and-with-dropconnect)
