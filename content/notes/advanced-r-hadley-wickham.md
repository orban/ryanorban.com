---
title: Advanced R — Hadley Wickham
date: 2014-02-12
categories:
  - r
  - programming
  - functional-programming
  - performance
  - reference
description: Hadley Wickham's Advanced R — the definitive guide to R's unusual object systems, functional programming patterns, environments, and performance profiling. Essential reading for anyone who wants to move from R user to R programmer.
params:
  source: pinboard
  sourceUrl: http://adv-r.had.co.nz/
---

## Summary

Hadley Wickham wrote Advanced R to cover the parts of the language that the standard R documentation under-explains: the three object-oriented systems (S3, S4, and R5/Reference Classes), R's functional programming features, the environment model, non-standard evaluation (which underlies the tidyverse's expressive syntax), and performance profiling and optimization.

R is unusual among programming languages in having multiple incompatible object-orientation systems. S3 is informal and flexible — methods are generic functions dispatched based on class attribute. S4 is formal with explicit class definitions and multiple dispatch. R5 (Reference Classes) gives mutable, Java-style objects. Knowing when each is appropriate, and why the tidyverse mostly uses S3, is essential for writing packages others can depend on.

The book's functional programming section covers R's first-class functions, closures, apply family, and the idea that R is fundamentally a functional language that also supports imperative code. Hadley Wickham himself applies this in ggplot2 (grammar of graphics, a declarative layering system) and dplyr (pipeline-based data manipulation using `%>%` pipes). The non-standard evaluation chapter explains how `dplyr` can capture unevaluated expressions from the user and evaluate them in a different context — the magic behind `select(df, column_name)` without quotes.

## Key points

- R's three OO systems: S3 (informal, method dispatch via generic functions), S4 (formal, multiple dispatch), R5/Reference Classes (mutable, Python-style).
- Non-standard evaluation (NSE): R can capture unevaluated expressions — the mechanism behind `dplyr`'s and `ggplot2`'s clean APIs.
- R environments: every function call creates an environment; closures capture the environment where they were defined — the source of R's scoping rules.
- Performance profiling: Rprof, `microbenchmark`, understanding vectorization, and when to call C via Rcpp.
- Hadley Wickham also wrote ggplot2, dplyr, tidyr, devtools — Advanced R is the foundation for understanding how those packages work internally.

[Original](http://adv-r.had.co.nz/)
