---
title: HYDRA — Live Coding Networked Visuals
date: 2022-11-22
categories:
  - creative-coding
  - live-coding
  - visuals
  - synth
  - browser
description: Hydra is a live coding environment for networked visual synthesis in the browser — patches of continuous signal transformations inspired by analog video synthesis. Code runs live in the browser and can be linked to audio or other Hydra instances across the network.
params:
  source: pinboard
  sourceUrl: https://hydra.ojack.xyz/?sketch_id=example_13
---

## Summary

Hydra is a browser-based live coding environment for creating real-time visuals through signal synthesis. The model is inspired by analog video synthesis — you write code that chains together sources (oscillators, cameras, external video) with effects (modulate, blur, colorize, blend) and transformations. Everything is continuous signal flow, not frame-by-frame logic. The result runs live in the browser as you type.

What makes Hydra distinctive is its network awareness — multiple instances can be connected, with one browser piping output into another. This enables collaborative live visual performance: a musician using Hydra at one computer can receive visual input from a performer at another. Olivia Jack (the creator) designed it for algorave and live AV performance contexts where visuals need to respond to music in real time.

The API is intentionally terse and function-chain-based, which makes it good for live performance where you need to type quickly while the visuals are running. It occupies the same space as Processing, p5.js, and [TouchDesigner](/notes/touchdesigner/) but with a bias toward the continuous synthesizer aesthetic over the frame-based drawing aesthetic. The browser deployment means no installation — every example can run immediately from a URL.

## Key points

- Live coding visual synthesizer in the browser — signal-flow model inspired by analog video synthesis.
- Network linking: multiple Hydra instances can exchange video streams for collaborative performance.
- Designed for algorave and live AV performance — terse API optimized for real-time typing.
- Sources (oscillators, cameras) chained through effects and transformations via function composition.
- No installation needed — runs fully in-browser; every sketch is a URL.
- Created by Olivia Jack; part of the live coding and creative coding performance community.

[Original](https://hydra.ojack.xyz/?sketch_id=example_13)
