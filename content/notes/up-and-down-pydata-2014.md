---
title: Up and Down PyData 2014 — Rob Story
date: 2014-05-05
categories:
  - python
  - data-visualization
  - pandas
  - pydata
  - notebooks
description: Rob Story's PyData SV 2014 talk notebook on 'Up and Down' — covering the landscape of Python data visualization tools from low-level (Matplotlib) to high-level (Bokeh, Vincent, Folium). A snapshot of the visualization stack debate of that era.
params:
  source: pinboard
  sourceUrl: http://nbviewer.ipython.org/gist/wrobstory/1eb8cb704a52d18b9ee8/Up%20and%20Down%20PyData%202014.ipynb
---

## Summary

Rob Story's PyData SV 2014 talk Up and Down surveyed the Python data visualization landscape, moving from lower-level tools like Matplotlib up to higher-level abstractions like Vincent (his own library for generating Vega specs from Pandas data), Bokeh, and Folium for geographic maps. The IPython notebook format made the talk interactive — attendees could follow along with executable code.

In 2014, the Python visualization landscape was fragmented. Matplotlib was the standard but produced publication-quality static plots at the cost of verbose configuration. Seaborn was maturing as a statistical visualization layer on Matplotlib. Bokeh was emerging as the interactive alternative (similar to what D3.js did in JavaScript but in Python). Folium wrapped Leaflet.js for Python map generation. Each lived at a different level of the abstraction stack.

Rob Story was a data scientist at an era before ML engineer was a standard job title, and he contributed tools like Vincent and Folium that reflected frustration with the fragmentation. The "Up and Down" framing was about navigating this stack intelligently — knowing when to go low-level for control and when to go high-level for speed.

## Key points

- Survey of 2014 Python visualization stack: Matplotlib → Seaborn → Bokeh → Vincent/Vega → Folium.
- Vincent: Rob Story's library for generating Vega grammar specs from Pandas DataFrames.
- Folium: Python wrapper around Leaflet.js for interactive geographic maps.
- 2014 landscape: fragmented — no single tool covered static + interactive + geographic cleanly.
- PyData SV was the main community venue for this kind of what tools should we use conversation.

[Original](http://nbviewer.ipython.org/gist/wrobstory/1eb8cb704a52d18b9ee8/Up%20and%20Down%20PyData%202014.ipynb)
