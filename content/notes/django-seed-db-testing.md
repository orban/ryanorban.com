---
title: Improving Django Testing with Seed Databases
date: 2024-02-26
categories:
  - django
  - testing
  - ci-cd
  - postgresql
  - developer-tools
description: A technique for speeding up Django CI test runs by pre-seeding a database with migrations already applied, then restoring it via pg_dump/pg_restore rather than re-running migrations from scratch each time. Significant CI speedup for projects with many migrations.
params:
  source: pinboard
  sourceUrl: https://tla.wtf/posts/django-seed-db/
---

![Improving Django Testing with Seed Databases](/images/notes/django-seed-db-testing.png)

## Summary

This post covers a Django testing optimization: instead of running all migrations from scratch at the start of every CI run, pre-apply them once, dump the result with pg_dump, commit the SQL file to version control, and restore it at CI start with `pg_restore`. Subsequent CI runs skip migration execution entirely — the schema is already in place.

The speedup compounds with project age. Early in a project, migrations run quickly; after years of development with hundreds of migrations, each test run might spend 30+ seconds just on schema setup. The seed database approach collapses that to a single restore operation regardless of migration count.

The key operational detail: the seed database needs to be updated whenever dependencies change in a way that affects schema. The author recommends restoring just before running migrations (not before test collection) to maximize CI caching effectiveness — this means you still run `migrate` each time, but it finds nothing to apply and completes instantly.

## Key points

- Pre-apply Django migrations once, dump with pg_dump, commit SQL file to version control.
- CI restores with `pg_restore` instead of running migrations — No migrations to apply.
- Speedup grows with migration count — significant for mature projects.
- Seed database must be updated when dependencies change schema.
- Restore just before migrations (not before test collection) for optimal CI cache use.
- Works for local development too — faster `test` setup after pulling new code.

[Original](https://tla.wtf/posts/django-seed-db/)
