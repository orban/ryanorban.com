---
title: "sklearn-pandas: Bridge Between pandas and scikit-learn"
date: 2013-10-09
categories:
  - scikit-learn
  - pandas
  - python
  - machine-learning
  - data-science
description: sklearn-pandas is a library bridging pandas DataFrames and scikit-learn's pipeline API — enabling column-level transformations with named features rather than anonymous numpy arrays. Fills a friction point that frustrated every data scientist using both libraries together.
params:
  source: pinboard
  sourceUrl: https://github.com/paulgb/sklearn-pandas
---

![sklearn-pandas: Bridge Between pandas and scikit-learn](/images/notes/sklearn-pandas-bridge.png)

## Summary

sklearn-pandas by Paul Butler addresses a real friction point in the Python data science stack: scikit-learn's pipeline API works with NumPy arrays, but pandas DataFrames are where most data scientists do their preprocessing. When you pass a DataFrame to a scikit-learn transformer, column names disappear and you're left with anonymous numeric indices. sklearn-pandas re-introduces named columns into the scikit-learn transformation pipeline.

The library's `DataFrameMapper` class lets you specify per-column transformations with the pandas column names still attached — you can apply StandardScaler to one column, LabelEncoder to another, and leave a third unchanged, all while maintaining the named structure through the transformation. The resulting array flows into scikit-learn estimators as expected.

This was a genuine ergonomics problem. Without it, data scientists had to maintain a mental mapping between column positions in NumPy arrays and the original feature names, which was error-prone and opaque. The problem was later addressed more comprehensively in scikit-learn itself (with `set_output(transform="pandas")` and `ColumnTransformer`), but in 2013 sklearn-pandas was the practical solution.

## Key points

- DataFrameMapper maps named pandas columns to scikit-learn transformers while preserving column name semantics through the pipeline.
- Solves the friction of going from pandas (named columns) to scikit-learn (anonymous NumPy arrays) in ML pipelines.
- Created by Paul Butler, a data scientist active in the Python community in 2013.
- Later superseded by scikit-learn's built-in `ColumnTransformer` and `set_output(transform="pandas")`, but was the standard solution for years.
- Saved during Zipfian Academy cohort when students were building scikit-learn pipelines on real datasets daily.

[Original](https://github.com/paulgb/sklearn-pandas) → GitHub
