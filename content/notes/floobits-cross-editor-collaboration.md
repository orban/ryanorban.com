---
title: "Floobits: Cross-Editor Real-Time Collaboration"
date: 2013-07-18
categories:
  - developer-tools
  - collaboration
  - editor
  - pair-programming
description: Floobits brought real-time multi-editor collaboration — like Google Docs for code — to Vim, Emacs, Sublime Text, and IntelliJ in 2013. A pre-cloud-IDE attempt to solve remote pair programming without forcing everyone onto the same editor.
params:
  source: pinboard
  sourceUrl: https://floobits.com/
---

## Summary

Floobits (2013) was a real-time collaborative coding platform that worked across different editors — Vim, Emacs, Sublime Text, and IntelliJ — via editor plugins. The value proposition: pair programming remotely without forcing both participants onto the same editor. You could be in Vim while your collaborator was in Sublime, and both would see each other's cursors and edits in real time, synchronized via the Floobits server.

This was the problem before cloud IDEs like Cloud9, Codeanywhere, and eventually GitHub Codespaces made the question moot by moving the entire environment to the browser. Floobits's insight was that editors are deeply personal — developers have years of muscle memory invested in their setup — and that forcing pair programming into one editor was a real adoption barrier.

The technical challenge was non-trivial: implementing operational transformation (or a similar CRDT-like consistency mechanism) across multiple editor plugins, each with different plugin APIs and concurrency models. Google Docs had cracked this for text documents; Floobits was doing it for code with multi-cursor awareness.

## Key points

- Synchronized multi-editor editing via plugins: each editor got its own plugin (Neovim, Emacs, Sublime, IntelliJ), all talking to a central Floobits server.
- Operational transformation for conflict resolution: edits from different users merged deterministically, like Google Docs but for code.
- Cursor awareness: you could see where your collaborator was looking and editing, the crucial feedback for effective pair programming.
- Predated the cloud IDE era — by 2016, Cloud9, Codeanywhere, and similar products made browser-native collaboration the dominant model.
- Floobits was eventually acquired and wound down as VS Code's Live Share extension solved the same problem with a larger installed base.

[Original](https://floobits.com/)
 → GitHub
