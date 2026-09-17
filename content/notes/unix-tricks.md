---
title: Unix Shell Tricks
date: 2013-03-07
categories:
  - unix
  - linux
  - shell
  - command-line
  - tips
description: Carles Fenoy's collection of Unix/Linux shell tricks and one-liners — a plain-text reference of practical command-line techniques. The kind of document that circulated among sysadmins and developers via bookmarks before Stack Overflow consolidated this knowledge.
params:
  source: pinboard
  sourceUrl: http://mmb.pcb.ub.es/~carlesfe/unix/tricks.txt
---

## Summary

This plain-text file from Carles Fenoy at the University of Barcelona was a community-shared collection of useful Unix and Linux shell tricks — the kind of document that circulated widely on pinboard and delicious before Stack Overflow centralized developer Q&A. The saved content shows a sample: a `psgrep` function that combines `ps` and `grep` to search running processes without the grep process appearing in its own results.

```bash
function psgrep() { ps axuf | grep -v grep | grep "$@" -i --color=auto; }
```

This classic `grep -v grep` pattern solves a specific irritation: when you run `ps | grep process_name`, the grep command itself shows up in the results. The function filters it out. This is representative of the document's character: small, practical solutions to specific Unix annoyances, often accumulated over years by practitioners.

These plain-text trick files were a significant genre in the pre-Stack Overflow era. They captured institutional knowledge that was hard to search for if you didn't know the right keywords, organized by topic rather than question-answer format. The command line mastery they represented was genuinely valuable — a good collection of shell tricks could save hours of repetitive work.

## Key points

- The `grep -v grep` pattern: filtering a process search's own grep invocation from results — a classic Unix one-liner pattern
- `ps axuf` shows all processes in a forest/tree format — useful for understanding parent-child process relationships
- Plain-text trick files like this were the primary format for Unix knowledge sharing before wikis and Stack Overflow
- Bash functions and aliases in `.bashrc` / `.zshrc` are the enduring mechanism for personalizing shell environments
- This genre of document is now largely superseded by tldr pages and cheat.sh, which provide the same quick reference format in a searchable form

[Original](http://mmb.pcb.ub.es/~carlesfe/unix/tricks.txt)
