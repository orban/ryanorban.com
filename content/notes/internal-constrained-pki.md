---
title: "Internal Constrained PKI: Safe TLS CA for .internal Networks"
date: 2024-10-22
categories:
  - security
  - tls
  - networking
  - pki
  - infrastructure
description: internal-constrained-pki creates a TLS root CA for .internal networks with X.509 Name Constraints — the CA is cryptographically prevented from signing certificates for public domains, making it safe to share with team members without compromising internet trust.
params:
  source: pinboard
  sourceUrl: https://github.com/nh2/internal-contstrained-pki
---

![Internal Constrained PKI: Safe TLS CA for .internal Networks](/images/notes/internal-constrained-pki.png)

## Summary

[internal-constrained-pki](/notes/internal-constrained-pki/) by nh2 solves a real problem: you want TLS encryption on your internal network (`.internal`, `.local`, or custom internal domains) but you don't want to install a self-signed root CA that could be used to sign certificates for `google.com` if compromised. The solution is X.509 Name Constraints — an extension that cryptographically restricts the CA to only sign certificates for specified domain subtrees.

With Name Constraints set to `.internal`, the CA literally cannot produce a valid certificate for a public domain — the constraint is enforced by the browser's certificate validation logic, not just by policy. This makes the CA safe to distribute to team members, embed in company-managed devices, and add to system trust stores without the security risk of a fully trusted internal CA.

This addresses the gap between three imperfect options: using Let's Encrypt (requires public DNS), using plain self-signed certificates with browser warnings, or using a fully-trusted internal CA (which is a serious security risk if the private key leaks). Name-constrained CAs are the "right" solution but require understanding X.509 extension semantics that most infrastructure engineers don't encounter in day-to-day work.

## Key points

- X.509 Name Constraints limits CA signing authority to `.internal` domains — cryptographically enforced, not policy-only
- Safe to distribute to team members: a compromised key still can't sign `google.com` certificates
- Closes the gap between self-signed warnings, Let's Encrypt (needs public DNS), and risky fully-trusted internal CAs
- Relevant for homelab, corporate internal networks, and private infrastructure where HTTPS is required internally
- Underused feature of X.509 that most engineers aren't aware of

[Original](https://github.com/nh2/internal-contstrained-pki) → GitHub
