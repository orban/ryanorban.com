---
title: Tributary — What We've Learned from a Year of Live Coding
date: 2013-03-17
categories:
  - data-visualization
  - creative-coding
  - d3
  - live-coding
  - tools
description: EJ Fox's retrospective on a year of building Tributary — a live-coding environment for D3.js data visualization. Tributary became an important tool for learning and prototyping D3 through immediate visual feedback.
params:
  source: pinboard
  sourceUrl: http://ejfox.github.com/happybirthdaytributary/
---

## Summary

EJ Fox published this retrospective on Tributary, the live-coding environment he built for D3.js data visualization. Tributary was a browser-based tool where you could write D3 code and see the visualization update in real time — no save-reload cycle, immediate visual feedback. The happy birthday URL suggests this was a one-year anniversary post.

Tributary occupied an important niche: D3.js had a steep learning curve because the connection between code changes and visual output was non-obvious, especially for newcomers from traditional programming backgrounds. Tributary made that connection immediate by running code on every keystroke and rendering the result live. It also enabled easy sharing of experiments via URL, creating a community of D3.js examples that could be forked and modified.

The live coding environment concept has roots in Bret Victor's Inventing on Principle (2012) — a hugely influential talk that argued programmers should have immediate feedback between code and output. Tributary was a direct application of this principle to data visualization. Its successors include Observable (Mike Bostock's reactive notebook platform) which brought the live-feedback model to the mainstream D3.js community after 2017.

## Key points

- Tributary implemented the Bret Victor live-feedback principle for D3.js: code changes update the visualization immediately without reload
- URL-shareable examples created a social layer for the D3.js community — fork, modify, share was more natural than the traditional GitHub/npm workflow
- EJ Fox was a prominent member of the data visualization and data journalism community in 2013, working at MSNBC and later Mother Jones
- Observable (2017+) is the spiritual successor — a reactive notebook that extended the live-coding concept with better state management and a richer sharing ecosystem
- The broader live-coding movement included Light Table (editor), Quartz Composer (visual programming), and later Jupyter notebooks — all sharing the immediate-feedback philosophy

[Original](http://ejfox.github.com/happybirthdaytributary/)
