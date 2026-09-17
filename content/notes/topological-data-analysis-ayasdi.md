---
title: Topological Data Analysis from Ayasdi
date: 2013-12-04
categories:
  - topological-data-analysis
  - ayasdi
  - genomics
  - data-science
  - visualization
description: Tweet from DataBeat 2013 noting Ayasdi's topological data analysis platform for sequential/genomic data. TDA was an emerging approach to finding structure in high-dimensional data without requiring dimensionality reduction assumptions.
params:
  source: pinboard
  sourceUrl: https://twitter.com/ryanorban/status/408328723843149824/photo/1
---

## Summary

Ayasdi was a Stanford spinout (founded by Gunnar Carlsson, Gurjeet Singh, and Harlan Sexton) that commercialized [topological data analysis](/notes/topological-data-analysis/) (TDA) — specifically the Mapper algorithm, which Carlsson and Singh had developed to extract shape and structure from high-dimensional datasets without requiring a fixed number of clusters or a distance metric.

The tweet from DataBeat 2013 notes Ayasdi's application to sequential and genomic data. TDA's key property is that it can find structure in data that resists traditional clustering or dimensionality reduction: loop structures, branches, flares. The Mapper algorithm projects data through a filter function, clusters within overlapping bins, and builds a simplicial complex that captures the topology of the dataset's shape.

Genomics was a natural application: gene expression data is high-dimensional, noisy, and often has non-euclidean structure. Finding topological features (continuous groups of patients with similar gene expression, branching trajectories in cell differentiation) required techniques that could capture the data's geometry without assuming it clusters into k blobs.

## Key points

- Ayasdi commercialized [topological data analysis](/notes/topological-data-analysis/) — specifically Gunnar Carlsson's Mapper algorithm from Stanford.
- Mapper algorithm: projects data → clusters in overlapping bins → builds a graph capturing the dataset's topological shape.
- Handles structure that standard clustering misses: loops, branches, flares in high-dimensional data.
- Application to genomics: gene expression data has topological structure (branching cell differentiation, patient subtypes) not well-captured by k-means.
- TDA is coordinate-free and invariant to certain deformations — more robust than Euclidean distance methods.
- Ayasdi raised significant funding in 2013 on the strength of genomics and defense applications.

[Original](https://twitter.com/ryanorban/status/408328723843149824/photo/1)
