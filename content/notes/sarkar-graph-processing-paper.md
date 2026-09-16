---
title: Sarkar — Graph Processing Paper (CMU AutonLab)
date: 2013-03-31
categories:
  - graph-algorithms
  - machine-learning
  - research-paper
  - cmu
  - social-networks
description: Prithwish Sarkar's paper from CMU's AutonLab on large-scale graph analysis — bookmarked alongside Apache Giraph as a reference for distributed graph processing. CMU's AutonLab works on scalable machine learning for graph-structured data.
params:
  source: pinboard
  sourceUrl: http://www.autonlab.org/autonweb/19590/version/2/part/5/data/fp56-sarkar.pdf?branch=main&language=en
---

![Sarkar — Graph Processing Paper (CMU AutonLab)](/images/notes/sarkar-graph-processing-paper.png)

## Summary

This paper from CMU's AutonLab (directed by Artur Dubrawski) by Prithwish Sarkar addresses large-scale graph analysis — likely covering graph-based semi-supervised learning, link prediction, or community detection at scale. The bookmark was saved alongside Apache Giraph (a distributed graph processing framework) in the same Twitter exchange, suggesting it was referenced as theoretical grounding for someone evaluating graph-scale distributed computing approaches.

CMU AutonLab focuses on scalable, automated machine learning — building systems that can analyze massive datasets with minimal manual intervention. Graph-structured data (social networks, knowledge graphs, biological interaction networks) is a key domain because graphs encode relationships that tabular data loses. Methods for graph analysis include spectral methods (analyzing graph eigenvalues), random walk-based algorithms (PageRank, SimRank), and message passing (the foundation of Apache Giraph and GraphX).

The fp56 filename prefix suggests this was a conference paper — likely from KDD, ICML, or WWW — where Sarkar presented work on graph-scale learning. Sarkar's research at CMU focused on latent space models for networks (representing nodes as points in a low-dimensional space where proximity reflects connection probability) and nonparametric methods for graph analysis that scale to large networks.

## Key points

- CMU AutonLab: Artur Dubrawski's lab focused on scalable, automated ML — graph analysis is a core domain.
- Prithwish Sarkar: researcher working on latent space models for networks, link prediction, and scalable graph learning.
- Connection to Apache Giraph: bookmarked together as theory + implementation for distributed graph processing.
- Latent space network models: represent nodes as points in geometric space — distance predicts connection probability — a generative alternative to feature engineering.
- Graph ML foundations: the theoretical work from this era (spectral methods, random walks, latent spaces) became the basis for graph neural networks in the deep learning era.

[Original](http://www.autonlab.org/autonweb/19590/version/2/part/5/data/fp56-sarkar.pdf)
