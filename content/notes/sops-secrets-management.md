---
title: "SOPS: Secrets OPerationS"
date: 2024-09-26
categories:
  - security
  - secrets
  - devops
  - encryption
  - developer-tools
description: SOPS (Secrets OPerationS) encrypts secret files using cloud KMS or PGP/age keys while keeping key names visible for diffs and version control. It's the standard tool for storing encrypted secrets in git without a centralized secrets server.
params:
  source: pinboard
  sourceUrl: https://github.com/getsops/sops
---

![SOPS: Secrets OPerationS](/images/notes/sops-secrets-management.png)

## Summary

SOPS (Secrets OPerationS) is an encrypted file editor for managing secrets in YAML, JSON, ENV, INI, and binary files. The key design insight is that it encrypts only leaf *values*, not key names — so a secrets file in a git repo remains human-readable and diff-able (you can see *what* changed), while the actual secret values stay encrypted. This makes it dramatically friendlier for version control workflows than approaches that encrypt entire files.

Under the hood, SOPS generates a random 256-bit data key that encrypts file contents with AES256-GCM. That data key is then encrypted with one or more master keys — supporting AWS KMS, GCP KMS, Azure Key Vault, HashiCorp Vault, age, and PGP/GPG. Multiple master keys can encrypt the same file, so different team members with different key access can each decrypt. The workflow: open the file, SOPS decrypts the data key using whichever master key is available, opens cleartext in your editor, re-encrypts on save.

SOPS is now maintained under the CNCF ecosystem as a getsops project after being originally developed at Mozilla. It's one of the most widely-used approaches for storing secrets in git alongside infrastructure code — common in Terraform, Helm, and GitOps workflows where secrets need to live near the code that uses them without being plaintext.

## Key points

- Encrypts values, not keys — files remain diff-able; you can see which secrets changed without seeing their values.
- Supports AWS KMS, GCP KMS, Azure Key Vault, HashiCorp Vault, age, PGP — mix and match.
- Multiple master keys per file: different users with different key access can decrypt the same secrets.
- AES256-GCM encryption with per-file random data keys — industry-standard symmetric encryption.
- Integrates with GitOps, Helm, Terraform, and Kubernetes secret workflows.
- Paired tools in the ecosystem: [dotenvx](/notes/dotenvx/) for dev workflows, External Secrets Operator for Kubernetes.

[Original](https://github.com/getsops/sops) → GitHub
