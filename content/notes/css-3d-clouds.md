---
title: CSS 3D Clouds
date: 2013-02-12
categories:
  - css
  - 3d
  - creative-coding
  - web-experiments
description: Jaume Sánchez's experiment generating volumetric 3D-like clouds using CSS3 3D Transforms and JavaScript — no WebGL required. A 2013 demonstration of what browser CSS transforms could do beyond 2D layout.
params:
  source: pinboard
  sourceUrl: http://www.clicktorelease.com/code/css3dclouds/
---

## Summary

Jaume Sánchez (clicktorelease) built this experiment to demonstrate that volumetric cloud effects were achievable using CSS3 3D Transforms without WebGL — a notable constraint given that WebGL support was still incomplete across browsers in early 2013. The experiment used JavaScript to position and rotate multiple partially-transparent sprite planes in 3D space, relying on CSS's `transform-style: preserve-3d` to create depth illusion from flat textures.

The technique is essentially billboard-based: each cloud puff is a flat sprite at a different position in 3D space, with transparency and a cloud texture. When viewed from different angles as the user moves the mouse, the parallax between sprites creates a convincing volumetric appearance. Pressing spacebar regenerated new cloud formations; scroll zoomed in/out.

This was part of a wave of browser-based creative experiments that appeared as CSS3 and JavaScript capabilities expanded in 2012-2013. The work drew inspiration from WebGL cloud implementations (Jaume credited Mr.doob's WebGL clouds) but achieved similar aesthetics with the more broadly supported CSS approach. The distinction mattered: CSS 3D worked in Internet Explorer 10+ while WebGL didn't.

## Key points

- CSS3 3D Transforms (`transform-style: preserve-3d`, `translateZ`, `rotateX/Y/Z`) enable genuine 3D positioning of DOM elements — not just perspective illusions
- Billboard technique: flat sprites at varying `translateZ` positions, with parallax from camera movement creating volumetric depth
- Browser compatibility advantage: CSS 3D worked in IE10+ while WebGL required Chrome or Firefox in 2013
- Draws from academic real-time cloud rendering research — simplified cloud-in-a-box impostor techniques adapted for browser sprites
- clicktorelease (Jaume Sánchez) was a leading figure in browser-based creative coding experiments alongside Mr.doob and the Chrome Experiments community

[Original](http://www.clicktorelease.com/code/css3dclouds/)
