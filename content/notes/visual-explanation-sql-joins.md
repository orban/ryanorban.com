---
title: A Visual Explanation of SQL Joins
date: 2013-05-27
categories:
  - sql
  - databases
  - education
  - data-engineering
description: Jeff Atwood's Coding Horror post using Venn diagrams to explain SQL JOIN types visually. One of the most-referenced SQL explanations on the web — the mental model that finally makes INNER, LEFT, RIGHT, and FULL OUTER joins click.
params:
  source: pinboard
  sourceUrl: http://www.codinghorror.com/blog/2007/10/a-visual-explanation-of-sql-joins.html
---

## Summary

Jeff Atwood's Coding Horror post uses Venn diagrams to explain the seven fundamental SQL JOIN types — the closest thing to a canonical visual reference for this topic. The post was written in 2007 and has been linked so frequently it's effectively the canonical explanation for developers learning SQL data modeling.

The key insight the diagrams convey: a JOIN is a set operation on the rows of two tables, where the overlapping region corresponds to rows that satisfy the join condition. `INNER JOIN` returns the intersection; `LEFT OUTER JOIN` returns all rows from the left table plus matching rows from the right (with NULLs for no match); `FULL OUTER JOIN` returns the union. Once you see it as set algebra, the behavior becomes predictable rather than memorized.

This Venn diagram framing maps cleanly to the Unix set operations tradition — `comm` does exactly what `INNER JOIN` does for sorted text files. The underlying abstraction is relational set theory, whether you're in PostgreSQL or a shell pipeline.

## Key points

- `INNER JOIN` = intersection (only rows matching in both tables)
- `LEFT OUTER JOIN` = all rows from A, with B columns NULL where no match
- `RIGHT OUTER JOIN` = all rows from B, with A columns NULL where no match
- `FULL OUTER JOIN` = union (all rows from both, NULLs where no match on either side)
- `CROSS JOIN` = Cartesian product (all combinations, rarely what you want)
- Exclusive LEFT JOIN (`WHERE b.key IS NULL`) finds rows in A not present in B — the difference operation
- The mental model: two circles (tables), the overlap is rows matching the join predicate

[Original](http://www.codinghorror.com/blog/2007/10/a-visual-explanation-of-sql-joins.html)
