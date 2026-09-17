---
title: "How to Fix Low-Code: With More Code"
date: 2022-12-03
categories:
  - low-code
  - internal-tools
  - developer-tools
  - product
  - software-engineering
description: Airplane's argument that low-code platforms fail because they try to eliminate code entirely rather than eliminating the wrong kinds of code — proposing a hybrid model where code handles logic while low-code handles layout and permissions. An honest critique from a developer tools company with skin in the game.
params:
  source: pinboard
  sourceUrl: https://www.airplane.dev/blog/how-to-fix-low-code-with-more-code
---

## Summary

This Airplane blog post argues that no-code/low-code platforms fail in practice because they try to eliminate code entirely rather than eliminating the *right kinds* of code. The critique: the hard part of internal tools isn't writing SQL queries or wiring API calls — it's building the UI, handling permissions, managing state, and deploying. Low-code platforms eliminate the easy parts (code) while often requiring just as much work for the hard parts (wiring logic together in a graphical environment that's harder to version, debug, and maintain than code).

The alternative Airplane proposes is a hybrid: let developers write code for logic (which they're good at and prefer), while providing low-code infrastructure for the boilerplate — the CRUD table, the form that submits to an API, the approval flow, the audit log, the permissions system. This is Airplane's own product positioning, but the diagnosis is reasonably sharp. The same critique applies to tools like Zapier for complex automation: they work for simple flows but accumulate technical debt in graph form once conditions and branches multiply.

The content from the bookmark includes the setup: low-code platforms let you build customer-facing apps with reduced code and internal tools for reading/writing data. The failure mode happens at complexity — once your internal tool needs custom business logic, the graphical environment becomes the limiting factor. Airplane (acquired by Airtable in 2023) positioned itself as the code-friendly internal tools platform that solved exactly this. The same tension shows up in Retool, Appsmith, Budibase, and other internal tools builders.

## Key points

- Low-code platforms eliminate the easy parts (writing code) while the hard parts (logic, permissions, deployment) remain difficult.
- The right fix: keep code for logic, provide low-code for boilerplate (CRUD, forms, audit logs, permissions).
- Airplane's product positioning: developer-friendly internal tools that don't require fully custom UI.
- Complexity cliff: simple low-code flows work well; once branching logic arrives, graphical editors become technical debt.
- Same critique applies to Zapier (for automation) and Retool/Appsmith/Budibase (for internal tools).
- Airplane was acquired by Airtable in 2023.

[Original](https://www.airplane.dev/blog/how-to-fix-low-code-with-more-code)
