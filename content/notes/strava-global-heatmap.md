---
title: Strava Global Heatmap
date: 2014-05-03
categories:
  - data-visualization
  - gps
  - fitness
  - open-data
  - geospatial
description: Strava's global heatmap aggregates GPS tracks from millions of runs and rides to show where athletes move around the world — a stunning geographic visualization that also accidentally revealed military base locations. Privacy implications aside, technically a landmark crowdsourced geospatial visualization.
params:
  source: pinboard
  sourceUrl: http://labs.strava.com/heatmap/#2/-72.60058/23.12465/gray/both
---

## Summary

Strava's global heatmap aggregates millions of GPS tracks from runners and cyclists into a single geographic visualization, showing where athletes move. Dense bright lines trace popular running paths, bike commuter corridors, and cycling routes; dim areas show where fewer people exercise. The result is both a beautiful data visualization and a revealing map of where human physical activity concentrates.

In 2014, this was an early example of a company visualizing the aggregate pattern of its user-generated data at global scale. The heatmap showed something genuinely unexpected: the global distribution of athletic activity, which traces urban form, parks, and cycling infrastructure in striking detail. Popular parks glow; highways are dark; waterfront paths light up everywhere.

The heatmap later became famous for a different reason — in 2017-2018, updates to the heatmap revealed GPS tracks at military bases in remote locations, exposing classified facility locations and patrol routes. This privacy implication (users who had not disabled tracking contributed data to a public map) became a case study in unintended data privacy consequences at scale.

## Key points

- Aggregate GPS visualization: millions of running and cycling tracks rendered as density heatmap.
- Visually traces urban form, park usage, and cycling infrastructure — geographic data art with analytical value.
- Later revealed military base locations and patrol patterns — a landmark data privacy case study (2018).
- Built with WebGL / tile-based rendering for performance at global scale.
- Early example of crowdsourced geospatial data visualization becoming more revealing than intended.

[Original](http://labs.strava.com/heatmap/)
