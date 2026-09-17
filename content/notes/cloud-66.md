---
title: Cloud 66 — Code to Cloud in 5 Minutes
date: 2013-02-13
categories:
  - devops
  - deployment
  - paas
  - infrastructure-as-code
description: Cloud 66 is a deployment and infrastructure management platform that handles production operations across any cloud or bare metal — zero-downtime deploys, auto-scaling, managed databases, no vendor lock-in. Fills the gap between PaaS simplicity and full DevOps control.
params:
  source: pinboard
  sourceUrl: https://www.cloud66.com/
---

## Summary

[Cloud 66](/notes/cloud-66/) launched as a deployment automation platform occupying the gap between full-service PaaS (like Heroku) and raw cloud infrastructure (like AWS EC2 without any tooling). The value proposition: you bring your own cloud account, and Cloud 66 handles the deployment, scaling, and operational complexity on top of it.

The Day 2 problem Cloud 66 addresses is real: Heroku-style PaaS makes initial deployment easy but constrains what you can run and charges premium prices at scale. Running directly on AWS or DigitalOcean gives you control but requires significant DevOps expertise to handle zero-downtime deploys, auto-scaling, database management, and security hardening. Cloud 66 tried to automate that operational layer while preserving the infrastructure flexibility.

By 2013, this positioned Cloud 66 in the same competitive space as EngineYard and early Dokku — developer-friendly deployment that didn't require a dedicated DevOps engineer. The category would later consolidate around Kubernetes-based tools, but in 2013 container orchestration didn't yet exist as a concept. Cloud 66 has continued to evolve, now supporting Docker and Kubernetes alongside its original stack-based deployment model.

## Key points

- Cloud 66 solves "Day 2" operations: the initial deployment is easy, but zero-downtime updates, scaling events, and database migrations on your own infrastructure require significant automation
- No vendor lock-in: deploys to any cloud or bare metal — unlike Heroku, which requires running on AWS and charges Heroku's markup
- Competes with EngineYard, Ninefold, and Dokku in the 2013 developer-operations automation market
- Supports Docker and Kubernetes in its modern form — has evolved beyond the original 2013 stack-as-unit model
- The demand for this category persisted: Render, Fly.io, and Railway in the 2020s serve similar needs for developer teams without dedicated platform engineers

[Original](https://www.cloud66.com/)
