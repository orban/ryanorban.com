---
title: On Undoing, Fixing, or Removing Commits in Git
date: 2013-12-15
categories:
  - git
  - version-control
  - developer-tools
  - reference
description: Seth Robertson's choose-your-own-adventure guide to undoing git mistakes — a decision tree covering uncommitted changes, unpublished commits, and pushed history. The go-to reference when something has gone wrong in git.
params:
  source: pinboard
  sourceUrl: http://sethrobertson.github.io/GitFixUm/fixup.html
---

## Summary

Seth Robertson's guide is structured as an interactive decision tree rather than a linear reference: you follow branches based on your situation until you reach a specific, actionable solution. This structure acknowledges that git recovery scenarios are highly situational — the right answer depends on whether you've committed, whether you've pushed, and exactly what you're trying to undo.

The guide branches on three main axes: work not yet committed (discard vs stash vs branch), commits made but not pushed (which can be rewritten freely with `git reset`, interactive git rebase, or `git commit --amend`), and commits that have been pushed (where the guide strongly advises against rewriting history and recommends `git revert` instead).

The most practically valuable section covers git reflog recovery — getting back commits that seem lost after a hard reset, a bad rebase, or a deleted branch. The reflog keeps track of every position HEAD has ever pointed to, making it possible to recover "lost" commits for up to 90 days. This is git's safety net that most users don't know exists.

## Key points

- Interactive decision tree format: start with your situation, follow branches, get the specific git commands you need.
- Uncommitted work: `git stash` (temporary save), `git checkout --` (discard), or create a branch to park it.
- Committed but unpushed: safe to rewrite with `git reset`, `git rebase -i`, or `--amend`. These are your own local commits.
- **Pushed commits: don't rewrite history** — use `git revert` to create a new commit that undoes the change.
- git reflog: recovers "lost" commits after bad resets or deleted branches. Every HEAD position is recorded for 90 days.
- Merge commit recovery and cross-branch cherry-picks are also covered for more complex scenarios.

[Original](http://sethrobertson.github.io/GitFixUm/fixup.html) → GitHub
