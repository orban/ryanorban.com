---
title: Git Tips from the Trenches
date: 2014-02-02
categories:
  - git
  - developer-tools
  - version-control
  - workflow
  - productivity
description: A practitioner's collection of git tips beyond the basics — covering aliases, bisect, stash, reflog, and workflow patterns learned from actual team use. The kind of git knowledge that only comes from running into the same problems repeatedly.
params:
  source: pinboard
  sourceUrl: https://ochronus.com/git-tips-from-the-trenches/
---

## Summary

Ochronus.com's git tips post collects the lesser-known git commands and workflows that become valuable once you're past the basic commit/push cycle. The from the trenches framing signals that these are patterns learned from real-world team use rather than from reading the documentation top-to-bottom.

Key areas covered: **git bisect** for binary search through commit history to find which commit introduced a bug (can be automated with a test script using `git bisect run`); **git reflog** as a safety net when you think you've lost commits — reflog tracks every position HEAD has been at, so you can recover from errant resets or rebases; **git stash** for temporarily shelving uncommitted work; and **git aliases** to reduce friction for frequently-used commands.

The `[[git log]]` formatting options get attention: `git log --oneline --graph --decorate --all` produces the visual branch/merge graph that makes history readable. `git log -S "search string"` (the pickaxe) finds commits that added or removed a specific string — useful for tracking down when a piece of code appeared or disappeared. These commands are available in every git installation but rarely taught in beginner tutorials.

## Key points

- `git bisect run <test-script>`: fully automates the binary search — runs your test on each candidate commit and finds the bad one without manual intervention.
- `git reflog`: the local undo history — shows every place HEAD has pointed, recoverable for ~90 days even after resets.
- `git log -S "string"` (pickaxe): search commit history for additions/removals of a specific string — more precise than `git grep` for tracking code changes over time.
- `git stash` with `git stash pop`/`git stash apply`: context-switch without committing — works in combination with `git stash list` to manage multiple stashes.
- `git log --graph --decorate --all --oneline`: the one-liner that makes branch topology visible — usually aliased as `git lg`.

[Original](https://ochronus.com/git-tips-from-the-trenches/)
