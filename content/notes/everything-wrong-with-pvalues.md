---
title: Everything Wrong With P-Values Under One Roof
date: 2013-10-07
categories:
  - statistics
  - p-values
  - null-hypothesis-testing
  - methodology
  - critique
description: A comprehensive critique of p-values and null hypothesis significance testing — cataloguing the ways researchers misinterpret and misuse them. Part of a growing 2013 literature on the replication crisis and statistical reform.
params:
  source: pinboard
  sourceUrl: http://preview.getprismatic.com/story/1381074475043?share=true
---

![Everything Wrong With P-Values Under One Roof](/images/notes/everything-wrong-with-pvalues.png)

## Summary

By 2013, the critique of p-values and null hypothesis significance testing (NHST) had accumulated into a substantial literature. This piece aggregated the main objections in one place: p-values answer the wrong question, they're routinely misinterpreted, the 0.05 threshold is arbitrary and creates publication bias, and statistical significance is routinely confused with practical significance.

The core misinterpretation: a p-value of 0.03 does not mean there's a 97% chance the null hypothesis is false. It means: if the null hypothesis were true, you'd see data this extreme only 3% of the time by chance. These are not the same thing. The probability of data given hypothesis ≠ the probability of hypothesis given data — the latter is what researchers actually want, which requires Bayesian inference and a prior distribution.

The 2013 context: the replication crisis in psychology and social science was becoming visible. A major replication effort had just found that many published findings couldn't be replicated. p-hacking — running multiple tests and reporting only the significant ones — was identified as a systematic driver of false discoveries. The FDA, major journals, and statistical societies were beginning to question whether NHST was producing reliable science.

## Key points

- p-values answer "how surprising is this data if H₀ is true — not how likely is H₀ to be false given this data." These are different questions.
- The 0.05 significance threshold is arbitrary (Fisher's heuristic) and creates publication bias toward false positives.
- Statistical significance ≠ practical significance — a p < 0.001 result can describe a tiny, meaningless effect with a large enough sample.
- p-hacking: multiple comparisons inflate false positive rate; selective reporting of significant results creates the appearance of reliable findings.
- Connected to the replication crisis in psychology, nutrition, and social science that was becoming apparent in 2013.

[Original](http://preview.getprismatic.com/story/1381074475043?share=true)
