---
title: ZSH-LOVERS — The Zsh Reference
date: 2013-03-30
categories:
  - zsh
  - shell
  - unix
  - productivity
  - command-line
description: ZSH-LOVERS is the classic reference for Zsh tips, tricks, and advanced features — a comprehensive man-page-style document covering everything from globbing to completion to prompt customization. The go-to resource for developers moving from bash to zsh.
params:
  source: pinboard
  sourceUrl: http://grml.org/zsh/zsh-lovers.html
---

## Summary

ZSH-LOVERS is a well-known reference document (formatted as a manual page) from the GRML Linux distribution project, covering Zsh features, idioms, and tricks in comprehensive depth. In 2013, Zsh was the preferred shell of developers who had outgrown bash — it had better tab completion, more powerful globbing, superior history handling, and a plugin ecosystem (centered around oh-my-zsh) that made configuration practical.

The document covers Zsh-specific features in categories that the bash manual omits: extended globbing patterns (`**/*.py` to recursively match, `^foo` to negate, `(#q...)` for glob qualifiers), parameter expansion tricks (`${foo:u}` to uppercase, `${foo//pattern/replacement}` for inline substitution), the completion system (compinit, compdefs, and writing custom completions), prompt expansion (precmd, RPROMPT, vcs_info for git status in prompt), and Zsh Line Editor (ZLE) keybindings and widgets.

The practical value: Zsh's advanced features are poorly documented in the official man pages — they're complete but dense and spread across multiple sections. ZSH-LOVERS distills the most useful parts into a practitioner reference with examples. For developers spending 8+ hours per day in a terminal, the productivity gains from proper globbing and completion — being able to expand `**/*.py` recursively, or tab-complete git branch names — are cumulative and significant.

## Key points

- Extended globbing: `**` for recursive matching, `^` for negation, numeric ranges, and qualifiers for filtering by file type/age/size.
- Parameter expansion: inline string manipulation without piping to sed/awk — case conversion, substring extraction, pattern replacement.
- Completion system: zsh's compsys is significantly more powerful than bash's — can complete git branches, npm scripts, docker containers, etc.
- oh-my-zsh: the plugin manager that made Zsh adoption practical — community-maintained completions and prompt themes (bookmarked in the same era).
- GRML: Debian-based Linux distribution optimized for sysadmins — ZSH-LOVERS reflects their use the shell well culture.

[Original](http://grml.org/zsh/zsh-lovers.html)
