---
title: Ad Hoc Data Analysis From the Unix Command Line
date: 2013-07-15
categories:
  - unix
  - command-line
  - data-analysis
  - tools
  - shell
description: Wikibooks guide to ad hoc data analysis using Unix command-line tools — awk, sed, sort, uniq, cut, and friends. A practical reference for doing quick data exploration without loading a language or framework.
params:
  source: pinboard
  sourceUrl: https://en.wikibooks.org/wiki/Ad_Hoc_Data_Analysis_From_The_Unix_Command_Line
---

![Ad Hoc Data Analysis From the Unix Command Line](/images/notes/ad-hoc-data-analysis-unix-command-line.png)

## Summary

This Wikibooks guide covers Unix command-line tools as a data analysis environment — specifically the classic pipeline tools: `awk`, `sed`, `sort`, `uniq`, `cut`, `paste`, `join`, and `wc`. The premise is that for many common data exploration tasks — counting occurrences, extracting columns, computing basic statistics, filtering rows — these tools are faster to reach for than loading Python or R, and compose well via Unix pipes.

The value in 2013 was particularly clear for data science practitioners who spent time on remote servers without a REPL or notebook environment handy. A `sort | uniq -c | sort -rn` pipeline could answer "what are the most common values in this column?" in seconds, from any shell, on any file system. AWK remains one of the most expressive tools for per-row computation with field splitting: it processes columnar text data with a pattern-action model that handles many tasks that would otherwise require a full scripting language.

The Unix philosophy of small tools composing via text streams is the underlying principle. Tools like crush-tools were built in this same tradition — extending the core toolkit for more complex transformations.

## Key points

- `sort | uniq -c | sort -rn`: the canonical frequency count idiom — works on any column of delimited text.
- `awk` for per-row computation: field splitting, arithmetic, and pattern matching without needing Python for simple transformations.
- `cut`, `paste`, `join`: column selection, horizontal concatenation, and relational join on sorted files.
- Unix pipes: composing single-purpose tools into data pipelines that process arbitrarily large files in a single pass — memory efficient via streaming.
- Still relevant: even with pandas and DuckDB, knowing these tools makes remote server work and quick exploratory analysis significantly faster.

[Original](https://en.wikibooks.org/wiki/Ad_Hoc_Data_Analysis_From_The_Unix_Command_Line)
