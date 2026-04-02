---
title: "Claude Interactive Documentation Workflow: markdown before code"
date: 2026-02-01
categories:
  - claude-code
  - documentation
  - developer-tools
  - workflow
  - methodology
description: "A structured interview-to-implementation workflow using Claude Code: document first, then code. The methodology produces specs that keep LLMs guardrailed and documentation that doesn't require clarifying questions."
params:
  source: pinboard
  sourceUrl: https://github.com/tobieapb/claude-interactive-documentation-workflow
---

![Claude Interactive Documentation Workflow: markdown before code](/images/notes/claude-doc-workflow.png)

## Summary

Claude Interactive Documentation Workflow captures a methodology for working with Claude Code that inverts the typical code first approach: interview → documentation → plan → implementation. The author summarizes it simply: "I used to whiteboard, then code. Now I markdown, then code." The resulting documentation serves as a living spec that keeps agents guardrailed and makes their output understandable six months later.

The workflow has four explicit stages with quality gates at each. The interview stage elicits requirements through structured conversation. Documentation turns those requirements into unambiguous specs — "documentation that doesn't require clarifying questions." Planning converts specs into implementation plans any competent developer (or agent) can execute. Implementation is then done against the plan, with the documents providing ongoing context to the LLM.

What makes this interesting isn't the workflow itself (document-before-code has a long history) but the application to AI coding specifically. The canonical documentation files serve as extremely efficient context window use — a well-structured spec gives Claude Code immediate, complete context without requiring it to infer intent from code or comments. The author reports this was used across 3+ production projects over 4 months.

## Key points

- Interview → documentation → plan → implementation: specification before execution.
- Documentation produces unambiguous specs that eliminate LLM clarifying question loops.
- Each stage has explicit quality gates — prevents ambiguity from becoming technical debt.
- Documentation files serve as efficient Claude Code context: complete intent without inference.
- Validated in production: maritime tracking, CV pipeline, database systems over 4 months.
- The docs remain valuable as human-readable project history after the project ships.

[Original](https://github.com/tobieapb/claude-interactive-documentation-workflow)
