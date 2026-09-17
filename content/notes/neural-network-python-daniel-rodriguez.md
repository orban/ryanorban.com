---
title: A Not-So-Basic Neural Network in Python
date: 2013-12-29
categories:
  - neural-networks
  - python
  - machine-learning
  - tutorial
  - backpropagation
description: Daniel Rodriguez's practical tutorial on implementing a non-trivial neural network in Python from scratch — going beyond the toy perceptron examples to show backpropagation and training on real data. A mid-2013 hands-on coding reference.
params:
  source: pinboard
  sourceUrl: http://danielfrg.github.io/blog/2013/07/27/not-so-basic-neural-network-python/
---

## Summary

Daniel Rodriguez wrote this tutorial to bridge the gap between hello world neural network examples and real implementations. The not so basic framing signals it goes beyond the standard perceptron toy example to cover backpropagation, multiple hidden layers, and training on actual data in Python.

In mid-2013, implementing a neural network from scratch was a common exercise for practitioners entering the field — the major frameworks (Theano, Caffe) existed but required significant setup, and building from numpy helped build intuition for the chain rule computations that underlie gradient descent. The post was part of a wave of neural nets in Python tutorials that appeared as the field became more accessible.

The implementation covers the forward pass (activation functions, layer computations), backpropagation (computing gradients via the chain rule), and a training loop with stochastic gradient descent. This kind of from-scratch implementation was pedagogically valuable: understanding the math at the numpy level makes the abstraction of frameworks like TensorFlow or PyTorch much more meaningful.

## Key points

- Implements backpropagation from scratch in Python with NumPy — not a toy perceptron but a multi-layer network.
- Activation functions: typically sigmoid or tanh at this period; ReLU was gaining traction but not yet dominant.
- Training with stochastic gradient descent — the loop that became the template for all modern deep learning training.
- From 2013 — before Keras and PyTorch made this abstracted away; building from scratch was the standard way to learn.
- Daniel Rodriguez was an active contributor to the Python data science community around this time.
- Useful companion to the theoretical deep learning tutorials: translating math into numpy code.

[Original](http://danielfrg.github.io/blog/2013/07/27/not-so-basic-neural-network-python/) → GitHub
