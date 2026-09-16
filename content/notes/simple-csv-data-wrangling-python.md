---
title: Simple CSV Data Wrangling with Python
date: 2014-12-03
categories:
  - python
  - data-wrangling
  - csv
  - tutorial
  - data-science
description: District Data Labs tutorial on CSV data wrangling with Python, covering the basics of loading, cleaning, and transforming tabular data before analysis. A foundational skill that every data scientist spends far more time on than they'd like.
params:
  source: pinboard
  sourceUrl: http://districtdatalabs.silvrback.com/simple-csv-data-wrangling-with-python
---

## Summary

District Data Labs was a data science consulting and education firm active in the mid-2010s that produced practical tutorials bridging the gap between classroom ML theory and real data work. This post focuses on CSV data wrangling — the unglamorous preprocessing step that precedes any actual analysis.

CSV wrangling in Python circa 2014 meant choosing between the standard library's `csv` module and Pandas. The `csv` module is lower-level: you get row-by-row iteration over dicts or lists, handle type coercion yourself, and write the data structures you want. Pandas `read_csv()` is higher-level: automatic type inference, missing value handling, and immediate access to the full Pandas API. The tradeoff is memory — `csv` is streaming, Pandas loads everything.

The tutorial likely covers the common wrangling tasks: handling headers, dealing with encoding issues (`utf-8` vs `latin-1`), cleaning dirty string fields, parsing dates, coercing numeric types, detecting and handling `None`/`NaN`, filtering rows, and writing cleaned output. These remain the daily operations of data wrangling even as the tools have evolved — Pandas, then Polars, now DuckDB, all doing the same conceptual operations.

## Key points

- CSV is the lingua franca of tabular data exchange — cleaning it is the first step of every real data project.
- Python's `csv` module: streaming, low memory, manual type handling — good for large files or simple transforms.
- `[[Pandas]].read_csv()`: loads to memory, automatic types, direct access to reshape/filter/aggregate API.
- Common operations: encoding fixes, header normalization, date parsing, null handling, numeric coercion.
- District Data Labs was producing practical data science content in 2014 before Medium/Towards Data Science dominated the space.
- The janitor work framing — later popularized by the NYT — describes the majority of real data science time.

[Original](http://districtdatalabs.silvrback.com/simple-csv-data-wrangling-with-python)
