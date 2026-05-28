---
title: "Webwright: AI-Powered Shell for Building and Running Software"
date: 2024-07-19
categories:
  - ai-tools
  - cli
  - developer-tools
  - natural-language
  - shell
description: Webwright is a natural language shell that translates conversational input into executable commands — three modes (shell, NL, AI agent) with file references and clipboard integration. A terminal that understands intent.
params:
  source: pinboard
  sourceUrl: https://github.com/MittaAI/webwright
---

![Webwright: AI-Powered Shell for Building and Running Software](/images/notes/webwright.png)

## Summary

[Webwright](/notes/webwright/) is a terminal shell by MittaAI that understands natural language alongside traditional commands. Rather than being a chatbot bolted onto a shell, it's designed as a shell-first tool where NL is just another input mode. Three modes: standard shell execution, natural language mode that translates conversational input into shell commands, and AI mode for complex multi-step tasks using 30+ built-in tools.

The transparency design is notable: generated commands are shown before execution, so you always know what's about to run. Input can reference files with `@file.py` syntax or pull from clipboard with `{clipboard}` — making it easy to give the AI context without copy-paste. Unix pipes work normally, so it composes with existing tooling rather than replacing it.

The key claim is determinism: identical inputs produce identical outputs. That's a meaningful constraint for a shell tool, where unexpected behavior is a real cost. [Webwright](/notes/webwright/) sits in the same space as Warp (terminal with AI), aider (AI coding assistant in terminal), and GitHub Copilot CLI — but with the explicit goal of being a complete shell replacement rather than a code completion overlay.

## Key points

- Three modes: traditional shell, natural language (default), AI agent with 30+ tools.
- Commands shown before execution — transparent, predictable behavior.
- `@file.py` references and `{clipboard}` interpolation for easy context injection.
- Pipes with Unix tools — composes rather than replaces existing tooling.
- Deterministic: identical inputs produce identical outputs.
- Built by MittaAI, positioned as an AI-native shell for software development workflows.

[Original](https://github.com/MittaAI/webwright) → GitHub
