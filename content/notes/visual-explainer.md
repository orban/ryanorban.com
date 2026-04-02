---
title: "visual-explainer: HTML pages instead of ASCII art from agents"
date: 2026-02-17
categories:
  - ai-agents
  - developer-tools
  - claude-code
  - visualization
  - html-generation
description: visual-explainer is a Claude Code agent skill that generates styled HTML pages instead of ASCII art for diagrams, diff reviews, architecture overviews, and data tables. Fixes the terminal readability problem for complex agent output.
params:
  source: pinboard
  sourceUrl: https://github.com/nicobailon/visual-explainer
---

![visual-explainer: HTML pages instead of ASCII art from agents](/images/notes/visual-explainer.png)

## Summary

[visual-explainer](/notes/visual-explainer/) is an AI agent skill by nicobailon that replaces the default ASCII art output of coding agents with styled, self-contained HTML pages. The problem it addresses is concrete: when you ask an agent to draw a diagram or compare a table of requirements, it defaults to box-drawing characters and pipe-and-dash tables that wrap and break in the terminal. Anything beyond a trivial case becomes unreadable.

The skill works with Claude Code, OpenAI Codex, and Pi. It intercepts requests for diagrams, diffs, architecture overviews, plan reviews, and data tables — and instead generates HTML with real typography, Mermaid diagrams with zoom/pan, dark/light themes, and no build step. The agent activates it automatically when output complexity crosses a threshold (4+ row tables, 3+ column comparisons). The output is a self-contained HTML file that opens in the browser.

The commands cover the main use cases: `/generate-web-diagram`, `/diff-review` (visual comparison with code review), `/plan-review` (plan vs. codebase), `/project-recap` (context-switching snapshot), `/fact-check` (document accuracy against code), `/generate-slides`, and `/share` (deploy to Vercel). The slide deck mode is a notable extension — any scrollable page can be rendered as a slide deck via `--slides`.

## Key points

- Replaces ASCII art and terminal tables with styled self-contained HTML pages — real typography, Mermaid diagrams, dark/light themes.
- Auto-activates for complex output (4+ rows, 3+ columns) without explicit invocation.
- Supports Claude Code (plugin marketplace), OpenAI Codex, and Pi.
- Key commands: `/diff-review`, `/plan-review`, `/project-recap`, `/fact-check`, `/generate-web-diagram`.
- `--slides` flag converts any output to a slide deck.
- `/share` deploys HTML pages to Vercel for a live URL.

[Original](https://github.com/nicobailon/visual-explainer)
