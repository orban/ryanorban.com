---
title: "Claude Code Auto Dream: automated memory consolidation"
date: 2026-03-26
categories:
  - claude-code
  - memory
  - ai-agents
  - developer-tools
description: Auto Dream is Anthropic's memory consolidation feature for Claude Code — a four-phase process that runs after sessions to merge, deduplicate, and prune memory files. Think of it as automated housekeeping that keeps your AI's long-term memory from accumulating contradictions.
params:
  source: pinboard
  sourceUrl: https://claudefa.st/blog/guide/mechanics/auto-dream
---

![Claude Code Auto Dream: automated memory consolidation](/images/notes/auto-dream.png)

## Summary

[Auto Dream](/notes/auto-dream/) is Anthropic's built-in memory consolidation feature for Claude Code that automatically organizes and maintains memory files between sessions. It mirrors how REM sleep works in humans: experiences accumulate during the day, and a background process runs during rest to consolidate them into cleaner, more durable knowledge.

The system triggers automatically after 24 hours have passed *and* 5 or more sessions have occurred since the last consolidation. You can also trigger it manually by telling Claude to dream or consolidate my memory files. It runs in the background, non-blocking, with a lock file to prevent concurrent runs.

The consolidation process has four phases: Orientation (review existing memory structure), Gather Signal (search session transcripts for user corrections, explicit saves, and recurring patterns), Consolidation (merge information, convert relative dates to absolute dates, resolve contradictions, prune stale entries), and Prune and Index (update the MEMORY.md index, kept under 200 lines). During all of this, it has read-only access to project code — it only writes to memory files.

## Key points

- Runs after 24 hours AND 5+ sessions since last consolidation — two conditions must both be met, preventing over-eager consolidation after quiet days.
- Converts relative dates to absolute dates during consolidation, so memories stay interpretable months later.
- Removes contradictions and stale entries — without this, auto memory accumulates noise that actively confuses Claude Code over time.
- Lock file prevents concurrent execution; designed to run without blocking the user's active session.
- Manually triggerable with natural-language commands like "dream" or "consolidate my memory files."

[Original](https://claudefa.st/blog/guide/mechanics/auto-dream)
