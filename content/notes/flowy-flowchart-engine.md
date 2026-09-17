---
title: "Flowy: The Simple Flowchart Engine"
date: 2020-08-02
categories:
  - javascript
  - ui
  - developer-tools
  - open-source
  - workflow
description: Flowy is a minimal JavaScript library for creating drag-and-drop flowchart UIs in the browser — designed to be embedded in web apps, not as a standalone tool. Lightweight alternative to React Flow or jsPlumb for simple workflow builder features.
params:
  source: pinboard
  sourceUrl: https://alyssax.com/x/flowy
---

## Summary

Flowy is a lightweight JavaScript library for adding drag-and-drop flowchart functionality to web applications. Created by Alyssax, it's designed to be embedded in existing web apps as a workflow builder component — not a standalone tool, but a library you integrate when you need users to visually construct pipelines or decision trees.

The appeal is simplicity: most flowchart libraries (jsPlumb, GoJS, React Flow) are feature-rich and correspondingly complex to integrate. Flowy's API is minimal — initialize it, define node templates, and handle the drop/connect events. The result is a custom workflow builder that feels native to your application rather than an embedded third-party tool.

Use cases: visual pipeline builders in ML tools, no-code automation tools, workflow configuration UIs, and any interface where users need to define sequential steps with branching logic. The pattern is common in tools like Zapier, n8n, Airflow's DAG visualizer, and various BPMN editors — Flowy gives you the primitive UI component for building simpler versions.

## Key points

- Minimal JavaScript flowchart library for embedding drag-and-drop workflow builders in web apps.
- Lightweight compared to React Flow, jsPlumb, or GoJS — less features, easier integration.
- Core functionality: drag node types onto canvas, connect nodes with edges, serialize/deserialize graph.
- By Alyssax — 2020 open-source release that attracted attention for its clean API.
- Relevant when building: no-code automation UIs, pipeline editors, decision tree builders.
- Adjacent tools: React Flow (more full-featured React component), n8n (visual workflow automation using similar UX paradigm).

[Original](https://alyssax.com/x/flowy)
