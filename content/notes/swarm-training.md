---
title: Swarm Training
date: 2022-03-04
categories:
  - machine-learning
  - distributed-training
  - deep-learning
  - open-source
  - tpu
description: Shawn Presser's Swarm Training explores distributed ML training across many commodity machines with low-bandwidth interconnects — democratizing large model training beyond clusters with expensive NVLink. Part of the broader open-source effort to train large models outside of big lab infrastructure.
params:
  source: pinboard
  sourceUrl: https://www.shawwn.com/swarm
---

## Summary

[Swarm Training](/notes/swarm-training/) is Shawn Presser's project exploring distributed machine learning training across many machines connected over low-bandwidth networks — rather than the tightly-coupled, high-bandwidth clusters (NVLink, InfiniBand) used by large labs. The core insight: if you can tolerate more communication overhead and less synchronous gradient sharing, you can train large models on commodity hardware that wouldn't otherwise be viable.

This connects to the broader distributed training research challenge: standard data parallel training with synchronous SGD requires high-bandwidth interconnects because gradients must be shared after every step. Shawn Presser was working on approaches inspired by Hivemind (the EleutherAI/BigScience distributed training library) and biological neural network analogies — networks of loosely coupled nodes that still converge on useful representations.

Shawn Presser had already done notable open-source ML work: replicating GPT-2 and training models on TPU pods via Google Research credits. The swarm training project was part of the EleutherAI community's ethos of reproducing and democratizing large model training. This work became more broadly relevant as Hivemind and later DiLoCo (Google DeepMind, 2023) formalized the low-bandwidth federated training concept.

## Key points

- Low-bandwidth distributed training: train large models across commodity hardware without expensive interconnects.
- Tolerates higher communication latency than synchronous SGD — nodes update asynchronously or in rounds.
- Related to Hivemind library (used in BLOOM training) and later DiLoCo from Google DeepMind.
- Shawn Presser context: open-source ML community figure, TPU experiments, GPT-2 replication work.
- Democratization thesis: large model training shouldn't require million-dollar cluster infrastructure.

[Original](https://www.shawwn.com/swarm)
