---
title: "Starship: Cross-Shell Prompt"
date: 2022-09-18
categories:
  - cli
  - shell
  - tools
  - developer-tools
  - rust
description: Starship is a minimal, fast, infinitely customizable shell prompt written in Rust. Works across bash, zsh, fish, PowerShell — one config file covers all shells, and it shows contextual info like git status, language version, and cloud context without slowing down.
params:
  source: pinboard
  sourceUrl: https://starship.rs/
---

## Summary

Starship is a shell prompt written in Rust that works across every major shell — bash, zsh, fish, PowerShell, nushell, and more. The key selling point is speed: because it's compiled Rust rather than shell script, it adds minimal latency to prompt rendering even when displaying complex context like Git status, language versions, and cloud environment info.

Configuration lives in a single TOML file (`~/.config/starship.toml`) that applies everywhere regardless of which shell you're using. This is a significant ergonomic win if you work across multiple systems or switch shells — one config to maintain. The defaults are sensible and context-aware: the prompt auto-detects what information is relevant (showing Node version only in Node projects, Python version only in Python projects) and hides everything else.

Starship has become one of the most popular developer productivity tools precisely because it solves a genuine annoyance (shell prompt configuration is traditionally painful and fragile) with a well-engineered solution. It sits alongside Oh My Zsh and Oh My Fish as prompt customization tools, but is cross-shell and faster than script-based solutions.

## Key points

- Cross-shell prompt written in Rust — works in bash, zsh, fish, PowerShell, nushell.
- Single TOML config applies to all shells — one file to maintain.
- Context-aware: shows Git branch, language versions, cloud env only when relevant.
- Fast: compiled Rust adds ~1ms latency vs shell-script-based alternatives.
- Highly customizable — over 40 built-in modules, custom commands, color themes.
- Apache 2.0 license; community-maintained.

[Original](https://starship.rs/)
