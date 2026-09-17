---
title: "Pi Messenger: file-based multi-agent coordination for Pi"
date: 2026-02-06
categories:
  - ai-agents
  - multi-agent
  - coordination
  - pi-coding-agent
  - open-source
description: Pi Messenger turns multiple AI coding agents in different terminals into a chat room — agents can see who's online, claim tasks, reserve files, and send messages. Coordination via plain files, no daemon required.
params:
  source: pinboard
  sourceUrl: https://github.com/nicobailon/pi-messenger
---

![Pi Messenger: file-based multi-agent coordination for Pi](/images/notes/pi-messenger.png)

## Summary

[Pi Messenger](/notes/pi-messenger/) is an extension for the Pi coding agent that lets multiple agent instances running in different terminals communicate as if they're in a shared workspace. Agents can see who's online, what each is working on, claim tasks, reserve files, and send messages to each other — a multi-agent coordination layer built entirely on the filesystem with no daemon, no server, no infrastructure.

The design philosophy is intentionally minimal: coordination happens through shared files in a common directory. This makes it trivially deployable (just `pi install npm:pi-messenger`) while supporting the core use case of multiple Pi agents working on the same project without stepping on each other. Task claiming and file reservation prevent conflicts; the presence system shows what each agent is doing.

[Pi Messenger](/notes/pi-messenger/) ships with crew agents — domain-specific personas stored in `crew/agents/*.md` and auto-discovered at install. Workers can load additional crew skills on demand during execution. This pattern (a small set of specialized agents that can be dynamically loaded) resembles multi-agent routing in more complex frameworks, but implemented at near-zero complexity via Markdown files and file I/O.

## Key points

- File-based multi-agent coordination — no daemon, no server, just shared filesystem.
- Agents can broadcast presence, claim tasks, reserve files, and message each other.
- Extension for Pi coding agent — install with a single command.
- "Crew agents" (`crew/agents/*.md`) auto-discovered; workers load domain skills on demand.
- Enables parallel agent workflows on the same codebase without manual conflict management.

[Original](https://github.com/nicobailon/pi-messenger)
