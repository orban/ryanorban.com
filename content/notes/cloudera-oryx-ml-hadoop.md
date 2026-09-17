---
title: Cloudera Rebuilding Machine Learning for Hadoop with Oryx
date: 2014-03-01
categories:
  - hadoop
  - machine-learning
  - cloudera
  - lambda-architecture
  - recommendation-systems
description: GigaOm's coverage of Cloudera launching Oryx — an open-source ML-on-Hadoop framework using the Lambda Architecture for batch retraining plus real-time serving. An early attempt to make production machine learning first-class on Hadoop.
params:
  source: pinboard
  sourceUrl: http://gigaom.com/2014/02/28/cloudera-is-rebuilding-machine-learning-for-hadoop-with-oryx/
---

## Summary

Cloudera launched Oryx as an open-source framework for large-scale, real-time machine learning on Hadoop. The design follows the Lambda Architecture pattern (coined by Nathan Marz): a batch layer periodically retrains models on all historical data stored in HDFS, while a speed layer serves the current model and handles real-time updates. The framework was built primarily around collaborative filtering for recommendation systems — predicting what content users would engage with based on historical behavior.

Oryx was an unusual move for Cloudera: a commercial company releasing infrastructure code as open source to drive Hadoop adoption. The reasoning was that if ML practitioners could use Hadoop as a first-class ML platform, they'd need Cloudera's commercial distribution, support, and tooling. The bet was that the complexity of deploying Hadoop meant most companies would pay for a managed distribution even if the ML algorithms were free.

The Alternating Least Squares (ALS) algorithm was Oryx's primary offering — the standard approach for matrix factorization in collaborative filtering, which scales well to distributed computation. Apache Spark's MLlib later adopted ALS as its core recommendation algorithm, making Oryx somewhat redundant. But in early 2014, Oryx represented the state of the art for production ML on Hadoop.

## Key points

- Oryx: Cloudera's open-source ML-on-Hadoop framework — Lambda Architecture (batch + speed layers) for production recommendation systems.
- Primary algorithm: Alternating Least Squares (ALS) for collaborative filtering — factorizes user-item interaction matrices at Hadoop scale.
- Lambda Architecture: Nathan Marz's pattern of batch layer (accuracy) + speed layer (recency) — later criticized for complexity and largely replaced by streaming architectures.
- Cloudera strategy: open-source tools to drive Hadoop adoption, commercial distribution for enterprise deployment.
- Historical: Apache Spark MLlib absorbed the same ALS algorithm, reducing Oryx's distinctiveness by 2015-2016.

[Original](http://gigaom.com/2014/02/28/cloudera-is-rebuilding-machine-learning-for-hadoop-with-oryx/)
