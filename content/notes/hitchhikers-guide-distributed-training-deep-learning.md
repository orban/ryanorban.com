---
title: A Hitchhiker's Guide to Distributed Training of Deep Neural Networks
date: 2022-05-26
categories:
  - distributed-computing
  - deep-learning
  - gpu
  - training
  - mlops
description: Chahal, Grover, and Dey survey the algorithms and engineering techniques for distributed deep learning training, covering data parallelism, model parallelism, AllReduce strategies, gradient compression, and mixed precision. A practical reference for scaling training from single GPU to multi-node clusters.
params:
  source: papers
  sourceUrl: https://arxiv.org/abs/1810.11787
---

## Summary

Karanbir Chahal, Manraj Singh Grover, and Kuntal Dey (arXiv:1810.11787, Oct 2018) survey the algorithms and systems techniques used to distribute deep learning training across multiple machines. The motivation is straightforward: a single GPU can take a week to train on ImageNet; recent work brought this down to 4 minutes using 2,048 GPUs. The gap between those two numbers represents an ecosystem of techniques for synchronization, communication, and gradient aggregation that this paper makes accessible.

The survey covers two primary decomposition strategies. **Data parallelism** distributes the dataset across nodes, each with a full model copy — nodes compute local gradients and aggregate them to update a global weight set. **Model parallelism** splits the model itself across nodes when it's too large to fit in a single device's memory. Within data parallelism, the paper covers **synchronous vs. asynchronous Stochastic Gradient Descent**: synchronous SGD waits for all nodes to compute gradients before updating (deterministic, easier to analyze), while asynchronous updates are faster but introduce staleness that can hurt convergence.

The AllReduce gradient aggregation strategies are central: ring-AllReduce (used in Horovod) reduces communication overhead compared to the parameter server approach by having each node communicate only with its neighbors in a ring topology. The paper also covers practical techniques: **mixed precision training** (using FP16 for computation, FP32 for master weights) reduces memory and improves throughput; **large batch training** with linear scaling rule for learning rate allows larger batches without accuracy degradation; **gradient compression** (quantization and sparsification) reduces the communication bandwidth bottleneck.

## Key points

- Data parallelism (divide data) vs. model parallelism (divide model) — the two fundamental decomposition strategies
- Ring-AllReduce outperforms parameter server architectures for gradient aggregation at scale (basis for Horovod)
- Synchronous vs. asynchronous SGD tradeoffs: determinism vs. speed, staleness vs. throughput
- Mixed precision training: FP16 computation + FP32 master weights — reduces memory, improves GPU throughput
- Linear scaling rule for learning rate enables large-batch training without accuracy loss

[Original](https://arxiv.org/abs/1810.11787)
