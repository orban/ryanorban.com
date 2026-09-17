---
title: Learn Git Branching
date: 2013-10-27
categories:
  - git
  - education
  - interactive
  - developer-tools
  - version-control
description: Learn Git Branching is an interactive visual tutorial for Git concepts — especially branching, merging, rebasing, and remotes. The best resource for building a mental model of how Git's DAG actually works.
params:
  source: pinboard
  sourceUrl: http://pcottle.github.io/learnGitBranching/?remoteDemo&defaultTab=remote
---

## Summary

[Learn Git Branching](/notes/learn-git-branching/) is an interactive browser-based tutorial that visualizes Git operations as a directed acyclic graph (DAG). Most Git confusion — especially around branching, rebasing, and merge conflicts — comes from not having a mental model of what Git actually stores. This tool makes the graph explicit and manipulable: you type commands and watch the commit graph change in real time.

The remote module (the URL in this save) covers Git remotes, fetch, push, and pull — the operations that trip up programmers most in team environments. Seeing `git fetch` move `origin/main` without touching your local branch, or watching `git rebase origin/main` replay your commits on top of the remote, makes these operations intuitive in a way that reading documentation rarely achieves.

Peter Cottle built this as an open-source project and it became the standard recommendation for developers learning Git branching concepts. It remains one of the best examples of interactive learning for a technical tool — the feedback loop between command and graph animation is tight enough to build real intuition.

## Key points

- Visualizes Git's directed acyclic graph (DAG) in real time as you type commands — the best way to build an accurate mental model.
- Covers all core concepts: commits, branches, merge, rebase, cherry-pick, detached HEAD, relative refs.
- Remote module teaches fetch/push/pull/rebase with remote tracking branches — the concepts most confusing in team workflows.
- Interactive > documentation for building Git intuition; the immediate visual feedback is what makes it click.
- Still actively used and recommended; one of the canonical Git learning resources a decade after launch.

[Original](http://pcottle.github.io/learnGitBranching/?remoteDemo&defaultTab=remote) → GitHub
