---
title: "Cronboard: terminal dashboard for cron job management"
date: 2026-02-27
categories:
  - developer-tools
  - cron
  - terminal
  - sysadmin
  - open-source
description: Cronboard is a terminal dashboard for managing cron jobs locally and on remote servers over SSH. Built with Python/Textual, supports smart scheduling expressions and case-insensitive search.
params:
  source: pinboard
  sourceUrl: https://github.com/antoniorodr/cronboard
---

![Cronboard: terminal dashboard for cron job management](/images/notes/cronboard.png)

## Summary

[Cronboard](/notes/cronboard/) is a terminal-based dashboard for managing cron jobs on local machines and remote servers via SSH. Built with Python using the Textual framework, it wraps the crontab utility with a proper TUI interface — not just a thin CLI wrapper but an interactive dashboard with visible scheduling, search, and navigation.

The problem it addresses is the friction of managing cron jobs across multiple machines. Standard `crontab -e` opens a bare file editor with no visibility into when jobs last ran, when they're next scheduled, or any way to search across entries. Cronboard shows formatted last and next run times, supports standard cron syntax plus expressions like `@daily` and `@yearly`, and provides path autocompletion when configuring jobs.

For remote servers it connects via SSH — password or key auth, checks `~/.ssh/known_hosts` — and can manage jobs for different users with appropriate permissions. The search feature uses case-insensitive keyword matching across all defined jobs.

## Key points

- Terminal dashboard UI via Textual — interactive rather than just crontab editing in a text file.
- Remote server support via SSH (password or key auth) — manage cron jobs across multiple machines from one interface.
- Shows formatted last/next run times — immediate visibility into schedule state.
- Supports standard cron syntax plus `@daily`, `@weekly`, `@monthly`, `@yearly` shorthand expressions.
- Case-insensitive search across all jobs — findable by name or command.

[Original](https://github.com/antoniorodr/cronboard)
