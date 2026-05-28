---
title: "SvelteFlow: Node-Based UI for Svelte"
date: 2023-11-10
categories:
  - svelte
  - frontend
  - ui
  - node-editor
  - open-source
description: SvelteFlow is the Svelte equivalent of React Flow — a customizable component library for building node-based editors and interactive flow diagrams in Svelte applications. Maintained by the same team as React Flow (xyflow).
params:
  source: pinboard
  sourceUrl: https://svelteflow.dev/
---

![SvelteFlow: Node-Based UI for Svelte](/images/notes/svelteflow.png)

## Summary

[SvelteFlow](/notes/svelteflow/) is a Svelte component library for building node-based editors and interactive diagrams — the Svelte equivalent of React Flow. Both are maintained by xyflow (formerly Webkid), which developed React Flow and extended it to the Svelte ecosystem when Svelte's popularity grew enough to justify the port.

Node-based editors are used across a wide range of applications: visual programming tools (like n8n or Flowise), mind mapping, workflow builders, graph visualizers, and LLM pipeline editors. The component handles the hard parts: node rendering with custom content, edge drawing with curves and arrows, zooming, panning, dragging, and the connection logic between nodes.

[SvelteFlow](/notes/svelteflow/)'s API mirrors React Flow's closely, which is deliberate — teams working in both frameworks can transfer knowledge. The Svelte version benefits from Svelte's reactive model: stores handle state naturally and re-rendering is more granular than React's virtual DOM approach, which can matter for large diagrams.

## Key points

- By xyflow — same team as React Flow, consistent API design between the two.
- Handles node rendering, edge drawing, pan/zoom, connection logic out of the box.
- Fully customizable: nodes are Svelte components, edges support custom paths.
- Used for visual programming, workflow builders, and LLM pipeline editors (Flowise pattern).
- MIT-licensed core with a commercial Pro version for advanced features.
- Integrates with SvelteKit and standard Svelte tooling.

[Original](https://svelteflow.dev/)
