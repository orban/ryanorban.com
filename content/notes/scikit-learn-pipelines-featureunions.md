---
title: Scikit-learn Pipelines and FeatureUnions
date: 2014-08-08
categories:
  - scikit-learn
  - python
  - machine-learning
  - pipelines
  - feature-engineering
description: Zac Stewart's deep dive into composing scikit-learn Pipelines and FeatureUnions — showing how to chain preprocessing steps, branch feature transformations, and combine them back together while preventing data leakage. The definitive 2014 guide to production-ready sklearn code.
params:
  source: pinboard
  sourceUrl: http://zacstewart.com/2014/08/05/pipelines-of-featureunions-of-pipelines.html
---

![Scikit-learn Pipelines and FeatureUnions](/images/notes/scikit-learn-pipelines-featureunions.png)

## Summary

Scikit-learn's `Pipeline` and `FeatureUnion` are the composition primitives that turn sklearn from a collection of algorithms into an actual system. Zac Stewart's 2014 post is one of the best explanations of how to use them together — particularly the nested pattern where `FeatureUnion` branches the feature engineering and `Pipeline` chains the steps.

A `Pipeline` sequences transformers and a final estimator: `[('scale', StandardScaler()), ('model', LogisticRegression())]`. The key benefit is that `fit()` on the pipeline fits each step in sequence, using only the training data at each stage — no data leakage through cross-validation folds. `FeatureUnion` runs multiple transformers in parallel and concatenates their outputs — useful when you want to apply different transformations to different columns (e.g., TF-IDF on text + normalization on numerics) and then combine the results.

The composition pattern the post describes: `Pipeline([('features', FeatureUnion([('text_pipe', Pipeline([...])), ('numeric_pipe', Pipeline([...]))])), ('model', SVC())])`. This builds the full feature engineering + modeling pipeline as a single object that can be cross-validated, pickled, and scored on new data without separately applying each transformation step.

## Key points

- `Pipeline`: chains transformers + estimator — `fit()` chains through training data only, preventing data leakage.
- `FeatureUnion`: runs multiple transformers in parallel, concatenates outputs — enables different processing paths per feature type.
- Nested composition: `Pipeline` inside `FeatureUnion` inside `Pipeline` — builds arbitrarily complex preprocessing as a single object.
- `cross_val_score(pipeline, X, y)`: cross-validates the entire pipeline — the correct way to get unbiased performance estimates.
- `pickle.dump(pipeline)`: serialize the entire fitted pipeline for serving — no separate serialization per step.
- This pattern is now idiomatic scikit-learn — the 2014 post was ahead of its time in formalizing it.

[Original](http://zacstewart.com/2014/08/05/pipelines-of-featureunions-of-pipelines.html)
