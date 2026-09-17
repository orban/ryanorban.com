---
title: 10 Categories of Deep Recommendation Systems
date: 2020-12-24
categories:
  - machine-learning
  - recommendation-systems
  - deep-learning
  - research
  - survey
description: James Le's survey of 10 categories of deep learning-based recommendation systems — from MLP and autoencoder approaches through attention-based and graph neural network methods. A useful taxonomy for understanding how the field moved beyond matrix factorization.
params:
  source: pinboard
  sourceUrl: https://jameskle.com/writes/rec-sys-part-2
---

## Summary

James Le's survey categorizes deep learning approaches to recommendation systems into 10 distinct families, providing a taxonomy for a field that had grown rapidly by 2020. The framework moves beyond classical collaborative filtering and matrix factorization to cover how deep learning architectures are applied to recommendation: MLP-based methods, autoencoders, convolutional neural networks for sequential patterns, recurrent neural networks for temporal dynamics, attention mechanisms, adversarial training (GAN-based augmentation), deep structured semantic models, restricted Boltzmann machines, neural factorization machines, and graph neural networks for relational data.

The motivation for this taxonomy is that "deep learning recommendation systems" is too broad a category to reason about practically. A model using LSTMs to capture sequential viewing history is solving a fundamentally different problem than one using a GNN to model social graph relationships. Understanding which architecture family fits which problem type is the practical SKILL this survey builds.

By 2020, Netflix, YouTube, Amazon, and Spotify had all published papers describing their recommendation architectures, many of which appear in this survey. The field was moving from treating recommendations as pure matrix factorization problems toward treating them as sequential prediction problems (what will you want next, given your history?) — a shift that transformer-based recommenders later accelerated.

## Key points

- 10 architecture families: MLP, autoencoder, CNN, RNN/LSTM, attention, adversarial network, deep structured semantic models, RBM, neural factorization machines, GNN.
- Each architecture captures different structure: RNNs for temporal sequences, GNNs for graph relationships, CNNs for local feature patterns.
- The field shifted from collaborative filtering (user-item interactions only) to hybrid models incorporating content, context, and social signals.
- Real-world systems referenced: YouTube DNN recommender, Neural Collaborative Filtering, Wide & Deep (Google).
- Good entry point before reading individual RecSys papers; provides the conceptual map.

[Original](https://jameskle.com/writes/rec-sys-part-2)
