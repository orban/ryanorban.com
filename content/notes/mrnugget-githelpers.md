---
title: mrnugget's Git Helpers Dotfile
date: 2024-10-23
categories:
  - developer-tools
  - git
  - dotfiles
  - cli
  - shell
description: Specific lines from Matej Hustau's (mrnugget) githelpers dotfile — a shell script of git log formatting and productivity aliases. A reference for clean git log output and workflow helper patterns from a seasoned developer's dotfiles.
params:
  source: pinboard
  sourceUrl: https://github.com/mrnugget/dotfiles/blob/c4624ed521d539856bcf764f04a295bb19093566/githelpers#L11-L15
---

![mrnugget's Git Helpers Dotfile](/images/notes/mrnugget-githelpers.png)

## Summary

mrnugget (Matej Hustáu, author of Writing an Interpreter in Go and Writing a Compiler in Go) maintains a set of git helper shell functions in his public dotfiles. Lines 11-15 of his `githelpers` file specifically were bookmarked — likely containing git log formatting aliases that produce cleaner, more readable history output than the default git log.

Dotfiles from experienced developers are a rich source of practical workflow improvements that don't get written up as blog posts — these are the small scripts someone reaches for dozens of times a day and never thinks to document. Git log formatting in particular is a common area: the default output is verbose and hard to scan, while `--oneline` loses too much context. Custom formats like `git log --graph --pretty=format:'%C(yellow)%h%Creset -%C(red)%d%Creset %s %C(green)(%cr) %C(blue)<%an>%Creset'` produce compact, colorized output that shows author, time, and branch structure at a glance.

The lines 11-15 reference suggests these are specific formatting variables or aliases that Hustáu finds worth reusing — a small, curated slice of a larger helper library. The pattern of sharing dotfiles publicly (as mrnugget does at mrnugget/dotfiles) has become a standard practice in the developer community, with GitHub as the canonical hosting point.

## Key points

- Bookmarked specifically for lines 11-15 of the `githelpers` file — likely git log formatting helpers
- mrnugget is the author of the Monkey language books (Writing an Interpreter in Go)
- Dotfiles repositories are a high-signal source of practical shell and git workflow improvements
- Git log formatting with `--pretty=format` and color codes is a common target for customization
- Related to git-extras and tools like git-recent for improved git UX

[Original](https://github.com/mrnugget/dotfiles/blob/c4624ed521d539856bcf764f04a295bb19093566/githelpers#L11-L15)
