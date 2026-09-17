---
title: "Kittydar: JavaScript Cat Face Detection"
date: 2012-09-28
categories:
  - javascript
  - machine-learning
  - computer-vision
  - open-source
  - humor
description: Kittydar is a JavaScript library for cat face detection in images — a real implementation of neural-network-based object detection in the browser, released in 2012 when running ML in JavaScript was novel and this kind of project showed what was becoming possible.
params:
  source: pinboard
  sourceUrl: http://harthur.github.com/kittydar/
---

## Summary

Kittydar by Heather Arthur is a JavaScript library that detects cat faces in images using a neural network trained in the browser. Released in 2012, it was a genuinely novel demo: most machine learning and computer vision work at the time ran in Python, MATLAB, or C++ — putting a working object detector in pure JavaScript, executable in a browser without any server-side compute, was a meaningful technical statement about what was becoming possible on the web platform.

The implementation used a cascade of Haar-like features (the approach from Viola-Jones face detection, published 2001) trained specifically on cat facial features — eyes, nose, and ear geometry that distinguishes feline faces. This was the same algorithm powering camera autofocus face detection in consumer cameras at the time. Adapting it to run in JavaScript required implementing the feature extraction and classification in JS and accepting some performance tradeoff against native implementations.

The project's importance in retrospect is as an early data point in the browser-as-compute-platform story. By 2012, V8 and other JavaScript engines had made JS fast enough that this kind of CPU-intensive work was at least tractable. WebAssembly (which would eventually make near-native compute in browsers practical) was still several years away. Kittydar was a working proof of concept before the infrastructure caught up — the kind of project that shows where a technology is heading by doing something the platform wasn't really designed for yet.

## Key points

- Haar-like features and Viola-Jones-style cascade classifier applied to cat face detection — real computer vision in the browser, not a toy.
- 2012 timing: JavaScript engines were fast enough for this to be tractable, but pre-WebAssembly — impressive for the platform constraints.
- By Heather Arthur — demonstrates browser-as-compute-platform before that framing became mainstream.
- Open-sourced on GitHub, which made it shareable and forkable — fitting for a project about making ML accessible.
- Signals the democratization of computer vision: what required C++ and a research lab in 2005 ran in a browser in 2012.

[Original](http://harthur.github.com/kittydar/)
