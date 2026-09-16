---
title: Random Sampling from Very Large Files
date: 2014-03-02
categories:
  - data-engineering
  - python
  - unix
  - sampling
  - big-data
description: Practical techniques for taking random samples from large files without loading them into memory — covering Unix tools (shuf, awk) and reservoir sampling. Essential for working with data too large for pandas to read in one shot.
params:
  source: pinboard
  sourceUrl: http://metadatascience.com/2014/02/27/random-sampling-from-very-large-files/
---

## Summary

A persistent practical problem in data engineering: you have a log file, a CSV, or a dataset that is gigabytes or terabytes — too large to load into Pandas or Python entirely — but you need a random sample for exploratory analysis or model training. This post from Meta Data Science covers the approaches that actually work at that scale.

The Unix-first approach uses tools already on any Linux machine: `shuf -n 1000 large_file.csv` draws a random sample without loading the whole file (shuf uses reservoir sampling internally). For CSV files where the header must be preserved, `head -1 file.csv && tail -n +2 file.csv | shuf -n 1000` handles it. The `awk` approach lets you sample probabilistically with `awk 'BEGIN{srand()}{if(rand()<0.01)print}'` for approximately 1% samples — simpler than reservoir sampling but with variance in the output size.

Reservoir sampling is the algorithmic backbone: given a stream of n items where n is unknown, maintain a reservoir of k items. When item i arrives (i > k), replace a random reservoir item with probability k/i. After processing all n items, the reservoir is a uniform random sample of size k. The algorithm uses O(k) memory regardless of n, making it applicable to arbitrarily large files. Python implementations are straightforward with `random.randrange`.

## Key points

- `shuf -n N file` is the fastest path on Linux for files that fit in the filesystem's address space — one-liner, no code.
- `awk` probabilistic sampling: `awk 'rand()<0.01'` for ~1% of rows — simple but output size varies.
- Reservoir sampling algorithm: O(k) memory, processes each line once, guaranteed uniform distribution over the file.
- For structured data, sample *before* loading into Pandas to avoid hitting memory limits — `pd.read_csv(file, skiprows=lambda i: i>0 and random.random()>0.01)`.
- At truly large scale (HDFS, Apache Spark), `spark.sql("SELECT * FROM table TABLESAMPLE(1 PERCENT)")` is cleaner.

[Original](http://metadatascience.com/2014/02/27/random-sampling-from-very-large-files/)
