---
title: Jeremy Howard on the Big Data Obsession
date: 2013-08-15
categories:
  - big-data
  - machine-learning
  - jeremy-howard
  - data-science
  - opinion
description: Jeremy Howard's Quora answer on why the 'big data' obsession was somewhat misplaced — arguing that algorithms and predictive modeling matter more than raw data volume, and that the real value was in applying machine learning, not just collecting more data. A contrarian view from someone who knew ML deeply before the hype peaked.
params:
  source: pinboard
  sourceUrl: http://www.quora.com/Why-the-current-obsession-with-big-data/answer/Jeremy-Howard
---

![Jeremy Howard on the Big Data Obsession](/images/notes/jeremy-howard-big-data-obsession.png)

## Summary

Jeremy Howard — founder of Kaggle at the time (later founder of [fast.ai](/notes/fastai/)) — answered a Quora question about why big data had become so culturally prominent. His answer pushed back on the premise: the obsession with data volume was somewhat misplaced, because machine learning algorithms and the ability to apply them well mattered more than raw scale. Most companies didn't have Google-scale data problems; they had algorithm and expertise problems.

This was a contrarian position in 2013, when "big data" had become a marketing phenomenon and Hadoop was being sold as a solution before companies had articulated the problem. Howard's view was that the real value came from predictive modeling — using whatever data you had to make better decisions — rather than from the infrastructure required to store and process massive volumes. A small dataset with a good model often beat a large dataset with a naive approach.

The argument was consistent with Howard's work: Kaggle was founded on the premise that machine learning competitions using bounded datasets could surface world-class predictive models. The best Kaggle competitors routinely used sophisticated feature engineering and ensemble methods rather than brute-force scale. This algorithms over data view later became more nuanced as deep learning showed that scale (both data and compute) genuinely mattered — but in 2013, most enterprises were nowhere near those thresholds.

## Key points

- Big data vs. machine learning: Howard's argument — most companies needed better algorithms and expertise before more data infrastructure.
- Kaggle as evidence: world-class ML performance achieved on fixed, bounded datasets through better modeling, not bigger data.
- The data flywheel counterargument: companies like Google and Netflix did genuinely benefit from data scale — but most businesses weren't at that threshold.
- Feature engineering > data volume: for typical business datasets in 2013, domain-informed features beat scale-based approaches.
- Jeremy Howard's subsequent work at [fast.ai](/notes/fastai/) focused on making deep learning accessible — eventually he'd advocate for scale too, but targeted at the algorithms side.
- The big data hype critique aged well: by 2015-2016, the industry was having serious conversations about whether companies had bought too much Hadoop infrastructure.

[Original](http://www.quora.com/Why-the-current-obsession-with-big-data/answer/Jeremy-Howard)
