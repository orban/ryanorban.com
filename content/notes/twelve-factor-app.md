---
title: The Twelve-Factor App
date: 2022-01-31
categories:
  - software-engineering
  - deployment
  - devops
  - cloud
  - saas
  - best-practices
description: The Twelve-Factor App is a methodology for building cloud-native SaaS applications, synthesized from Heroku's experience with hundreds of deployed apps. Canonical reference for why config should live in env vars, why logs should be streams, and why stateless processes matter.
params:
  source: pinboard
  sourceUrl: https://12factor.net/
---

## Summary

The [Twelve-Factor App](/notes/twelve-factor-app/) methodology is a set of twelve principles for building software-as-a-service applications that are portable, scalable, and maintainable. Synthesized by Adam Wiggins and contributors from the Heroku platform's experience with hundreds of deployed applications, it remains the canonical reference for cloud-native app design.

The factors span the full lifecycle of an application: from codebase management (one repo, multiple deploys) and dependency isolation, through configuration via environment variables, backing services as attached resources, and strict build/release/run separation. The later factors address process design (stateless, share-nothing), port binding, concurrency via process model, disposability (fast startup, graceful shutdown), dev/prod parity, treating logs as event streams, and admin processes as one-off commands.

These aren't arbitrary rules. Each factor addresses a specific class of operational problems that show up at scale: config drift between environments, dependency hell, inability to scale horizontally, fragile deployments, and poor observability. The methodology's influence is visible in how Docker, Kubernetes, and modern PaaS platforms are designed — they make twelve-factor apps easy and twelve-factor violations hard.

## Key points

- Config in environment variables — not hardcoded, not config files checked into the repo. Enables the same build to run anywhere.
- Stateless processes that share nothing — state lives in backing services (databases, Redis, etc.), not in memory or local disk.
- Logs as streams — write to stdout, let the platform aggregate and route. Enables centralized observability.
- Dev/prod parity — minimize differences between environments to avoid works on my machine failures.
- Disposability — fast startup and graceful shutdown enable elastic scaling and robust deployments.
- The methodology's influence is embedded in how Heroku, Docker, Kubernetes, and cloud-native tooling are designed.

[Original](https://12factor.net/)
