---
title: Twitter Visualizes Billions of Tweets in Interactive 3D Maps
date: 2013-06-29
categories:
  - data-visualization
  - twitter
  - geospatial
  - interactive
  - big-data
description: The Verge's coverage of Twitter's interactive 3D tweet visualization showing billions of geotagged tweets rendered as a globe. An early example of browser-based 3D data visualization at social media scale using WebGL.
params:
  source: pinboard
  sourceUrl: http://www.theverge.com/2013/6/28/4475804/twitter-interactive-3d-map-tweet-visualization
---

## Summary

Twitter released an interactive 3D visualization in June 2013 mapping billions of geotagged tweets as a globe, using WebGL to render the data directly in the browser. The visual showed tweet density by geography over time — bright clusters forming around major cities, patterns emerging around events, the asymmetry of internet access visible in the density differences between North America/Europe and the rest of the world.

The technical challenge: billions of data points can't be rendered directly as individual objects. Twitter's visualization used spatial aggregation and level-of-detail rendering — zooming out collapses individual tweets into density representations, zooming in reveals individual geotagged events. The interactive design let users rotate the globe, zoom into regions, and watch temporal patterns play out.

This was part of a broader moment in 2013 when big data visualization was developing as a discipline. D3.js had launched in 2011 and enabled sophisticated browser-based data visualization; WebGL was making 3D rendering in browsers practical; and companies with massive datasets were finding that visual exploration revealed patterns that statistical summaries missed. Twitter, with hundreds of millions of users generating real-time geotagged content, had uniquely compelling raw material.

## Key points

- WebGL for browser-native 3D rendering: no plugin required, runs on consumer hardware — made the interactive globe practical without a native app.
- Spatial aggregation at scale: billions of data points require hierarchical binning (spatial indices, quadtrees) for interactive performance.
- Geospatial inequality visible in the data: tweet density maps showed the uneven global distribution of internet access and smartphone adoption in 2013.
- D3.js ecosystem: this visualization was part of a wave of sophisticated browser-based data visualization enabled by D3 and WebGL becoming available together.
- Real-time dimension: geotagged tweet streams let the visualization animate events unfolding across the globe — sports events, breaking news, concerts.

[Original](http://www.theverge.com/2013/6/28/4475804/twitter-interactive-3d-map-tweet-visualization)
