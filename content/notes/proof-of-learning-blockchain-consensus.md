---
title: "Proof of Learning (PoLe): Blockchain Consensus via Neural Network Training"
date: 2022-04-28
categories:
  - blockchain
  - consensus
  - deep-learning
  - proof-of-work
  - machine-learning
description: Proof of Learning (PoLe) repurposes the computation wasted on Proof-of-Work consensus by directing it toward training neural networks, making blockchain nodes useful ML workers. The cheating-prevention mechanism (Secure Mapping Layer) is the interesting technical contribution — a linear layer baked into the network architecture that makes it costly to fake training progress.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2007.15145.pdf
---

## Summary

Proof of Learning (PoLe) (arXiv:2007.15145, 2020) proposes replacing Proof of Work (PoW) consensus in blockchain networks with a mechanism that directs compute toward training neural networks. In PoW systems like Bitcoin, miners spend enormous energy computing hash nonces that serve no purpose beyond being hard to compute. PoLe asks: what if that computation trained a model instead? The blockchain network releases training data to all nodes; consensus nodes train neural network models on the data; a valid model serves as the proof that sufficient compute was performed.

The key technical challenge is cheating prevention. In PoW, the hash function is its own proof — you can't fake having done the work without actually doing it. In PoLe, a node could submit a pre-trained model without having performed the designated training run. To address this, the authors introduce the **Secure Mapping Layer** (SML) — a linear layer inserted into the network architecture that encodes a hidden secret. The mapping is constructed so that a model trained without the correct secret produces degraded results when evaluated by the network, making it detectable. Nodes must obtain the secret from the previous block, then train with it, making it infeasible to precompute or steal results.

Experimentally, PoLe achieves more stable block generation rates than PoW (which suffers from difficulty adjustment cycles) and processes transactions more efficiently. The authors frame this as a win-win: blockchain nodes produce useful machine learning artifacts instead of burning energy on meaningless hashes. Related ideas include Proof of Useful Work and systems like Gridcoin that repurpose blockchain compute for distributed computing tasks (BOINC, protein folding).

## Key points

- Proof of Work (PoW) wastes compute on hash nonces; PoLe redirects it to neural network training, producing useful models as a byproduct of consensus.
- Secure Mapping Layer (SML): a linear layer parameterized by a block-specific secret, making it impossible to fake training without the designated data and key.
- Block validation: nodes evaluate submitted models against held-out test data; models below a performance threshold are rejected.
- More stable block generation rate than PoW, which oscillates with difficulty adjustment.
- Related to Proof of Useful Work, Gridcoin, and the broader idea of making blockchain compute economically productive.
- Significant open question: who decides what models to train and what datasets to use? Centralization of that decision is a meaningful governance problem not fully addressed.

[Original PDF](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/2007.15145.pdf)
