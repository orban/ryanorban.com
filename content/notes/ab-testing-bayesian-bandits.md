---
title: A/B Testing with Bayesian Bandits in Google Analytics
date: 2013-12-16
categories:
  - a-b-testing
  - bayesian
  - multi-armed-bandit
  - optimization
  - google-analytics
description: FastML walkthrough of Google Analytics Content Experiments — which use a multi-armed bandit algorithm instead of fixed 50/50 splits to dynamically allocate traffic toward better-performing variants. A practical introduction to bandit-based online optimization.
params:
  source: pinboard
  sourceUrl: http://fastml.com/ab-testing-with-bayesian-bandits-in-google-analytics/
---

## Summary

This FastML article explains multi-armed bandit algorithms as an alternative to classical A/B testing, using Google Analytics Content Experiments (introduced in 2013) as the practical vehicle. Where traditional A/B tests maintain a fixed traffic split until the experiment ends, bandits adapt in real time: traffic is progressively shifted toward the better-performing variant as evidence accumulates.

The multi-armed bandit name comes from casino slot machines — each variant is an "arm" with an unknown payoff distribution, and the algorithm must balance exploration (trying all arms to learn their distributions) against exploitation (concentrating traffic on the arm currently believed to be best). Google's implementation uses this dynamically, so a clearly losing variant gets less and less traffic during the experiment rather than wasting half your visitors on a bad page until a fixed end date.

The core operational difference from frequentist A/B testing: bandits make decisions continuously rather than requiring a fixed time horizon. You don't wait for a pre-specified sample size. This matters when traffic is limited or the cost of showing a bad variant is high.

## Key points

- Multi-armed bandit algorithms allocate traffic dynamically, concentrating on better variants as evidence accumulates — unlike fixed 50/50 splits in classical A/B testing.
- Named for casino slot machines: each variant = an "arm" with unknown reward distribution. Must balance exploration vs exploitation.
- Google Analytics Content Experiments (2013) made this accessible via JavaScript + API — no custom infrastructure needed.
- Key practical advantage: losing variants waste fewer conversions than equal-allocation designs.
- The implicit Bayesian inference sits in the bandit's belief update — it maintains a distribution over the true conversion rate of each arm and updates it with each observation.
- Related to Thompson sampling and UCB (Upper Confidence Bound) algorithms from the reinforcement learning literature.

[Original](http://fastml.com/ab-testing-with-bayesian-bandits-in-google-analytics/)
