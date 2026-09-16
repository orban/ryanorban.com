---
title: "Fun with Stats: How Big of a Sample Size Do I Need?"
date: 2014-07-12
categories:
  - statistics
  - sample-size
  - ab-testing
  - experimental-design
description: Julia Evans walks through sample size calculation for experiments, grounding statistical power and significance in a concrete worked example. A good entry point for engineers who run A/B tests but haven't internalized what sample size actually buys you.
params:
  source: pinboard
  sourceUrl: http://jvns.ca/blog/2014/07/11/fun-with-stats-how-big-of-a-sample-size-do-i-need/
---

## Summary

Julia Evans writes characteristically direct posts about technical concepts, and this one tackles sample size calculation for statistical hypothesis testing. The core question she answers is practical: if I want to detect a 5% improvement in my metric, how many users do I need in my experiment? The answer requires understanding statistical power — the probability that your test will detect a real effect if one exists.

The calculation depends on three interacting parameters: the effect size you care about detecting, the desired statistical significance level (commonly α = 0.05), and the desired statistical power (commonly 80% or 90%). These aren't independent — if you shrink the effect size you want to detect (i.e., you want to find smaller improvements), you need a proportionally larger sample. The relationship is roughly quadratic: halving the detectable effect size quadruples the required sample.

This matters enormously for A/B testing in practice. Many teams run experiments that are far too small to detect the effects they're actually interested in, then declare no significant effect — a false negative driven by underpowered tests. Evans makes this concrete with numbers, which is the kind of thing that sticks.

## Key points

- Statistical power (1 - β) is the probability of detecting a real effect — 80% power means a 20% chance of missing a true improvement.
- Required sample size scales with 1/effect_size² — smaller effects require dramatically more data.
- Underpowered experiments are a silent source of incorrect no difference conclusions in A/B testing.
- Two-sample t-test is the standard test for comparing means; chi-squared test for comparing proportions (click rates, conversion rates).
- Power analysis should happen before running an experiment, not after — post-hoc power calculations on failed tests are misleading.

[Original](http://jvns.ca/blog/2014/07/11/fun-with-stats-how-big-of-a-sample-size-do-i-need/)
