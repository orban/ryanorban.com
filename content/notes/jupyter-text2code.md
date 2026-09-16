---
title: "jupyter-text2code: English to Python in Jupyter"
date: 2021-07-27
categories:
  - machine-learning
  - jupyter
  - nlp
  - code-generation
  - developer-tools
description: jupyter-text2code is a proof-of-concept Jupyter extension that converts English queries into Python code — an early 2021 demonstration of natural language to code generation in notebooks, before Copilot and ChatGPT made this mainstream.
params:
  source: pinboard
  sourceUrl: https://github.com/deepklarity/jupyter-text2code
---

## Summary

[jupyter-text2code](/notes/jupyter-text2code/) is a proof-of-concept Jupyter extension by deepklarity that converts English-language queries into relevant Python code within a notebook cell. You type a description of what you want to do (e.g., "read a CSV file into a DataFrame") and the extension generates the code. This was built and published in mid-2021, before GitHub Copilot became publicly available and before ChatGPT made code generation widely accessible.

The technical approach used a fine-tuned model (based on CodeBERT or similar) trained on pairs of natural language descriptions and corresponding Python code. The training data came from notebook comment-code pairs and similar aligned sources. The model quality in 2021 was limited compared to what became available with GPT-3-based tools, but the concept demonstrated the demand clearly.

The project is historically interesting as an early indicator of the direction that developer tooling would take. The same core idea — describe what you want in English, get code — became the defining feature of the 2022–2023 AI developer tools wave. GitHub Copilot (launched for broad access in June 2022), Cursor, and Claude Code all represent the mature version of what this proof-of-concept was gesturing at.

## Key points

- Code generation from English descriptions in Jupyter notebooks — 2021 proof-of-concept before Copilot/ChatGPT.
- Trained on natural language + Python code pairs; limited quality by 2023 standards but clear demand signal.
- Historically significant: predates the AI developer tools wave by ~1 year and captures the moment the idea surfaced.
- The feature it demonstrated is now standard in GitHub Copilot, Cursor, and AI coding assistants generally.

[Original](https://github.com/deepklarity/jupyter-text2code) → GitHub
