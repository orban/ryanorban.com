---
title: Language Models Can Teach Themselves to Program Better
date: 2022-08-13
categories:
  - llm
  - code-generation
  - self-improvement
  - synthetic-data
  - research
description: Haluptzok, Bowers, and Kalai show that language models can generate their own programming problems and solutions, verify correctness with a Python interpreter, then fine-tune on the verified examples — more than doubling test accuracy. A clean demonstration of self-improvement via external verification.
params:
  source: papers
  sourceUrl: https://arxiv.org/abs/2207.14502
---

## Summary

Patrick Haluptzok, Matthew Bowers, and Adam Kalai at Microsoft Research demonstrate a virtuous cycle for improving code generation models: generate programming problems and solutions, verify them with a Python interpreter, fine-tune on verified examples, repeat. The model bootstraps its own training data using an external oracle — the interpreter — that can certify whether generated solutions are correct without human labeling.

The setup uses programming puzzles as the task format, where each puzzle specifies a function `f` that a solution must satisfy. The model generates both the puzzle and a solution; the interpreter verifies whether the solution passes the puzzle's test. Only verified (puzzle, solution) pairs are added to the training set. Fine-tuning on this self-generated dataset more than doubles test accuracy compared to the base model — demonstrating that the key constraint on LLM code generation SKILL isn't model capacity but training data diversity and difficulty.

The key technical contribution is the interplay between generation and verification: code generation provides high-recall but noisy candidate solutions, while interpreter execution provides precise, cheap verification. This self-play dynamic — similar conceptually to AlphaGo's use of self-play with a ground-truth game evaluator — lets the model gradually expand its competence by generating harder problems and solving them. This anticipates the broader test-time compute and process reward model research by showing that correctness verification is a powerful training signal.

## Key points

- Self-improvement loop: generate (problem, solution) pairs → verify with Python interpreter → fine-tune → repeat
- Test accuracy more than doubles — suggesting training data diversity matters more than model size for code generation
- Programming puzzle format enables unambiguous correctness verification: the interpreter is the judge
- Analogous to self-play in games: external verification (interpreter) plays the role of the game evaluator
- Precursor to process reward models, test-time compute scaling, and synthetic data approaches like OSS-Instruct
- Cheap verification is the key: scalable self-improvement requires a cheap, reliable way to judge outputs

[Original](https://arxiv.org/abs/2207.14502)
