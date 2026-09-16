---
title: Converting Categorical Data into Numbers with Pandas and Scikit-Learn
date: 2014-05-01
categories:
  - machine-learning
  - pandas
  - scikit-learn
  - python
  - data-preprocessing
description: FastML tutorial on converting categorical variables to numeric form using Pandas and scikit-learn's LabelEncoder and OneHotEncoder. A foundational data preprocessing step that trips up many beginners.
params:
  source: pinboard
  sourceUrl: http://fastml.com/converting-categorical-data-into-numbers-with-pandas-and-scikit-learn/
---

## Summary

Most machine learning algorithms require numeric inputs, but real datasets are full of categorical variables — things like city names, product categories, or user types. This FastML post covers the two primary encoding strategies available in Pandas and Scikit-Learn: label encoding (assigning an integer to each category) and one-hot encoding (creating a binary column for each category value).

Label encoding is fast but imposes a spurious ordinal relationship — the algorithm may interpret category 3 as greater than category 1, even when no such ordering exists. One-hot encoding avoids this but expands the feature space, which can cause problems with high-cardinality columns. Choosing between them correctly depends on the algorithm and the nature of the variable, and getting it wrong is a common source of subtle bugs in ML pipelines.

In the Scikit-Learn ecosystem, this is handled by `LabelEncoder` and `OneHotEncoder` in `sklearn.preprocessing`, or via Pandas `get_dummies()`. The post walks through both approaches with code, which was valuable in 2014 when Scikit-Learn's documentation was less polished than today.

## Key points

- Categorical variables must be encoded before use with most machine learning algorithms.
- Label encoding (`LabelEncoder`): fast but implies ordinal ranking — safe only for tree-based models.
- One-hot encoding (`OneHotEncoder` / `pd.get_dummies()`): correct for nominal categories, expands feature space.
- High-cardinality columns (thousands of unique values) can make one-hot encoding impractical.
- Both Pandas and Scikit-Learn provide utilities — the post covers both in parallel.

[Original](http://fastml.com/converting-categorical-data-into-numbers-with-pandas-and-scikit-learn/)
