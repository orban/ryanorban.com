---
title: "Git Organized: A Better Git Flow"
date: 2022-01-19
categories:
  - git
  - workflow
  - engineering-practices
  - version-control
description: "A simple git workflow improvement: make changes freely on a branch with WIP commits, then git reset to the branch point and recommit in logically grouped chunks before opening a PR. Separates the messy work of development from the clean artifact of a review-ready commit history."
params:
  source: pinboard
  sourceUrl: https://render.com/blog/git-organized-a-better-git-flow
---

![Git Organized: A Better Git Flow](/images/notes/git-organized-better-git-flow.png)

## Summary

This post from the Render blog proposes a small workflow change that meaningfully improves pull request quality: separate the act of making changes from the act of organizing commits. Work freely on a feature branch with informal WIP commits, then use `git reset` back to the branch point (which unstages everything while preserving your working directory changes), and recommit the work in logically grouped, clean chunks.

The problem this solves is the common PR failure mode: commits that are technically "working" but interleave unrelated changes, or leave the codebase in broken states between commits. This makes the history hard to review, hard to bisect, and risky to revert (reverting a commit that contains multiple unrelated changes creates unexpected consequences).

The approach is low-tech — `git reset` + `git add --patch` for fine-grained staging of partial file changes. It requires no special tooling, no rebase gymnastics, just a mental model shift: the working branch is scratch space; the final commit history is the deliverable. The cost is one extra step before opening a PR; the benefit is a history that reads like a coherent explanation of the change rather than a recording of how you discovered it.

## Key points

- Workflow: commit freely with WIP messages → `git reset <branch-point>` → recommit in logical chunks with clean messages.
- `git add --patch` stages partial file changes — commit the refactor separately from the bug fix even if they touch the same file.
- Clean commit history enables safe, targeted reverts and clear PR reviews — a deliverable, not just a record.
- No special tooling needed: `git reset --soft` or `git reset` (mixed mode) both work.
- Related: conventional commits, git bisect (clean history makes bisect fast and accurate).

[Original](https://render.com/blog/git-organized-a-better-git-flow)
