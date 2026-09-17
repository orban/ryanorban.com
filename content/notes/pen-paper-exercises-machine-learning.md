---
title: Pen & Paper Exercises in Machine Learning
date: 2022-06-29
categories:
  - machine-learning
  - mathematics
  - exercises
  - textbook
  - education
description: Michael Gutmann's (Edinburgh) collection of pen-and-paper exercises covering the mathematical foundations of machine learning — linear algebra, optimization, graphical models, density estimation, and classification. Designed to build mathematical fluency that coding-first courses skip, using derivation rather than implementation as the primary learning mode.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2206.13446v1.pdf
---

## Summary

Michael U. Gutmann at the University of Edinburgh compiled this problem set (arXiv:2206.13446) to address a gap in machine learning education: most practitioners learn ML through code and libraries, building intuition for what functions do but not the mathematical reasoning behind why they work. Pen-and-paper exercises force derivations — you can't rely on automatic differentiation when you have to compute a gradient by hand.

The collection spans the core mathematical foundations: linear algebra (Gram-Schmidt, eigendecompositions, traces and determinants), optimization (gradients of vector- and matrix-valued functions, Newton's method, descent directions), directed graphical models (d-separation, hidden Markov models, belief propagation), and density estimation and classification. The exercises are at the level of a graduate ML course but accessible to anyone comfortable with calculus and linear algebra.

This kind of resource is particularly valuable for people who learned ML empirically and want to close the theoretical gap — or for anyone who wants to read papers that assume mathematical fluency (most research papers). The University of Edinburgh ML curriculum is known for rigorous mathematical treatment; this problem set reflects that.

## Key points

- Fills the derivation gap: coding-first ML education skips mathematical reasoning that research-level work requires
- Covers: linear algebra, optimization, graphical models, density estimation, classification
- Pen-and-paper format forces explicit computation — you can't outsource to PyTorch
- Good bridge between practitioner-level ML understanding and research paper fluency
- Creative Commons licensed — freely available, usable as a course supplement
- From University of Edinburgh ML group, known for mathematical rigor

[Original (arXiv 2206.13446)](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/2206.13446v1.pdf)
