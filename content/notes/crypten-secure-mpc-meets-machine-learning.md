---
title: "CrypTen: Secure Multi-Party Computation Meets Machine Learning"
date: 2022-04-19
categories:
  - privacy
  - cryptography
  - machine-learning
  - mpc
  - pytorch
  - neurips-2021
description: CrypTen is a PyTorch-compatible framework from Facebook AI Research that wraps secure multi-party computation protocols behind a familiar tensor API, making private inference and training accessible to ML practitioners without cryptography expertise. The bet is that adoption bottlenecks for privacy-preserving ML are mostly about developer experience, not theoretical limits.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/NeurIPS-2021-crypten-secure-multi-party-computation-meets-machine-learning-Paper.pdf
---

## Summary

Secure multi-party computation (MPC) lets parties compute jointly on their combined data without revealing what each party holds. The obstacle to adoption in machine learning has always been that MPC frameworks speak the language of circuit compilers and cryptographic protocols — not the language of tensors, backpropagation, and neural network modules. CrypTen from Facebook AI Research (NeurIPS 2021) fixes this by implementing an MPC computation layer that mirrors the PyTorch API almost exactly: same tensor ops, same autograd, same `nn.Module` structure. In principle you change one import and your code runs over encrypted data.

Under the hood, CrypTen uses arithmetic secret sharing for operations like matrix multiplications and convolutions, and binary secret sharing for comparisons (required for ReLU activations). Converting between these two representations is the main computational overhead — each ReLU requires an A2B conversion followed by B2A, which explains why the framework is 2.5–3 orders of magnitude slower than plain PyTorch on Wav2Letter and ResNet benchmarks. GPU support helps enormously: Wav2Letter inference in the two-party setting on GPUs runs faster than real-time. The current threat model is semi-honest (honest-but-curious), meaning parties follow the protocol but may try to learn from intermediate values.

CrypTen is particularly well-suited for the case where multiple parties each own private datasets or private model weights and want to jointly run inference or training without either party revealing their data. The ONNX importer means you can train a model in PyTorch normally, then load it into CrypTen for encrypted deployment. A trusted third party generates Beaver triples for the multiplication protocol, though the authors plan to replace this with TTP-free alternatives.

## Key points

- Two parties can privately evaluate ResNet-18 on ImageNet in ~2.5 seconds and ViT-B/16 in ~8.5 seconds per image on GPUs
- Communication is the bottleneck on GPU (63% of wall time in 8-party Wav2Letter), computation dominates on CPU
- Non-linear functions (sigmoid, softmax, ReLU) require conversion between arithmetic secret sharing and binary secret sharing — this is the main source of overhead
- Word embedding lookups can't be done sparsely under encryption (would reveal input position), so CrypTen does full matrix multiplication instead — big overhead for NLP models
- The semi-honest threat model limits applicability: real deployments may need malicious security or at minimum TTP-free triple generation
- Architecture implications: attention (with its per-head softmax) is very expensive under MPC; MLP-Mixer-style models may be better suited to private inference

[Original paper](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/NeurIPS-2021-crypten-secure-multi-party-computation-meets-machine-learning-Paper.pdf)
