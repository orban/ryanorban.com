---
title: Deep Learning 101
date: 2013-11-15
categories:
  - deep-learning
  - neural-networks
  - machine-learning
  - tutorial
  - introduction
description: Introductory survey of deep learning for non-specialists — covers hierarchical representation learning, RBMs, autoencoders, and the four core obstacles. Written to help readers mentally filter hype from substance in 2013.
params:
  source: pinboard
  sourceUrl: http://markus.com/deep-learning-101/
---

![Deep Learning 101](/images/notes/deep-learning-101.png)

## Summary

This introductory article on deep learning was written for people who wanted to follow research in the area without being misled by press coverage. The central concept is hierarchical representation learning: deep neural networks discover multiple levels of features that work together to define increasingly abstract aspects of the data — from raw pixels to edges to shapes to objects.

Two main architectural approaches are described. Probabilistic models like Restricted Boltzmann Machines (RBMs) treat layers as probability distributions over latent variables, stacking them to form Deep Belief Networks. Encoding models like autoencoders use encoder-decoder functions to map inputs through a bottleneck into a compressed feature representation. Both approaches can be stacked to create depth, and Principal Component Analysis (PCA) is introduced as the simplest case of dimensionless encoding.

The article identifies four core obstacles in deep learning: computational scaling (the hardware wall), optimization difficulty during training, complex inference requirements, and the challenge of disentangling the underlying factors of variation in data. All four were active research problems in 2013, and this piece captures the state of the field at the moment before the current wave of results made them tractable.

## Key points

- Core idea: learn hierarchical features from data rather than hand-engineering them — representation learning.
- Two families: probabilistic (RBM, Deep Belief Networks) and encoding (autoencoder).
- PCA is the simplest encoding model — deep learning generalizes this to nonlinear, multi-layer hierarchies.
- Four obstacles at the time: computation, optimization, inference, disentanglement of factors.
- Written as a primer to help readers evaluate the breathless coverage deep learning was getting in 2013.
- This is roughly where the field stood before AlexNet and ImageNet results had fully sunk in.

[Original](http://markus.com/deep-learning-101/)
