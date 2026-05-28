---
title: How D3 Selections Work
date: 2013-04-27
categories:
  - d3js
  - data-visualization
  - javascript
  - tutorial
description: Mike Bostock's definitive explanation of D3's selection model — how data joins, enter/update/exit selections, and subselections actually work under the hood. Essential for anyone who wants to go beyond copying D3 examples to understanding why they work.
params:
  source: pinboard
  sourceUrl: http://bost.ocks.org/mike/selection/
---

## Summary

This essay by Mike Bostock (creator of D3.js) is the definitive explanation of D3.js's selection model — the core abstraction that separates D3 from every other charting library. Most D3.js tutorials teach the mechanics (call `.data()`, then `.enter().append()`) without explaining why the model works this way. Bostock wrote this to close that gap.

The insight is that a D3 selection isn't just an array of DOM elements — it's a two-dimensional subclass array where each element retains its position in a group. This positional structure is what makes data joins work correctly when elements are added or removed. When you call `selection.data(array)`, D3 performs a join between existing elements and new data, producing three virtual selections: **enter** (data with no element yet), **update** (elements with matching data), and **exit** (elements with no matching data). The ability to handle these three cases independently is what makes animated transitions possible — enter elements fade in, exit elements fade out, update elements transition between states.

The key function (second argument to `.data()`) controls how elements are matched to data during the join. Without a key, matching is by index — element 0 gets datum 0. With a key (like `d => d.id`), elements are matched by identity across updates. This distinction is critical for transitions: index-based matching causes all elements to move when the data order changes; key-based matching lets each element track its own datum across updates.

## Key points

- D3 selections are grouped arrays — the two-dimensional structure preserves parent-child relationships for subselections
- The **data join** produces three selections: enter (new), update (existing), exit (removed)
- Key functions control how data maps to elements — use them for identity-tracked transitions, omit for positional
- `.enter().append()` creates placeholder elements for data that has no DOM element yet
- Method chaining on selections operates on the current selection — `.select()` and `.selectAll()` create subselections and change context
- This model is why D3 can animate data changes cleanly — each datum is bound to an element, not just rendered once
- Later superseded in common practice by Observable Plot and Vega-Lite for standard charts, but the selection model remains the foundation for custom SVG work

[Original](http://bost.ocks.org/mike/selection/)
