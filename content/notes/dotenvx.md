---
title: dotenvx
date: 2024-09-26
categories:
  - developer-tools
  - secrets
  - environment
  - cli
  - open-source
description: dotenvx is an improved dotenv from the original creator — adding encrypted .env files, multi-environment support, and a CLI that works across any language or stack. Lets you commit encrypted .env files to git without a secrets server.
params:
  source: pinboard
  sourceUrl: https://dotenvx.com/
---

![dotenvx](/images/notes/dotenvx.png)

## Summary

[dotenvx](/notes/dotenvx/) is a modernized dotenv replacement built by the original creator of dotenv, Mot. Standard dotenv has been the de facto standard for local environment variable management since 2012, but it has never evolved to handle the gap between local development and production: `.env` files can't be committed, encrypted, or versioned, so teams end up with shared secrets in a Slack channel, a separate secrets manager, or `.env.example` files that are perpetually out of sync with the actual values.

[dotenvx](/notes/dotenvx/) addresses this by adding encryption: you can encrypt your `.env` files and commit the encrypted versions to git, similar to what SOPS does for YAML/JSON secrets. The decryption key stays outside the repository. It also adds multi-environment support (`.env.production`, `.env.staging`, etc.) and a CLI that's language-agnostic — it works by injecting environment variables before any runtime, so it's not tied to Node.js or any specific ecosystem.

The from the creator of dotenv positioning matters because it signals intentional evolution rather than a competing tool. [dotenvx](/notes/dotenvx/) maintains backward compatibility with existing `.env` syntax while adding encryption and better CLI ergonomics on top. For teams that don't want a full secrets manager like HashiCorp Vault or AWS Secrets Manager but need something better than plaintext `.env` files, it fills an important gap.

## Key points

- Encrypted `.env` files committable to git — decryption key stored separately.
- Multi-environment: `.env.production`, `.env.staging`, etc. — explicit environment management.
- Language-agnostic CLI: injects vars before any runtime, not tied to Node.js.
- Backward compatible with standard `.env` syntax; drop-in for existing projects.
- From the original dotenv creator — intentional evolution, not a competing fork.
- Lighter-weight alternative to SOPS for teams that don't need KMS/Vault integration.

[Original](https://dotenvx.com/)
