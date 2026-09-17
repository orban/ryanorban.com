---
title: Many Models Workflows in Python
date: 2021-03-28
categories:
  - python
  - machine-learning
  - data-science
  - workflows
  - statistics
description: Alex Hayes's port of the R 'many models' workflow pattern to Python — fitting many models across groups using tidy data conventions. Bridges the gap between R's purrr/broom/tidymodels idioms and Python's pandas/scikit-learn ecosystem.
params:
  source: pinboard
  sourceUrl: https://www.alexpghayes.com/blog/many-models-workflows-in-python-part-i/
---

## Summary

Alex Hayes writes this as a translation of the many models pattern from R to Python. In R, the idiom (popularized by Hadley Wickham in *R for Data Science*) involves nesting data frames, fitting a model for each group using `purrr::map`, and tidying results with `broom` — all staying within a tidyverse workflow. Python has the components but lacks the idiomatic glue.

The post demonstrates fitting models across groups using Pandas `groupby`, `apply`, and storing model objects in DataFrame cells — a technique that feels un-Pythonic but works. Each group gets its own fitted model, and results can be extracted and compared systematically. This is useful for exploratory analysis where you want to understand how a relationship varies across subgroups (e.g., separate linear models per country, per product category, per cohort).

The broader appeal is the functional programming discipline: treat models as data, compose operations over them, and keep everything in a tabular structure that can be inspected, filtered, and joined. Alex Hayes brings an R statistician's sensibility to Python, which is useful for data scientists who cross the R/Python boundary or who find Python's scientific stack less ergonomic for statistical work.

## Key points

- Many models pattern: fit one model per group, compare results across groups — useful for exploratory stratified analysis.
- Uses Pandas `groupby` + `apply` to store model objects per group in DataFrame cells.
- Ports tidyverse R idioms (purrr, broom) to Python — bridges the two ecosystems.
- Functional programming discipline: models as data, composable operations.
- By Alex Hayes — R statistician perspective applied to Python data workflows.

[Original](https://www.alexpghayes.com/blog/many-models-workflows-in-python-part-i/)
