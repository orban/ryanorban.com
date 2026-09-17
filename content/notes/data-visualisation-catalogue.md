---
title: The Data Visualisation Catalogue
date: 2014-03-07
categories:
  - data-visualization
  - reference
  - charts
  - design
  - tools
description: Severino Ribecca's Data Visualisation Catalogue — a reference library of chart types organized by function, with descriptions of when to use each. The go-to resource for choosing the right chart type for your data and communication goal.
params:
  source: pinboard
  sourceUrl: http://www.datavizcatalogue.com/
---

## Summary

Severino Ribecca's [Data Visualisation Catalogue](/notes/data-visualisation-catalogue/) is a reference library that catalogs chart types by their function and use case. Rather than organizing charts by visual form (which doesn't help you find what you need when starting from a data/communication problem), the catalogue is organized by what you're trying to show: comparison, distribution, relationship, composition, or flow.

The catalogue covers the standard chart types (bar chart, line chart, scatter plot, pie chart) and extends into less-common but useful visualizations: treemaps, Sankey diagrams, chord diagrams, Voronoi diagrams, violin plots, parallel coordinates, sunburst charts, and more. Each entry describes what the chart shows, when to use it, when not to use it, and variations. This makes it a decision tool rather than just a gallery.

In 2014, D3.js was making an expanding set of visualizations practically implementable in the browser, but practitioners still needed guidance on *which* chart to use before they could implement it. Tools like Tableau and R's ggplot2 had chart menus that constrained choices; the catalogue helped practitioners think past the default options. This kind of reference also implicitly argues against chart abuse: pie charts for too many categories, 3D charts that distort perception, dual-axis charts that imply false correlations.

## Key points

- Organized by function (comparison, distribution, flow, relationship) not by visual form — starts from what do I want to show? not what do charts look like?
- Sankey diagrams: flow diagrams showing quantity moving between states — good for energy, budget, or user journey flows.
- Parallel coordinates: multi-dimensional data where each axis represents a variable and each observation is a line — good for high-dimensional comparison.
- Treemaps: hierarchical data as nested rectangles sized by value — effective for part-whole relationships in hierarchies.
- Chart selection is a communication decision: the right chart makes the key relationship in your data obvious; the wrong chart obscures it or misleads.

[Original](http://www.datavizcatalogue.com/)
