---
title: "crush-tools: Custom Reporting Utilities for Shell"
date: 2013-07-15
categories:
  - unix
  - command-line
  - data-analysis
  - tools
  - shell
description: crush-tools is a Google-hosted collection of Unix command-line utilities extending the standard toolkit for custom reporting — field manipulation, aggregation, and transformation on tab-delimited files. Purpose-built for the kind of ad hoc data work that awk handles awkwardly.
params:
  source: pinboard
  sourceUrl: https://code.google.com/p/crush-tools/
---

![crush-tools: Custom Reporting Utilities for Shell](/images/notes/crush-tools-shell-reporting.png)

## Summary

crush-tools is a set of Unix command-line utilities hosted on Google Code (circa 2013) for working with tab-delimited text files — the common format that bridged databases and shell pipelines before CSV became universal. The tools extend the standard Unix toolkit with operations that `awk`, `sed`, and `cut` handle clumsily: proper field-by-name selection, multi-key aggregation, date arithmetic on text columns, and pivot-style summaries.

The project reflects a real pain point in data engineering work: the standard Unix tools were designed for general text processing, not specifically for the structured columnar data that analysts deal with daily. Doing a sum-by-group operation in `awk` is possible but requires non-obvious idioms; crush-tools made it a single command. It was part of the same tradition as csvkit (which would emerge later) and the Ad Hoc Data Analysis From The Unix Command Line approach — keep the shell pipeline model but add domain-specific tools for tabular data.

## Key points

- Designed for tab-delimited (and configurable-delimiter) files — the lingua franca of ETL pipelines before Parquet and Arrow formats became common.
- Field-by-name rather than field-by-position: a major ergonomic improvement over `cut -f3` when column order changes.
- Aggregation operations (sum, count, mean by key) as single commands — the kind of thing that requires multiple `awk` passes or a temp file otherwise.
- Part of the "command-line as data analysis environment" tradition alongside csvkit, `mlr` (Miller), and DuckDB's later CLI.

[Original](https://code.google.com/p/crush-tools/)
