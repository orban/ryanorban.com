---
title: Using Data to Show Product Integrations (Interactive)
date: 2015-08-05
categories:
  - data-visualization
  - d3
  - product-analytics
  - galvanize
  - ryan-orban
  - network-graph
description: Ryan Orban's Galvanize blog post introducing an interactive D3 visualization of SaaS product integrations — using network graph structure to show which tools companies use together. An early example of using graph visualization for product market analysis.
params:
  source: pinboard
  sourceUrl: http://www.galvanize.com/blog/2015/08/05/the-first-interactive-visualization-of-product-integrations/
---

## Summary

This Galvanize blog post by Ryan Orban presents an interactive visualization showing the network structure of SaaS product integrations — which tools are commonly used together, and what clusters emerge from co-usage patterns. The visualization treats products as nodes and integrations (or co-usage) as edges, then applies graph layout algorithms to surface the natural clusters.

The methodology likely draws on co-occurrence data: if many companies use both Salesforce and Marketo, they share an edge. The more companies share a tool combination, the stronger the edge weight. Running community detection or force-directed layout on this graph reveals which products cluster together (marketing stacks, engineering stacks, finance tools, etc.) — and which products are hubs that connect disparate clusters.

This is an early example of what would later be called product intelligence or market mapping. The interactive D3.js visualization format was the right choice: static graphs of this complexity are unreadable, but being able to zoom, hover, and filter individual nodes makes the structure explorable. It also reflects the Galvanize ethos of applying data science to tangible business questions, then communicating results visually.

## Key points

- Network graph of SaaS product co-usage: products as nodes, integrations as edges.
- Community detection or force-directed layout reveals natural product stacks (marketing, engineering, etc.).
- D3.js interactive visualization — essential for graph complexity at this scale.
- Anticipates the product intelligence category (Slintel, G2, Bombora) that emerged later.
- By Ryan Orban at Galvanize — an example of applied data science used for market research.
- Methodology pattern: co-occurrence matrix → graph construction → layout → cluster interpretation.

[Original](http://www.galvanize.com/blog/2015/08/05/the-first-interactive-visualization-of-product-integrations/)
