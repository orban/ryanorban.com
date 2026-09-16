---
title: git-flight-rules
date: 2014-07-29
categories:
  - git
  - developer-tools
  - reference
  - version-control
description: "A comprehensive guide by k88hudson covering what to do when things go wrong in git — structured as flight rules (NASA-style: if X happens, do Y). One of the most-starred git reference repos on GitHub."
params:
  source: pinboard
  sourceUrl: https://github.com/k88hudson/git-flight-rules
---

## Summary

[git-flight-rules](/notes/git-flight-rules/) is a GitHub repository by Kate Hudson (k88hudson) structured as a practical reference guide for recovering from common git mistakes. The name comes from NASA flight rules — a set of hard-won protocols built from past incidents so that teams don't have to improvise under pressure. For git, that means: "I committed to the wrong branch — now what? or I accidentally deleted a branch — is it recoverable?"

The format is Q&A: each entry is a concrete situation (often phrased as an I did X, now what?) followed by the exact git commands to resolve it. This is more immediately useful than documentation organized around commands, because you typically know what went wrong, not which commands to reach for. Categories include undoing commits, fixing branches, staging and stashing, rewriting history with git rebase, recovering deleted commits from git reflog, and resolving merge conflicts.

The repo reflects a real gap in git's UX: the commands are powerful but the error messages are unhelpful, and the mental model required to fix mistakes isn't the same as the mental model for normal workflow. Flight rules act as a translation layer between what happened and what to type.

## Key points

- Organized as situation → solution rather than command → description — searchable by what went wrong, not by command name.
- Covers git rebase, git reflog, git reset, git cherry-pick, git stash — the recovery toolkit that most tutorials skip.
- git reflog is the escape hatch for most I lost my work disasters; this guide surfaces it prominently.
- Pairs well with Oh Shit, Git! for a more humorous take on the same recovery scenarios.
- Became one of the most-starred git references on GitHub — which itself signals how common these situations are.

[Original](https://github.com/k88hudson/git-flight-rules)
