---
title: "Heinsen Routing: Vector Routing for Sequences and Capsule Networks"
date: 2023-04-09
categories:
  - machine-learning
  - capsule-networks
  - research
  - neural-networks
  - pytorch
description: Heinsen routing is a novel algorithm for routing vectors in sequences and capsule networks — an alternative to Hinton's dynamic routing that generalizes across domains. A niche but foundational contribution to the capsule network research line.
params:
  source: pinboard
  sourceUrl: https://github.com/glassroom/heinsen_routing
---

## Summary

Heinsen routing is an algorithm by Franz Heinsen (Glassroom) for routing vectors in sequences and capsule networks, described across two papers: \"An Algorithm for Routing Vectors in Sequences\ (2022) and \An Algorithm for Routing Capsules in All Domains\" (2019). The repo provides a clean PyTorch reference implementation of both.

Capsule networks, originally proposed by Geoffrey Hinton, attempt to address limitations of standard convolutional neural networks by having units output vectors (capsules) rather than scalars, with dynamic routing determining how lower-level capsule outputs are combined into higher-level representations. The routing algorithm is the key mechanism — it determines how lower-level predictions are aggregated while ignoring those inconsistent with the overall structure. Hinton's original dynamic routing by agreement had computational limitations; Heinsen's formulation provides a more general and efficient alternative.

The 2022 paper extends the routing concept to arbitrary sequences, not just vision tasks — making it applicable to NLP and other sequence processing. The theoretical appeal of capsule-based approaches: they're designed to be more robust to viewpoint variation, better at representing part-whole relationships, and potentially more sample-efficient than CNNs for structure-aware tasks. In practice, capsule networks haven't displaced transformers, but the routing mechanism research continues to be relevant to equivariant neural networks and structured prediction.

## Key points

- Implements routing algorithms for capsule networks — more general than Hinton's original dynamic routing.
- Two papers: 2019 (all domains) and 2022 (sequences) — both implemented in PyTorch.
- Routing determines how lower-level capsule outputs aggregate into higher-level representations.
- 2022 extension covers sequence tasks: applicable to NLP, not just computer vision.
- Related to broader research on equivariant neural networks and part-whole relationship modeling.
- Capsule networks remain a research interest despite transformers dominating practical applications.

[Original](https://github.com/glassroom/heinsen_routing) → GitHub
