---
title: "GOMP: Git Branch Comparison Tool"
date: 2020-07-31
categories:
  - git
  - developer-tools
  - cli
  - open-source
description: GOMP (Git COMPare) is a CLI tool for visually comparing files that differ between two Git branches — a focused alternative to git diff for branch comparison workflows.
params:
  source: pinboard
  sourceUrl: https://github.com/MarkForged/GOMP
---

## Summary

GOMP (Git COMPare) is a command-line tool for comparing two Git branches and visually reviewing the differences. Where `git diff branch1..branch2` shows a unified diff, GOMP provides a more interactive comparison interface that makes it easier to navigate which files differ and inspect the changes between branches.

The tool targets a specific workflow gap: when reviewing a pull request or comparing feature branches, you often want to understand the shape of the differences before diving into individual file diffs. GOMP provides an interactive file list showing which files changed, with the ability to open specific file comparisons. This is especially useful for large PRs or release comparisons where the naive `git diff` output is too long to navigate linearly.

Git tooling for branch comparison has several options: `git diff`, `git difftool` with a configured external diff viewer (like Kaleidoscope or Beyond Compare), GitHub's PR diff UI, and specialized tools like GOMP. The case for a dedicated CLI tool is that it works offline, doesn't require a GitHub remote, and integrates into a terminal workflow without context switching to a browser.

## Key points

- GOMP (Git COMPare): CLI tool for interactive branch-to-branch file comparison.
- Addresses the workflow gap between `git diff` (too raw) and GitHub PR UI (requires remote push).
- Interactive file list: see which files differ between branches before diving into diffs.
- Works offline, no GitHub remote required — useful for local branch comparison.
- Part of the broader Git productivity tooling ecosystem alongside git-delta, tig, etc.

[Original](https://github.com/MarkForged/GOMP)
