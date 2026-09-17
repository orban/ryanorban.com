---
title: A Pandas Cookbook — Julia Evans
date: 2013-12-30
categories:
  - python
  - pandas
  - data-science
  - tutorial
  - data-manipulation
description: Julia Evans's hands-on pandas cookbook — eight chapters of real-dataset exercises covering groupby, merging, text ops, and timestamp handling. The go-to resource that made pandas approachable before the official docs caught up.
params:
  source: pinboard
  sourceUrl: http://jvns.ca/blog/2013/12/22/cooking-with-pandas/
---

## Summary

Julia Evans published this pandas cookbook as a practical antidote to the library's intimidating documentation. Instead of abstract explanations, she compiled a GitHub repository of eight interactive notebooks built around real datasets: NYC noise complaints, Canadian weather records, and bikeshare usage data. The philosophy is explicit — "take a real dataset or three, play around with it, and learn how to use pandas along the way."

The cookbook covers the full data manipulation lifecycle in Python: reading CSVs, filtering and selecting rows, using `groupby` to aggregate (e.g., bike usage by weekday), merging and joining dataframes, string operations for messy text, cleaning inconsistent data, and parsing Unix timestamps. Each chapter is self-contained and reproducible, which was unusual for data science tutorials at the time.

This kind of example-first pedagogy was influential in 2013 — it prefigures the show don't tell style that would later define Jupyter notebook-based education. Evans went on to produce many more such technical resources (zines, etc.) using the same accessible voice.

## Key points

- Eight chapters, each built around a real pandas dataset — NYC complaints, bikeshare, Canadian weather.
- Covers the core manipulation verbs: filter, groupby, merge, string ops, timestamp parsing — the daily toolkit of any data scientist.
- Example-driven approach rather than API documentation; the target reader is someone who knows Python but is new to pandas.
- Published as interactive notebooks on GitHub — one of the early examples of sharing data analysis as reproducible, runnable code.
- Julia Evans is known for clarity and approachability; this was a landmark early resource in the Python data science ecosystem.

[Original](http://jvns.ca/blog/2013/12/22/cooking-with-pandas/)
