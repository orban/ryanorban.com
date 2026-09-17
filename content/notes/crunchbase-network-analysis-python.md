---
title: Crunchbase Network Analysis with Python
date: 2014-09-15
categories:
  - network-analysis
  - python
  - data-science
  - graph-theory
  - crunchbase
description: A Zipfian Academy alumnus's network analysis of the Crunchbase investment graph in Python — using graph centrality measures to identify influential investors and startups. An early example of applying graph algorithms to startup ecosystem data.
params:
  source: pinboard
  sourceUrl: http://blog.dominoup.com/network-analysis-of-the-crunchbase-graph/
---

## Summary

Casson Stallings, a Zipfian Academy graduate, built a network analysis of the Crunchbase startup-investor graph using Python. This is the kind of applied project that bootcamp graduates produce at the intersection of technical SKILL and domain interest — taking a publicly available dataset and answering questions about its graph structure.

The Crunchbase data models a bipartite graph: startup companies on one side, investors on the other, with edges representing funding relationships. Converting this to a projected graph (startups connected if they share an investor, or investors connected if they've co-invested) enables standard graph algorithms. NetworkX was the primary Python library for this type of analysis in 2014.

The key metrics for this type of analysis: degree centrality (how many connections), betweenness centrality (how often a node sits on the shortest path between others — measures brokerage and bridge roles), PageRank (recursive importance based on neighbors' importance), and clustering coefficient (how densely connected are a node's neighbors). For investor networks, betweenness centrality identifies connectors between different startup clusters; PageRank identifies the most influential investors.

## Key points

- Crunchbase investment graph: bipartite (startups ↔ investors) — project to get investor co-investment network.
- NetworkX: the standard Python library for graph algorithms in 2014 — degree, betweenness, PageRank, clustering.
- Betweenness centrality: measures brokerage role — which investors bridge different parts of the startup ecosystem?
- PageRank: recursive centrality — important investors are connected to other important investors.
- Zipfian Academy alumnus project — demonstrates how bootcamp training enabled applied research on real datasets.
- Connected to the broader 2014 interest in applying data science to startup ecosystem mapping and VC network analysis.

[Original](http://blog.dominoup.com/network-analysis-of-the-crunchbase-graph/)
