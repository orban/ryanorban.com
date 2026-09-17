---
title: Docker layer caching in GitHub Actions
date: 2024-04-07
categories:
  - docker
  - github-actions
  - ci-cd
  - performance
  - devops
description: Blacksmith's guide to Docker layer caching in GitHub Actions — covering the different cache backends (inline, registry, gha), when each works, and how to get 2x faster builds. Practical guide to a topic where bad defaults waste significant CI time.
params:
  source: pinboard
  sourceUrl: https://blacksmith.sh/blog/cache-is-king-a-guide-for-docker-layer-caching-in-github-actions
---

![Docker layer caching in GitHub Actions](/images/notes/docker-layer-caching-github-actions.png)

## Summary

Docker layer caching is one of the highest-leverage CI optimizations available — yet GitHub Actions' default behavior defeats it on every run. This guide from Blacksmith (a GitHub Actions compute provider) covers the three main caching strategies for Docker builds in CI: inline cache (baked into the image), registry cache (stored in a container registry), and GitHub Actions cache (stored in GHA's native cache store via BuildKit).

The core problem: GitHub Actions runners are ephemeral. Each run starts fresh, meaning Docker's local layer cache doesn't survive between runs. Without explicit cache configuration, every build rebuilds from scratch — even if the base image and most layers haven't changed. For typical application images this means 3-5 minute builds for steps that could be sub-minute with caching.

The GHA cache backend (`type=gha`) is the most convenient for pure GitHub users — it stores BuildKit cache artifacts in GitHub's native cache infrastructure, accessible across runs on the same branch. The registry backend is more portable and works better for large teams with many concurrent runners. The guide covers configuration for `docker/build-push-action` which is the standard GitHub Actions action for Docker builds.

## Key points

- GitHub Actions runners are ephemeral — Docker layer cache must be explicitly configured to persist across runs.
- Three backends: inline (baked in image), registry (container registry storage), `type=gha` (GitHub cache API).
- `type=gha` is the easiest to configure for GitHub-native workflows; registry works better at scale.
- Claims 2x faster builds at half cost — consistent with avoiding full rebuilds on unchanged layers.
- From Blacksmith, a GitHub Actions compute alternative — they have strong incentives to understand CI performance.
- Requires BuildKit (default in modern Docker versions).

[Original](https://blacksmith.sh/blog/cache-is-king-a-guide-for-docker-layer-caching-in-github-actions)
