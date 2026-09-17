---
title: How I Write SQL
date: 2013-05-01
categories:
  - sql
  - style
  - postgresql
  - readability
  - best-practices
description: Craig Kerstiens' SQL style guide — uppercase keywords, meaningful aliases, explicit JOINs, and consistent formatting. A practitioner-written standard that became influential in the PostgreSQL and analytics communities.
params:
  source: pinboard
  sourceUrl: http://www.craigkerstiens.com/2012/11/17/how-i-write-sql/
---

![How I Write SQL](/images/notes/how-i-write-sql-craig-kerstiens.png)

## Summary

Craig Kerstiens (at the time working on Heroku Postgres) wrote this style guide for SQL formatting — a topic that most SQL references ignore entirely, treating SQL as a query language rather than code that humans read and maintain. The guide advocates for a consistent set of conventions that make queries readable at a glance.

Key conventions: **Uppercase reserved words** (`SELECT`, `FROM`, `WHERE`, `JOIN`, `GROUP BY`) — distinguishes SQL keywords from identifiers and column names at a glance. **One clause per line** — putting `FROM`, `WHERE`, `GROUP BY`, `ORDER BY` on separate lines makes the query structure immediately parseable. **Meaningful aliases** — `u` for users table, `o` for orders, with aliases declared explicitly using `AS`. **Explicit `JOIN` type** — always specify `INNER JOIN`, `LEFT JOIN`, etc. rather than relying on the implicit default (`JOIN` alone means `INNER JOIN`, but the explicit form communicates intent). **Column list instead of `*`** in production queries — makes the query's data contract explicit and protects against schema changes breaking downstream consumers.

The underlying principle is treating SQL like any other code: readable, self-documenting, and consistent across a codebase. In analytics teams and data engineering contexts, SQL queries are shared artifacts — multiple people read a query for every one time it's written. Kerstiens was early in articulating this SQL as code perspective before tools like dbt formalized it into full software engineering practices for analytics.

## Key points

- Uppercase SQL keywords for visual parsing — `SELECT` vs `select` makes keyword/identifier distinction visible without color highlighting
- One major clause per line: `SELECT`, `FROM`, `WHERE`, `JOIN`, `GROUP BY`, `HAVING`, `ORDER BY` each start a new line
- Explicit `JOIN` type always specified: `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL OUTER JOIN` — the type communicates the intent
- CTE (Common Table Expressions) over nested subqueries for complex logic — `WITH cte_name AS (...)` is more readable than nesting
- Column aliases with `AS` explicitly — `SUM(amount) AS total_revenue` documents the output schema
- This style predates dbt (2016) but is consistent with what dbt codified as standard analytics SQL — Kerstiens' influence on Postgres and analytics community contributed to that convergence

[Original](http://www.craigkerstiens.com/2012/11/17/how-i-write-sql/)
