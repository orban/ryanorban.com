---
title: "Piranha: A GPU Platform for Secure Computation"
date: 2022-08-10
categories:
  - privacy
  - cryptography
  - gpu
  - secure-computation
  - mpc
  - machine-learning
description: Piranha (USENIX Security 2022) is a GPU platform for secure multi-party computation that exploits GPU parallelism to accelerate MPC protocols by 10-15× over CPU implementations. It shows that GPU hardware can close the practical performance gap for privacy-preserving machine learning at scale.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Piranha- A GPU Platform for Secure Computation.pdf
---

## Summary

Jean-Luc Watson, Sameer Wagh, and Raluca Ada Popa at UC Berkeley present Piranha — a GPU-accelerated platform for secure multi-party computation (MPC) that achieves 10–15× speedup over CPU-based MPC systems (USENIX Security 2022). The core insight: MPC protocols like secret sharing-based arithmetic (used in 2PC, 3PC, and 4PC settings) consist largely of matrix multiplications and element-wise operations — precisely the workloads GPUs were designed to accelerate. The obstacle has been that MPC protocols operate over custom finite fields, not the floating-point arithmetic GPU vendor libraries expect.

Piranha resolves this by implementing a GPU-accelerated MPC backend that handles integer arithmetic over custom finite fields using CUDA kernels. The architecture is protocol-agnostic: by abstracting share representation and arithmetic operations, the platform can run multiple MPC protocols (SecureML, FALCON, FantasticFour) on top of the same GPU layer without rewriting protocol logic. This is similar to how CrypTen abstracts MPC behind a PyTorch API, but Piranha operates at a lower level — hardware acceleration rather than API compatibility.

For private machine learning inference and training, Piranha demonstrates that neural network workloads (including ResNet-50 training in the 3-party honest-majority setting) can run with GPU-level throughput. The 10–15× speedup compared to prior CPU-based MPC implementations brings privacy-preserving ML latencies closer to acceptable ranges for real-world deployment. This connects to the broader goal of making federated learning and secure inference practical, not just theoretically possible.

## Key points

- GPU-accelerated MPC via custom CUDA kernels for finite-field arithmetic — not floating-point, but custom integer ops that GPU throughput still dominates
- Protocol-agnostic design: SecureML, FALCON, FantasticFour all run on the same Piranha backend — architecture separates protocol logic from hardware acceleration
- 10–15× speedup over CPU-based MPC baselines; enables ResNet-50 training under 3-party honest majority setting
- Complements CrypTen (PyTorch API layer over MPC) — Piranha sits below the API, accelerating the underlying arithmetic
- Bridges MPC theory and practice: practical performance is the bottleneck for privacy-preserving ML adoption, not theoretical protocol design

[Original paper →](https://www.usenix.org/conference/usenixsecurity22/presentation/watson)
