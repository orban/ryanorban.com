---
title: SADDLE — Scala Data Library
date: 2013-04-02
categories:
  - scala
  - data-analysis
  - jvm
  - dataframes
  - finance
description: SADDLE is a Scala data manipulation library modeled after pandas and R's data.frame — bringing labeled, indexed data structures to the JVM. Aimed at quantitative analysts who wanted Python/R-style data manipulation within Scala's type system.
params:
  source: pinboard
  sourceUrl: http://saddle.github.com/
---

## Summary

SADDLE (Scala Data Library) was an attempt to bring pandas-style labeled data manipulation to the JVM ecosystem via Scala. In 2013, Python's pandas (released 2008, v0.10 in late 2012) had established the DataFrame as the dominant abstraction for tabular data manipulation in the data science community. R's `data.frame` predated pandas but had similar semantics. SADDLE asked: can we give Scala/JVM-based quantitative analysts the same ergonomic data manipulation tools without leaving the JVM?

The core data structures: `Series[X, Y]` (indexed 1D vector, like pandas Series) and `Frame[RX, CX, T]` (indexed 2D labeled table, like pandas DataFrame). Both used Scala's type system to make index and value types statically typed — a pandas DataFrame carries Python objects throughout, losing type safety; a SADDLE Frame knows at compile time what types its row index, column index, and values contain. This was the JVM advantage: catch type errors at compile time rather than runtime.

The target audience was quantitative finance practitioners who used Scala (common in high-frequency trading and risk systems, where JVM performance and Akka/Spark ecosystem integration mattered) and wanted to do exploratory data analysis without dropping to Python. SADDLE didn't achieve mass adoption — Apache Spark's DataFrame API (2015) and later Breeze for numerical computing became the JVM data science answers — but it was an interesting early attempt to port the pandas model to a statically typed functional language.

## Key points

- DataFrame-style data manipulation in Scala: labeled 1D Series and 2D Frame with typed indices — the pandas model on the JVM.
- Static typing advantage: index and value types known at compile time vs. pandas' dynamic Python typing — catches errors earlier.
- Target audience: quant finance practitioners in the JVM ecosystem who wanted exploratory data tools without switching to Python.
- Scala ecosystem: positioned alongside Breeze (numerical computing) and later Spark DataFrames as JVM-native data tools.
- Not widely adopted: Apache Spark's 2015 DataFrame API became the dominant JVM answer to the pandas problem, largely by solving the distributed use case.

[Original](http://saddle.github.com/) → GitHub
