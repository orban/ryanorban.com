---
title: C3.js — D3-Based Reusable Chart Library
date: 2014-05-07
categories:
  - data-visualization
  - javascript
  - d3js
  - charts
  - open-source
description: C3.js is a reusable chart library built on top of D3.js that provides a higher-level API for common chart types. It removes the need to write D3 directly while still exposing D3 objects for customization.
params:
  source: pinboard
  sourceUrl: http://c3js.org/
---

## Summary

C3.js is a chart library built on top of D3.js that abstracts away the hard parts of building charts from scratch. While D3.js is extremely powerful, it has a steep learning curve — you have to manually handle scales, axes, data binding, and transitions. C3.js wraps those patterns into a simple configuration-based API, letting you generate line charts, bar charts, donut charts, and more with a few lines of JavaScript.

The library stays close to D3.js rather than hiding it: C3.js exposes the underlying D3.js selection objects, so if you need custom behavior beyond the built-in chart types you can still drop down to raw D3.js code. This hybrid approach makes it a practical choice for teams that want standard charts quickly but don't want to lose access to D3.js when requirements change.

In the 2014 data visualization ecosystem, C3.js filled a real gap between "write everything in D3.js" and use a black-box BI tool. It was especially popular in data science workflows where Python or R code needed to be paired with interactive browser-based charts.

## Key points

- Built on D3.js — all underlying selection objects remain accessible.
- Declarative configuration API: define chart type, columns, colors, and axes in a single JS object.
- Supports line, bar, scatter, donut, gauge, area, and step charts out of the box.
- Responsive and interactive: built-in tooltips, data hide/show, zoom.
- Common choice for data science dashboards and Jupyter-adjacent web apps in the 2014 era.

[Original](http://c3js.org/)
