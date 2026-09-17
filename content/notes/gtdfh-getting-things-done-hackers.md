---
title: "GTDFH: Getting Things Done for Hackers"
date: 2012-04-08
categories:
  - productivity
  - gtd
  - getting-things-done
  - command-line
  - workflow
description: GTD for Hackers adapts David Allen's Getting Things Done methodology for command-line-oriented developers — plain text files, version control, and shell scripts instead of dedicated GTD apps. An attempt to bring systematic personal productivity into the terminal workflow where developers already live.
params:
  source: pinboard
  sourceUrl: http://gtdfh.branchable.com/
---

## Summary

GTD for Hackers (gtdfh) applies David Allen's Getting Things Done methodology to the command-line-oriented developer workflow. The friction point it addresses: most dedicated GTD applications (OmniFocus, Things, Todoist) are visual, mouse-driven, and separate from the terminal where many developers spend most of their time. Switching context to a GUI app to capture a task breaks flow. A plain-text, version-controlled system that lives in the shell eliminates that switch.

The implementation philosophy: GTD concepts (inbox, contexts, projects, next actions, waiting-for, someday-maybe) mapped onto plain text files, organized in a directory structure, and manipulated with standard Unix tools. Tasks are text. The inbox is a file. Processing means editing files. The system requires no special software beyond a text editor and shell.

This approach connects to the broader plain text productivity and org-mode tradition in the hacker community — the belief that a simple, durable, portable format (text files) beats any proprietary app because it survives software changes, works on any machine, and integrates with everything else in a text-based workflow. Joey Hess's `todo.txt` and the `todo.sh` project are related efforts.

## Key points

- Adapts David Allen's GTD methodology for terminal-based developers — no GUI apps required.
- Plain text files as the data format: portable, durable, version-controllable, editor-agnostic.
- GTD concepts (inbox, next actions, contexts, projects, waiting-for) map to directory structure and text conventions.
- Reduces context-switching cost: tasks live in the same terminal environment as code work.
- Part of the plain text productivity tradition alongside [todo.txt](/notes/todotxt/), Taskwarrior, and org-mode.
- Hosted on Branchable, a git-based wiki hosting service — appropriate for a hacker-oriented project.

[Original](http://gtdfh.branchable.com/)
