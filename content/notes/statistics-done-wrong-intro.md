---
title: An Introduction to Data Analysis — Statistics Done Wrong
date: 2013-10-27
categories:
  - statistics
  - p-values
  - bayesian
  - scientific-method
  - data-analysis
description: Alex Reinhart's 'Statistics Done Wrong' introduction to data analysis — opens with the key insight that a p-value measures surprise, not correctness. A corrective for scientists trained in classical statistics who misinterpret their own results.
params:
  source: pinboard
  sourceUrl: http://www.refsmmat.com/statistics/data-analysis.html
---

## Summary

Alex Reinhart's Statistics Done Wrong is a guide to the statistical errors that permeate published scientific research. The introduction establishes the core reframe immediately: a p-value is not a measure of how right your hypothesis is — it's a measure of how surprised you should be by your data if the null hypothesis were true. Conflating low p-value with hypothesis is correct is the single most common error in empirical research.

The guide was written as a corrective for scientists who had been taught to use statistics as a ritual rather than a reasoning tool. Null hypothesis significance testing (NHST) produces p-values, confidence intervals, and the magic 0.05 threshold — none of which directly answer the question scientists actually want to ask: "Given this data, how likely is my hypothesis?" That question requires Bayesian inference, not frequentist statistics.

The save note mentions surprise Bayesian — reflecting the pedagogical move Reinhart makes: showing that the Bayesian framing (posterior probability given data) is actually the more natural way to reason about evidence, even though frequentist methods are what most scientists learn.

## Key points

- A p-value measures surprise under the null, not probability that your hypothesis is correct — this distinction is widely misunderstood.
- Null hypothesis significance testing answers a different question than what researchers want to know; Bayesian inference answers the right question directly.
- The 0.05 significance threshold is arbitrary and was chosen by Fisher as a rough heuristic, not a principled cutoff.
- Statistics Done Wrong documents real errors in published research: underpowered studies, multiple comparisons problems, p-hacking, confidence interval misinterpretation.
- Required reading for anyone analyzing data and drawing conclusions from statistical tests.

[Original](http://www.refsmmat.com/statistics/data-analysis.html)
