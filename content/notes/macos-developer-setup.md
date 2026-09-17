---
title: MacOS Developer Setup
date: 2023-06-30
categories:
  - macos
  - developer-tools
  - setup
  - terminal
  - dotfiles
description: Chris @ Machine's macOS developer setup guide — covering Homebrew, Nerd Fonts, terminal configuration, and the foundational tooling for a productive development environment on macOS. A practical reference for setting up a new machine.
params:
  source: pinboard
  sourceUrl: https://www.chrisatmachine.com/posts/01-macos-developer-setup
---

![MacOS Developer Setup](/images/notes/macos-developer-setup.png)

## Summary

This guide by Chris (chrisatmachine.com, known for Neovim configuration content) covers setting up a productive macOS development environment from scratch. The setup covers Homebrew as the package manager foundation, Nerd Fonts for terminal and editor icon support, terminal configuration (typically iTerm2 or Alacritty with Zsh and Oh My Zsh), and the foundational tooling that makes the rest of the stack possible.

The guide reflects the conventions of a terminal-centric developer workflow: a well-configured terminal replaces the need for most GUI tools, a good font with icon support makes Neovim and terminal multiplexers like tmux or Wezterm much more pleasant, and Homebrew provides reproducible installation of everything from command-line tools to GUI applications via Homebrew Cask.

The Nerd Fonts dependency is particularly specific to terminal-heavy workflows: file icons in Neovim (via nvim-tree or similar), git symbols in status lines (lualine, starship), and branch indicators in shell prompts all depend on the extra icon codepoints that Nerd Fonts include alongside standard characters. Without the right font, these symbols render as boxes. Chris is primarily known in the Neovim community, so the guide is implicitly oriented toward that editor ecosystem.

## Key points

- Homebrew: foundational macOS package manager — installs CLI tools and GUI apps (Homebrew Cask).
- Nerd Fonts: fonts patched with icon codepoints — essential for file icons and prompt symbols in terminal workflows.
- Terminal emulator choice: iTerm2 (feature-rich), Alacritty (fast, GPU-rendered), Wezterm (Lua config).
- Shell setup: Zsh + Oh My Zsh or Starship prompt — git status, virtualenv, directory in the prompt.
- The guide is oriented toward Neovim users — assumes a terminal-first development workflow.
- Homebrew `brew bundle` + Brewfile: reproducible setup — document your installed packages for new machine setup.

[Original](https://www.chrisatmachine.com/posts/01-macos-developer-setup)
