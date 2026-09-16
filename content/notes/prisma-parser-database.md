---
title: "Prisma Engines: parser-database Source"
date: 2022-07-16
categories:
  - prisma
  - rust
  - parser
  - database
  - open-source
description: The parser-database module inside Prisma's Rust engine — where Prisma Schema Language (PSL) is parsed and validated into a semantic model. Useful reference for understanding how Prisma's schema compiler works internally.
params:
  source: pinboard
  sourceUrl: https://github.com/prisma/prisma-engines/tree/main/libs/datamodel/parser-database/src
---

## Summary

This is the source directory for the `parser-database` crate inside Prisma's Rust-based engine (`prisma-engines`). The parser-database is the semantic analysis layer between raw Prisma Schema Language (PSL) parsing and the higher-level datamodel representation used by Prisma's query engine and migration engine.

Prisma compiles the `schema.prisma` file you write into an internal representation that drives query generation, migration plans, and type-safe client generation. The parser-database crate is where the raw AST (from the PSL parser) gets resolved into a semantic model: models get their fields typed and validated, relations are analyzed for referential integrity, indexes and constraints are checked, and database-specific validations (e.g. which connectors support which field types) happen.

Browsing this code in 2022 was likely motivated by understanding how Prisma handles schema evolution, building a Prisma-adjacent tool, or contributing to the engine. The `parser-database` layer is particularly interesting for anyone studying schema compiler design or building their own ORM schema language — it shows how a production tool handles the translation from user-facing DSL to internal data model.

## Key points

- Part of `prisma-engines`, the Rust core that powers Prisma's query engine, migration engine, and introspection engine
- `parser-database` sits between raw AST parsing and the semantic datamodel — the validation and resolution stage
- Handles relation analysis (implicit many-to-many, explicit join tables), field type resolution, and connector-specific validation
- Written in Rust; uses a two-phase approach: parse first, then resolve references across the schema
- Good reference for studying schema compiler design in a production ORM context

[Original](https://github.com/prisma/prisma-engines/tree/main/libs/datamodel/parser-database/src) → GitHub
