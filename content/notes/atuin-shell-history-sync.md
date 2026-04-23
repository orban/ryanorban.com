---
title: "Atuin: shell history as a searchable, synced database"
date: 2025-02-10
categories:
  - developer-tools
  - shell
  - cli
  - productivity
  - sync
description: Atuin replaces shell history with a searchable SQLite database that syncs across machines, with fuzzy search, context-aware filtering (host, directory, exit code), and end-to-end encrypted sync. A meaningful upgrade over the default shell history experience.
params:
  source: pinboard
  sourceUrl: https://atuin.sh/
---

![Atuin: shell history as a searchable, synced database](/images/notes/atuin-shell-history-sync.png)

## Summary

Atuin replaces the default append-only shell history file with a SQLite database, enabling rich querying, cross-machine sync, and context-aware search. The standard shell history (`~/.bash_history`, `~/.zsh_history`) loses metadata — you can't filter by exit code, working directory, or hostname. Atuin stores all that alongside each command, making it possible to search "what did I run successfully in this project directory last week?"

The sync is end-to-end encrypted — commands are encrypted on-device before upload. Atuin offers a hosted sync server and the option to self-host. The fuzzy search replaces Ctrl+R with a full-screen TUI showing commands with timestamps, duration, directory context, and exit codes. Filtering by host or directory makes it practical to maintain separate command histories for different machines without losing shared context.

Atuin has become a standard tool in the terminal-power-user stack, alongside tools like zoxide, fzf, and starship. It works with bash, zsh, fish, and nushell. Installation is a single script; the database is portable and can be imported from existing history files.

## Key points

- Replaces shell history with a SQLite database storing commands + metadata (exit code, directory, duration, hostname).
- Cross-machine sync with end-to-end encryption — hosted or self-hosted.
- Context-aware search: filter history by host, directory, exit code, time range.
- Replaces Ctrl+R with a full-screen TUI fuzzy search.
- Supports bash, zsh, fish, nushell.
- Portable database format with import from existing history files.

[Original](https://atuin.sh/)
