---
title: Visualizing all books in ISBN-space
date: 2025-10-27
categories:
  - data-visualization
  - books
  - isbn
  - webgl
  - creative-coding
description: A GPU-accelerated interactive map of all ~2 billion ISBN numbers, using a custom Bookshelf-Curve algorithm that preserves ISBN decimal structure better than Hilbert curves. Shows publication dates, publishers, and availability across hierarchically-loaded map tiles.
params:
  source: pinboard
  sourceUrl: https://phiresky.github.io/blog/2025/visualizing-all-books-in-isbn-space/
---

![Visualizing all books in ISBN-space](/images/notes/isbn-space-visualization.png)

## Summary

phiresky built an interactive GPU-accelerated visualization mapping all ~2 billion ISBN numbers into a 2D space, displaying book metadata from shadow libraries. The core technical challenge: ISBNs have a hierarchical decimal structure (publisher prefix + title number) that a standard Hilbert curve space-filling algorithm doesn't preserve. The solution is a custom Bookshelf-Curve algorithm that preserves decimal structure, giving the layout a bookshelf-like appearance when zoomed out.

Rendering uses GLSL shaders for performance — painting metadata (publication dates, publishers, availability) across hierarchically-loaded map tiles similar to web map tile systems. The visualization includes smooth flight paths to search results, barcode-style displays, and multiple data layers.

The paradox the post identifies is interesting: ISBNs are a constrained identifier space with limited slots, but that constraint makes them more visualizable than expansive systems like UUIDs. The tight structure gives the data geography. Built entirely with static web technologies (Three.js, React, PNG/JSON tile files) — no backend needed. Sits alongside Every Noise at Once and similar map the whole domain data art projects.

## Key points

- Maps all ~2 billion ISBNs into 2D space with GPU-accelerated GLSL rendering.
- Custom Bookshelf-Curve algorithm preserves ISBN decimal structure better than Hilbert curves.
- Multiple metadata layers: publication dates, publishers, shadow library availability.
- Hierarchical tile loading (like web maps) for interactive navigation at any zoom.
- Static site: Three.js + React + PNG/JSON tiles — no backend.

[Original](https://phiresky.github.io/blog/2025/visualizing-all-books-in-isbn-space/) → GitHub
