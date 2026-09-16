---
title: The Architecture Behind A One-Person Tech Startup
date: 2021-04-08
categories:
  - saas
  - architecture
  - solo-founder
  - infrastructure
  - cloud
description: Anthony Simon's honest account of the infrastructure architecture behind his one-person SaaS business — the actual stack, costs, tradeoffs, and what he'd do differently. Rare for its specificity and honesty about complexity vs. simplicity tradeoffs.
params:
  source: pinboard
  sourceUrl: https://anthonynsimon.com/blog/one-man-saas-architecture/
---

## Summary

Anthony Simon wrote this from his flat in Germany, running a low-stress one-person SaaS business. The essay is notable for its specificity — actual numbers, actual tools, actual tradeoffs — in contrast to the usual vague advice about "use the right tool for the job." He details what he runs, what it costs, and where the complexity lives.

The stack at time of writing: Kubernetes on DigitalOcean (via DigitalOcean Kubernetes), PostgreSQL for the primary database, Redis for caching and queues, Traefik as the ingress controller, and GitHub Actions for CI/CD. Monitoring via Prometheus and Grafana. The honest admission: this is probably overkill for a one-person shop, but Kubernetes was something he wanted to learn and the operational overhead became manageable.

The interesting tension in the essay is between the you should use what works pragmatism and the reality that engineers often choose infrastructure that's more complex than strictly necessary for reasons of learning and personal interest — which is a legitimate reason, but should be named as such. For a solo SaaS at typical indie hacker scale, Fly.io, Railway, or even Heroku would be simpler choices than self-managed Kubernetes. The essay is valuable precisely because it makes this tension explicit rather than presenting the architecture as obviously correct.

## Key points

- Full stack: Kubernetes (DigitalOcean), PostgreSQL, Redis, Traefik, GitHub Actions, Prometheus/Grafana.
- Honest admission: Kubernetes is overkill for one person but chosen for learning value.
- Solo SaaS pragmatic alternatives: Fly.io, Railway, Render — lower operational overhead.
- CI/CD via GitHub Actions: push to main → automated tests → container build → deploy.
- By Anthony Simon — rare for specificity: actual costs, actual tools, named tradeoffs.

[Original](https://anthonynsimon.com/blog/one-man-saas-architecture/) → GitHub
