---
title: "roborev: continuous code review for AI agent commits"
date: 2026-02-06
categories:
  - ai-agents
  - code-review
  - developer-tools
  - git
  - coding-agent
description: "roborev automatically reviews every commit an AI coding agent makes via git hooks, accumulating findings in a persistent queue. The problem it solves: agents write fast but move on before reviewing their own mistakes."
params:
  source: pinboard
  sourceUrl: https://www.roborev.io/
---

![roborev: continuous code review for AI agent commits](/images/notes/roborev.png)

## Summary

[roborev](/notes/roborev/) is a code review tool designed specifically for the output of AI coding agents. The problem it targets is precise: agents write code quickly, commit it, and move on — but they don't look back. Mistakes made in one session get buried under subsequent changes before anyone reviews them. [roborev](/notes/roborev/) runs automatically on every commit via git hooks, queuing findings immediately while the context is still fresh.

The interface is a terminal UI (`roborev tui`) that accumulates review findings into a persistent queue. The queue doesn't close until you explicitly resolve items, applying a different discipline than typical review workflows that let findings slip. Works with Claude Code, Codex, Gemini, Copilot, and other major coding agents. Findings can be piped directly back into agent sessions or applied via a `/roborev-fix` skill.

This occupies an interesting niche: not a human code review replacement, but a feedback loop specifically for vibe coding workflows where humans are directing rather than writing. The analysis covers duplication, complexity, refactoring opportunities, test gaps, and dead code — standard static analysis concerns, but applied continuously to agent output rather than on demand.

## Key points

- Reviews every AI agent commit automatically via git hooks — no manual invocation.
- Persistent review queue in terminal UI: findings accumulate until explicitly resolved.
- Works with Claude Code, Codex, Gemini, Copilot, and other coding agents.
- `/roborev-fix` skill lets agents apply fixes directly from review findings.
- Runs locally — no external services or infrastructure required.
- Covers duplication, complexity, refactoring, test gaps, and dead code detection.

[Original](https://www.roborev.io/)
