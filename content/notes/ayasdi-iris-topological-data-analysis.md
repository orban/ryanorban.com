---
title: Data-Visualization Firm's New Software Autonomously Finds Abstract Connections
date: 2013-01-21
categories:
  - data-visualization
  - machine-learning
  - topological-data-analysis
  - ayasdi
  - enterprise-software
description: Wired's profile of Ayasdi and its Iris software — a topological data analysis platform that finds abstract structure in high-dimensional data without the analyst specifying what to look for. Raises the question of whether a machine can find connections a human wouldn't have thought to look for.
params:
  source: pinboard
  sourceUrl: http://www.wired.com/design/2013/01/data-viz-ayasdi-iris/
---

## Summary

Ayasdi launched Iris, a [topological data analysis](/notes/topological-data-analysis/) (TDA) platform, in early 2013. The pitch was unusual: instead of building dashboards to visualize data that analysts already understood, Iris used algebraic topology to find structure in high-dimensional datasets automatically — connections and clusters that analysts wouldn't have known to look for. The Wired piece framed this as "autonomously finding abstract connections," which was both accurate and somewhat misleading.

The underlying technique is Mapper, an algorithm developed by Gunnar Carlsson and colleagues at Stanford. Mapper works by projecting high-dimensional data through filter functions, clustering nearby points, and then tracking which clusters overlap across the projection — the result is a network graph (or mapper graph) that captures the topological shape of the data. Features like loops, voids, and branches in that graph correspond to meaningful structure in the original high-dimensional space. It's dimension-independent: works on genetics data, financial data, sensor data, without needing to know which dimensions matter.

Ayasdi was a Stanford spinout; Gunnar Carlsson (mathematics professor, co-developer of Mapper) was a co-founder. The company raised significant venture capital and targeted enterprise applications: fraud detection, drug discovery, military intelligence. The promise was finding the "shape" of data that summary statistics miss.

## Key points

- [Topological data analysis](/notes/topological-data-analysis/) (TDA): studies the "shape" of data using algebraic topology — properties that persist across different scales and representations
- Mapper algorithm: the TDA technique behind Iris — projects data, clusters, tracks overlaps, produces a topological network graph
- Gunnar Carlsson: Stanford mathematician, co-developed Mapper, co-founded Ayasdi; made TDA accessible for applied work
- The key claim: finds structure that hypothesis-driven analysis misses, because it doesn't require the analyst to specify what to look for first
- Ayasdi targeted enterprise: eventually acquired by Prove AI (2019); TDA tools are now also available in open-source form (Gudhi, scikit-tda)

[Original](http://www.wired.com/design/2013/01/data-viz-ayasdi-iris/)
