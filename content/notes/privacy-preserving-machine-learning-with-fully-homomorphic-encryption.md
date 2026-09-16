---
title: Privacy-Preserving Machine Learning with Fully Homomorphic Encryption for Deep Neural Networks
date: 2022-06-22
categories:
  - homomorphic-encryption
  - privacy
  - machine-learning
  - deep-learning
  - cryptography
  - security
  - inference
description: This paper demonstrates running deep neural network inference entirely on encrypted data using fully homomorphic encryption, so the server never sees plaintext inputs or outputs. It makes encrypted ML inference practical by combining FHE with approximation-friendly neural network architectures.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Privacy-Preserving Machine Learning with Fully Homomorphic Encryption for Deep Neural Network.pdf
---

## Summary

Fully homomorphic encryption (FHE) allows computation on ciphertext such that the result, when decrypted, matches what you'd get from computing on the plaintext directly. This paper applies FHE to deep neural network (DNN) inference, enabling a cloud service to evaluate a neural network on a client's encrypted data without ever decrypting it — the server learns nothing about the input or output. The approach is significant because it eliminates the trust assumption in machine learning as a service (MLaaS): even a compromised or malicious server cannot access user data.

The core challenge with FHE and neural networks is that standard activations like ReLU are non-polynomial and expensive to approximate in encrypted arithmetic. The paper addresses this by replacing ReLU with low-degree polynomial approximations (such as degree-2 or degree-3 polynomials) and retraining the network to compensate for the accuracy loss. Batch normalization and pooling layers also require careful treatment. The resulting encrypted inference pipeline uses the CKKS (Cheon-Kim-Kim-Song) leveled FHE scheme, which natively handles real-number arithmetic with controlled noise growth.

The results show competitive accuracy on benchmark tasks (MNIST, CIFAR-10) with substantial but manageable latency overhead — seconds to minutes per inference depending on network depth. This demonstrates that privacy-preserving inference is practically achievable for moderate-depth networks, with federated learning as an alternative paradigm for training-time privacy.

## Key Points

- Fully homomorphic encryption lets the server compute on encrypted inputs without decryption, giving cryptographic privacy guarantees stronger than differential privacy or secure multi-party computation for inference
- ReLU and other non-polynomial activations must be replaced with polynomial approximations; degree-2 polynomials (e.g., $x^2$) work but hurt accuracy, which is partially recovered by fine-tuning
- Uses the CKKS scheme for approximate real-number FHE, enabling vectorized SIMD-style batching of encrypted values across ciphertext slots
- Benchmark results on MNIST and CIFAR-10 show accuracy within 1-2% of plaintext baselines with latency in the seconds-to-minutes range
- Practical deployment requires co-design of the neural network architecture and the FHE scheme — off-the-shelf models don't transfer directly

[Original](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/Privacy-Preserving%20Machine%20Learning%20with%20Fully%20Homomorphic%20Encryption%20for%20Deep%20Neural%20Network.pdf)
