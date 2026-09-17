---
title: Datavisualization.ch Selected Tools
date: 2013-01-15
categories:
  - data-visualization
  - tools
  - reference
  - d3
  - javascript
description: Datavisualization.ch's curated selection of data visualization tools — a 2013 reference for the ecosystem of charting libraries, mapping tools, and visualization frameworks available before the current consolidation. A snapshot of what practitioners were using.
params:
  source: pinboard
  sourceUrl: http://selection.datavisualization.ch/
---

![Datavisualization.ch Selected Tools](/images/notes/datavisualization-ch-selected-tools.png)

## Summary

Datavisualization.ch is a Swiss data visualization consultancy and content site run by Jan Willem Tulp, Severino Ribecca, and others. Their "Selected Tools" page was a curated list of the best libraries, frameworks, and tools for building data visualizations in 2012-2013 — a useful reference at a time when the ecosystem was fragmenting into specialized tools and practitioners needed a map.

The 2013 visualization tool landscape included: D3.js (general-purpose, requires coding), Highcharts and Raphaël (chart libraries), Protovis (D3's predecessor from Jeff Heer's lab, being superseded), Processing.js (web port of Processing), Leaflet and Mapbox (mapping), Crossfilter (fast multidimensional filtering for dashboards), and various specialized tools for network graphs (Gephi) and statistical visualization (R / ggplot2).

The curation was useful because the right tool depended heavily on context: D3.js was powerful but required significant coding knowledge; Highcharts could produce good charts with less effort; Processing was pedagogically accessible but limited for web deployment. Understanding the trade-offs required familiarity with all of them, which is what a curated list like this provided.

## Key points

- D3.js (Mike Bostock, 2011): most powerful and flexible JS visualization library — data-driven DOM manipulation; steep learning curve
- Highcharts: commercial (free for non-commercial use) charting library; excellent out-of-box charts with simpler API than D3
- Crossfilter: library for fast in-browser multidimensional filtering — enables linked brushing and filtering across multiple chart views
- Gephi: open-source network graph visualization tool; the standard for exploratory graph analysis
- The 2013 reference point shows how much consolidation has happened: many of these tools are now deprecated or superseded by Vega/Vega-Lite, Observable Plot, and others

[Original](http://selection.datavisualization.ch/)
