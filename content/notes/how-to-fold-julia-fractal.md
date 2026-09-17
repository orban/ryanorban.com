---
title: How to Fold a Julia Fractal
date: 2013-01-11
categories:
  - mathematics
  - fractals
  - creative-coding
  - visualization
  - complex-numbers
description: Steven Wittens' (acko.net) interactive explainer on Julia sets and complex number iteration — using animated WebGL visualizations to show how complex plane geometry folds into the fractal boundary. One of the best mathematical explanations written for the web.
params:
  source: pinboard
  sourceUrl: http://acko.net/blog/how-to-fold-a-julia-fractal/?second
---

![How to Fold a Julia Fractal](/images/notes/how-to-fold-julia-fractal.png)

## Summary

Steven Wittens (acko.net) wrote this interactive explainer as a way to make complex number geometry viscerally understandable through animation. The core insight is that a Julia set is not a strange mathematical curiosity but the natural boundary that emerges when you ask which points in the complex plane stay bounded under repeated iteration of a simple function — typically `z → z² + c` for some constant `c`. Points that escape to infinity form one region; points that stay bounded form another; the boundary between them is the fractal.

The explainer shows the iteration process as a literal folding: the complex plane being repeatedly mapped onto itself, with the boundary of the Julia set being the curve that neither escapes nor collapses. By animating the iteration with WebGL, Wittens makes the topology of the transformation visible — you watch the plane fold, and you see the fractal emerge as the fixed set of that fold.

The piece was part of a period (2012-2013) when interactive, browser-based mathematical visualization was flourishing. D3.js, Three.js, and WebGL were making it possible to explain mathematics through motion rather than static diagrams. Other notable examples from the same era: Mike Bostock's D3.js examples, Bret Victor's explorable explanations. Wittens' work used MathBox, a library he developed for doing precisely laid-out mathematical animations in WebGL.

## Key points

- Julia set: the set of complex numbers that remain bounded under iterated application of a polynomial — the boundary is the fractal
- The same iteration `z → z² + c` with different `c` values produces completely different fractal shapes — the Mandelbrot set is the map of which `c` values yield connected Julia sets
- MathBox: the WebGL visualization library Wittens built to make precise mathematical animations on the web
- Explorable explanations as a format: this piece is part of the Bret Victor-inspired movement to make math interactive rather than passive
- Mathematical elegance: the fractal boundary emerges from a two-line algorithm; the complexity is not put in, it comes out

[Original](http://acko.net/blog/how-to-fold-a-julia-fractal/?second)
