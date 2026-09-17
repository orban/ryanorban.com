---
title: Deriving Formulas for Sample Size in A/B Tests
date: 2013-12-29
categories:
  - a-b-testing
  - statistics
  - sample-size
  - statistical-power
  - hypothesis-testing
description: Mathematical derivation of the expected sample size needed in A/B tests using frequentist power analysis. Derives the N formula from effect size, significance level (α), and power (1-β) — useful for anyone designing experiments who wants to understand where 'you need at least X users' comes from.
params:
  source: pinboard
  sourceUrl: http://camdp.com/blogs/number-samples-needed-b-test
---

## Summary

This camdp.com post derives the formula for the minimum sample size needed in an A/B test from first principles, using frequentist hypothesis testing. The derivation starts from two parameters the test designer controls: the significance level (α, the false positive rate) and the statistical power (1-β, the probability of detecting a real effect). Combined with the minimum detectable effect size, these determine N.

The standard formula: N ≈ (z_α/2 + z_β)² × 2σ² / δ², where δ is the minimum effect size you care about detecting and σ² is the variance of the metric. In the common binomial proportion case (conversion rates), σ² = p(1-p) and the formula simplifies to a well-known expression. The key insight is that N scales as 1/δ² — to detect an effect half as large, you need four times as many users.

This kind of derivation matters because sample size calculators for A/B tests often hide the math and let practitioners enter "significance = 95%, power = 80%" without understanding why those defaults exist or how conservative they are. Understanding the formula makes it clear that detecting small effect sizes at internet scale requires enormous N, and that the 80% power default means you'll miss real effects 20% of the time.

## Key points

- Sample size formula: N ≈ (z_α/2 + z_β)² × 2σ² / δ² — scales inversely with the square of the effect size.
- Statistical power (1-β): probability of detecting a real effect when it exists. 80% is the common default, but that means 20% miss rate.
- Significance level (α): false positive rate. 0.05 means 1-in-20 tests will reject a true null hypothesis by chance.
- Effect size δ: the minimum practically meaningful difference. Choosing this requires domain knowledge, not statistics.
- N ∝ 1/δ²: halving the minimum detectable effect requires quadrupling the sample size.
- Related to the critique in Dave Giles's large-dataset post: with huge N, statistically tiny and economically meaningless effects become detectable.

[Original](http://camdp.com/blogs/number-samples-needed-b-test)
