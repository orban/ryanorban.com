---
title: "MLGarden: Visual Neural Network Editor"
date: 2024-11-13
categories:
  - machine-learning
  - visualization
  - education
  - neural-networks
  - interactive
description: MLGarden is an interactive visual editor for building and training neural networks without linear algebra — you construct computation graphs visually, watch backpropagation happen, and train on classification tasks. Built in C++ for performance, runs in the browser for accessibility.
params:
  source: pinboard
  sourceUrl: https://github.com/PavleMiha/mlgarden
---

![MLGarden: Visual Neural Network Editor](/images/notes/mlgarden.png)

## Summary

[MLGarden](/notes/mlgarden/) is an interactive visual editor that lets you build and train neural networks using a node-based computation graph interface, with no linear algebra required. You connect nodes visually to define architecture, then watch backpropagation happen in real time as the network trains on classification tasks. Built in C++ for performance, accessible in the browser.

The educational philosophy mirrors tools like TensorFlow Playground but goes deeper — you're constructing actual computation graphs, not just adjusting hyperparameters on a pre-built architecture. This means you can experiment with different architectures, activation functions, and connection patterns and immediately see how they affect learning.

[MLGarden](/notes/mlgarden/) sits in the space between "here's a slider to tune learning rate educational tools and write PyTorch from scratch" implementation exercises. It's accessible to people with only high school math — a genuine on-ramp for visual learners who find code-first ML education intimidating. The C++ implementation means it runs the training efficiently without being limited to tiny toy networks.

## Key points

- Visual computation graph editor — build neural networks by connecting nodes, no code required.
- Watch backpropagation and gradient flow in real time during training.
- No linear algebra prerequisite — accessible from high school math.
- Built in C++ for real performance; runs in browser for accessibility.
- Deeper than TensorFlow Playground — you construct the architecture, not just tune it.

[Original](https://github.com/PavleMiha/mlgarden) → GitHub
