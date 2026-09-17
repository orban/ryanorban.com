---
title: OpenRefine
date: 2022-04-12
categories:
  - data-cleaning
  - etl
  - data-tools
  - open-source
  - spreadsheet
description: OpenRefine is an open-source desktop tool for cleaning and transforming messy data — originally Google Refine, now community-maintained. Handles clustering, deduplication, format normalization, and reconciliation against external databases like Wikidata.
params:
  source: pinboard
  sourceUrl: https://openrefine.org/
---

## Summary

[OpenRefine](/notes/openrefine/) is an open-source desktop application for working with messy data — cleaning, transforming, and reconciling records that don't conform to a consistent format. Originally built by Metaweb and then acquired and developed as Google Refine, it was open-sourced in 2012 and has been community-maintained since. It occupies a useful middle ground between a spreadsheet and a full ETL pipeline: interactive enough to explore data visually, powerful enough to apply programmatic transformations at scale.

The key capabilities are faceting (group and filter by value patterns), clustering (automatically group values that likely refer to the same thing — New York, "new york", N.Y. → merge), expression-based column transformations via GREL/Jython/Clojure, and reconciliation against external databases like Wikidata or custom REST APIs. Reconciliation is particularly useful for research: if you have a list of company names and want to link them to their Wikidata entries, [OpenRefine](/notes/openrefine/) handles the fuzzy matching and disambiguation interactively.

OpenRefine stores data in-memory and applies transformations non-destructively — every operation is logged and reversible, similar to a undo history. This makes it safe to experiment: you can always roll back to the original. The output can go to CSV, JSON, Excel, RDF, or any format a custom exporter supports. It's widely used in data journalism, digital humanities, library science, and anywhere that real-world data requires careful hand-cleaning before analysis.

## Key points

- Interactive data cleaning: faceting, clustering (fuzzy deduplication), format normalization, and column transformations.
- Reconciliation: link values to external databases (Wikidata, custom APIs) via fuzzy matching — entity resolution at human speed.
- Non-destructive: every operation is logged and reversible; reproducible via exportable JSON operation history.
- Output to CSV, JSON, Excel, RDF — or any custom format via scripting.
- Originally Google Refine (2010–2012); community-maintained open source since the Google handoff.
- Widely used in data journalism, digital humanities, and open data work where bespoke cleaning is required.

[Original](https://openrefine.org/)
