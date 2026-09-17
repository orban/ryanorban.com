---
title: A Generalist Neural Algorithmic Learner
date: 2022-12-08
categories:
  - neural-algorithmic-reasoning
  - graph-neural-networks
  - multi-task-learning
  - algorithms
description: ""
params:
  source: papers
  sourceUrl: https://arxiv.org/abs/2209.11142
---

## Summary

Borja Ibarz, Vitaly Kurin, George Papamakarios, Kyriacos Nikiforou, Mehdi Bennani, Róbert Csordás, Andrew Dudzik, Matko Bošnjak, Alex Vitvitskyi, Yulia Rubanova, Andreea Deac, Beatrice Bevilacqua, Yaroslav Ganin, Charles Blundell, and Petar Veličković (DeepMind, LoG 2022 spotlight) ask whether a single graph neural network can learn to execute multiple classical algorithms rather than one. The answer, with the right architecture and training setup, is yes — and the generalist model beats specialist single-task baselines by over 20% on the CLRS benchmark.

The paper builds on prior work in neural algorithmic reasoning, where the goal is to train models that can learn the input-output behavior of algorithms like sorting, shortest paths, and dynamic programming — and generalize to larger inputs than seen during training. The key contributions here are improvements to input representation, training methodology (ensuring single-task mastery before multi-task training), and a redesigned graph neural network processor that better handles the diverse structural demands across algorithm families. The multi-task setup also lets the model incorporate inductive biases from related algorithms, which is why it can outperform specialists despite covering more ground.

This connects to a broader question in machine learning about algorithmic generalization: can learned systems acquire something like the composable, step-by-step reasoning that makes algorithms powerful? Veličković's group has argued that GNNs are structurally well-suited for this because many classical algorithms have natural graph representations. The generalist result strengthens that bet — it's evidence that the capacity for algorithmic reasoning isn't fragmented across isolated modules but can be shared.

## Key points

- A single graph neural network processor trained on CLRS benchmark tasks (sorting, searching, dynamic programming, pathfinding, geometry) outperforms specialist models by >20%
- Key architectural improvements: better input representation, upgraded processor design, and a training curriculum that requires single-task proficiency before multi-task training
- Multi-task learning provides a form of knowledge transfer: algorithms with shared structure reinforce each other's generalization
- Results support the thesis that neural algorithmic reasoning is achievable with GNNs, and that algorithmic generalization to out-of-distribution input sizes is a tractable goal
- Petar Veličković and collaborators frame this as evidence that GNNs can serve as general-purpose algorithmic computers, not just structure-exploiting classifiers

[Original paper](https://arxiv.org/abs/2209.11142)
