---
title: Kickstarter SQL Style Guide
date: 2020-09-03
categories:
  - sql
  - style-guide
  - data-engineering
  - best-practices
  - code-quality
description: Kickstarter's SQL style guide — conventions for formatting, naming, CTEs, joins, and documentation that prioritize reproducibility and shareability across a data team. A practical reference for writing SQL others can read and maintain.
params:
  source: pinboard
  sourceUrl: https://gist.github.com/fredbenenson/7bb92718e19138c20591
---

## Summary

Kickstarter's SQL style guide (authored by Fred Benenson, originally a GitHub Gist) codifies formatting and structural conventions for writing readable, maintainable SQL in a team environment. The primary goals are reproducibility and transparency — queries that can be understood, debugged, and modified by someone other than the original author.

The guide targets AWS Redshift/PostgreSQL but applies broadly across SQL dialects. Key principles: always capitalize SQL keywords, use 2-space indentation, prefer explicit over implicit (always use `AS` for aliases, always use `INNER JOIN` not `JOIN`), and use Common Table Expressions (CTEs) heavily rather than nested subqueries.

The structural rules have a strong opinion about query readability: each SELECT column on its own line, each WHERE condition on its own line beginning with the operator, and JOINs listed with INNER JOINs first followed by LEFT JOINs. The CTE emphasis is particularly strong — the guide recommends joining CTEs within subsequent CTEs rather than in the main query body, which keeps the final SELECT clean.

## Key points

- **CTEs over subqueries**: Common Table Expressions are preferred for anything non-trivial because they're named, reusable, and self-documenting — `WITH clean_orders AS (...)` is easier to follow than a nested `SELECT`.
- **Explicit `AS`**: always alias columns you've computed or renamed — `SUM(amount) AS total_amount` not `SUM(amount)`. Names communicate intent.
- **No implicit JOINs**: `FROM a, b WHERE a.id = b.a_id` is an anti-pattern — use explicit `INNER JOIN`.
- **Underscore_naming**: `user_id` not `userId` — SQL identifiers are case-insensitive in most engines, so underscore convention is safer.
- Comments should explain non-obvious logic — not what the code does (the query is readable) but why (what edge case or business rule this handles).

[Original](https://gist.github.com/fredbenenson/7bb92718e19138c20591)
