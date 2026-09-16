---
title: My First 5 Minutes On A Server; Or, Essential Security for Linux Servers
date: 2013-03-04
categories:
  - linux
  - security
  - server
  - devops
  - sysadmin
description: Bryan Kennedy's definitive guide to the essential security hardening steps for a new Linux server — create a non-root user, set up SSH keys, disable root login, configure ufw, enable automatic updates, install fail2ban. One of the most bookmarked sysadmin articles of its era.
params:
  source: pinboard
  sourceUrl: http://plusbryan.com/my-first-5-minutes-on-a-server-or-essential-security-for-linux-servers
---

## Summary

Bryan Kennedy's guide became the canonical reference for Linux server security hardening in the early 2010s — the article that defined what good enough baseline security looked like for developers who were standing up VPS instances on DigitalOcean, Linode, or AWS EC2. It was widely shared and bookmarked because it addressed a real gap: most tutorials showed you how to install software, not how to secure the machine it ran on.

The procedure covered: (1) **Create a new user** with sudo access — never operate as root. (2) **Set up SSH key-based authentication** and add your public key to `~/.ssh/authorized_keys`. (3) **Disable root SSH login** by setting `PermitRootLogin no` in `sshd_config`. (4) **Disable password authentication** — keys only. (5) **Configure ufw** (Uncomplicated Firewall) to allow only necessary ports. (6) **Enable automatic security updates** via `unattended-upgrades`. (7) **Install fail2ban** to automatically block IP addresses making repeated failed login attempts.

These steps addressed the most common attack vectors for an internet-facing Linux server: brute force SSH password attacks (mitigated by key-only auth and fail2ban), accidental root compromise (mitigated by sudo-only access), and exposed unnecessary services (mitigated by firewall defaults-deny policy).

## Key points

- **Key-only SSH auth** + **disabled password login** closes the brute-force SSH attack vector entirely — the most common attack on new servers
- **Non-root sudo user**: principle of least privilege — daily operations don't require root, so root login should be impossible
- **fail2ban**: rate-limits login attempts by banning IPs after a configured threshold — effective against distributed brute force
- **ufw** (Uncomplicated Firewall): a sane iptables frontend — default deny all inbound, explicitly allow SSH (22), HTTP (80), HTTPS (443)
- **Automatic updates**: security patches for Ubuntu/Debian should be applied automatically — manual update discipline doesn't hold in practice

[Original](http://plusbryan.com/my-first-5-minutes-on-a-server-or-essential-security-for-linux-servers)
