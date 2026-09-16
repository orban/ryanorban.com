---
title: Learning to Rank for Personalised Search (Yandex Kaggle Competition)
date: 2020-07-25
categories:
  - machine-learning
  - learn-to-rank
  - search
  - personalization
  - kaggle
description: Yanir Seroussi's Kaggle competition post-mortem on Yandex Search Personalisation — applying learning-to-rank techniques to personalized search with behavioral signals. A practical case study of LTR on real search logs.
params:
  source: pinboard
  sourceUrl: https://yanirseroussi.com/2015/02/11/learning-to-rank-for-personalised-search-yandex-search-personalisation-kaggle-competition-summary-part-2/
---

## Summary

Yanir Seroussi wrote this retrospective on the Yandex Search Personalisation Kaggle competition, which released a large dataset of Yandex search logs including user behavior signals (clicks, dwell time) alongside query-document pairs. The task: predict which results users would click on given their historical behavior — essentially personalised search ranking as a supervised learning problem.

The competition dataset was unusual in scale and quality for a public ML dataset at the time — real production search logs from a major search engine with behavioral ground truth. This made it a valuable benchmark for learning-to-rank approaches that use implicit feedback rather than explicit relevance judgments. The difference matters: explicit labels (TREC style) are expensive and sparse; implicit signals (clicks, time on page) are abundant but noisy.

The key insight from Seroussi's analysis: behavioral personalization signals (what this user has clicked on before, their query history, their interaction patterns) substantially improve ranking quality over generic relevance signals. This validates the intuition behind personalized search — a user who consistently clicks engineering results for ambiguous queries should get engineering-biased rankings. The implementation used gradient boosted trees trained on a rich feature set combining query-document similarity features with user history features. Related work is LambdaMART, which is typically the algorithm underlying this kind of competition solution.

## Key points

- Yandex Search Personalisation Kaggle competition — rare public dataset of real production search logs.
- Task: personalised search ranking using behavioral signals (click history, dwell time) + query features.
- Key finding: user history signals significantly improve ranking over generic relevance signals.
- Implicit feedback (clicks) as supervision for ranking — abundant but noisy vs. sparse but accurate explicit labels.
- Solution approach: gradient boosted trees with combined query-document and user history features — related to LambdaMART.
- Connects to learning-to-rank ecosystem: see Metarank, hybrid search, and the LTR cluster.

[Original](https://yanirseroussi.com/2015/02/11/learning-to-rank-for-personalised-search-yandex-search-personalisation-kaggle-competition-summary-part-2/)
