---
title: Why Machine Learning Fails
date: 2013-10-16
categories:
  - machine-learning
  - data-science
  - failure-modes
  - methodology
  - critique
description: Louis Dorard's analysis of why machine learning projects fail in practice — usually not because the algorithms are wrong but because the problem setup, data quality, or evaluation approach is broken. The engineering side of ML is where most projects die.
params:
  source: pinboard
  sourceUrl: http://www.louisdorard.com/blog/why-machine-learning-fails
---

![Why Machine Learning Fails](/images/notes/why-machine-learning-fails.png)

## Summary

Louis Dorard's post identifies the failure modes that kill machine learning projects in practice. The core argument: ML projects rarely fail because the algorithm is wrong. They fail because the problem was poorly defined, the training data was unrepresentative, the evaluation metric didn't match the business objective, or the model was deployed into a production environment that looked nothing like the training data distribution.

This was important perspective in 2013, when the field was still in a period of hype where many teams believed that having better algorithms was the main bottleneck. In practice, garbage in, garbage out applied at every stage — unclear problem formulation, weak feature engineering, data leakage, and misaligned metrics each independently doomed projects before the algorithm choice ever mattered.

Dorard also points to the evaluation trap: optimizing on the wrong metric. A spam filter optimized for precision but evaluated on accuracy looks fine on paper while missing high-value targets. A recommendation system optimized for click-through rate pushes clickbait. The disconnect between what models are trained to do and what business outcomes require is a perennial machine learning failure mode.

## Key points

- ML failure is usually upstream of algorithms: bad problem definition, poor data quality, data leakage, wrong evaluation metric.
- Feature engineering often matters more than algorithm choice — a simple model on great features beats a complex model on bad ones.
- Evaluation misalignment: optimizing for a proxy metric that diverges from the actual business objective is a common silent failure mode.
- Distributional shift: models fail when production data distribution differs from training data — a problem that grows worse the longer a model runs.
- Written in 2013, as the first wave of ML hype peaked; anticipates the AI winter conversations about why so many ML projects fail to deliver value.

[Original](http://www.louisdorard.com/blog/why-machine-learning-fails)
