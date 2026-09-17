---
title: "Neon: Serverless Branchable Postgres"
date: 2022-05-29
categories:
  - postgres
  - serverless
  - database
  - developer-tools
  - cloud
description: Neon is serverless, fault-tolerant, branchable Postgres — separating storage from compute so you can scale to zero, branch databases like git branches, and get instant provisioning. Positions itself as the Postgres for the serverless/edge computing era.
params:
  source: pinboard
  sourceUrl: https://neon.tech/
---

## Summary

Neon is a PostgreSQL-compatible cloud database that rearchitects Postgres for the serverless era. The two headline features are scale-to-zero (the database pauses when idle and resumes in milliseconds) and database branching (create instant copy-on-write branches of a database, like git branches for your data). These capabilities emerged from separating Postgres storage from compute — storage lives in a distributed object store (S3-backed), and the compute layer can be spun up and down independently.

Database branching is the most novel feature. Traditional Postgres required copying an entire database (slow, expensive) to get an isolated environment for a feature branch. Neon's copy-on-write storage means branching is instant and space-efficient — the branch only stores what's changed from the parent. This integrates naturally with CI/CD pipelines: each pull request gets its own isolated database branch with the same production data, enabling realistic integration testing without shared state between branches.

Scale-to-zero addresses the major economics problem of serverless applications: you're already paying per-invocation for compute (AWS Lambda, Vercel Functions) but still paying 24/7 for a database server. Neon closes that gap. The cold-start latency (database resuming from zero) is measured in hundreds of milliseconds — acceptable for development environments, borderline for production depending on the use case.

## Key points

- Neon = serverless PostgreSQL: storage (S3-backed) separated from compute — enables scale-to-zero and instant branching
- Database branching: copy-on-write instant branches for feature development, CI/CD isolation, and testing with real data
- Scale-to-zero economics: stops the database billing clock when idle — closes the gap with serverless compute costs
- PostgreSQL-compatible: runs existing Postgres drivers, ORMs (Prisma, Drizzle, SQLAlchemy) without code changes
- Cold-start latency is the constraint: ~500ms resume time limits suitability for latency-sensitive production workloads
- Competes with PlanetScale (MySQL-based branching), Supabase (full-stack Postgres), Railway, Fly Postgres

[Original](https://neon.tech/)
