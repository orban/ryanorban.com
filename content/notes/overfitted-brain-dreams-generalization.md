---
title: "The Overfitted Brain: Dreams Evolved to Assist Generalization"
date: 2020-07-26
categories:
  - neuroscience
  - machine-learning
  - dreams
  - generalization
  - theory
  - research
description: A 2020 paper proposing that dreams evolved as a biological regularization mechanism — the brain 'trains' on noisy, hallucinated data during sleep to prevent overfitting to waking experience. A striking bridge between ML theory and sleep neuroscience.
params:
  source: pinboard
  sourceUrl: https://arxiv.org/abs/2007.09560
---

## Summary

This paper by Erik Hoel takes the concept of overfitting in machine learning and applies it as a hypothesis for why biological brains dream. The argument: waking experience is not randomly sampled — it's highly structured, repetitive, and correlated with your environment, habits, and surroundings. A brain that only trains on waking experience will overfit to it, developing narrow models that fail to generalize. Dreams, on this account, are the brain's data augmentation strategy — a way of injecting noisy, hallucinated, out-of-distribution training data to prevent the brain's models from becoming too specialized.

The ML analogy is precise. A neural network trained only on its training distribution performs poorly on novel inputs — this is overfitting. Techniques like dropout, data augmentation, and noise injection address this by artificially introducing variance. Dreams are proposed to play the same role: REM sleep generates bizarre, impossible scenarios (flying, familiar places with wrong details, impossible sequences) that expose the brain's prediction machinery to inputs far outside the distribution of real experience.

The paper fits within a broader tradition of computational theories of sleep, including memory consolidation accounts (dreams help transfer information from short-term to long-term memory) and synaptic homeostasis theory (sleep pruning of synaptic strength). The overfitted brain hypothesis is distinct: it's not about consolidating existing memories but about preventing overfitting by training on fictional data.

## Key points

- Hypothesis: dreams are data augmentation for biological brains — random noise injection to prevent overfitting to waking experience.
- Waking experience is non-IID: heavily correlated with your environment, which would cause overfitting if used as sole training signal.
- REM sleep generates out-of-distribution "data" (bizarre imagery) that forces generalization beyond the waking distribution.
- This is mechanistically analogous to dropout, Gaussian noise injection, and data augmentation in deep learning.
- Alternative theories: memory consolidation (Stickgold), synaptic homeostasis (Tononi) — the overfitted brain hypothesis is complementary rather than exclusive.
- If true, sleep deprivation harms not just memory but the brain's ability to generalize — a testable prediction.

[Original](https://arxiv.org/abs/2007.09560)
