---
title: "pbproxy: Remote Clipboard Over SSH"
date: 2022-12-28
categories:
  - cli
  - ssh
  - clipboard
  - developer-tools
  - productivity
description: pbproxy is a small tool that lets you use your local clipboard over SSH connections — pipe text into it from a remote server and it appears in your local clipboard. Solves the common frustration of needing to copy output from a remote machine.
params:
  source: pinboard
  sourceUrl: https://github.com/nikvdp/pbproxy
---

## Summary

pbproxy is a small utility that enables using your local clipboard from a remote SSH session. The problem it solves is common: you're working on a remote server over SSH, you want to copy the output of a command to your local clipboard, and there's no easy way to do it — you either select text in the terminal (awkward for large output) or copy-paste via a text file.

pbproxy works by proxying clipboard operations over the SSH connection. On macOS, `pbcopy` and `pbpaste` are the native clipboard commands — pbproxy provides equivalents that forward the data to your local machine. It can be combined with tools like `xclip` on Linux to provide a unified interface.

This is a tiny quality-of-life tool in the category of small shell utilities that make SSH-heavy development workflows significantly more pleasant — alongside tmux, mosh (mobile shell for flaky connections), and `.ssh/config` tricks. The clipboard problem becomes especially acute when working on remote machines and needing to copy: error messages, API responses, file contents, or command outputs that are too long to type. pbproxy eliminates the friction of that workflow.

## Key points

- Proxies clipboard (`pbcopy`/`pbpaste`) from remote SSH sessions to local machine.
- Solves the "copy output from server to local clipboard" friction in SSH workflows.
- Small, single-purpose utility — the Unix philosophy of one tool doing one thing well.
- Pairs with tmux and mosh as quality-of-life improvements for SSH-heavy development.

[Original](https://github.com/nikvdp/pbproxy) → GitHub
