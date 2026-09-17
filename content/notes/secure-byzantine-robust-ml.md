---
title: Secure Byzantine-Robust Machine Learning
date: 2022-04-15
categories:
  - federated-learning
  - cryptography
  - privacy
  - distributed-ml
  - research
description: He, Karimireddy, and Jaggi propose a two-server cryptographic protocol that simultaneously achieves Byzantine robustness, input privacy, and local differential privacy for distributed machine learning — three properties usually addressed separately. Bridges the privacy-robustness gap in federated learning.
params:
  source: papers
  sourceUrl: https://arxiv.org/abs/2006.04747
---

## Summary

Lie He, Sai Praneeth Karimireddy, and Martin Jaggi (EPFL) address a key tension in federated learning: robustness and privacy are both desirable properties, but most work treats them independently. Byzantine robustness filters out malicious or faulty workers who submit corrupt gradients; privacy protects each worker's local data from the aggregating server. Combining them is non-trivial because many Byzantine-robust aggregation rules require inspecting individual updates in ways that leak private information.

The paper proposes a two-server cryptographic protocol that handles this jointly. The core idea: two non-colluding servers jointly perform Byzantine-robust aggregation using secure two-party computation (2PC) so that neither server sees individual worker updates in plaintext. Workers submit their data via secret sharing between the two servers, allowing Byzantine-robust aggregation rules (like coordinate-wise median or clipping) to run on encrypted data. The system also incorporates local differential privacy (LDP) so even if the servers collude, individual contributions remain private.

The construction achieves communication efficiency and fault tolerance alongside the privacy-robustness guarantee — a notably complete security profile. This puts it in a rare position: most privacy-preserving ML systems (like CrypTen) assume honest participants and focus on privacy from external observers, while Byzantine-robust systems like SCAFFOLD or Byzantine-resilient aggregation ignore cryptographic input privacy. This paper is one of the first to explicitly bridge the two threat models with a practical protocol.

## Key points

- Two non-colluding servers jointly run Byzantine-robust aggregation via secure two-party computation — neither sees individual updates
- Achieves Byzantine robustness (tolerates malicious workers), input privacy, and local differential privacy simultaneously
- Workers use secret sharing to distribute their updates: privacy is cryptographic, not just anonymity-based
- Communication efficient and fault-tolerant — practical, not just theoretically sound
- Bridges federated learning robustness literature (SCAFFOLD, coordinate-wise median) with privacy-preserving ML (CrypTen, MPC)
- Relevant threat model: the aggregating infrastructure is untrusted; workers don't trust each other or the servers

[Original](https://arxiv.org/abs/2006.04747)
