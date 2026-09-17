---
title: "ConvNetJS: Deep Learning in Your Browser"
date: 2014-01-05
categories:
  - deep-learning
  - javascript
  - neural-networks
  - visualization
  - interactive
description: Andrej Karpathy's JavaScript library for training neural networks entirely in the browser — no install, no GPU, instant demos. In 2014 it made deep learning tangible for anyone with a web browser.
params:
  source: pinboard
  sourceUrl: http://cs.stanford.edu/people/karpathy/convnetjs/
---

## Summary

Andrej Karpathy built ConvNetJS as a pure JavaScript library for training neural networks in the browser — no server, no GPU, no installation required. The library supports convolutional neural networks, recurrent networks, and fully-connected networks, and includes built-in demos for MNIST, CIFAR-10, and reinforcement learning via deep Q-learning.

The project appeared in early 2014 as deep learning was transitioning from a research specialty to a mainstream tool. Running a neural network in the browser was both technically impressive and pedagogically valuable — watching training happen in real time, adjusting hyperparameters and seeing loss curves respond, gives a felt sense of the optimization landscape that reading papers alone doesn't.

## Key points

- Runs backpropagation and stochastic gradient descent entirely in JavaScript — accessible to anyone with a browser
- Supports convolutional layers, pooling layers, dropout, batch normalization, and multiple activation functions
- MNIST demo trains in the browser with visible per-epoch accuracy improvements — a compelling 2014 demo of live learning
- Reinforcement learning demo shows a simple agent learning to navigate using deep Q-learning — predates DQN Atari paper by months
- Andrej Karpathy later joined OpenAI as research director, continuing his pattern of making neural networks accessible

[Original](http://cs.stanford.edu/people/karpathy/convnetjs/) → AI agent
