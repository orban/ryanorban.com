---
title: "Legit: Git Workflow for Humans"
date: 2012-08-03
categories:
  - git
  - developer-tools
  - workflow
  - cli
  - open-source
description: "Legit is a Python-based git extension by Kenneth Reitz that wraps git branch management in more human-friendly commands. It fills a real gap: git's branch model is powerful but the command interface is notoriously user-hostile."
params:
  source: pinboard
  sourceUrl: http://www.git-legit.org/
---

![Legit: Git Workflow for Humans](/images/notes/legit-git-workflow.png)

## Summary

Legit is a git extension by Kenneth Reitz (author of the Requests library) that adds a more human-oriented layer to git branch management. The core problem it addresses: git's internal model is sound, but the CLI surface is designed around plumbing rather than developer intent. You end up memorizing incantations (`git checkout -b`, `git push --set-upstream origin <branch>`) for operations that are conceptually simple.

Legit introduces branch-centric commands that map to what you actually mean: `git feature <name>` creates a topic branch and switches to it; `git sync` pulls and pushes the current branch; `git publish` pushes a branch to origin and tracks it; `git unpublish` removes a remote branch; and `git switch <branch>` does a clean context switch (stashing if needed). The result is a workflow vocabulary that reads more like intent than git internals.

This was part of a broader 2012 pattern of tools trying to make git more ergonomic — alongside GitHub's own GUI clients and Atlassian's SourceTree. The interesting question at the time was whether these abstractions would become standard or whether developers would just learn git. For the most part, git won: its commands are now widely known and tooling like zsh completions reduced the friction enough that wrapper tools largely faded.

## Key points

- `git feature <name>` / `git feature -d <name>`: create and delete topic branches — the common case, made simple.
- `git switch <branch>`: stash current work, switch branches, pop stash — a safe single command for context switching.
- `git sync`: synchronize the current branch with its remote, handling both pull and push.
- `git publish` / `git unpublish`: manage remote tracking with human-readable commands instead of `push --set-upstream`.
- Kenneth Reitz applied the same beautiful API for humans philosophy from Requests to git workflow — consistent with his design aesthetic.

[Original](http://www.git-legit.org/)
