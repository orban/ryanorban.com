---
title: Troll Detection with Scikit-Learn
date: 2014-01-14
categories:
  - machine-learning
  - nlp
  - text-classification
  - scikit-learn
  - content-moderation
description: Impermium's Kaggle blog post on building a troll detection classifier with scikit-learn — text features, gradient boosting, and the practical challenges of training on imbalanced toxic comment data.
params:
  source: pinboard
  sourceUrl: http://blog.kaggle.com/2012/09/26/impermium-andreas-blog/
---

## Summary

Impermium's post on the Kaggle blog walks through building a troll and spam detection system using scikit-learn. The problem is standard text classification — extract features from comments, train a classifier to distinguish toxic from benign — but the practical challenges are more interesting: class imbalance (toxic comments are rare), adversarial dynamics (users adapt to avoid detection), and the cost asymmetry between false positives (blocking legitimate users) and false negatives (allowing toxicity).

The post covers feature engineering from text: bag-of-words, TF-IDF, character n-grams, and behavioral signals like posting frequency and account age. It's one of the earlier practical demonstrations that these NLP pipelines could be assembled quickly in Python using scikit-learn's `Pipeline` and `FeatureUnion` constructs.

## Key points

- TF-IDF combined with behavioral features (account age, post frequency) outperforms text features alone — trolls have distinctive posting patterns beyond just word choice
- Class imbalance is the central practical challenge: toxic comments are rare, so a naive classifier achieves high accuracy by predicting not toxic for everything
- scikit-learn's `Pipeline` abstraction lets you compose preprocessing and classification steps cleanly — shown as a concrete example here
- Character n-grams capture deliberate misspellings used to evade keyword filters — a key feature for adversarial text classification
- The arms race dynamic: once patterns are known, adversarial users adapt, so models need continuous retraining on fresh data

[Original](http://blog.kaggle.com/2012/09/26/impermium-andreas-blog/)
