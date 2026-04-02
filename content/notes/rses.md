---
title: "rses: cross-agent session handoff"
date: 2026-03-26
categories:
  - claude-code
  - ai-agents
  - developer-tools
  - context
description: rses lets you transfer a full session context — task, git diff, conversation history — between Claude Code, Codex CLI, and OpenCode. Useful when you want to pick up where one agent left off in a completely different tool.
params:
  source: pinboard
  sourceUrl: https://github.com/yazcaleb/rses
---

![rses: cross-agent session handoff](/images/notes/rses.png)

## Summary

[rses](/notes/rses/) is a CLI tool for transferring complete session context between Claude Code, Codex CLI, and OpenCode. The premise is that these tools store conversations differently — Claude Code uses JSONL files, Codex CLI uses SQLite — but they all contain enough structure to reconstruct what the agent was working on: the original task, git diffs, working tree status, and conversation history.

The tool reads from each agent's native storage location, extracts that context, and launches the target agent with a structured handoff prompt as its first message. You can filter by working directory and control how many conversation turns to include (default is 6, which captures enough back-and-forth without overwhelming the target agent's context window).

The practical use case is straightforward: you've been working with Claude Code and hit its context limit, or you want to switch to a cheaper model mid-session. `rses cc with cdx --last` hands the Codex session over to Claude Code with full context about what was happening. All parsers are read-only and designed to degrade gracefully if tool formats change.

## Key points

- Supports handoffs in any direction between Claude Code, Codex CLI, and OpenCode — three of the most common terminal AI coding agents.
- Extracts original task description, git diffs, working tree status, and recent conversation turns — not just the last message.
- `rses ls` shows available sessions across all installed tools, useful for reviewing what's been worked on recently.
- Requires Node.js 22+ and macOS/Linux; runs fully locally, no data leaves the machine.
- Includes `rses export` to stdout, making it composable with other tools in a pipeline.

[Original](https://github.com/yazcaleb/rses)
