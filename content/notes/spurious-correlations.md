---
title: Spurious Correlations
date: 2014-05-12
categories:
  - statistics
  - correlation
  - causation
  - humor
  - data-visualization
description: Tyler Vigen's Spurious Correlations site generates charts showing absurd correlations between unrelated variables — US cheese consumption vs. deaths by bedsheet tangling, etc. The clearest possible demonstration that correlation does not imply causation.
params:
  source: pinboard
  sourceUrl: http://www.tylervigen.com/
---

## Summary

[Spurious Correlations](/notes/spurious-correlations/) by Tyler Vigen is a website that automatically generates charts showing statistically strong correlations between completely unrelated variables: per capita cheese consumption correlated with deaths by bedsheet tangling (r = 0.947), number of films Nicolas Cage appeared in correlated with swimming pool drownings, etc.

The site is simultaneously a comedy project and a statistics lesson. Every chart is real data with a real correlation — and completely meaningless. The mechanism is data dredging (also called p-hacking or fishing): if you test enough variable pairs, you will find spurious high correlations by chance. With thousands of variables and years of data, the chance of finding a nonsense correlation above 0.9 approaches certainty.

The practical lesson for data science: never stop at "these two things are correlated." You must have a causal mechanism, a theoretical reason why A might cause B (or both might be caused by C), before a correlation becomes evidence of anything. This is the correlation vs. causation fallacy made viscerally obvious. Vigen turned this into a book in 2015.

## Key points

- Data dredging / multiple comparisons problem: test enough pairs, find spurious correlations — the site demonstrates this at scale with real government datasets.
- Correlation does not imply causation: the canonical, clearest demonstration of the most-misunderstood concept in applied statistics.
- High correlation coefficient (r ≈ 0.95) with zero causal relationship — readers often assume high r means real relationship, this corrects that.
- Defense: pre-registration (specify hypothesis before seeing data), Bonferroni correction (adjust significance threshold for multiple tests), domain knowledge as a prior.
- Tyler Vigen also made the methodological point serious: the book version included a discussion of confounders and causal inference as the corrective.

[Original](http://www.tylervigen.com/)
