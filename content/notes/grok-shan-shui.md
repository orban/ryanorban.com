---
title: Grok {Shan, Shui}* — Understanding Generative Art Code
date: 2021-12-29
categories:
  - generative-art
  - javascript
  - creative-coding
  - programming
  - art
description: Viktor Zverok's deep-dive into understanding the Shan, Shui* generative art codebase — a JavaScript program that generates ink-wash style Chinese landscape paintings. An 'advent of understanding' tracing how algorithmic art is constructed from procedural noise and layered rendering.
params:
  source: pinboard
  sourceUrl: https://zverok.github.io/blog/2021-12-28-grok-shan-shui.html
---

## Summary

Viktor Zverok (zverok) wrote this article as an advent of understanding — a methodical walkthrough of the Shan, Shui* JavaScript generative art program by Lingdong Huang. Shan, Shui* generates ink-wash style Chinese landscape paintings algorithmically: mountains, trees, boats, and rocks rendered with a brush-stroke aesthetic that looks hand-painted but is entirely computational.

The technique builds from Perlin noise or similar smooth random functions as the terrain generator, combined with layered rendering passes that simulate ink opacity, brush width variation, and atmospheric perspective. Mountains are generated as height fields with noise-based silhouettes; trees are procedural L-system or recursive branching structures; the color palette is constrained to the muted earth tones of traditional shan shui (mountain-water) painting.

Zverok's analysis is useful because generative art code is notoriously hard to read — the visual output is immediately beautiful but the code path from math to pixels is opaque. The grok approach traces execution carefully: what does each function do, what does it render, how do components compose. This mirrors the experience of encountering demoscene code or shader programs — small functions that produce complex behavior through mathematical composition.

The article is part of a genre of understanding creative code writing that became prominent as p5.js, three.js, and browser-based creative coding tools lowered barriers to generative art.

## Key points

- Shan, Shui* by Lingdong Huang: JavaScript program generating traditional Chinese ink landscape paintings algorithmically
- Core technique: Perlin noise terrain + recursive tree generation + layered rendering for ink-wash aesthetic
- Zverok's method: trace execution carefully, isolate each function's visual contribution, build a mental model bottom-up
- Connection to creative coding ecosystem: p5.js, Processing, GLSL shaders — math as artistic medium
- Open-source generative art is a genre worth reading: visual feedback makes the code unusually comprehensible

[Original](https://zverok.github.io/blog/2021-12-28-grok-shan-shui.html) → GitHub
