---
title: Byzantine-Robust Learning on Heterogeneous Datasets via Bucketing
date: 2022-04-15
categories:
  - federated-learning
  - byzantine-robust
  - distributed-systems
  - security
  - iclr-2022
description: EPFL researchers show that existing Byzantine-robust aggregation rules (Krum, coordinate-wise median, RFA) fail catastrophically on non-iid data, then fix the problem with a one-step bucketing scheme that randomly groups worker updates before aggregation. The first result with provable convergence guarantees for Byzantine robustness under realistic data heterogeneity.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2006.09365.pdf
---

## Summary

This ICLR 2022 paper from EPFL researchers Sai Praneeth Karimireddy, Lie He and Martin Jaggi punches a hole in the Byzantine-robust learning literature: the standard aggregation rules — Krum, coordinate-wise median, geometric median (RFA) — all assume workers share the same data distribution. That assumption is unrealistic in federated learning, where heterogeneity across clients is the norm.

The authors introduce a new attack called mimic that explicitly exploits data heterogeneity to bypass median-based defenses, and show existing defenses can fail to converge even with no adversaries present, purely because honest workers' updates differ. Then they propose the fix: a bucketing step that randomly groups worker updates into small buckets, averages within each bucket, then feeds those bucket-means into any existing robust aggregator. Bucketing reduces variance enough that median-style methods regain their robustness guarantees.

They formalize the notion of an Approximate Robust AGGregator (ARAGG), prove that bucketing plus Krum/CM/RFA satisfies this property, and combine it with worker momentum to derive optimal convergence rates with matching lower bounds. A clean limit emerges: under arbitrary heterogeneity, exact convergence is impossible, but under mild heterogeneity or overparameterization (the interpolation regime), the method does converge to the optimum. This is the first such guarantee in the non-iid Byzantine setting.

## Key points

- Existing Byzantine-robust aggregators (Krum, coordinate-wise median, RFA) fail under non-iid data even without adversaries — heterogeneity alone breaks them.
- The "mimic" attack uses one honest worker as cover, weaponizing data heterogeneity to slip past median-based filters.
- Bucketing is a one-line preprocessing step: randomly group updates, average inside buckets, then aggregate — and it provably restores robustness guarantees for any reasonable aggregator.
- Combining bucketing with worker momentum yields optimal Byzantine-robust convergence rates with matching lower bounds.
- Under overparameterization or mild heterogeneity, exact convergence is recoverable; otherwise an irreducible error floor exists.

[Original PDF](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2006.09365.pdf)
