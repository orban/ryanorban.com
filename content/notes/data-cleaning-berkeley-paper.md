---
title: "Data Cleaning: Problems and Current Approaches (Berkeley/UNECE)"
date: 2013-09-21
categories:
  - data-cleaning
  - data-quality
  - database
  - berkeley
  - research
description: Joe Hellerstein's Berkeley paper on data cleaning for UNECE — a systematic treatment of the data quality problem from a database research perspective. The academic foundation for what practitioners know as the most time-consuming part of data science work.
params:
  source: pinboard
  sourceUrl: http://db.cs.berkeley.edu/jmh/papers/cleaning-unece.pdf
---

## Summary

This paper by Joe Hellerstein (UC Berkeley database group) for the UNECE (United Nations Economic Commission for Europe) provided a systematic treatment of data cleaning — the process of detecting and correcting errors in datasets. The paper was academic but practical: it catalogued the types of data quality problems (missing values, duplicates, inconsistent formats, rule violations) and reviewed approaches for each.

Data cleaning occupies a strange position in data science: it's universally acknowledged as consuming 60–80% of a data scientist's time, but receives comparatively little research attention or tooling investment compared to the ML algorithms that get applied afterward. Hellerstein's paper was part of the database research community's attempt to treat data quality as a first-class research problem.

The UNECE connection is interesting — national statistics offices deal with exactly this problem at scale: census data, economic indicators, trade statistics all require rigorous cleaning before analysis. The database research framing (constraint-based detection, master data management, entity resolution) is different from the ad-hoc pandas-based approach most data scientists use, but the problems are the same.

## Key points

- Data cleaning taxonomy: missing values, duplicate records, inconsistent representations, constraint violations, entity resolution failures.
- 60–80% of data science time is typically data preparation — the ratio that hasn't changed despite tooling improvements.
- Database research approach: specify data quality rules as constraints, detect violations, apply transformations systematically.
- Entity resolution (record linkage, deduplication) is a hard subproblem: recognizing that J. Smith and "John Smith" at the same address are the same person.
- Joe Hellerstein was a key figure in the database research world; this paper influenced later tools like Trifacta (which he co-founded).

[Original](http://db.cs.berkeley.edu/jmh/papers/cleaning-unece.pdf)
