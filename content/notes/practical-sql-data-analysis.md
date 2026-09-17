---
title: Practical SQL for Data Analysis
date: 2021-04-28
categories:
  - sql
  - data-science
  - analytics
  - python
  - pandas
description: Haki Benita's essay showing how SQL can replace Pandas for a surprising range of data analysis tasks — window functions, aggregations, pivoting, and data quality checks. Makes the case that analysts often reach for Python when SQL would be faster and simpler.
params:
  source: pinboard
  sourceUrl: https://hakibenita.com/sql-for-data-analysis
---

## Summary

Haki Benita's essay is a pointed argument: analysts reach for Pandas out of habit, but SQL can handle a large fraction of typical data analysis tasks more cleanly and at better performance. The subtitle What you can do without Pandas frames it as corrective — not anti-Python, but anti-reflexive-Python.

The essay demonstrates SQL window functions (`ROW_NUMBER()`, `LAG()`, `LEAD()`, `RANK()`, running totals, moving averages) applied to analytical questions that people typically load into a DataFrame to solve. It covers CTEs (Common Table Expressions) for readable multi-step queries, pivoting data with `CASE WHEN`, and running data quality checks (null counts, duplicate detection, value distribution) entirely in SQL without exporting to Python first.

The performance argument matters: for large datasets, pushing computation into the database avoids the network transfer cost of moving data to Python, uses the database's optimized execution engine, and keeps analysis close to where the data lives. For datasets that fit in a Pandas DataFrame comfortably, the tradeoff is less clear — but for anything at serious scale, SQL-first analysis is often faster and simpler.

## Key points

- SQL window functions replace many Pandas operations: `LAG()`, `LEAD()`, `RANK()`, `ROW_NUMBER()`, running totals.
- CTEs (Common Table Expressions) allow readable multi-step queries without subquery nesting.
- Data quality checks in SQL: null counts, duplicates, distribution histograms — no export to Python needed.
- Performance: for large datasets, SQL computation beats Python DataFrame processing by avoiding data transfer.
- By Haki Benita — practical focus, PostgreSQL-flavored but broadly applicable.

[Original](https://hakibenita.com/sql-for-data-analysis)
