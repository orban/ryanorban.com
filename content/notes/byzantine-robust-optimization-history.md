---
title: Learning from History for Byzantine Robust Optimization
date: 2022-04-15
categories:
  - federated-learning
  - byzantine-robustness
  - distributed-ml
  - optimization
  - research
description: Karimireddy, He, and Jaggi (EPFL, arXiv:2012.10333, 2021) propose using historical gradient information to detect and filter Byzantine workers in distributed training, achieving near-optimal convergence even with a constant fraction of corrupt workers. The historical approach is notable because it breaks the fundamental limitation of single-round Byzantine filters without requiring cryptographic overhead.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2012.10333.pdf
---

## Summary

Sai Praneeth Karimireddy, He, and Martin Jaggi (EPFL, arXiv:2012.10333, 2021) address a core vulnerability in distributed optimization and federated learning: Byzantine workers — nodes that send arbitrarily corrupted gradient updates — can derail convergence even if they represent only a small fraction of all workers. The naive aggregation (averaging all gradients) is provably broken when any Byzantine workers are present. Existing robust aggregation rules (geometric median, coordinate-wise trimmed mean) can filter outliers in a single round but face fundamental statistical limitations: with enough corruption budget, a Byzantine worker can fake a gradient that looks like a legitimate outlier rather than a clear deviation.

The paper's key insight is that Byzantine workers can sustain consistent corruption over time only at the cost of behaving differently across rounds. A worker that consistently reports false gradients will — over rounds — develop a history that diverges from honest workers. By maintaining historical gradient information for each worker and comparing current updates against that history, the aggregator can identify and filter Byzantine participants more reliably than single-round methods allow. This temporal detection approach accumulates evidence across multiple rounds rather than making a pass/fail decision at each step.

The authors prove that this history-based approach achieves near-optimal convergence rates even when a constant fraction f of workers are Byzantine, matching the information-theoretic lower bounds for Byzantine-robust optimization. The analysis is tight: convergence degrades gracefully with f rather than failing catastrophically. The work connects directly to federated learning security research, where the server cannot inspect or verify individual client updates, and Byzantine robustness is a requirement for deployment in adversarial settings. It pairs naturally with concurrent work from the same group on combining Byzantine robustness with differential privacy (arXiv:2006.04747).

## Key points

- Single-round Byzantine filters are limited: a Byzantine worker with enough budget can craft updates that look like legitimate outliers
- Historical gradient tracking accumulates evidence across rounds, catching Byzantine workers that behave consistently wrong over time
- Near-optimal convergence guarantees even with a constant fraction f of Byzantine workers — matches information-theoretic lower bounds
- Directly relevant to federated learning where the aggregator can't verify client updates
- Complements privacy-preserving aggregation work — robustness and privacy are separable concerns addressed by different mechanisms

[Source](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/2012.10333.pdf)
