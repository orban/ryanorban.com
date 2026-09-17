---
title: BayesDB
date: 2013-12-10
categories:
  - bayesian
  - databases
  - probabilistic-programming
  - mit
  - machine-learning
description: BayesDB from MIT CSAIL's probabilistic computing group — a database system that lets you query statistical relationships using a SQL-like language (BQL) without specifying a model. Automatically infers the right probabilistic model from data.
params:
  source: pinboard
  sourceUrl: http://probcomp.csail.mit.edu/bayesdb/
---

## Summary

BayesDB is a probabilistic database system developed at MIT CSAIL's Probabilistic Computing Project (probcomp). The core premise: analysts should be able to ask statistical questions about data using a familiar SQL-like interface without needing to choose, fit, and diagnose a statistical model manually. BayesDB handles the model selection internally.

The system introduces BQL (Bayesian Query Language), an extension to SQL with statements like `ESTIMATE PROBABILITY OF`, `SIMULATE`, and `ESTIMATE DEPENDENCE PROBABILITY`. These let users ask questions like "given this patient's symptoms, what is the probability they have this condition? or which columns are statistically dependent on each other?" without writing any model code.

Under the hood, BayesDB uses CrossCat — a nonparametric Bayesian inference engine that simultaneously discovers the column-level structure (which features are related) and the row-level clustering (which data points are similar). This avoids the need to pre-specify the number of clusters or the dependency structure.

## Key points

- BQL (Bayesian Query Language): SQL-like syntax for probabilistic queries — `ESTIMATE`, `SIMULATE`, `INFER` operators.
- No model specification required: CrossCat nonparametric model infers column dependencies and row clusters automatically.
- Query types: probability estimation, simulation of new data, dependence analysis between variables, anomaly detection.
- Target users: data analysts who want statistical inference without the modeling overhead.
- From MIT CSAIL Probabilistic Computing Project — same group behind Church and later Gen (probabilistic programming languages).
- Represents the probabilistic programming vision applied to the database abstraction layer.

[Original](http://probcomp.csail.mit.edu/bayesdb/)
