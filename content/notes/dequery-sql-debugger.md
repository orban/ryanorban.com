---
title: "Dequery: The SQL Debugger"
date: 2025-05-29
categories:
  - sql
  - debugging
  - developer-tools
  - databases
  - data-engineering
description: Dequery is a SQL debugger that traces data lineage step-by-step through CTEs, subqueries, JOINs, and window functions — showing which source rows contributed to each result. Fills the long-standing gap between SQL query execution and traditional debugging.
params:
  source: pinboard
  sourceUrl: https://dequery.io/
---

![Dequery: The SQL Debugger](/images/notes/dequery-sql-debugger.png)

## Summary

Dequery positions itself as "the world's first SQL debugger" — and the gap it fills is real. Unlike most programming languages where you can step through execution and inspect state at each point, SQL has traditionally been opaque: you write a query, run it, get results, and if they're wrong you're left working backwards through CTEs and subqueries trying to figure out where data went wrong.

Dequery adds step-by-step data lineage tracing. For a complex query with CTEs, subqueries, JOINs, GROUP BY, and window functions, you can follow specific rows through the execution, seeing which source rows contributed to each result. This is the equivalent of setting a breakpoint in SQL — instead of getting the final answer and wondering why a particular row is included or excluded, you can trace it back to its origins.

The tool runs locally with no data leaves your machine — important for anyone dealing with sensitive data. It supports PostgreSQL, Snowflake, BigQuery, DuckDB, MS SQL Server, MySQL, and Oracle. The web version is free.

## Key points

- Step-by-step data lineage tracing through complex SQL queries.
- Traces rows through CTEs, subqueries, JOINs, GROUP BY, and window functions.
- Fills the fundamental gap in SQL tooling: you can finally debug a query, not just run it.
- Privacy-preserving: local execution, no data leaves your machine.
- Supports PostgreSQL, Snowflake, BigQuery, DuckDB, MySQL, Oracle, and MS SQL.
- Directly addresses the class of bugs where "why is this row in/out of the result?" is the question.

[Original](https://dequery.io/)
