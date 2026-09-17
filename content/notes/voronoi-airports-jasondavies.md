---
title: Voronoi Diagram of the World's Airports
date: 2014-04-19
categories:
  - data-visualization
  - d3js
  - voronoi
  - cartography
  - javascript
description: Jason Davies' interactive Voronoi diagram of the world's airports — a D3.js visualization showing the nearest-airport region for every point on Earth. Technically elegant and a canonical example of geographic Voronoi tessellation.
params:
  source: pinboard
  sourceUrl: https://www.jasondavies.com/maps/voronoi/airports/
---

## Summary

Jason Davies built this interactive D3.js visualization computing the Voronoi diagram of all the world's airports on a spherical projection. Each region on the map represents the area for which a given airport is the nearest commercial airport. The visual result shows how uneven airport coverage is globally — dense tessellation over Europe and the US, massive polygons over central Africa and ocean regions.

A Voronoi diagram partitions a plane into regions based on proximity to a set of points. For n seed points, each region contains all points closer to that seed than any other. On a map, this has natural interpretations: nearest facility, delivery zone boundaries, coverage areas. Jason Davies implemented this correctly on a sphere (not a flat map projection), which requires spherical Voronoi computation — significantly more complex than the flat-plane version.

Davies was one of the most skilled D3.js practitioners of the 2012-2015 era. His work pushed the boundaries of what D3.js could do with geographic projections, geometric algorithms, and interactive cartography. Many of his visualizations circulated widely on social media because they were both technically impressive and immediately beautiful.

## Key points

- Voronoi diagram on a sphere: each region contains all points for which that airport is nearest.
- Implemented using spherical Voronoi computation — not a flat-plane approximation.
- Built with D3.js — Jason Davies was among the most technically sophisticated D3 practitioners.
- Shows geographic airport coverage inequality starkly: dense in US/Europe, vast gaps elsewhere.
- D3.js geographic projection work by Davies influenced how cartographers approached browser-based maps.

[Original](https://www.jasondavies.com/maps/voronoi/airports/)
