---
title: "Helix: Post-Modern Terminal Editor"
date: 2022-01-18
categories:
  - editor
  - terminal
  - rust
  - vim
  - kakoune
  - tree-sitter
  - developer-tools
description: Helix is a post-modern terminal text editor written in Rust — Kakoune-inspired multiple selections, built-in LSP and tree-sitter support, no plugin system needed. The editor that ships batteries included, unlike Neovim which requires substantial configuration to reach the same point.
params:
  source: pinboard
  sourceUrl: https://helix-editor.com/
---

![Helix: Post-Modern Terminal Editor](/images/notes/helix-editor.png)

## Summary

Helix is a terminal text editor written in Rust that positions itself as post-modern — meaning it learns from Vim and Kakoune and makes breaking changes where the old design is wrong. Built from scratch rather than as a fork, it has the freedom to make different defaults and a smaller codebase.

The key design difference from Vim is the selection model. Helix uses multiple selections as a first-class primitive, borrowed from Kakoune: selections come before actions (select, then do), rather than actions coming before motions (verb-object). This inversion is subtle but changes how you think about text editing. Tree-sitter integration provides error-tolerant syntax trees that enable more accurate highlighting, navigation by syntax node, and code folding than regex-based approaches.

The batteries-included philosophy is the main practical selling point over Neovim: Helix ships with built-in LSP support (autocompletion, diagnostics, go-to-definition, hover docs), fuzzy finder, project-wide search, bracket pairing, and theming — no plugin configuration needed to reach a functional IDE-equivalent setup. The tradeoff is no plugin system yet, which limits extensibility but also eliminates configuration drift. For users who want Vim-like editing without 200 lines of `init.lua`, Helix is the answer.

## Key points

- Multiple selections as first-class primitive (Kakoune-inspired): select then act, rather than Vim's act then move.
- Tree-sitter for syntax trees: more accurate highlighting, structural navigation, and code-aware operations than regex patterns.
- Built-in LSP support — no plugins needed for autocompletion, diagnostics, go-to-definition.
- No plugin system yet (planned) — opinionated by design; batteries included avoids configuration overhead.
- Written in Rust from scratch — smaller, faster, modern codebase compared to Neovim.
- Related: Dance VS Code extension for Kakoune-style editing in VS Code.

[Original](https://helix-editor.com/)
