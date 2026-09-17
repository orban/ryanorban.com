---
title: "fnox: secret manager for mise workflows"
date: 2025-10-28
categories:
  - developer-tools
  - secrets
  - mise
  - security
  - cli
description: fnox is a new secret management tool designed to pair with mise in dev workflows — storing secrets outside dotfiles and injecting them at runtime. Announced by the mise author as a companion to mise's tool/runtime management.
params:
  source: pinboard
  sourceUrl: https://github.com/jdx/mise/discussions/6779
---

![fnox: secret manager for mise workflows](/images/notes/fnox-secret-manager-mise.png)

## Summary

fnox is a secret management tool announced in the mise GitHub discussions by the mise author (jdx). It's designed to complement mise's runtime and tool management with a secrets layer — keeping credentials outside of dotfiles and environment files while making them available to development workflows.

mise manages runtime versions (Node, Python, Go, etc.) and dev tools via `.mise.toml` files. The missing piece has been secrets — developers typically resort to `.env` files (which get accidentally committed) or separate tools with more setup overhead. fnox fills that gap with something that integrates naturally with the mise ecosystem.

The announcement marks it as version 1.0, indicating stable enough for production use despite being new. The mise ecosystem has grown significantly as an asdf replacement, and having a companion secret manager from the same author means tighter integration and shared design philosophy. Relevant for teams using mise who want consistent secrets handling across environments.

## Key points

- Secret management tool designed to pair with mise in development workflows.
- Stores credentials outside dotfiles/env files — no accidental commits.
- Announced by jdx (mise author) as a companion to mise's tool management.
- Version 1.0 — designed to be stable for production use despite being new.
- Closes the gap in the mise ecosystem around secrets alongside runtime management.

[Original](https://github.com/jdx/mise/discussions/6779)
