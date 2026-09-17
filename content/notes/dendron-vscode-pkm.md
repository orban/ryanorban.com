---
title: "Dendron: VS Code Personal Knowledge Management"
date: 2021-01-25
categories:
  - pkm
  - knowledge-management
  - vscode
  - note-taking
  - developer-tools
description: Dendron is a VS Code-native personal knowledge management system built around hierarchical note organization with dot-notation (e.g. 'project.backend.api'). It's designed for developers who want their notes to live in their editor with Git-based sync and structured linking.
params:
  source: pinboard
  sourceUrl: https://dendron.so/
---

## Summary

Dendron is a personal knowledge management (PKM) system built as a VS Code extension, designed specifically for developers. Its defining feature is hierarchical note organization using dot-notation: a note named `project.backend.api` is a child of `project.backend`, which is a child of `project`. This creates a deterministic, navigable structure rather than the flat-plus-tags approach of tools like Roam Research or the folder-based approach of Obsidian.

The architecture is Git-native: notes live as plain Markdown files in a directory, versioned and synced via Git. This appeals to developers who are uncomfortable with proprietary sync services and want their knowledge base to be readable tooling-independently. Dendron also includes schema validation — you can define what fields a note type should have — which makes it more structured than most PKM tools.

Compared to Obsidian, Dendron is more opinionated and developer-focused. The VS Code integration means you get code highlighting, terminal access, and your existing keybindings in the same tool where you take notes. The hierarchy-first approach forces more upfront organization but makes the structure more navigable at scale. Dendron saw significant early adoption among software engineers who found Roam Research's graph-first model too unstructured.

## Key points

- Hierarchical dot-notation organization (`project.area.topic`) enforces predictable structure — notes can't be ambiguously placed.
- Git-native: plain Markdown files, no proprietary sync, version history via standard tooling.
- VS Code extension: notes live in your editor alongside your code, with all extensions available.
- Includes schema validation for note types — can enforce required frontmatter fields per hierarchy level.
- Competes with Obsidian (graph-based, folder-native) and Roam Research (flat + backlinks); Dendron is the most structured of the three.

[Original](https://dendron.so/)
