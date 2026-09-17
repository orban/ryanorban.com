---
title: "pydantic-resolve: Hierarchical Data Fetching for Pydantic"
date: 2024-02-26
categories:
  - python
  - pydantic
  - data-fetching
  - graphql
  - n-plus-one
description: pydantic-resolve is a Python library that eliminates N+1 queries through declarative resolve/post methods on Pydantic models. Automatically batches related data fetches and maps results back to parents, with optional GraphQL and MCP service generation.
params:
  source: pinboard
  sourceUrl: https://github.com/allmonday/pydantic-resolve
---

![pydantic-resolve: Hierarchical Data Fetching for Pydantic](/images/notes/pydantic-resolve.png)

## Summary

[pydantic-resolve](/notes/pydantic-resolve/) is a Python library that solves the N+1 query problem declaratively on top of Pydantic models. The core idea: instead of writing explicit nested fetches that issue one query per parent record, you declare what related data a field needs via `resolve_*` methods, and the framework batches all those requests automatically. The results map back to their parent records without manual coordination.

It works through two method types. `resolve_*` methods fetch related data — the library collects all requested IDs across the entire object tree, issues a single batched fetch, then distributes results back. `post_*` methods compute derived fields after child data is loaded, useful for counts, sums, or computed summaries that depend on already-assembled nested data. For larger projects, an ER Diagram centralization mode removes the need to repeat relationship wiring across multiple models.

The GraphQL and MCP generation features are a practical bonus: the same Pydantic model definitions can be used to generate GraphQL schemas or MCP service endpoints, reducing duplication between data-fetching logic and API surface.

## Key points

- Eliminates N+1 queries: `resolve_*` methods auto-batch related data fetches.
- `post_*` methods compute derived fields after nested data is assembled.
- ER Diagram mode centralizes relationship declarations for larger projects.
- Type-safe: native Pydantic models, no separate schema files.
- Can generate GraphQL schemas and MCP services from the same model definitions.
- Framework-agnostic: works with any Python web framework.

[Original](https://github.com/allmonday/pydantic-resolve) → GitHub
