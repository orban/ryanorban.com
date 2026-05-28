---
title: "Dance: Kakoune-Style Editing for VS Code"
date: 2022-01-18
categories:
  - editor
  - vscode
  - kakoune
  - modal-editing
  - developer-tools
description: Dance is a VS Code extension that brings Kakoune-style modal editing — selection-first multiple cursors, custom modes, scripting via JavaScript, and pipe/expression support. The option for developers who want Kakoune ergonomics without leaving VS Code.
params:
  source: pinboard
  sourceUrl: https://github.com/71/dance
---

![Dance: Kakoune-Style Editing for VS Code](/images/notes/dance-vscode-kakoune.png)

## Summary

Dance is a VS Code extension that brings Kakoune-inspired modal editing to VS Code without requiring you to fully switch editors. Where Vim extensions for VS Code (VSCodeVim) try to replicate Vim's key bindings faithfully, Dance takes Kakoune's selection-first paradigm and implements it as a VS Code-native extension — using VS Code's built-in multi-cursor functionality rather than emulating a different editor.

The key conceptual shift from Vim: in Kakoune-style editing, you select first and then act, rather than Vim's verb-object model (act then move). This makes the current selection always visible before you commit to an action, which reduces errors from misjudged motions. Dance adds custom editing modes (normal, insert, and user-definable), scripting via the `dance.run` command that exposes the Dance API for advanced operations, pipe support (run shell commands on selected text), and regex-based transformations.

The extension also supports Helix-compatible keybindings, reflecting the convergence of both editors on the selection-first model. This makes Dance useful as a middle ground: Kakoune and Helix ergonomics, VS Code ecosystem (extensions, IntelliSense, debugger). The tradeoff compared to actually switching to Helix is that VS Code's architecture means some Kakoune operations that are native in Helix require scripting workarounds in Dance.

## Key points

- Selection-first editing: selections are always visible before you commit to an action — reduces errors vs. Vim's verb-object model.
- Uses VS Code's native multi-cursor rather than emulating a foreign editor — better integration with VS Code features.
- `dance.run` command exposes the Dance API for JavaScript scripting — custom operations beyond standard key bindings.
- Supports Helix-compatible keybindings — both Dance and Helix converge on the Kakoune selection model.
- Related: Helix editor (terminal, built-in LSP/tree-sitter), Kakoune (the original inspiration for both).

[Original](https://github.com/71/dance) → GitHub
