---
title: "Agatha: Smart Contract for DNN Computation"
date: 2022-04-28
categories:
  - smart-contracts
  - deep-learning
  - blockchain
  - verification
  - ethereum
description: Agatha is a system for verifiable DNN computation on Ethereum smart contracts, achieving native-speed off-chain inference with only 3% overhead via a graph-based pinpoint protocol. It bridges AI and blockchain by solving the mismatch between neural network computational graphs and the VM-based execution model that existing verification schemes assume.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2105.04919.pdf
---

## Summary

Agatha (arXiv:2105.04919, 2021) tackles a fundamental mismatch: smart contract verification protocols like TrueBit, Arbitrum, and Optimism were designed around VM-based off-chain execution — but deep neural network computation doesn't map cleanly onto a virtual machine instruction set. Running DNN inference inside a VM for the purpose of fraud-proof arbitration is orders of magnitude slower than native execution. Agatha fixes this by redesigning the pinpoint protocol to operate over computational graphs instead of VM bytecodes.

The system introduces two key mechanisms. The first is the **Graph-based Pinpoint Protocol** (GPP), which extends the classic pinpoint bisection approach to the graph structure of DNN forward passes. Instead of bisecting over sequential VM instructions, GPP bisects over graph nodes — layers and operations in the neural network. This means arbitration on Ethereum only needs to verify a single node's computation, keeping on-chain cost negligible. The second is **Cross-evaluator Consistent Execution** (XCE), a technique that ensures identical numerical outputs across different hardware and platforms. Without XCE, floating-point nondeterminism across CPUs and GPUs would cause honest parties to disagree, breaking the fraud-proof guarantee entirely.

Evaluation on MobileNet, ResNet50, and VGG16 on Ethereum shows that Agatha achieves only 3% off-chain execution overhead compared to baseline native inference — a 602× latency improvement over the prior state-of-the-art that wrapped DNN execution in an off-chain VM. The on-chain arbitration cost is negligible, because GPP reduces dispute resolution to verifying a single graph node rather than replaying the full computation.

## Key points

- Smart contract verification (TrueBit-style) assumes VM-based execution — DNN workloads are graph-structured and don't fit this model without massive slowdown.
- GPP (Graph-based Pinpoint Protocol): bisection fraud proofs operating on computational graph nodes rather than VM instructions — keeps Ethereum arbitration costs low.
- XCE (Cross-evaluator Consistent Execution): guarantees bit-identical results across platforms, solving floating-point nondeterminism that would break the fraud-proof system.
- 602× latency improvement over VM-based verification; only 3% overhead vs. native off-chain DNN inference.
- Enables decentralized AI inference as an Ethereum service — third parties can verifiably compute DNN results for DeFi and other applications.
- Closely related to zero-knowledge proofs for ML inference (e.g., zkML) as an alternative verification strategy — Agatha's interactive arbitration is cheaper but requires multiple parties.

[Original PDF](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/2105.04919.pdf)
