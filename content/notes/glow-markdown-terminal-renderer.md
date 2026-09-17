---
title: "Glow: Markdown renderer for the terminal"
date: 2025-02-10
categories:
  - cli
  - markdown
  - developer-tools
  - terminal
  - charmbracelet
description: Glow renders Markdown beautifully in the terminal with syntax highlighting, styled headings, and an optional pager TUI — from Charmbracelet, the creators of Bubbletea. Makes README and docs files readable without leaving the terminal.
params:
  source: pinboard
  sourceUrl: https://github.com/charmbracelet/glow
---

![Glow: Markdown renderer for the terminal](/images/notes/glow-markdown-terminal-renderer.png)

## Summary

Glow renders Markdown files in the terminal with proper styling: formatted headings, code blocks with syntax highlighting, bold/italic text, tables, and links — rather than showing raw Markdown syntax. It's from Charmbracelet, the team behind Bubbletea, Lip Gloss, and other polished Go TUI tools.

Beyond basic rendering, Glow includes a TUI stash mode — a local library where you can save Markdown files for later reading, like a personal knowledge base viewer. The pager handles long documents with keyboard navigation. It can render from files, URLs, or stdin, making it composable with other tools (e.g., piping GitHub API output directly to glow).

For developers who read a lot of README files, documentation, and notes, Glow removes the annoyance of either switching to a browser or reading raw Markdown. In the same category as bat (syntax-highlighted cat) and delta (Git diff viewer) — terminal tools that make reading text more pleasant without changing the underlying workflow.

## Key points

- Renders Markdown with full styling in the terminal — headings, code blocks, tables, links.
- TUI stash mode for saving and browsing a local Markdown library.
- From Charmbracelet (Bubbletea, Lip Gloss ecosystem).
- Reads from files, URLs, or stdin — composable in pipelines.
- In the same family as bat and delta.

[Original](https://github.com/charmbracelet/glow)
