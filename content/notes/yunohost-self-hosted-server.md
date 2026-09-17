---
title: "YunoHost: Self-Hosted Server for Everyone"
date: 2022-09-10
categories:
  - self-hosted
  - infrastructure
  - linux
  - privacy
  - open-source
description: YunoHost is an open-source server OS that makes self-hosting web apps as simple as clicking install — Nextcloud, Gitea, Mastodon, and 100+ others available in one catalog. It handles DNS, SSL, user management, and backups automatically, dramatically lowering the barrier to self-hosting.
params:
  source: pinboard
  sourceUrl: https://yunohost.org/
---

## Summary

YunoHost is a Debian-based server distribution designed to make self-hosting accessible to non-sysadmins. The central feature is a curated app catalog — over 100 applications including Nextcloud, Gitea, Mastodon, Pleroma, Synapse (Matrix), Jellyfin, and Bitwarden — each installable in a few clicks with automatic SSL certificate provisioning, nginx configuration, and user management handled by the framework.

The design goal is explicitly political as well as technical: YunoHost positions itself as infrastructure for digital sovereignty. The name is a playful corruption of Why you no host? — reflecting the frustration that self-hosting remains unnecessarily hard, keeping users dependent on platforms they don't control. The federated web (ActivityPub, Matrix, XMPP) is a natural fit: self-hosting a Mastodon instance or Matrix homeserver becomes practical when YunoHost handles the operational complexity.

YunoHost sits in a category alongside Sandstorm, Cloudron, and Umbrel — managed self-hosting platforms that abstract over server administration. The difference from a VPS is that you install apps rather than configure services; the difference from cloud SaaS is that you own the data and the infrastructure. Let's Encrypt integration means HTTPS just works; the built-in user directory means all apps share a single login.

## Key points

- Debian-based self-hosting OS with a curated 100+ app catalog — one-click installs for Nextcloud, Gitea, Mastodon, etc.
- Handles nginx config, Let's Encrypt SSL, and LDAP user management automatically.
- Explicitly designed for digital sovereignty — federated apps (ActivityPub, Matrix) are core use cases.
- Comparable to Cloudron and Umbrel; simpler than a raw VPS, more control than SaaS.
- Community-maintained; apps in the catalog are packaged to YunoHost's standards for update compatibility.
- Lowers the technical bar enough that non-sysadmins can run meaningful federated infrastructure.

[Original](https://yunohost.org/)
