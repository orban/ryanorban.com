---
title: Statistical Formulas for Programmers
date: 2013-05-20
categories:
  - statistics
  - programming
  - education
  - ab-testing
  - data-science
description: Evan Miller's reference sheet of statistical formulas presented as code-friendly pseudocode rather than academic notation. A practical bridge between statistical theory and implementation, covering the formulas programmers actually need for A/B testing and product analytics.
params:
  source: pinboard
  sourceUrl: http://www.evanmiller.org/statistical-formulas-for-programmers.html
---

## Summary

Evan Miller wrote a post translating the most commonly needed statistics formulas into programmer-friendly notation — avoiding the Greek letter soup of academic statistics textbooks and presenting formulas in a way that maps to implementation. The target audience: software engineers who need to implement A/B testing, analyze experiment results, or build product analytics without a statistics background.

The formulas covered include sample size calculation for A/B tests, confidence intervals for proportions (using the Wilson score interval, which is better than the naive normal approximation for small samples), chi-squared tests, and basic regression formulas. Evan Miller is particularly known for advocating the Wilson confidence interval for rating systems — a formula he popularized for ranking user-generated content by lower confidence bound rather than raw average.

This kind of reference was important in 2013 because the data science tooling ecosystem was still immature. A programmer building experimentation infrastructure couldn't assume teammates understood statistical power or Type I/II errors. Having formulas in pseudocode form lowered the barrier to correct implementation.

## Key points

- Wilson score interval for proportion confidence: better than naive (p ± z√(p(1-p)/n)) for small n or extreme p
- Sample size formula: n = (z_α/2 + z_β)² × (p₁(1-p₁) + p₂(1-p₂)) / (p₁-p₂)² — the required sample for A/B test power
- Chi-squared test for categorical data: measures deviation from expected frequencies
- Effect size (Cohen's d) separates statistical significance from practical significance
- Evan Miller's separate post How Not to Run an A/B Test is a companion to this — covers peeking bias
- The Wilson lower bound ranking formula: (p + z²/2n - z√(p(1-p)/n + z²/4n²)) / (1 + z²/n)

[Original](http://www.evanmiller.org/statistical-formulas-for-programmers.html)
