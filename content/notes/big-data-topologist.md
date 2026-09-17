---
title: Big Data and the Topologist
date: 2013-03-30
categories:
  - topology
  - machine-learning
  - mathematics
  - tda
  - big-data
description: Low Dimensional Topology blog post on what topologists bring to big data — specifically topological data analysis (TDA) and the Mapper algorithm for finding shape in high-dimensional datasets. An unusual perspective on why geometric intuition matters for data analysis.
params:
  source: pinboard
  sourceUrl: https://ldtopology.wordpress.com/2012/04/11/big-data-and-the-topologist/
---

## Summary

This post from the Low Dimensional Topology blog (a professional mathematics blog) examined what topology has to offer big data analysis — specifically topological data analysis (TDA) as a complement to statistical and machine learning approaches. The bookmark note — "Project, Feature Selection, Extraction, Classification, and Clustering" — suggests it covered the full pipeline of how topological methods apply to standard data science tasks.

The core contribution of topology to data analysis is the Mapper algorithm, developed by Gurjeet Singh, Facundo Mémoli, and Gunnar Carlsson at Stanford. Mapper computes a graph that captures the "shape" of high-dimensional data: it partitions the data by projecting onto some lens function (like the first principal component or a density estimate), applies clustering within each partition, then connects clusters that share data points. The resulting graph (a simplicial complex approximation) reveals global structure — looping paths, branches, flares — that statistics and PCA flatten out.

The practical applications: Carlsson's company Ayasdi (founded 2008) was commercializing TDA for medical data (diabetes subtypes, cancer gene expression), materials science, and financial risk. The topologist's argument was that homology (counting holes, loops, voids in data structure) was a more robust shape descriptor than eigenvalues from PCA — it was invariant to coordinate changes and captured multi-scale structure. The bookmark was prescient: TDA remained a niche but respected methodology and became more practically accessible with libraries like scikit-tda and Giotto-TDA.

## Key points

- Topological data analysis (TDA): studies the shape of data — holes, loops, connected components — rather than summary statistics.
- Mapper algorithm: computes a graph representation of high-dimensional data shape; reveals branching, looping, and cluster structure invisible to PCA or k-means.
- Persistent homology: tracks topological features across scales — features that persist across many scales are likely real; transient ones are likely noise.
- Ayasdi: Gunnar Carlsson's Stanford spinout commercializing TDA; early applications in genomics, clinical data, and financial risk.
- TDA's advantage over PCA/clustering: invariant to coordinate choice, captures multi-scale structure, and doesn't require assuming a distribution.

[Original](https://ldtopology.wordpress.com/2012/04/11/big-data-and-the-topologist/)
