---
title: "Tessl: package manager for AI agent skills"
date: 2026-02-25
categories:
  - ai-agents
  - skills
  - package-manager
  - developer-tools
description: Tessl is npm for AI agent skills — versioned, evaluated, and discoverable through a public registry. Skills can be submitted via GitHub URL or evaluated locally via CLI before publishing.
params:
  source: pinboard
  sourceUrl: https://tessl.io/registry/skills/submit
---

![Tessl: package manager for AI agent skills](/images/notes/tessl-skill-registry.png)

## Summary

Tessl is a package registry and evaluation platform for AI agent skills — functioning like npm or pip, but for agent capabilities rather than code libraries. The parallel is intentional: just as npm solved the problem of sharing and discovering JavaScript packages, Tessl aims to solve the same problem for Claude Code skills, MCP tools, and other agent-callable capabilities.

The evaluation layer is what distinguishes it from a simple registry. Before a skill enters the public index, Tessl reviews it — either by scanning a submitted GitHub repo automatically or via a CLI tool that lets developers evaluate privately before publishing. This quality check prevents the registry from becoming a dump of half-working prompts and ensures skills in the index meet some baseline standard.

Two submission paths: GitHub URL (Tessl scans automatically, evaluated version becomes discoverable) or CLI (`tessl eval` for local, private, or work-in-progress skills without publishing). The explicit positioning as versioned & verified distinguishes it from informal skill-sharing that happens in GitHub repos and Slack threads.

## Key points

- Package manager for agent skills: versioned, evaluated, discoverable in a public registry.
- Evaluation before listing: GitHub URL auto-scan or local CLI eval — prevents low-quality skills from polluting the registry.
- Two paths: public submission via GitHub URL, or local evaluation via `tessl eval` without publishing.
- Addresses a real gap: there's currently no standard way to discover, evaluate, or version Claude Code skills and MCP tools.
- Explicit parallel to npm — same problem of package discovery and quality, different domain.

[Original](https://tessl.io/registry/skills/submit)
