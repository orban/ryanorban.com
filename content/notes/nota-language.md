---
title: "Nota: A Document Language for the Browser"
date: 2022-05-12
categories:
  - programming-languages
  - publishing
  - browser
  - research-communication
  - interactive
description: Nota is a document language designed for the browser that lets authors write reactive, interactive documents with inline computation and bidirectional updates — imagine Markdown with embedded executable code that readers can modify. Will Crichton's project extending explorable explanations into a proper authoring language.
params:
  source: pinboard
  sourceUrl: https://nota-lang.org/#def-nota
---

![Nota: A Document Language for the Browser](/images/notes/nota-language.png)

## Summary

Nota is a document language created by Will Crichton specifically for authoring interactive, reactive documents in the browser. Where Markdown produces static HTML and LaTeX produces static PDFs, Nota lets authors embed live code, reactive variables, and explorable elements directly in document prose. A definition in one section can propagate changes to examples throughout the document — the document is a reactive computation graph, not a static template.

The design addresses what Will Crichton calls the medium mismatch in research communication: mathematical and computational ideas are dynamic and relational, but papers are static. Nota's syntax extends Markdown with components that can define variables, reference other definitions, and render interactively. A reader who changes a parameter value in one section sees related examples update elsewhere in the document — the document behaves like a spreadsheet where cells are prose paragraphs.

Nota builds on earlier ideas in explorable explanations (notably Bret Victor's work) and literate programming, but specifically targets academic and technical authors rather than data journalists. The goal is to make interactive document authoring as natural as writing LaTeX — not requiring users to build a custom web app for each document. This positions it alongside tools like Observable notebooks and Quarto in the better research communication space.

## Key points

- Nota language: Markdown-like syntax extended with reactive variables, inline computation, and interactive components
- Reactive document model: changing a definition propagates updates through the document — no stale examples
- Target users: researchers and technical authors who want interactive articles without building a web app
- Literate programming lineage: text and computation coexist in the same source — extends the tradition of Knuth's WEB and Jupyter notebooks
- Key design goal: authoring simplicity — the document source should be as clean as Markdown while enabling interactivity
- Companion to the Nota interactive articles essay from Distill.pub / Will Crichton's research at CMU

[Original](https://nota-lang.org/#def-nota)
