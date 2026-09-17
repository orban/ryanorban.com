---
title: D2 — Diagram Scripting Language
date: 2022-11-22
categories:
  - diagrams
  - developer-tools
  - visualization
  - open-source
  - dsl
description: D2 is a modern diagram scripting language that compiles text to diagrams — like Graphviz but with a cleaner syntax, built-in layouts, and themes. Treats diagrams as code, enabling version control and programmatic generation.
params:
  source: pinboard
  sourceUrl: https://github.com/terrastruct/d2
---

## Summary

D2 is a diagram scripting language that turns text into diagrams. You write a declarative definition of nodes and edges in a clean syntax, and D2 renders it as an SVG or PNG. The comparison to Graphviz is apt — both are diagram-as-code tools — but D2 has a significantly more modern and readable syntax, plus first-class support for themes, layouts, and interactive features that Graphviz's DOT language lacks.

The core language is simple: `a -> b -> c` draws a directed graph; you can label edges, group nodes into containers, add shapes, and style elements. Multiple layout engines are supported — including ELK for hierarchical layouts and TALA (Terrastruct's proprietary engine) for more sophisticated automatic layout. The web playground at d2lang.com lets you iterate without any tooling setup.

D2 positions itself as the tool for technical diagrams embedded in documentation and codebases. The pitch to developers: your architecture diagrams should live in version control as text files, not as Visio documents or Lucidchart links. Changes can be reviewed in PRs, and diagrams stay in sync with the code because they're edited the same way. It occupies the same niche as Mermaid (which is embedded in GitHub and Notion) and PlantUML, but with a cleaner aesthetic and more sophisticated layout.

## Key points

- Text-to-diagram language: declare nodes and edges in a clean syntax, output SVG or PNG.
- Modern alternative to Graphviz — better syntax, themes, multiple layout engines.
- Multiple layout engine support: ELK, Dagre, and TALA (proprietary, better auto-layout).
- Designed for diagrams-as-code — version-controlled architecture diagrams alongside code.
- Competes with Mermaid, PlantUML, and Graphviz in the technical documentation diagramming space.
- Open source core from Terrastruct with a paid TALA layout engine.

[Original](https://github.com/terrastruct/d2)
