---
title: "Piku: The Tiniest PaaS You've Ever Seen"
date: 2024-06-09
categories:
  - self-hosted
  - devops
  - paas
  - git
  - open-source
  - infrastructure
description: Piku is a tiny self-hosted PaaS that lets you git-push to deploy to your own servers — a minimal Heroku-style experience with no containers required. Under 2000 lines of Python, runs on any Linux server.
params:
  source: pinboard
  sourceUrl: https://github.com/piku/piku
---

![Piku: The Tiniest PaaS You've Ever Seen](/images/notes/piku-tiny-paas.png)

## Summary

Piku is a minimal self-hosted PaaS (Platform as a Service) that provides Heroku-style `git push` deployments to your own Linux server. You install it on any Linux machine, add a SSH key, and then `git push piku main` deploys your application — similar to how Heroku, Render, or Railway work, but running entirely on your own infrastructure. No containers required, no Kubernetes, no Docker Compose — it uses uwsgi, nginx, and process supervision directly.

The design philosophy is radical minimalism. Piku is under 2000 lines of Python, handles multiple apps on a single server, manages environment variables via a `.env` file pattern, supports Python, Node.js, Go, Ruby, Clojure, and static sites via Procfile configuration, and uses nginx for routing. You can read the entire codebase in an afternoon — there's nothing hidden. This is the antithesis of the Kubernetes/Helm/Istio stack.

The use case: you have a VPS or small server and you want to deploy multiple small applications without the overhead of container orchestration. Piku sits between just run it with screen and run a full Kubernetes cluster. It's particularly well-suited for solo developers, small teams, or homelab setups where Heroku is too expensive and Kubernetes is too complex. Think personal projects, side projects, internal tools. Compares to Dokku (more featured, Docker-based) but is simpler and lighter.

## Key points

- Git push to deploy: `git push piku main` deploys your app to your own server.
- Under 2000 lines of Python — fully readable codebase.
- No Docker or containers: uses uwsgi, nginx, and process supervision directly.
- Supports Python, Node.js, Go, Ruby, Clojure, static sites via Procfile.
- Manages multiple apps on a single server with nginx-based routing.
- Lighter than Dokku; simpler than Kubernetes; more powerful than raw systemd scripts.

[Original](https://github.com/piku/piku) → GitHub
