---
title: Asynchronous Decentralized SGD with Quantized and Local Updates
date: 2022-04-15
categories:
  - distributed-ml
  - optimization
  - sgd
  - decentralized-learning
  - quantization
  - gossip
description: SwarmSGD is an asynchronous decentralized optimization algorithm that provably converges when combining gossip communication, gradient quantization, and local update steps simultaneously across heterogeneous data distributions. It achieves performance comparable to large-batch SGD on supercomputing systems while reducing communication overhead.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/1910.12308.pdf
---

## Summary

Nadiradze et al. address a core tension in distributed machine learning: reducing communication cost without sacrificing convergence guarantees. Classical decentralized approaches like gossip protocols require synchronized rounds, but synchronization itself becomes a bottleneck at scale. This paper analyzes SwarmSGD, which operates under the asynchronous gossip model—nodes communicate by randomly selecting partners, with no global synchronization barrier.

The theoretical contribution is proving that SwarmSGD converges even when three communication-reduction techniques are applied simultaneously: non-blocking (asynchronous) communication, gradient quantization, and local gradient steps before communicating. Prior work handled these individually or in pairs; handling all three concurrently under heterogeneous data distributions and arbitrary network topologies required a novel analytical connection to multi-dimensional load balancing processes.

Empirical validation on supercomputing hardware shows results competitive with optimized large-batch stochastic gradient descent, making this practically relevant for training at HPC scale. The work sits at the intersection of distributed optimization and communication-efficient learning.

## Key points

- Proves convergence of SwarmSGD under asynchronous gossip with quantization + local steps applied simultaneously—harder than prior settings requiring global sync
- Novel analytical technique: connects decentralized optimization to multi-dimensional load balancing processes
- Handles heterogeneous node data distributions and arbitrary network topologies
- Competitive empirical performance against large-batch SGD on supercomputing systems
- Extends the frontier of communication-efficient learning for distributed optimization

[Original](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/1910.12308.pdf)
