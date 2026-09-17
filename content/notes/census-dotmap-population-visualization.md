---
title: Census Dotmap
date: 2013-04-17
categories:
  - data-visualization
  - census
  - maps
  - population
  - cartography
description: Brandon Martin-Anderson's Census Dotmap places one dot per person from the 2010 US Census — a 308 million-dot map that makes population density and racial segregation viscerally visible through visual density alone, without choropleth distortion.
params:
  source: pinboard
  sourceUrl: http://bmander.com/dotmap/index.html
---

![Census Dotmap](/images/notes/census-dotmap-population-visualization.png)

## Summary

Brandon Martin-Anderson's Census Dotmap placed one dot per person from the 2010 US Census on a single interactive map — 308 million dots, each colored by the racial/ethnic category of the individual represented. The result is a map that shows the United States as a pattern of human density, where cities appear as bright clusters and rural areas are nearly empty, and where residential segregation is visible as color clustering without any additional annotation.

The technique belongs to the dot density map tradition in cartography, but the scale (one dot per person from a full census) and the interactivity (pan and zoom down to neighborhood level) made it more powerful than traditional dot density maps that use representative dots (one dot = 1000 people). At full resolution, you can see individual blocks in cities like Chicago or Detroit where the color boundary between neighborhoods is sharp enough to trace the historical redlining maps.

The visualization requires no legend explanation: population is density, race is color, segregation is visible as color patterns. This makes it an unusually direct encoding — the data is the visual directly, with no intermediate aggregation step that might obscure individual patterns. The technical challenge was rendering 308 million dots interactively, solved with a pre-rendered tile system similar to standard map tile infrastructure.

## Key points

- Dot density map: one dot per person avoids the choropleth problem where large-area low-density regions visually dominate over small-area high-density ones
- Racial segregation is visible as color clustering without any additional analysis — the data speaks directly through spatial pattern
- Scale-appropriate encoding: at country level it shows urban/rural density; at city level it shows neighborhood segregation; at block level it shows individual buildings
- The technical pipeline: US Census Bureau TIGER/Line shapefiles + block-level demographic data → dot placement with weighted random sampling within each block
- Mapbox and later Deck.gl made this kind of large-scale point rendering accessible; in 2013 it required custom tile-generation infrastructure
- Connected to The Racial Dot Map (University of Virginia, 2013) which had a similar concept but added more interactive annotation

[Original](http://bmander.com/dotmap/index.html)
