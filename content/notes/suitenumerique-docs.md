---
title: "Docs (suitenumerique): Open-Source Collaborative Editor"
date: 2025-03-16
categories:
  - collaboration
  - open-source
  - wiki
  - django
  - self-hosted
  - knowledge-management
description: Docs is an open-source collaborative text editor built with Django and React, designed as a Notion or Google Docs alternative for organizations that want self-hosted data ownership. MIT licensed, real-time with live cursors and offline editing, with optional AI writing assistance.
params:
  source: pinboard
  sourceUrl: https://github.com/suitenumerique/docs
---

![Docs (suitenumerique): Open-Source Collaborative Editor](/images/notes/suitenumerique-docs.png)

## Summary

Docs from La Suite Numérique is an open-source collaborative editor built with Django and React, targeting public organizations, companies, and open communities that want data sovereignty through self-hosting. The technical stack is Yjs for real-time sync and BlockNote.js for the block-based editing experience. MIT licensed.

The feature set covers the basics well: rich text and Markdown support, slash commands, block-based editing, live cursors, real-time comments, hierarchical subpages, search, and granular access controls. Import/export to `.docx`, `.odt`, `.md`, and `.pdf`. Offline editing with sync on reconnect. An optional AI writing assistance layer can rewrite, summarize, translate, and fix typos — but it's opt-in, not the product's core identity.

The La Suite Numérique project is the French government's open-source software suite for public administration, analogous to what Germany has done with Nextcloud. This means Docs has institutional backing and real production usage in government contexts — it's not just a hobby project. The comparison to Notion or Outline is accurate: it's a knowledge wiki / collaborative editor, not a specialized tool. The self-hostable, MIT-licensed, government-backed combination makes it a credible option for organizations with compliance requirements that rule out US cloud services.

## Key points

- Open-source collaborative editor: Django + React + Yjs + BlockNote.js.
- Real-time collaboration with live cursors, offline editing, hierarchical subpages.
- Import/export: `.docx`, `.odt`, `.md`, `.pdf`.
- Self-hosted via Docker or Kubernetes; MIT licensed.
- Backed by the French government's La Suite Numérique open-source suite.
- Optional AI writing assistance (rewrite, summarize, translate) — not the core feature.

[Original](https://github.com/suitenumerique/docs) → GitHub
