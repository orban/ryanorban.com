---
title: "Pandas and Python: Top 10"
date: 2013-03-08
categories:
  - python
  - pandas
  - data-science
  - reference
description: Manish Amde's top 10 Pandas techniques for data scientists — written in March 2013 when pandas was still a young library (0.10.x era). Captures the practical workflows that made pandas the dominant tool for tabular data manipulation in Python.
params:
  source: pinboard
  sourceUrl: http://manishamde.github.com/blog/2013/03/07/pandas-and-python-top-10/
---

## Summary

Manish Amde's post from March 2013 collected the ten most practically useful pandas operations for data scientists — written at a time when pandas was still in its 0.10.x release cycle and the community was still developing best practices. Wes McKinney had created pandas at AQR Capital Management and open-sourced it in 2009; by 2013 it was becoming the standard tool for tabular data manipulation in Python, but documentation was sparse and learning happened primarily through community posts like this one.

The techniques covered the core pandas workflow: reading data (`read_csv`, `read_excel`), selecting rows and columns (`loc`, `iloc`, boolean indexing), grouping and aggregating (`groupby` + `agg`), handling missing data (`fillna`, `dropna`), merging datasets (`merge`, `join`), applying functions (`.apply`), reshaping (`pivot_table`, `melt`), and time series operations. The GroupBy/split-apply-combine pattern — split the dataframe into groups, apply a function to each, combine results — was the pattern that made pandas most powerful for analytics, analogous to SQL's GROUP BY but with arbitrary Python functions as the aggregation.

What made posts like this valuable in 2013 was that the official pandas documentation was less comprehensive than it later became, and Stack Overflow answers were thin. The community was learning together in real time. The techniques in this post were also building blocks for what would become standard data science workflows: load data, clean and reshape it with pandas, then hand off to scikit-learn or matplotlib for modeling and visualization.

## Key points

- `groupby` + `agg`: the split-apply-combine pattern — the most powerful pandas idiom for analytics, replacing loops over subsets
- `loc` vs. `iloc`: label-based vs. integer-position indexing — a distinction that trips up most new pandas users
- `apply` with custom functions: escaping the built-in aggregations to run arbitrary Python per row or per group
- `pivot_table`: reshaping between wide and long formats — the pandas equivalent of Excel pivot tables
- `merge` / `join`: SQL-style joins between DataFrames — the key to combining datasets that share a key column
- Historical context: 2013-era pandas (0.10-0.11) had different defaults and APIs vs. current versions — `sort` became `sort_values`, `ix` was deprecated in favor of `loc`/`iloc`

[Original](http://manishamde.github.com/blog/2013/03/07/pandas-and-python-top-10/)
 → GitHub
