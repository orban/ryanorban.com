---
title: "Meshu: Turn Your Places into Beautiful Objects"
date: 2012-05-30
categories:
  - 3d-printing
  - personalization
  - location-data
  - data-visualization
  - maker-culture
description: Meshu turned personal location data from Foursquare and other sources into 3D-printed jewelry using Delaunay triangulation — an early example of mass-customization through algorithmic design and 3D printing.
params:
  source: pinboard
  sourceUrl: http://meshu.io/
---

![Meshu: Turn Your Places into Beautiful Objects](/images/notes/meshu-location-3d-objects.png)

## Summary

Meshu was a startup that took location data — check-ins from Foursquare, places you'd lived or traveled — and converted them into 3D-printed jewelry and objects using Delaunay triangulation. You'd input a set of coordinates (cities you've lived in, places you've traveled), the algorithm would generate a geometric mesh connecting them, and that mesh would be manufactured as a pendant, ring, or print.

The approach combined several things that were converging in 2012: 3D printing was becoming accessible (personal printers via MakerBot, manufacturing services via Shapeways and i.materialise), location data from social networks was rich and personal, and algorithmic design tools (using code to generate geometry rather than manual CAD modeling) were being explored by designers like Nervous System.

Delaunay triangulation is a mathematical technique for connecting a set of points with triangles such that no point falls inside the circumcircle of any triangle — producing a mesh that maximizes the minimum angle and avoids thin, sliver triangles. It's used in computational geometry, finite element analysis, and terrain modeling. Meshu used it aesthetically: the triangulated graph of your places had a distinctive geometric structure that read as both abstract and personally meaningful.

This was an early instance of what would become "mass customization" — products manufactured individually at near-mass scale, differentiated by personal data.

## Key points

- Delaunay triangulation on geographic coordinates (your places) → geometric mesh → 3D-printed jewelry.
- Shapeways and i.materialise provided the manufacturing backend — Meshu was the design/personalization layer.
- Location data from Foursquare as personal material for physical objects — early quantified self aesthetics.
- Algorithmic design: using computation to generate unique geometry rather than manual CAD modeling.
- Pattern: combine accessible 3D printing manufacturing with personal data + algorithmic form → mass-customized physical goods.

[Original](http://meshu.io/)
