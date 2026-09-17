---
title: Intro to pandas Data Structures
date: 2013-10-27
categories:
  - pandas
  - python
  - data-science
  - tutorial
  - data-analysis
description: Greg Reda's introduction to pandas data structures — Series, DataFrame, and Index — written in 2013 when pandas was still new enough to need a clear on-ramp. A canonical early tutorial that helped many data scientists learn the library.
params:
  source: pinboard
  sourceUrl: http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
---

## Summary

Greg Reda's tutorial series on pandas was one of the go-to references for learning the library in 2013. This first part covers the three core data structures: Series (a one-dimensional labeled array), DataFrame (a two-dimensional labeled table), and Index (the shared labeling system). Understanding how pandas uses labeled indices as a first-class concept — rather than integer row numbers — is the key insight that makes the library's operations make sense.

The tutorial was written at a moment when pandas had matured enough to be clearly the Python data analysis tool of choice, but documentation was still sparse and fragmented. Wes McKinney had released Python for Data Analysis in 2012, but blog posts like Reda's filled an important gap: working examples that showed how real data analysts used the library rather than abstract API documentation.

The critical concept Reda explains well: pandas operations align on Index labels, not position. When you add two Series, pandas matches them by label. When you filter a DataFrame, the result retains original labels. This label-alignment behavior is what makes pandas powerful for messy real-world data but also the source of the most common bugs when new users expect positional behavior.

## Key points

- Series: 1D labeled array; DataFrame: 2D labeled table — the two structures that cover 95% of pandas use.
- Index labels as first-class objects: operations align on labels, not integer positions — the key mental model shift from NumPy arrays.
- Written in 2013 when pandas tutorials were scarce; became widely circulated as a canonical on-ramp.
- Greg Reda's three-part series covers structures, indexing, and groupby — the three core pandas patterns.
- Context: Wes McKinney created pandas while at AQR Capital to handle time-series financial data, and the design shows.

[Original](http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/)
