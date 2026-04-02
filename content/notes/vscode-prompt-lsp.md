---
title: "VS Code PR: LSP linting for AI prompt files"
date: 2026-02-13
categories:
  - developer-tools
  - vs-code
  - prompt-engineering
  - lsp
  - ai-agents
description: VS Code PR that adds LSP-based real-time linting for AI prompt files — flags weak instructions, ambiguity, XML structure issues, redundancy, template variable errors, and token budget problems. Like ESLint for prompts.
params:
  source: pinboard
  sourceUrl: https://github.com/microsoft/vscode/pull/294986
---

![VS Code PR: LSP linting for AI prompt files](/images/notes/vscode-prompt-lsp.png)

## Summary

This VS Code pull request by microsoft adds a Language Server Protocol (LSP) implementation specifically for AI prompt authoring files. The analogy is apt: just as ESLint provides real-time feedback on code quality as you type, this adds the same kind of static analysis feedback loop for writing AI instructions.

The linting runs in two layers. The static analysis layer fires on a 400ms debounce — fast enough to feel responsive — and checks for deterministic issues: weak language (\try to\, \consider\, \might\ flagged in favor of \Must\, \Always\, \Never\), ambiguous quantifiers (\several\, \"a few\"), structure issues (mixed XML/Markdown conventions, mismatched XML tags), redundancy (duplicate instructions, constraints that subsume each other), template variable errors (empty `{{}}` placeholders, undefined variables), and token budget warnings. The LLM-powered semantic layer uses Copilot to detect contradictions, persona inconsistencies, cognitive load issues, and coverage gaps.

This addresses a real pain point: prompt engineering is iterative and error-prone, but the feedback loop is usually a full model invocation away. A fast local linter that catches structural and clarity issues before you even test the prompt compresses that loop significantly. The feature targets CLAUDE.md, system prompts, agent instruction files — the text artifacts that define AI agent behavior.

## Key points

- LSP-based real-time linting for AI prompt files directly in VS Code.
- Two layers: fast static analysis (400ms debounce) + LLM-powered semantic analysis via GitHub Copilot.
- Static checks: weak language, ambiguity, XML structure, redundancy, template variables, token budget.
- Semantic checks: contradictions, persona inconsistencies, cognitive load, coverage gaps.
- Effectively brings ESLint-style developer experience to prompt engineering.

[Original](https://github.com/microsoft/vscode/pull/294986)
