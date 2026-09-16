---
title: Let's Make a Map
date: 2013-02-11
categories:
  - d3
  - data-visualization
  - maps
  - geospatial
  - topojson
description: Mike Bostock's tutorial on building geographic maps with D3.js and TopoJSON — from raw Natural Earth shapefiles to rendered SVG maps. The canonical reference for browser-based cartography in 2013.
params:
  source: pinboard
  sourceUrl: http://bost.ocks.org/mike/map/
---

![Let's Make a Map](/images/notes/lets-make-a-map-d3.png)

## Summary

Mike Bostock (creator of D3.js) published this tutorial as the definitive reference for creating geographic maps in the browser using D3.js and TopoJSON. It walked through the full pipeline: obtaining geographic data from Natural Earth (a curated open dataset of country boundaries and populated places), converting shapefiles to web-friendly formats using GDAL/OGR, generating TopoJSON with the `topojson` command-line tool (which Bostock also created), and rendering to SVG with D3.

The technical innovation TopoJSON introduced over plain GeoJSON: topology-aware encoding that eliminates shared boundaries between adjacent regions (so country borders aren't stored twice) and simplifies geometry while preserving topological correctness. A TopoJSON file of world countries was typically 10x smaller than the equivalent GeoJSON, making it practical for browser download.

The tutorial used the UK as its example — showing labelled countries and populated places. The D3 projection system let you choose from dozens of map projections (Mercator, Albers, Robinson, etc.) and configure center, rotation, and scale. Combined with standard D3 data binding, geographic maps became as composable as any other D3 visualization.

## Key points

- TopoJSON vs GeoJSON: topology encoding eliminates duplicate shared borders, achieving ~10x file size reduction — critical for web delivery
- Natural Earth is the canonical free geographic dataset: country boundaries, coastlines, rivers, populated places — curated, simplified, ready for web use
- GDAL/OGR for shapefile-to-GeoJSON conversion: the command-line geospatial toolkit that handles coordinate system transformations and feature filtering
- D3.js projection system: declarative configuration of map projection, centering, rotation, and scale — dozens of built-in projections
- This tutorial established the standard D3.js mapping workflow still used today, though Mapbox GL JS and deck.gl have since added WebGL-based alternatives for large datasets

[Original](http://bost.ocks.org/mike/map/)
