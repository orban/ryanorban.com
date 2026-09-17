---
title: Drawing Inferences From Very Large Datasets
date: 2013-12-29
categories:
  - statistics
  - econometrics
  - big-data
  - p-values
  - statistical-significance
description: Econometrician Dave Giles on why large datasets make standard p-value thresholds useless — with N in the millions, almost any null hypothesis rejects, regardless of practical importance. A necessary corrective for data scientists drowning in statistical significance.
params:
  source: pinboard
  sourceUrl: http://davegiles.blogspot.ca/2011/04/drawing-inferences-from-very-large-data.html
---

## Summary

Dave Giles (UVic econometrician) makes a pointed argument: with very large N, the standard p-value thresholds of 0.05 or 0.10 become dangerously permissive. Granger (1998) showed that with a sufficiently large sample, it's virtually impossible not to reject almost any null hypothesis — statistical significance becomes trivially cheap, and economic significance is what actually matters.

The mechanism is straightforward. Confidence intervals shrink at rate O(1/n), so with N in the millions, even a practically meaningless coefficient difference from zero will produce a p-value near zero. Giles illustrates with three real econometrics papers: a health economics study (N=17,754), a tobacco control paper (N=13,099), and a patent duration study (N≈2,000,000) where p-values are essentially zero. In the last case, statistically significant effects may be economically negligible.

The corrective advice is to either dramatically lower acceptable p-value thresholds when N is large, or shift focus entirely to effect size and practical significance rather than hypothesis testing. This critique became increasingly relevant as big data grew — the same warning applies directly to A/B testing at internet scale.

## Key points

- With large N, confidence intervals shrink as O(1/n) — statistical significance becomes trivially achievable for tiny effects.
- Granger's observation: sufficiently large samples make virtually any null hypothesis rejectable.
- Researchers should use much more conservative p-value thresholds (well below 0.05) when N is in the thousands to millions.
- Better still: focus on effect size and economic significance rather than statistical significance alone.
- Directly relevant to internet-scale A/B testing where N is large enough to detect meaningless differences.
- Three real examples shown: health economics, tobacco control, patent approval — all with N large enough to make standard inference misleading.

[Original](http://davegiles.blogspot.ca/2011/04/drawing-inferences-from-very-large-data.html)
