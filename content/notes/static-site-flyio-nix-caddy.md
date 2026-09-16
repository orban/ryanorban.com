---
title: Hosting a Static Site on Fly.io with Nix and Caddy
date: 2022-09-06
categories:
  - devops
  - nix
  - fly-io
  - caddy
  - infrastructure
description: A walkthrough of hosting a static site on Fly.io using Nix for reproducible builds and Caddy as the web server — an elegant stack for anyone who wants declarative, reproducible deployments without the complexity of Kubernetes or the cost of AWS.
params:
  source: pinboard
  sourceUrl: https://mat.services/posts/static-site-with-nix-and-caddy/
---

## Summary

This tutorial walks through deploying a static site on Fly.io using Nix for reproducible build environments and Caddy as the web server. The stack combines three tools that each solve a specific problem: Nix ensures the build environment is exactly reproducible — same inputs always produce the same outputs, regardless of what's installed on the host machine; Caddy provides automatic HTTPS via Let's Encrypt with a simple configuration syntax; Fly.io handles deployment to edge infrastructure close to users with a straightforward CLI workflow.

The appeal of this combination: it avoids the common failure modes of simpler hosting setups. Static site hosting on S3 + CloudFront works but requires AWS familiarity and has fiddly CORS and cache-invalidation behavior. Netlify and Vercel are simpler but opinionated and not self-hosted. Fly.io + Caddy gives you a containerized, globally distributed server with proper HTTP/2 and automatic certificate management, while Nix ensures the Docker image is built reproducibly without manual dependency pinning.

Nix is the key differentiator here — most static site build pipelines use `npm install` or similar which can drift over time as packages update. Nix pins the entire dependency graph including system-level dependencies, which means builds from six months ago still work the same way today. This matters for long-lived sites where you want to be able to rebuild without debugging dependency drift.

## Key points

- Stack: Nix (reproducible builds) + Caddy (automatic HTTPS web server) + Fly.io (edge deployment).
- Nix pins entire dependency graph including system libraries — eliminates dependency drift over time.
- Caddy handles Let's Encrypt certificate provisioning automatically — no manual cert management.
- Fly.io provides global edge deployment with a simple CLI — `fly deploy` does the full push.
- Alternative to S3+CloudFront (complex), Netlify/Vercel (opinionated), or bare VPS (more maintenance).
- The Nix + Docker pattern is underused — produces minimal, reproducible images without manual Dockerfile tuning.

[Original](https://mat.services/posts/static-site-with-nix-and-caddy/)
