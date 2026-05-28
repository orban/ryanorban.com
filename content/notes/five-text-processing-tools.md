---
title: Five Text Processing Tools You Should Know
date: 2013-06-18
categories:
  - unix
  - command-line
  - tools
  - text-processing
  - shell
description: Symkat's guide to five Unix text processing tools beyond the basics — covering less-known utilities that handle common data munging tasks more cleanly than awk/sed alone. Practical shell tooling for anyone working with text data on the command line.
params:
  source: pinboard
  sourceUrl: http://www.symkat.com/five-text-processing-tools-you-should-know
---

![Five Text Processing Tools You Should Know](/images/notes/five-text-processing-tools.png)

## Summary

This Symkat post covers five Unix text processing tools that practitioners often overlook in favor of reaching for Python or awk. The premise: the standard toolkit is deeper than most people learn. Tools like `tr`, `column`, `tee`, `watch`, and `paste` each handle specific text transformation tasks more cleanly than constructing equivalent awk one-liners.

These tools fit into the Unix philosophy of small, composable programs. `tr` (translate/delete characters) is the right tool for character-level transformations — stripping newlines, converting case, squeezing repeated characters. `column` formats output into aligned columns for human-readable tables without a spreadsheet. `tee` splits a stream to both stdout and a file simultaneously, enabling logging pipelines without buffering. `paste` combines files line-by-line horizontally (the complement to `cat`'s vertical stacking).

The value of knowing these tools is avoiding unnecessary complexity: a task that requires 20 lines of Python might be a 3-part Unix pipeline. This connects directly to the Ad Hoc Data Analysis From The Unix Command Line and crush-tools tradition — the command line as a capable data analysis environment.

## Key points

- `tr`: character-level translation, deletion, and squeezing — converts uppercase to lowercase, strips control characters, normalizes whitespace.
- `column`: formats whitespace-delimited text into aligned columns for human-readable output from pipelines.
- `tee`: reads stdin and writes to both stdout and a file — enables inline logging in pipelines without breaking the stream.
- `paste`: horizontal concatenation of files by line — the dual of `cat`'s vertical stacking.
- `watch`: runs a command repeatedly at an interval and displays output — simple monitoring without a cron job or shell loop.

[Original](http://www.symkat.com/five-text-processing-tools-you-should-know)
