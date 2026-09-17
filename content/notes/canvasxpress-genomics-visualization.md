---
title: "CanvasXpress: Scientific Data Visualization"
date: 2013-01-10
categories:
  - bioinformatics
  - visualization
  - genomics
  - javascript
  - tools
description: CanvasXpress — a JavaScript library for scientific and genomics data visualization, specifically designed for bioinformatics use cases like expression heatmaps, scatter plots with gene annotations, and interactive exploration of multi-dimensional biological data.
params:
  source: pinboard
  sourceUrl: http://www.canvasxpress.org/
---

![CanvasXpress: Scientific Data Visualization](/images/notes/canvasxpress-genomics-visualization.png)

## Summary

CanvasXpress is a JavaScript visualization library specifically designed for scientific and bioinformatics data. Unlike general-purpose charting libraries, it includes chart types that are standard in genomics analysis: heatmaps with hierarchical clustering, scatter plots with gene/sample annotation overlays, venn diagrams, and multi-track genome browser-style displays. It was built for the pharmaceutical and academic research context where data has specific structure (samples × features matrices, gene expression values, pathway annotations) and interactivity is required for exploration.

The library was developed by Isaac Neuhaus at Bristol-Myers Squibb's computational biology group — corporate pharmaceutical bioinformatics, which means it was designed for production use in drug discovery pipelines rather than academic toy examples. By 2013 it was a notable option in the scientific visualization space, alongside R/ggplot2 (static, publication quality), D3.js (flexible but requires significant custom work), and Protovis (D3's predecessor).

The bioinformatics visualization problem is specific: data matrices are large (thousands of genes, hundreds of samples), standard charts don't represent the structure well, and scientists need to interact with the data (hover to see gene names, click to filter, select subsets for comparison) in ways that require purpose-built tools.

## Key points

- CanvasXpress use cases: gene expression heatmaps, PCA scatter plots, survival curves, pathway visualizations — chart types standard in bioinformatics but absent from general libraries
- Developed at Bristol-Myers Squibb: pharmaceutical bioinformatics context means production-grade, not academic prototype
- Hierarchical clustering + heatmap: the canonical bioinformatics visualization — rows/columns reordered by similarity, patterns become visible
- Alternative landscape in 2013: R/ggplot2 for publication figures, D3.js for custom web viz, CanvasXpress for interactive web-based scientific exploration
- The library still exists and is actively maintained — unusual longevity for a niche scientific tool

[Original](http://www.canvasxpress.org/)
