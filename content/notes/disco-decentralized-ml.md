---
title: "DISCO: Decentralized Privacy-Preserving ML Training"
date: 2022-04-15
categories:
  - federated-learning
  - privacy
  - machine-learning
  - p2p
  - open-source
description: DISCO (from EPFL) is a decentralized, privacy-preserving ML training framework using peer-to-peer networking — no central server, nodes train locally and share model updates directly. Extends federated learning to remove the trusted aggregator requirement.
params:
  source: pinboard
  sourceUrl: https://github.com/epfml/disco
---

## Summary

DISCO (Decentralized, Intelligent, Scalable, and Collaborative Optimization) is an open-source ML training framework from EPFL's Machine Learning and Optimization Laboratory (MLO lab). It uses peer-to-peer networking to enable distributed ML training without a central server — nodes train locally on private data and share model updates directly with other nodes, bypassing the trusted aggregator that standard federated learning requires.

Standard federated learning (as designed by Google) still requires a central parameter server that aggregates model updates from clients. This creates a trust bottleneck: the aggregator can potentially reconstruct training data from gradients, or simply be a privacy liability if compromised. DISCO's decentralized topology removes this requirement: nodes communicate directly, potentially using protocols like gossip learning or D-PSGD (Decentralized Parallel SGD), where each node averages its model with randomly selected peers rather than a central server.

The practical applications are in healthcare (hospitals training diagnostic models on patient data that can't leave the institution), finance (banks training fraud detection on transaction data), and any domain where data is siloed by regulation or competitive sensitivity. Federated learning has been the dominant approach to this problem, but central aggregator trust requirements and communication bottlenecks limit it. DISCO's p2p approach is more robust to single points of failure and potentially better for privacy, at the cost of convergence complexity.

## Key points

- Decentralized federated learning: no central parameter server — nodes share updates directly via P2P networking.
- Removes the trusted aggregator requirement from standard federated learning — stronger privacy guarantees.
- EPFL MLO lab (Martin Jaggi's group) — serious academic ML optimization background.
- Decentralized SGD protocols: gossip learning, D-PSGD — convergence analysis is more complex than centralized training.
- Use cases: healthcare (hospital data), finance (transaction data), any domain with data locality requirements.
- JavaScript/TypeScript implementation: runs in browser nodes — interesting for truly distributed settings.

[Original](https://github.com/epfml/disco) → GitHub
