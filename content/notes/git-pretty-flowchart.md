---
title: Git Pretty — Recovery Flowchart
date: 2014-09-06
categories:
  - git
  - developer-tools
  - workflow
  - version-control
description: Justin Hileman's flowchart for deciding which git command to run when you're in a mess — a decision tree that starts with 'did you push?' and branches into the right cleanup command. The most-shared git recovery reference of its era.
params:
  source: pinboard
  sourceUrl: http://justinhileman.info/article/git-pretty/
---

## Summary

Justin Hileman's git pretty is a flowchart-style decision tree for recovering from common git mistakes. The premise: when you've made a mess of your git history, the right repair command depends on answers to a sequence of yes/no questions — did you push? did you commit? are you in the middle of a merge? The flowchart walks you through this decision tree to the correct command.

The common recovery scenarios the chart addresses: undoing the last commit (before and after push), amending a commit message, removing a file from a commit, discarding unstaged changes, recovering a deleted branch, squashing commits before push, and cleaning up a rebase gone wrong. Each scenario has the right `git` command, and the flowchart prevents the most dangerous mistake: running a destructive operation like `git push --force` or `git reset --hard` without understanding whether it will lose work.

This kind of reference has permanent utility because git's command vocabulary is large and the relationship between commands (cherry-pick vs. rebase, reset vs. revert, stash vs. WIP commit) is non-obvious. The flowchart encodes the decision logic that experienced git users have internalized.

## Key points

- Decision tree for git recovery: starts with did you push? — the key branch that determines safe vs. destructive options.
- `git reset --soft HEAD~1`: undo last commit, keep changes staged.
- `git reset --hard HEAD~1`: undo last commit, discard changes — dangerous after push.
- `git revert HEAD`: create a new commit that undoes the last one — safe for pushed commits.
- `git commit --amend`: rewrite last commit message or add forgotten files — only safe before push.
- git reflog: the escape hatch — shows every HEAD movement, lets you recover "lost" commits.

[Original](http://justinhileman.info/article/git-pretty/)
