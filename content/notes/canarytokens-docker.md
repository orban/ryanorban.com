---
title: Canarytokens Docker — Self-Hosted Honeytokens
date: 2022-10-17
categories:
  - security
  - honeypot
  - intrusion-detection
  - self-hosted
  - docker
  - open-source
description: Thinkst's Canarytokens Docker setup lets you self-host your own canarytoken server — tripwires that alert you when someone accesses a file, URL, or credential they shouldn't know about. The DIY version of Thinkst's hosted canary service.
params:
  source: pinboard
  sourceUrl: https://github.com/thinkst/canarytokens-docker
---

![Canarytokens Docker — Self-Hosted Honeytokens](/images/notes/canarytokens-docker.png)

## Summary

Canarytokens are tripwires designed to detect intrusions or unauthorized access. The concept: place a canary token (a URL, a document, a credential, a DNS name) somewhere an attacker would find it, and get alerted the moment it's touched. Unlike traditional IDS (intrusion detection systems) that monitor traffic, canary tokens are passive — they only fire when specifically accessed, which means alerts are high-signal with very low false positive rates.

Thinkst built Canarytokens as both a hosted service (canarytokens.org, free) and an open-source project. This Docker setup lets you run your own canarytoken server for cases where you can't use the hosted service — internal networks, airgapped environments, or organizations that need full control over token deployment and alert routing.

The types of tokens are inventive: web bugs (pixel images that ping home when an email is opened), credential honey tokens (AWS access keys, Azure credentials that trigger when used), Office documents with embedded web requests, DNS-based tokens, and custom URLs. The AWS key canary token is particularly elegant — you create a fake IAM key and get alerted if someone uses it, which catches both external attackers who find credentials and insiders who test whether monitored credentials work.

Thinkst (the company behind Canary hardware network sensors and the Canarytokens project) has been influential in making deception-based security more accessible. The self-hosted Docker version lowers the barrier for teams that need control over their own infrastructure.

## Key points

- Self-hosted canary token server via Docker — deploy tripwire tokens that alert on unauthorized access.
- Canary tokens: passive honeypots that fire only when accessed — high signal, low false positive rate.
- Token types: web bugs, AWS credential traps, DNS tokens, Office documents, custom URLs.
- AWS key canary token is especially useful: catches both external attackers and insider credential testing.
- Docker setup from Thinkst — the company behind the Canary hardware sensor product.
- Complements active IDS with passive detection; alerts mean something meaningful happened.

[Original](https://github.com/thinkst/canarytokens-docker) → GitHub
