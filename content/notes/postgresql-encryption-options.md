---
title: "PostgreSQL Encryption: The Available Options"
date: 2023-11-08
categories:
  - postgresql
  - security
  - encryption
  - database
  - reference
description: Matt Palmer's comprehensive overview of PostgreSQL encryption options — covers full-disk encryption, TLS in transit, column-level encryption with pgcrypto, and the tradeoffs between each. A clear-headed reference for teams navigating database encryption requirements.
params:
  source: pinboard
  sourceUrl: https://www.hezmatt.org/~mpalmer/blog/2023/11/07/postgresql-encryption-options.html
---

![PostgreSQL Encryption: The Available Options](/images/notes/postgresql-encryption-options.png)

## Summary

Matt Palmer surveys the encryption landscape for PostgreSQL, covering what's available, what each approach actually protects, and where the gaps are. The post is practical and honest — it doesn't oversell what encryption buys you, which is exactly what makes it useful for designing security controls.

The four layers covered: **at-rest encryption** (full disk encryption via LUKS or cloud provider managed keys — protects against physical storage theft, not application-layer access); **in-transit encryption** (TLS between clients and server — straightforward, widely configured); **column-level encryption** via pgcrypto (application encrypts before storing, database sees ciphertext — strong isolation but query complexity, no indexing on encrypted values); and **transparent data encryption** (not natively supported in open-source PostgreSQL — commercial offerings like Postgres Pro add it).

The key insight: most PostgreSQL encryption discussions conflate these layers. Encrypting your disk doesn't protect you from SQL injection; encrypting columns prevents the DB from indexing or querying the data. The right choice depends on your threat model — specifically, who you're protecting against.

## Key points

- Full-disk encryption (LUKS, cloud KMS) protects physical storage, not active database sessions.
- TLS in transit is table stakes — easy to configure, no tradeoffs.
- pgcrypto column encryption: high isolation, but no indexing on encrypted columns and query complexity increases.
- [Supabase Vault](/notes/supabase-vault/) (and similar) adds key management on top of pgcrypto for better operational handling.
- Native TDE (Transparent Data Encryption) not in open-source PostgreSQL — commercial extension only.
- Always define your threat model first: are you protecting against storage theft, DBA access, or application compromise?

[Original](https://www.hezmatt.org/~mpalmer/blog/2023/11/07/postgresql-encryption-options.html)
