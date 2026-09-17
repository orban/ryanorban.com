---
title: Multiple A/B/n Tests in Marketing with ANOVA and R
date: 2014-08-18
categories:
  - a-b-testing
  - statistics
  - anova
  - r
  - marketing
description: Marketing Distillery's practical guide to running multiple A/B/n tests using ANOVA in R — extending the standard two-group t-test to handle multiple variants simultaneously without inflating false positive rates.
params:
  source: pinboard
  sourceUrl: http://www.marketingdistillery.com/2014/08/10/multiple-abn-tests-in-marketing-with-anova-and-r/
---

![Multiple A/B/n Tests in Marketing with ANOVA and R](/images/notes/multiple-abn-tests-anova-r.png)

## Summary

Standard A/B testing compares two groups — a control and a treatment. A/B/n testing extends this to multiple treatment variants simultaneously (A vs. B vs. C vs. D). The statistical challenge: if you run separate pairwise t-tests for every pair of variants, you inflate the false positive rate — with 4 variants and 6 pairwise tests, the probability of at least one false positive at p<0.05 is much higher than 5%.

ANOVA (Analysis of Variance) solves this by testing whether *any* group means differ simultaneously, rather than running pairwise comparisons. If the ANOVA F-test rejects the null hypothesis that all group means are equal, you then run post-hoc pairwise tests (Tukey's HSD, Bonferroni correction) to find *which* pairs differ — with corrections that maintain the family-wise error rate.

The R implementation: `aov()` fits the ANOVA model; `summary()` shows the F-statistic and p-value; `TukeyHSD()` provides pairwise comparisons with simultaneous confidence intervals. This workflow is standard in academic experimental design but was less commonly used in marketing analytics circles in 2014, where the simpler t-test dominated.

## Key points

- A/B/n testing with multiple variants: running separate t-tests inflates false positive rate — use ANOVA instead.
- ANOVA F-test: does any group mean differ? The global test before pairwise comparisons.
- Tukey's HSD (Honestly Significant Difference): post-hoc pairwise test that controls family-wise error rate.
- Bonferroni correction: conservative alternative — divide alpha by number of comparisons.
- `aov()` + `TukeyHSD()` in R: the standard workflow for multi-variant experiments.
- Multiple comparisons problem: the statistical reason A/B/n analysis requires more than repeated t-tests.

[Original](http://www.marketingdistillery.com/2014/08/10/multiple-abn-tests-in-marketing-with-anova-and-r/)
