---
title: How to Back Up Your Git Repositories
date: 2021-12-31
categories:
  - git
  - backup
  - devops
  - self-hosting
  - infrastructure
description: A Medium guide on backing up git repositories — covering bare clone strategy, rsync to external storage, and hosting your own Gitea/Gogs instance. Addresses the risk of losing code when hosting platforms go down or accounts get banned.
params:
  source: pinboard
  sourceUrl: https://threkk.medium.com/how-to-back-up-your-git-repositories-1298a4487a31
---

## Summary

Git repositories hosted on GitHub, GitLab, or Bitbucket are not safe by default — if your account is banned, the platform goes down, or the company changes policy, your code disappears. This Medium article by threkk covers strategies for maintaining your own backups independent of any single hosting platform.

The core technique: `git clone --bare` creates a bare repository (the internal git data without a working tree) that can be pushed to multiple remotes or stored locally. A cron job that `git fetch --all` from all remotes and pushes to a backup location (NAS, Backblaze B2, rsync target) keeps it current. For a complete self-hosted backup: Gitea or Gogs are lightweight self-hosted git servers that can mirror repos from GitHub automatically.

The article likely covers: bare clone vs normal clone for backups, git bundle for single-file archives, mirroring to a second hosting provider (GitHub → GitLab), scripted backup with rsync to local/cloud storage, and Gitea mirroring setup. The 3-2-1 backup principle applies: 3 copies, 2 different media, 1 offsite.

For most developers the risk is low but the consequence is high. Losing years of side projects because GitHub suspended an account is not theoretical — it happens due to payment failures, DMCA takedowns, or algorithm-flagged content. A weekly bare clone to a NAS or cloud bucket costs almost nothing in disk space.

## Key points

- `git clone --bare` + `git fetch --all` is the standard pattern for repository backups
- Gitea / Gogs: lightweight self-hosted git servers with automatic GitHub/GitLab mirroring built in
- git bundle: creates a single portable file containing the entire repository history
- Multiple remote strategy: push to both GitHub and GitLab simultaneously for passive redundancy
- cron job + rsync to local NAS or Backblaze B2 for simple, cheap offsite backup

[Original](https://threkk.medium.com/how-to-back-up-your-git-repositories-1298a4487a31)
