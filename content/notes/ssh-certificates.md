---
title: "SSH Certificates: Why You're Doing SSH Wrong"
date: 2022-03-25
categories:
  - ssh
  - security
  - infrastructure
  - certificates
  - zero-trust
description: Smallstep's case for SSH certificates over authorized_keys — short-lived certificates issued by a CA eliminate the credential sprawl that makes SSH key management a compliance nightmare. The practical alternative to key-based SSH at scale.
params:
  source: pinboard
  sourceUrl: https://smallstep.com/blog/use-ssh-certificates/
---

![SSH Certificates: Why You're Doing SSH Wrong](/images/notes/ssh-certificates.png)

## Summary

Smallstep's argument is direct: if you're still using `authorized_keys` for SSH access control, you have a key sprawl problem you probably don't fully understand. Every long-lived SSH key that gets added to a server is a credential that persists indefinitely unless someone manually removes it — and in practice, nobody does. Engineers leave companies, contractors finish projects, and their keys stay on servers for years. SSH certificates solve this by introducing a Certificate Authority that issues short-lived credentials, making revocation the default rather than an active task.

The mechanism works like TLS for websites. Instead of distributing public keys to every server's `authorized_keys` file, you configure servers to trust a CA's public key. When a user authenticates, they present an SSH certificate (their public key signed by the CA) rather than a raw key. The server verifies the certificate against the trusted CA — no need to distribute individual keys. Certificates carry metadata: identity, allowed principals (usernames), and critically, an expiry. A certificate valid for 8 hours means access automatically expires; you don't need to revoke anything when someone leaves, their certificate just becomes invalid.

Tools like Smallstep CA, Teleport, and HashiCorp Vault's SSH secrets engine implement this pattern. The operational improvement is significant: instead of maintaining `authorized_keys` files across a fleet, you manage one CA whose public key is deployed everywhere. Revoking access means stopping issuing certificates to a principal — the existing short-lived certs expire on their own schedule. This is the same logic behind zero trust networking: assume breach, minimize credential lifetime, log everything.

## Key points

- authorized_keys files accumulate stale keys indefinitely; SSH certificates expire automatically — eliminating one of the most common SSH security failures.
- Certificates are issued by a Certificate Authority — servers trust the CA, not individual keys.
- Short-lived certificates (hours, not years) make revocation trivial: just stop issuing them.
- Certificates carry identity metadata: who the user is, what principals they can assume, when it expires.
- Smallstep CA is an open-source CA server that implements this pattern; Teleport and HashiCorp Vault offer similar functionality.
- Same trust model as TLS — well-understood, battle-tested approach applied to SSH.

[Original](https://smallstep.com/blog/use-ssh-certificates/)
