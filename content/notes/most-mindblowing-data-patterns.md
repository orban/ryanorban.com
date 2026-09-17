---
title: The Most Mind-Blowing Patterns from Data Analysis
date: 2013-05-23
categories:
  - data-science
  - stories
  - discovery
  - quora
  - analytics
description: A Quora thread collecting data scientists' most surprising analytical discoveries — unexpected patterns that upended assumptions or revealed hidden structure. A catalog of the 'aha moments' that make exploratory data analysis valuable.
params:
  source: pinboard
  sourceUrl: http://www.quora.com/Big-Data/What-is-the-most-mind-blowing-pattern-you-have-ever-discovered-through-any-form-of-analysis
---

![The Most Mind-Blowing Patterns from Data Analysis](/images/notes/most-mindblowing-data-patterns.png)

## Summary

This Quora thread asked data scientists and analysts to share the most surprising patterns they'd discovered through analysis — the counterintuitive findings, hidden correlations, and unexpected structure that made exploratory data analysis worthwhile. The thread collected a range of answers spanning fraud detection, social networks, epidemiology, and consumer behavior.

The kinds of answers that appear in threads like this tend to cluster around a few archetypes: Simpson's paradox (a trend appears in combined data but reverses in every subgroup), unexpected null results (two things you'd expect to correlate don't), scale surprises (a pattern only visible at a certain data granularity), and network effects (small network position changes cascading to large outcome changes).

The thread is valuable as a catalog of the aha moments that characterize skilled data analysis — the moments where a chart or query reveals something the intuition didn't predict. These stories also function as templates for what to look for: check for Simpson's paradox in your aggregates, look for non-linear scale effects, visualize distributions before running tests.

## Key points

- Exploratory data analysis uncovers patterns that confirm-first hypothesis testing would miss
- Simpson's paradox is a recurring theme: aggregate trends masking reversed sub-group trends
- Network effects and power law distributions consistently surprise: most graphs are dominated by a small number of high-degree nodes
- Null results are as informative as positive findings — things that *don't* correlate tell you about causal structure
- The collection reinforces that data visualization before statistical testing catches anomalies and distributional issues
- Quora in 2013 was a significant knowledge-sharing venue for data scientists — this kind of informal case study collection was its strength

[Original](http://www.quora.com/Big-Data/What-is-the-most-mind-blowing-pattern-you-have-ever-discovered-through-any-form-of-analysis)
