---
title: Statistical Analysis Made Easy in Python
date: 2014-01-02
categories:
  - python
  - statistics
  - data-science
  - tutorial
  - scipy
description: Randy Olson's tutorial on statistical analysis in Python using SciPy stats and pandas — t-tests, ANOVA, chi-squared, and more. A practical bridge from R's built-in stats to Python's ecosystem in 2012.
params:
  source: pinboard
  sourceUrl: http://www.randalolson.com/2012/08/06/statistical-analysis-made-easy-in-python/
---

## Summary

Randy Olson's tutorial walks through common statistical tests in Python using SciPy stats and pandas: t-tests, ANOVA, chi-squared tests, and Pearson correlation. The post was written as a practical reference for analysts coming from R who needed to replicate their workflow in Python without relearning statistics from scratch.

The value in 2012-2014 was partly filling a documentation gap: SciPy stats had the functions, but knowing which one to call for which situation wasn't obvious. This tutorial mapped statistical test names (things R users already knew) to their Python equivalents, making the transition less painful.

## Key points

- Covers the most common inferential statistics tests: one-sample t-test, two-sample t-test, paired t-test, ANOVA, chi-squared, Pearson correlation
- Uses SciPy stats (`scipy.stats`) throughout — the standard library for statistical tests in Python
- Demonstrates with pandas DataFrames as the data container — the idiomatic combination for data analysis
- Includes interpretation guidance: not just how to call the function, but how to read the output (p-value, test statistic, degrees of freedom)
- Part of Randy Olson's broader data science education work, which also includes matplotlib tutorials and data visualization guides

[Original](http://www.randalolson.com/2012/08/06/statistical-analysis-made-easy-in-python/)
