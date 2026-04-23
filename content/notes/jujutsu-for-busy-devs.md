---
title: "Jujutsu For Busy Devs: Practical Intro to jj"
date: 2025-07-22
categories:
  - developer-tools
  - version-control
  - jujutsu
  - git
  - workflow
description: A pragmatic intro to Jujutsu (jj), the new version control system that's git-compatible but fixes many of git's ergonomic frustrations — written for developers who don't have time for a deep-dive. jj's working-copy-as-a-commit model and first-class conflict handling make it worth adopting.
params:
  source: pinboard
  sourceUrl: https://maddie.wtf/posts/2025-07-21-jujutsu-for-busy-devs
---

![Jujutsu For Busy Devs: Practical Intro to jj](/images/notes/jujutsu-for-busy-devs.png)

## Summary

Jujutsu (command: `jj`) is a version control system built on top of git's object model but with a fundamentally different user interface. This post from maddie.wtf gives a pragmatic introduction for developers who want to try it without reading the full documentation. The key point: `jj` is git-compatible (uses git repos, pushes to git remotes) so you can adopt it incrementally without abandoning your existing workflow.

The signature feature is the working copy as a commit. In git, the working directory is distinct from commits — you `add`, then `commit`. In `jj`, the working directory is always the latest commit, automatically updated on every change. You never stage files explicitly; you just describe the commit when you're happy with it. This eliminates the staging area entirely and makes the common pattern of "show me what's different from main" much simpler.

First-class conflicts are the other major difference. Where git aborts on conflicts and forces you to resolve them immediately, `jj` stores conflicts inside commits. You can rebase through a merge conflict, keep working, and resolve it when convenient. This makes complex rebases (feature branch on top of recent main) far less disruptive. The post explains these concepts with concrete commands for developers coming from `git`.

## Key points

- Jujutsu (`jj`) is git-compatible: uses git repos, pushes to git remotes — incrementally adoptable.
- Working copy as a commit: no staging area, working directory is always the latest commit.
- First-class conflicts: conflicts stored inside commits, resolvable at any point — not blocking.
- Simpler rebasing: rebase through conflicts without immediate resolution.
- Written for busy devs — pragmatic commands, not theoretical VCS concepts.
- Growing adoption in the open-source community; used at Google internally.

[Original](https://maddie.wtf/posts/2025-07-21-jujutsu-for-busy-devs)
