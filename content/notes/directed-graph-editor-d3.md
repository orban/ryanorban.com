---
title: Directed Graph Editor in D3
date: 2013-08-18
categories:
  - d3js
  - visualization
  - graphs
  - javascript
  - interactive
description: A D3.js bl.ocks example implementing an interactive directed graph editor with drag-to-create nodes and edges, arrow rendering, and selectable/deletable elements. A canonical reference for anyone building graph editing UIs in D3 before dedicated libraries like Cytoscape.js were widely adopted.
params:
  source: pinboard
  sourceUrl: http://bl.ocks.org/rkirsling/5001347
---

![Directed Graph Editor in D3](/images/notes/directed-graph-editor-d3.png)

## Summary

This bl.ocks.org example by Rob Kirsling implements an interactive directed graph editor using D3.js — a browser-based tool where you can create nodes by double-clicking, draw edges by dragging from node to node, select and delete elements, and see arrow markers rendered on edges to indicate direction. It was a commonly referenced starting point for anyone building graph editing interfaces with D3.

D3.js is particularly well-suited for graph rendering because of its force layout simulation and SVG rendering capabilities. The force layout positions nodes via physics simulation — nodes repel each other, edges attract connected nodes — producing readable graph layouts without manual coordinate assignment. The directed graph editor builds on this with interaction: making the graph not just displayable but editable in the browser.

In 2013, dedicated graph visualization libraries (Cytoscape.js, vis.js) were less mature than they are today. Practitioners who wanted interactive graph UIs either used D3 with custom interaction code or reached for heavier desktop tools. This example served as a practical template: the combination of SVG arrow markers, drag-to-connect interaction, and D3 force simulation in a few hundred lines of JavaScript was useful reference code.

## Key points

- D3.js force layout: physics-based node positioning with configurable spring constants for edge attraction and charge-based node repulsion.
- SVG arrow markers: `<defs>` and `<marker>` elements define reusable arrow shapes referenced by path `stroke` properties — the standard approach for directed edge rendering.
- Drag interaction: D3's drag behavior with custom start/drag/end handlers to distinguish node movement from edge creation.
- bl.ocks.org: the community site for sharing D3 examples that served as the primary learning resource before Observable became dominant.
- Historical context: graph editing UIs were increasingly needed as graph databases (Neo4j), knowledge graphs, and network analysis tools became more common.
- Building block for tools that visualize DAGs, dependency graphs, workflow editors — use cases that expanded significantly as data pipelines and MLOps matured.

[Original](http://bl.ocks.org/rkirsling/5001347)
