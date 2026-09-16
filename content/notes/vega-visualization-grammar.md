---
title: Vega — A Visualization Grammar
date: 2013-04-02
categories:
  - data-visualization
  - javascript
  - d3
  - grammar-of-graphics
  - open-source
description: Vega is a declarative visualization grammar built on D3.js by Trifacta (Jeffrey Heer's group) — JSON specifications describe charts rather than imperative D3 code, making visualizations more composable and shareable. The foundation for what later became Vega-Lite and Altair.
params:
  source: pinboard
  sourceUrl: http://trifacta.github.com/vega/
---

## Summary

Vega was a declarative visualization grammar built on top of D3.js, released by Trifacta (the company commercializing Jeffrey Heer's academic work on data visualization). Where D3 required writing imperative JavaScript — specifying every DOM manipulation, transition, and scale computation — Vega let you describe a visualization as a JSON specification: what data, what marks (bars, lines, points), what scales, what axes. The runtime rendered the spec into SVG or Canvas.

The intellectual lineage was Leland Wilkinson's Grammar of Graphics (1999), which provided the theoretical basis for thinking about visualizations as compositions of data mappings, geometric objects, and aesthetic attributes. Hadley Wickham had implemented this in ggplot2 for R; Vega brought the same declarative approach to the web/JavaScript ecosystem. A Vega spec was also language-agnostic — the JSON could be generated from Python, R, or any other language and rendered by the Vega JavaScript runtime.

The practical impact: Vega specifications were more portable and reproducible than D3 code, and easier to generate programmatically. This design decision — JSON specs rather than code — became the foundation for Vega-Lite (a higher-level grammar, 2016) and Altair (the Python API for Vega-Lite, 2017), which became dominant tools for exploratory data visualization in the Python data science stack.

## Key points

- Declarative visualization: JSON specification describes what to show, not how to draw it — the runtime handles rendering.
- Built on D3.js but higher-level: Vega handles scales, axes, legends, and interactions; D3 handles the actual DOM manipulation.
- Grammar of Graphics lineage: Leland Wilkinson's theory → ggplot2 (R) → Vega (JavaScript web) → Vega-Lite → Altair (Python).
- Jeffrey Heer / Trifacta: Heer's group at Stanford/UW produced foundational work in interactive visualization (also: Prefuse, Protovis, D3, Vega).
- Language-agnostic specs: a visualization defined in Vega JSON can be generated from any language — critical for cross-language data science workflows.
- Foundation for Vega-Lite (2016) and Altair (2017) — which became the dominant Python declarative visualization stack.

[Original](http://trifacta.github.com/vega/) → GitHub
