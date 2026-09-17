---
title: Secrets Management Overview
date: 2024-09-26
categories:
  - security
  - secrets
  - devops
  - reference
  - infrastructure
description: A comparative overview of 10 secrets management tools across on-premises, SaaS, and hybrid deployment models, from open-source options like Ansible Vault and Conjur to commercial platforms like HashiCorp Vault, Doppler, and Akeyless.
params:
  source: pinboard
  sourceUrl: https://hsm.tunnel53.net/article/secrets-management/
---

![Secrets Management Overview](/images/notes/secrets-management-overview.png)

## Summary

This article from Hyper Super Meta provides a comparative overview of secrets management tools, mapping the landscape between cloud-vendor solutions (AWS Secrets Manager, GCP Secret Manager) and third-party platforms that work on-premises or in hybrid environments. The comparison table covers 10 solutions across three dimensions: on-premises deployment availability, SaaS version availability, and license type.

The tools covered span open-source, commercial, and hybrid models. Open-source options include Ansible Vault (simpler, file-based), Conjur (enterprise-grade, CyberArk-backed), and ejson (lightweight JSON encryption). Commercial platforms include 1Password Connect, Akeyless, BeyondTrust, and Doppler. Hybrid options include HashiCorp Vault, Bitwarden Secrets Manager, and Infisical.

The article's notable observation: outside cloud-vendor offerings, HashiCorp Vault dominates market presence. This reflects Vault's positioning as the default enterprise secrets management standard over the past decade — though its BSL license change has pushed some teams toward alternatives like OpenBao (the open-source fork) or managed Vault services. The article serves as a directory rather than a deep implementation guide.

## Key points

- Maps secrets management across three deployment models: cloud-vendor, SaaS, on-premises.
- Open-source options: Ansible Vault, Conjur, ejson.
- Commercial: Doppler, Akeyless, BeyondTrust, 1Password Connect.
- Hybrid: HashiCorp Vault (dominant), Bitwarden Secrets Manager, Infisical.
- HashiCorp Vault is the most widely adopted non-cloud-vendor solution.
- Pairs with SOPS (file encryption) and [dotenvx](/notes/dotenvx/) (dev workflows) for different parts of the secrets stack.

[Original](https://hsm.tunnel53.net/article/secrets-management/)
