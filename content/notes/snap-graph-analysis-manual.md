---
title: "SNAP: Stanford Network Analysis Project Manual"
date: 2012-12-06
categories:
  - graph-theory
  - network-analysis
  - c++
  - stanford
  - research
description: The manual for SNAP (Stanford Network Analysis Project) v0.15 — Jure Leskovec's C++ library for large-scale graph analysis and network mining. One of the earliest high-performance graph analysis toolkits, predating Spark GraphX and Neo4j's graph algorithms by years.
params:
  source: pinboard
  sourceUrl: http://snap.cs.berkeley.edu/downloads/snap-0.15-manual.pdf
---

![SNAP: Stanford Network Analysis Project Manual](/images/notes/snap-graph-analysis-manual.png)

## Summary

SNAP (Stanford Network Analysis Project) is a general-purpose graph analysis library written in C++ by Jure Leskovec and colleagues at Stanford University. Version 0.15 in 2012 represented the toolkit in its early research release stage — before it became a standard reference for network science and social network analysis research.

SNAP handles large-scale directed and undirected graphs, multigraphs, and attributed networks. It provides algorithms for community detection, graph centrality metrics, small-world properties, link prediction, and statistical properties of scale-free networks. The C++ implementation makes it fast enough to process graphs with hundreds of millions of nodes and edges on a single machine.

The project also maintains the SNAP dataset collection — a curated set of real-world networks including social networks, collaboration networks, web graphs, and road networks used extensively in network science research. Jure Leskovec became one of the most influential researchers in graph machine learning, and SNAP's dataset collection is still widely used as benchmark data.

## Key points

- SNAP = Stanford Network Analysis Project — C++ library for large-scale graph analysis
- Author Jure Leskovec (Stanford) — later became a leading figure in graph neural network research
- Handles both directed/undirected graphs, multigraphs, attributed networks at scale
- Ships with the SNAP dataset collection — real-world networks used as research benchmarks
- Predates distributed graph tools like Apache Spark GraphX and GraphFrames

[Original](http://snap.cs.berkeley.edu/downloads/snap-0.15-manual.pdf)
