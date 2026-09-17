---
title: SOANM — Shell Of A New Machine
date: 2022-10-30
categories:
  - developer-tools
  - dotfiles
  - shell
  - setup
  - automation
  - open-source
description: SOANM (Shell Of A New Machine) is a minimal shell script for quickly configuring new environments — bootstrapping dotfiles and core tooling without a heavy framework. The anti-Ansible approach to machine setup.
params:
  source: pinboard
  sourceUrl: https://github.com/benwr/soanm
---

## Summary

SOANM (Shell Of A New Machine — a riff on the Talking Heads song) is a lightweight shell script for bootstrapping new development environments quickly. The philosophy is minimalism: rather than a full Ansible playbook or Nix configuration, it's a simple script you run on a new machine that installs your core tools and pulls your dotfiles. The trade-off is reduced reproducibility for reduced complexity.

The name captures the anxiety of the fresh machine: you have your usual workflows and tools, but none of them are configured yet. Tools like Ansible, Chef, and Nix solve this comprehensively but require significant upfront investment. SOANM's approach is the pragmatic middle ground: a checked-in script that you can run once and get 80% of the way there, knowing you'll configure the remaining 20% manually.

It sits in a category of developer tooling that includes chezmoi, yadm, Stow, and traditional shell scripts for dotfiles management. The key tradeoff: script-based setups are simpler to understand and modify but don't guarantee idempotency; declarative tools like Nix Home Manager or Ansible guarantee reproducibility but have steeper learning curves. For personal machine setup rather than team infrastructure, the simpler approach is often right.

## Key points

- Minimal shell script for bootstrapping new machine environments — installs tools, pulls dotfiles.
- Anti-framework approach: no Ansible, no Nix, just a script.
- Trades perfect reproducibility for simplicity — gets you 80% configured with minimal overhead.
- Competes with chezmoi, yadm, GNU Stow for dotfile/environment management.
- Appropriate for personal machine setup; team infrastructure warrants more rigorous tools.
- Name riffs on the Talking Heads song Once in a Lifetime ("this is not my beautiful machine").

[Original](https://github.com/benwr/soanm) → GitHub
