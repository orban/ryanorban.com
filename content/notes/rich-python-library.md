---
title: "Rich: Python Library for Beautiful Terminal Output"
date: 2021-04-05
categories:
  - python
  - terminal
  - cli
  - developer-tools
  - open-source
description: Rich is Will McGugan's Python library for beautiful terminal output — syntax highlighting, markdown rendering, tables, progress bars, and formatted logging. Became the standard for making Python CLI tools and scripts look professional.
params:
  source: pinboard
  sourceUrl: https://github.com/willmcgugan/rich
---

## Summary

Rich is a Python library by Will McGugan that makes it easy to produce visually rich output in the terminal — syntax-highlighted code, markdown, tables, progress bars, and formatted logging. Before Rich, getting anything beyond plain text in a Python terminal meant wrestling with ANSI escape codes or heavyweight libraries with poor documentation.

Rich's design philosophy is that terminal output should look good with minimal effort. `from rich import print` immediately gives you colored output with markdown rendering. `rich.logging.RichHandler` adds colored, structured output to any Python logging setup with one line. Progress bars, spinners, live-updating tables, and syntax-highlighted tracebacks all follow the same pattern: import, drop in, done.

The library spawned an ecosystem: Textual (also by Will McGugan) extends Rich into a full TUI (terminal user interface) framework for building interactive terminal applications. Rich has become the de facto standard for Python CLI output — major tools like Typer, FastAPI's CLI, pip, and many others use it internally. The GitHub star count reflected its rapid adoption: thousands of stars within weeks of launch.

## Key points

- `from rich import print` immediately enables colored markdown output — lowest friction entry point.
- RichHandler adds structured, colored logging to any Python app with one line.
- Tables, progress bars, spinners, syntax highlighting, formatted tracebacks — all in one library.
- Spawned Textual for full TUI applications using the same paradigm.
- By Will McGugan — became the standard for Python CLI output; used by pip, FastAPI, and many others.

[Original](https://github.com/willmcgugan/rich)
