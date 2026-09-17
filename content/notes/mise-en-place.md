---
title: "mise-en-place: developer environment manager"
date: 2024-04-24
categories:
  - developer-tools
  - version-manager
  - cli
  - devenv
  - productivity
description: mise-en-place (mise) is a developer tool version manager and task runner — a single tool that manages language runtimes (Node, Python, Ruby), sets environment variables per-project, and replaces make for task running. The modern polyglot replacement for nvm/rbenv/pyenv.
params:
  source: pinboard
  sourceUrl: https://mise.jdx.dev/about.html
---

![mise-en-place: developer environment manager](/images/notes/mise-en-place.png)

## Summary

mise (mise-en-place) is a polyglot version manager and task runner for developer environments. It replaces a chain of individual version managers — nvm for Node, rbenv or rvm for Ruby, pyenv for Python — with a single tool that manages all of them via a unified `.mise.toml` config file. Clone a repo, run `mise install`, and you have the right versions of every runtime.

Beyond version management, mise handles environment variables per-project (a direct replacement for direnv) and task running (a more explicit replacement for Makefile workflows). The combination means one config file per project describes everything needed to get a development environment working: runtimes, environment variables, and the commands to run them.

The tool is written in Rust for performance — activating the environment on directory entry needs to be fast, since it runs on every `cd`. mise is backward-compatible with asdf plugins (the previous polyglot version manager standard), so existing plugin ecosystems transfer directly. The `about.html` page frames it as a thoughtful rethinking of the asdf design with better ergonomics and significantly faster activation.

## Key points

- Single tool replaces nvm, pyenv, rbenv, direnv, and make for most development workflows.
- `.mise.toml` per-project config specifies runtime versions, env vars, and task definitions.
- asdf-plugin compatible — existing plugin ecosystem works out of the box.
- Written in Rust — activation speed is a first-class concern.
- Strong adoption in the developer tools community as the successor to asdf.

[Original](https://mise.jdx.dev/about.html)
