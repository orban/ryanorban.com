---
title: "Difftastic: structural diff that understands syntax"
date: 2026-03-11
categories:
  - developer-tools
  - git
  - diff
  - open-source
description: Difftastic is a structural diff tool that parses code with tree-sitter and compares syntax trees rather than lines, filtering out reformatting noise. Essential for anyone who's debugged a reformatted file in a unified diff.
params:
  source: pinboard
  sourceUrl: https://difftastic.wilfred.me.uk/
---

![Difftastic: structural diff that understands syntax](/images/notes/difftastic.png)

## Summary

[Difftastic](/notes/difftastic/) is a command-line diff tool that compares code structurally using tree-sitter parsing, rather than line-by-line text comparison. The key insight is that most diff noise comes from reformatting: a developer runs a code formatter, and the resulting diff shows hundreds of lines changed even though the logic is identical. [Difftastic](/notes/difftastic/) addresses this by comparing syntax trees — if the inner expression hasn't changed, it doesn't report a change, even if the surrounding whitespace and line breaks have shifted.

The output is more readable than unified diff format in several ways. It shows actual line numbers from both file versions side-by-side, rather than the `+`/`-` notation of traditional diffs. Delimiter matching is precise: if a wrapper changes from `{` to `(`, difftastic highlights that specifically rather than reporting every line inside as changed.

It supports 20+ programming languages via tree-sitter grammars, plus structured file formats including JSON, YAML, and HTML. Integration with git as a custom diff driver is straightforward — one config line. MIT-licensed and open source.

## Key points

- Uses tree-sitter syntax parsing to diff structure rather than text — formatting changes don't appear as diffs.
- Side-by-side output with actual file line numbers, vs unified diff's `+`/`-` notation.
- 20+ language support plus JSON, YAML, HTML — not just programming languages.
- Integrates with git as a custom diff driver via a single config option.
- MIT-licensed; actively maintained by Wilfred Hughes.

[Original](https://difftastic.wilfred.me.uk/)
