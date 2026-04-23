---
title: "Dotfiles: Neovim + tmux + Ghostty"
date: 2025-08-20
categories:
  - dotfiles
  - neovim
  - tmux
  - ghostty
  - developer-tools
description: Dotfiles for a focused development workflow using Neovim (Lua/LSP), tmux, and Ghostty terminal — notably includes CUDA support for clangd without a local toolkit. Philosophically oriented around distraction-free deep work after forming a mental model.
params:
  source: pinboard
  sourceUrl: https://github.com/sumitdotml/dotfiles
---

![Dotfiles: Neovim + tmux + Ghostty](/images/notes/sumitdotml-dotfiles.png)

## Summary

This dotfiles repository by sumitdotml configures a focused development environment built around three tools: Neovim with a Lua-based configuration and LSP support, tmux for session management, and Ghostty as the terminal emulator. The workflow is intentionally minimal, described by the author as being "for when I've finished creating a mental model of how I want to do something" — a distraction-free mode distinct from exploratory work in Cursor or similar tools.

The Neovim config includes a notable CUDA development setup: clangd diagnostics for `.cu` files work even without a local CUDA toolkit installed — useful for working on GPU code on machines where the toolkit isn't available. A todo manager plugin integrates with `notes/todo.md` in the project root.

The broader philosophy is gradual consolidation: using specialized tools for learning and exploration (like Cursor Chat), but progressively pulling capabilities into Neovim as workflows mature. This represents a common pattern in developer tooling: start with high-level tools that scaffold decisions, then move toward more deliberately configured environments as defaults become constraints.

## Key points

- Three-tool stack: Neovim (Lua/LSP) + tmux + Ghostty terminal.
- CUDA clangd diagnostics without local toolkit — useful for GPU development.
- Philosophy: distraction-free workflow engaged after forming a mental model.
- Gradual consolidation from Cursor/high-level tools into deliberate Neovim config.
- Todo manager plugin using `notes/todo.md` in project root.
- Modular Lua config architecture.

[Original](https://github.com/sumitdotml/dotfiles) → GitHub
