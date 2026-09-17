---
title: A Short Chronology of Deep Learning for Tabular Data
date: 2022-09-05
categories:
  - machine-learning
  - tabular-data
  - deep-learning
  - gradient-boosting
  - research
description: Sebastian Raschka's chronological survey of deep learning approaches for tabular data — the domain where gradient boosted trees still dominate. A clear-eyed accounting of why deep learning hasn't won on structured data despite winning everywhere else.
params:
  source: pinboard
  sourceUrl: https://sebastianraschka.com/blog/2022/deep-learning-for-tabular-data.html
---

## Summary

Sebastian Raschka's post surveys the history of applying deep learning to tabular data — structured data in rows and columns, as opposed to images or text. The central tension: deep learning has dramatically outperformed older methods in computer vision, NLP, and speech, but for tabular data, gradient boosted trees (XGBoost, LightGBM, CatBoost) continue to win on most benchmarks. Why?

The chronology covers key milestones: entity embeddings for categorical variables, TabNet (attention-based tabular learning), SAINT (self-attention and intersample attention), FT-Transformer (adapting the standard transformer architecture to tabular features), and various self-supervised pretraining approaches. Each attempted to close the gap with gradient boosting, but none definitively surpassed it. The 2021 paper "Why tree-based models still outperform deep learning on tabular data" by Grinsztajn et al. offered a systematic analysis: tabular datasets have features that don't exhibit the spatial or temporal locality that deep learning architectures exploit in images and text.

The practical implication: for most tabular ML problems in industry (fraud detection, credit scoring, churn prediction), start with XGBoost or LightGBM before reaching for deep learning. Deep learning on tabular data makes sense when: (1) the dataset is very large (millions+ rows), (2) you need embeddings for downstream use, or (3) the features contain heterogeneous types (images + tabular) that benefit from joint training.

## Key points

- Gradient boosted trees (XGBoost, LightGBM) still outperform deep learning on most tabular benchmarks.
- Key deep learning approaches surveyed: entity embeddings, TabNet, SAINT, FT-Transformer.
- Grinsztajn et al. (2021) explains why: tabular data lacks spatial/temporal locality that DL architectures exploit.
- Deep learning is competitive on tabular data when datasets are very large or require joint training with other modalities.
- Self-supervised pretraining on tabular data is an active area but hasn't matched BERT-style gains in NLP.
- Practical default: start with XGBoost/LightGBM; justify deep learning before using it.

[Original](https://sebastianraschka.com/blog/2022/deep-learning-for-tabular-data.html)
