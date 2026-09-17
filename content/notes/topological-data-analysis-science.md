---
title: The Mathematical Shape of Big Science Data
date: 2013-10-05
categories:
  - topological-data-analysis
  - mathematics
  - data-science
  - topology
  - ayasdi
description: Quanta Magazine on topological data analysis (TDA) and Ayasdi's commercialization of it — using persistent homology to find structure in high-dimensional data where standard clustering fails. One of the more intellectually ambitious 2013 data science articles.
params:
  source: pinboard
  sourceUrl: https://www.simonsfoundation.org/quanta/20131004-the-mathematical-shape-of-things-to-come/
---

## Summary

Quanta Magazine's coverage of [topological data analysis](/notes/topological-data-analysis/) (TDA) explained how mathematicians were applying algebraic topology — specifically persistent homology — to find structure in high-dimensional datasets where conventional clustering and dimensionality reduction techniques fail. The company Ayasdi, founded by Stanford mathematician Gunnar Carlsson, was commercializing these methods.

The core idea of TDA: instead of asking which points cluster together? (which depends heavily on distance metric and cluster count), ask what is the shape of the data? Persistent homology tracks topological features (connected components, loops, voids) across multiple scales, identifying which structural features persist rather than appearing at only one resolution. This persistence is what makes the approach more robust than scale-sensitive methods.

The application domains were compelling: genomics (finding cancer subtypes by the shape of gene expression data), neuroscience (characterizing brain connectivity patterns), finance (detecting market regimes). The mathematical machinery is heavy — simplicial complexes, Betti numbers, persistence diagrams — but the underlying insight is accessible: data has shape, and shape carries information that point-based statistics misses.

## Key points

- [Topological data analysis](/notes/topological-data-analysis/) uses algebraic topology to characterize the "shape" of data — a different lens than distance-based clustering.
- Persistent homology: track which topological features (connected components, loops, voids) persist across multiple scales — robust to scale sensitivity.
- Ayasdi, founded by Gunnar Carlsson (Stanford), commercialized TDA for enterprise applications in genomics, finance, and healthcare.
- Connected to dimensionality reduction: TDA methods like Mapper produce graph-based representations of high-dimensional data structure.
- The replication crisis context: TDA's topological invariants are more robust to small parameter changes than clustering methods, potentially more reproducible.

[Original](https://www.simonsfoundation.org/quanta/20131004-the-mathematical-shape-of-things-to-come/)
