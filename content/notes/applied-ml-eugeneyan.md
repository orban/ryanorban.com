---
title: "applied-ml: Papers and Tech Blogs on ML in Production"
date: 2021-08-31
categories:
  - machine-learning
  - production-ml
  - data-science
  - research
  - resources
description: Eugene Yan's curated list of papers and engineering blog posts from companies sharing real-world ML in production — classification, recommendation, search, NLP, and more. One of the most useful ML reference repositories because it focuses on what actually shipped, not just what was published.
params:
  source: pinboard
  sourceUrl: https://github.com/eugeneyan/applied-ml#data-quality
---

## Summary

eugeneyan/applied-ml is a GitHub repository maintained by Eugene Yan (Amazon, ex-Lazada) that curates papers and engineering blog posts from companies sharing their work on data science and machine learning in production. Unlike academic paper lists, this focuses on what companies actually deployed: recommendation systems, search ranking, NLP pipelines, data quality, and feature engineering in real environments.

The categories reflect what ML practitioners actually spend time on: data quality (a perennial underrated problem), feature stores, model training at scale, inference and serving, monitoring and observability in production, and A/B testing for ML systems. The blog posts included are from Google, Netflix, Airbnb, Uber, LinkedIn, Pinterest, and many others — organizations that have solved these problems at large scale and written about their approaches.

What makes this list valuable is the focus on production ML vs. research ML. Academic papers optimize for novelty; production posts optimize for reliability, latency, cost, and maintainability. The gap between these worlds is real — a SOTA model that takes 3 seconds to serve is useless in many products — and this list sits firmly on the production side.

## Key points

- Curated by Eugene Yan — ML practitioner known for writing about applied ML on his blog.
- Categories: data quality, feature engineering, model training, inference/serving, monitoring, A/B testing — the full production lifecycle.
- Company sources: Google, Netflix, Airbnb, Uber, LinkedIn, Pinterest — teams at real scale.
- Production ML focus distinguishes it from academic reading lists — what actually shipped under real constraints.
- Bookmark URL includes `#data-quality` — that section was likely the specific entry point of interest.

[Original](https://github.com/eugeneyan/applied-ml#data-quality)
