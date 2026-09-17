---
title: "Supabase Vault: Secrets and Encryption in PostgreSQL"
date: 2023-11-07
categories:
  - postgresql
  - security
  - encryption
  - supabase
  - secrets-management
description: Supabase Vault is a PostgreSQL extension for managing secrets and encrypted data inside the database — built on pgsodium and Libsodium, it handles key management and column encryption without application-layer complexity.
params:
  source: pinboard
  sourceUrl: https://supabase.com/blog/supabase-vault
---

![Supabase Vault: Secrets and Encryption in PostgreSQL](/images/notes/supabase-vault.png)

## Summary

[Supabase Vault](/notes/supabase-vault/) is a PostgreSQL extension that adds a secrets management and column encryption layer directly inside the database. It's built on pgsodium (a PostgreSQL wrapper around Libsodium) and solves the key management problem that makes raw pgcrypto column encryption operationally painful.

The core problem with pgcrypto: you have to handle key management yourself. Where do the encryption keys live? How are they rotated? If the keys are stored alongside the encrypted data, the encryption is meaningless. [Supabase Vault](/notes/supabase-vault/) adds a `vault.secrets` table for storing encrypted secrets and a key management layer that separates the key hierarchy from the data — keys stored in a secure enclave (or server environment variable), data encrypted with derived keys.

Practically, you can store API keys, credentials, and sensitive column data in PostgreSQL and retrieve them with SQL functions, with the encryption/decryption handled transparently by the extension. This is close to what HashiCorp Vault does at the infrastructure level, but scoped to database operations and accessible via SQL.

## Key points

- Built on pgsodium and Libsodium — proven cryptographic primitives.
- `vault.secrets` table for encrypted secret storage; retrieved with `vault.decrypted_secrets` view.
- Key management separates master key (env var / secure store) from per-row derived keys.
- Closer to AWS Secrets Manager-style usage than raw pgcrypto column encryption.
- Available as a first-class feature in Supabase projects; installable in self-hosted PostgreSQL.
- Pairs naturally with row-level security for access control over which users can decrypt which secrets.

[Original](https://supabase.com/blog/supabase-vault) → Supabase
