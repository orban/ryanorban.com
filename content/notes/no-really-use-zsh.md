---
title: No, Really. Use Zsh.
date: 2012-09-28
categories:
  - shell
  - zsh
  - developer-tools
  - terminal
  - productivity
description: A 2012 advocacy post for switching from Bash to Zsh — making the case that Zsh's superior tab completion, history search, and plugin ecosystem (via oh-my-zsh) make it the obvious shell for developers. Still relevant a decade later.
params:
  source: pinboard
  sourceUrl: http://fendrich.se/blog/2012/09/28/no/
---

## Summary

This post from 2012 makes the case for Zsh as the shell every developer should use instead of Bash. The no, really framing acknowledges that this recommendation had been circulating for years without converting most developers — the author's position is that the friction of switching is genuinely lower than people assume, and the quality-of-life improvements are substantial enough to be worth emphasizing again.

The core advantages Zsh offered over Bash in 2012: superior tab completion (context-aware, showing options rather than just completing to the longest common prefix), shared history across terminal sessions, better glob pattern expansion, spelling correction for mistyped commands, and the oh-my-zsh plugin ecosystem that made configuring a rich shell environment a matter of minutes rather than hours of dotfile archaeology. For developers spending most of their day in the terminal, these compound into a meaningful productivity difference.

The post's timing is interesting from a historical perspective. In 2012, oh-my-zsh had been around for about two years and was gaining rapid adoption in the developer community. The Fish shell was a newer alternative pushing the idea of sensible defaults further, but with less compatibility with existing scripts. Zsh occupied the sweet spot: mostly POSIX-compatible (so existing Bash scripts mostly just worked), but with a much richer interactive experience. Apple eventually made Zsh the default shell in macOS Catalina (2019), essentially validating the recommendation.

## Key points

- Zsh's context-aware tab completion is the biggest practical improvement over Bash — shows options, not just extends to longest common match.
- oh-my-zsh turned Zsh configuration from an investment into a commodity — good defaults and plugins in minutes.
- Shared history across terminal sessions: no more losing commands run in other tabs.
- POSIX compatibility: most Bash scripts run in Zsh without modification — the switching cost is lower than it appears.
- Apple made Zsh the default macOS shell in 2019 — the 2012 recommendation aged very well.

[Original](http://fendrich.se/blog/2012/09/28/no/)
