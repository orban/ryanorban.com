---
title: So You Think You Can Test?
date: 2014-07-02
categories:
  - ab-testing
  - statistics
  - interactive
  - experimentation
description: An interactive tool by Lukas Vermeer that lets you distinguish A/A tests from A/B tests visually — a demonstration that human intuition about statistical significance is unreliable. Forces the realization that we can't eyeball whether a difference is real.
params:
  source: pinboard
  sourceUrl: http://destack.home.xs4all.nl/projects/confidence/
---

## Summary

Lukas Vermeer's hackathon project is a deceptively simple interactive quiz: you're shown a series of test results and asked to judge whether each shows a real effect (A/B test) or no effect (A/A test). The exercise is humbling — human intuition for statistical patterns is poor, and most people perform near chance. It's a visceral demonstration of why A/B testing requires statistical significance testing rather than visual inspection.

The core insight: A/A tests (where both variants are identical) still produce noisy data that *looks* like there might be a difference. Conversion rates fluctuate day to day; sample sizes within a single session are often too small for the noise to average out; and human pattern-detection tends to see signal in noise. We are cognitively predisposed to find patterns — which makes us bad at distinguishing random variation from true effects.

This is why null hypothesis significance testing exists: not as a bureaucratic formality, but as a check on our tendency to over-interpret data. The p-value formalizes the question "could this result have arisen by chance?" and gives a threshold for when we should be skeptical of that explanation.

## Key points

- Human intuition for distinguishing real effects from noise is poor — statistical testing exists precisely because eyeballing data doesn't work.
- A/A tests produce the same visual noise as small-effect A/B tests — you cannot reliably tell them apart without a significance test.
- p-value threshold (α = 0.05) means: accept a 5% false positive rate. Running many tests without correction inflates this — the multiple testing problem.
- Effect size vs. statistical significance: a result can be statistically significant but practically irrelevant (tiny effect, huge sample), or practically important but not yet significant (real effect, small sample).
- Interactive format drives the lesson home better than any explanation: experiencing your own failure rate is more memorable than reading about the concept.

[Original](http://destack.home.xs4all.nl/projects/confidence/)
