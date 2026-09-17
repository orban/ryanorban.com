---
title: Personal Security Checklist
date: 2022-04-04
categories:
  - security
  - privacy
  - reference
  - checklist
  - opsec
description: Lissy93's personal security checklist on GitHub — 300+ categorized tips for protecting digital security and privacy. A practical reference for hardening accounts, devices, and browsing habits without becoming a full-time security researcher.
params:
  source: pinboard
  sourceUrl: https://github.com/Lissy93/personal-security-checklist
---

## Summary

Alicia Sykes (Lissy93) compiled this GitHub repository as a comprehensive, categorized checklist of personal digital security measures — 300+ recommendations spanning authentication, networking, devices, browsing, email, and operational security. Unlike most security advice that's either too vague (use strong passwords) or too extreme (Tails OS for grocery shopping), this checklist is tiered by effort and threat model, letting users pick the practices that match their actual risk level.

The authentication section covers the most impactful practices: unique passwords per service via a password manager (Bitwarden, 1Password), two-factor authentication with authenticator apps rather than SMS (which is vulnerable to SIM swapping), and regular audit of authorized third-party app access. These three practices together close the vast majority of account compromise vectors for most users. The checklist is explicit that SMS 2FA is significantly weaker than TOTP or hardware keys.

Networking and browsing sections address VPN usage, DNS-over-HTTPS, browser fingerprinting, tracker blocking, and Tor for high-sensitivity browsing. Device security covers full disk encryption (FileVault on macOS, BitLocker on Windows), screen lock, software update hygiene, and secure deletion. The opsec section goes further: email aliases for third-party signups, minimal data sharing, and compartmentalization strategies. The repository is regularly updated and community-contributed, making it a living reference rather than a static document.

## Key points

- Tiered by threat level — practical for most users without requiring extreme measures; covers both basic hygiene and advanced hardening.
- Authentication priorities: password manager + TOTP 2FA (not SMS) + third-party app audit covers most attack surface.
- SIM swapping makes SMS 2FA weak: carriers can be social-engineered; authenticator apps can't be.
- Full disk encryption is table stakes: FileVault (macOS), BitLocker (Windows), LUKS (Linux) — covers physical device theft.
- DNS-over-HTTPS prevents ISP-level DNS surveillance; VPN shifts trust from ISP to VPN provider (not a panacea).
- Open-source, community-maintained at GitHub; last updated regularly — check the repo date for currency.

[Original](https://github.com/Lissy93/personal-security-checklist)
