---
title: "Onlook: Open-Source Visual Editor for React"
date: 2024-07-25
categories:
  - react
  - visual-editor
  - open-source
  - developer-tools
  - design
description: Onlook is an open-source visual editor for React that lets you edit your running app and writes changes back to code in real-time — Webflow-style design control for your own codebase, without leaving the local-first desktop environment.
params:
  source: pinboard
  sourceUrl: https://onlook.dev/
---

![Onlook: Open-Source Visual Editor for React](/images/notes/onlook.png)

## Summary

[Onlook](/notes/onlook/) is an open-source desktop application that lets you visually edit a running React app and write those changes back to code in real-time. The pitch: the design flexibility of Webflow applied to your own codebase. You click on elements in a rendered view, modify them visually, and the corresponding React component code updates automatically.

The local-first framing matters — it's not a cloud tool or a plugin; it runs as a desktop app against your local development server. The design-to-code pipeline is the core innovation: changes made visually aren't written to some intermediate representation, they're written directly to your TypeScript/JavaScript source files. This is closer to what Figma's developer handoff workflow aspires to than what it actually delivers.

[Onlook](/notes/onlook/) is an early-stage answer to a persistent pain point: the disconnect between design tools and production code. Most design systems require manually translating Figma changes into code; Onlook eliminates that translation step by making the code itself the editable artifact. For React developers who work with designers, this could meaningfully reduce back-and-forth. The open-source release means the community can extend it for specific frameworks and component libraries.

## Key points

- Visual editor that targets your running React app and writes changes back to source code.
- Local-first desktop app — no cloud, no plugin, runs against your local dev server.
- Targets React + TypeScript/JavaScript codebases; preserves component structure.
- Bridges the design-to-code gap that Figma handoff doesn't fully solve.
- Open-source — community can extend for specific component libraries or frameworks.
- Described as "the power of Webflow for your own app."

[Original](https://onlook.dev/)
