---
title: Developing Inside a Container with VS Code Remote Development
date: 2021-02-28
categories:
  - vscode
  - docker
  - developer-tools
  - devcontainers
  - remote-development
description: VS Code's official documentation for Remote Development with containers — using Docker containers as a full development environment, with VS Code connecting to a containerized shell. Predates GitHub Codespaces, which uses the same devcontainer spec.
params:
  source: pinboard
  sourceUrl: https://code.visualstudio.com/docs/remote/containers
---

![Developing Inside a Container with VS Code Remote Development](/images/notes/vscode-remote-containers.png)

## Summary

VS Code's Remote Development extension lets you open a folder inside a Docker container and use it as your full development environment — the editor runs locally but the shell, file system, extensions, and processes all run inside the container. This means your local machine needs no project dependencies: Python, Node, compilers — all live in the container image.

The configuration is a `.devcontainer/devcontainer.json` file that specifies the Docker image (or Dockerfile), VS Code extensions to install inside the container, port forwarding rules, and post-create commands. The devcontainer spec is the open standard that emerged from this work. It's now also the foundation for GitHub Codespaces — cloud-hosted development environments that use the same `.devcontainer.json` configuration.

The practical value: onboarding a new engineer to a project becomes `git clone` + open in container, rather than an afternoon of dependency installation and environment configuration. Reproducible development environments mean works on my machine stops being an excuse. The approach also makes it easier to work on projects with conflicting requirements (e.g., Python 2 vs Python 3 projects) without managing multiple local environments.

## Key points

- Opens a project inside a Docker container — shell, extensions, processes all run in container, editor runs locally.
- Configuration via `.devcontainer/devcontainer.json` — specifies image, extensions, port forwarding.
- Devcontainer spec (now open standard) — same configuration used by GitHub Codespaces.
- Eliminates "works on my machine" — consistent environment for all contributors.
- Pairs with Docker Compose for multi-container development (e.g., app + database).

[Original](https://code.visualstudio.com/docs/remote/containers) → GitHub
