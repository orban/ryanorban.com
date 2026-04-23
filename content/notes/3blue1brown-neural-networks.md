---
title: Neural Networks — 3Blue1Brown
date: 2025-03-18
categories:
  - neural-networks
  - education
  - video
  - math
  - backpropagation
  - deep-learning
description: 3Blue1Brown's neural networks playlist is the canonical visual introduction to how neural networks and backpropagation work — four episodes, starting from scratch and building to the chain rule. The most-watched math explainer for deep learning fundamentals.
params:
  source: pinboard
  sourceUrl: http://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi
---

![Neural Networks — 3Blue1Brown](/images/notes/3blue1brown-neural-networks.png)

## Summary

3Blue1Brown (Grant Sanderson) produced a four-episode YouTube series on neural networks that has become the default recommendation for visual learners approaching deep learning for the first time. The series starts from zero — what is a neuron, what is a layer — and builds through gradient descent to a full visual treatment of backpropagation using the chain rule.

The distinctive approach is the use of manim, Sanderson's own math animation library, to render abstract concepts as moving geometries. Gradient descent is shown as a ball rolling down a loss surface. Backpropagation is shown as a reverse pass of influence flowing backwards through layers. These visualizations give genuine intuition for why the algorithms work, not just how to implement them.

The series connects naturally to the MNIST handwritten digit recognition example, which makes the concepts concrete. After 3Blue1Brown, the next step is usually Andrej Karpathy's Building makemore or Neural Networks: Zero to Hero for hands-on coding depth, or the fastai course for applied usage. The series doesn't cover transformers or attention mechanisms directly — those require different resources like The Illustrated Transformer or the Transformer Circuits Thread.

## Key points

- 4-episode series: what neural nets are, how they learn via gradient descent, and how backpropagation works through the chain rule.
- Visual-first: uses manim animations to build genuine geometric intuition.
- Starts from zero: accessible without prior ML knowledge.
- Uses MNIST digit classification as the running example.
- Canonical starting point before diving into Andrej Karpathy's coding tutorials or fastai.

[Original](http://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
