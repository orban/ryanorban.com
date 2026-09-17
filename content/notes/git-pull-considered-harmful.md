---
title: Why is
date: 2014-03-12
categories:
  - git
  - developer-tools
  - version-control
  - workflow
description: Stack Overflow thread on why git pull creates problems in divergent branches — advocates for git pull --rebase or a fast-forward-only alias instead. A workflow habit that eliminates unnecessary merge commits from shared history.
params:
  source: pinboard
  sourceUrl: http://stackoverflow.com/questions/15316601/why-is-git-pull-considered-harmful
---

`git pull` Considered Harmful?

## Summary

`git pull` is shorthand for `git fetch` followed by `git merge` — and the merge step is the problem. When your branch has diverged from the remote, `git pull` creates a merge commit to reconcile the two histories. In a shared repo with multiple contributors, this fills the git log with noise commits like Merge branch 'main' of ... that carry no information and make `git bisect` and history reading harder.

The recommended alternative is `git pull --rebase`, which replays your local commits on top of the fetched remote state instead of creating a merge commit. The result is a linear history that reads like commits actually happened in sequence. Even safer is `git pull --ff-only`, which fails rather than create a merge commit — forcing you to decide explicitly how to integrate diverged branches.

The content here records a practical alias: `git config --global alias.up 'pull --ff-only --all -p'`. Breaking it down: `--ff-only` refuses to merge, `--all` fetches from all configured remotes, and `-p` (prune) removes tracking branches for remote branches that no longer exist. This alias makes the safe behavior the default while keeping the full remote picture current.

## Key points

- `git pull` = `git fetch` + `git merge`: the merge creates a commit even when there's nothing to resolve.
- Spurious merge commits clutter git log and confuse tools like git bisect that rely on linear-ish history.
- `git pull --rebase` produces a clean linear history; `git pull --ff-only` is stricter — it fails if a rebase or merge would be needed.
- The alias `git up = pull --ff-only --all -p` makes the safe path the default: fetch all remotes, refuse to auto-merge, prune stale tracking branches.
- Downstream: teams that adopt git rebase discipline typically also use feature branches and squash commits before merging.

[Original](http://stackoverflow.com/questions/15316601/why-is-git-pull-considered-harmful)
