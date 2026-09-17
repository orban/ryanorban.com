---
title: Pandas Pivot Table Explained
date: 2015-01-03
categories:
  - python
  - pandas
  - data-science
  - tutorial
description: A step-by-step tutorial on using Pandas pivot tables for business data analysis from the Practical Business Python blog. Pivot tables are the single most useful tool for quickly summarizing and reshaping tabular data, and this covers the full API clearly.
params:
  source: pinboard
  sourceUrl: http://pbpython.com/pandas-pivot-table-explained.html
---

## Summary

Pandas pivot tables bring Excel-style cross-tabulation into Python data workflows — without Excel's limitations on data size, reproducibility, or scriptability. The Practical Business Python blog (pbpython.com) is one of the better resources for translating spreadsheet-native analysis patterns into Python idioms, and this post is a thorough walkthrough of `pd.pivot_table()`.

The core idea: you take a flat table of records and reorganize it by aggregating rows into a matrix indexed by two dimensions, with a summary statistic (sum, mean, count) filling the cells. Unlike SQL `GROUP BY`, pivot tables make the two-dimensional structure of the aggregation visible at a glance. This is especially useful when you want to compare categories against each other — e.g., sales by region and quarter, or errors by type and month.

Pandas implements pivot tables via `pd.pivot_table(df, values, index, columns, aggfunc)`. The `index` and `columns` arguments define the two axes; `values` is what gets aggregated; `aggfunc` defaults to mean but accepts any numpy function or list of functions. The `margins=True` argument adds row/column totals, mimicking Excel's "Grand Total" behavior.

## Key points

- `pd.pivot_table()` takes `index`, `columns`, `values`, and `aggfunc` — the four axes of any cross-tabulation.
- `aggfunc` can be a list of functions (e.g., `[np.sum, np.mean]`) to compute multiple statistics at once.
- `margins=True` adds row and column totals — essential for sanity-checking that sums add up.
- `fill_value` handles NaN cells in the output matrix — important when not all index-column combinations have data.
- Works alongside `pd.crosstab()` which is a simpler wrapper for count-based pivot tables.
- Part of the broader Pandas reshaping toolkit alongside `melt()`, `stack()`, and `unstack()`.

[Original](http://pbpython.com/pandas-pivot-table-explained.html)
