---
title: Will Crichton's Nota Research
date: 2022-05-15
categories:
  - research-communication
  - interactive
  - programming-languages
  - browser
description: Will Crichton's Nota project page — the research motivation and design thinking behind the Nota document language for interactive browser-based technical writing. Companion to the nota-lang.org specification site.
params:
  source: pinboard
  sourceUrl: https://willcrichton.net/nota/
---

![Will Crichton's Nota Research](/images/notes/will-crichton-nota-research.png)

## Summary

This is Will Crichton's research page for Nota at willcrichton.net, presenting the academic motivation behind the Nota document language. Crichton is a programming languages researcher (then at CMU, later Brown University) who has worked on Rust documentation tooling, Aquascope (Rust borrow checker visualizer), and various human-computer interaction questions around how people read and understand code.

The Nota research page situates the language in the context of academic publishing: most scientific knowledge is communicated through PDF documents, which are static artifacts ill-suited to the interactive, computable nature of modern research. Will Crichton's argument is that the browser is a superior medium for technical communication — it supports computation, animation, reader interaction, and dynamic content — but there's no good authoring tool that makes browser-based technical writing as easy as LaTeX or Markdown.

Nota is the proposed solution: a language that compiles to rich browser documents while keeping the authoring experience close to plain text. The page describes the core ideas: reactive variables, definition-reference tracking, and the ability to write prose with inline computations that update when parameters change. This connects to the broader explorable explanations tradition and to Will Crichton's work on making programming education more interactive.

## Key points

- Will Crichton's research motivation: PDF is the wrong format for computable knowledge; the browser enables better science communication
- Nota fills the authoring gap: makes browser-based interactive documents as easy to write as LaTeX
- Connected to Crichton's broader PL research: Aquascope (Rust borrow checker visualizer), Rust documentation tooling
- The reactive variable system is the key technical contribution: prose and computation exist in the same reactive graph
- Pairs with [Nota language](/notes/nota-language/) (nota-lang.org spec) and [Distill interactive articles](/notes/distill-interactive-articles/) for full context
- Related work: Idyll (interactive article authoring), Quarto, Observable — the same space approached differently

[Original](https://willcrichton.net/nota/)
