---
title: "DIFFUSER: Discrete Diffusion via Edit-Based Reconstruction"
date: 2022-11-16
categories:
  - nlp
  - diffusion-models
  - text-generation
  - generative-models
  - research
description: Introduces DIFFUSER, an edit-based text generation model that adapts denoising diffusion to discrete text by framing generation as iterative editing rather than left-to-right token production. Competitive with autoregressive models on translation and summarization while enabling unique capabilities like prototype-conditioned generation and iterative revision.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2210.16886.pdf
---

## Summary

Vincent Hellendoorn (CMU), Machel Reid (Google Research), and Graham Neubig (CMU/Inspired Cognition) introduce DIFFUSER — a text generation model that adapts denoising diffusion models to the discrete text domain. The core problem: dominant autoregressive language models generate text left-to-right in a single pass and cannot revise it. Humans write through iterative revision; DIFFUSER aims to enable that.

DIFFUSER frames text generation as a Markov chain of edit operations: starting from a noisy or incomplete sequence, the model applies denoising steps that gradually reconstruct the target text. The edits are not arbitrary transformations — they map naturally to insertions, deletions, and substitutions, making the generation process interpretable as revision. Unlike continuous diffusion models (which operate on real-valued embeddings and can't be directly applied to discrete tokens), DIFFUSER works in the discrete token space.

On standard benchmarks — machine translation, summarization, and style transfer — DIFFUSER is competitive with autoregressive baselines. But it enables qualitatively different generation modes: conditioning on a prototype (partial text to revise from), continuing from an incomplete sequence, and iterating on previous edit steps. These aren't possible in standard left-to-right generation. The paper is part of a broader wave of 2022 work applying diffusion to language — alongside papers like MDLM, Plaid, and DiffuSeq.

## Key points

- Discrete diffusion for text: adapts denoising diffusion to the token domain by framing generation as iterative editing, not continuous noise reduction
- Competitive with autoregressive models on translation, summarization, style transfer
- Unique capabilities: prototype-conditioned generation, iterative revision from partial sequences — not possible in AR models
- Addresses the text revision problem: unlike AR models that write once, DIFFUSER can refine existing text
- Part of a 2022 wave applying diffusion models to NLP — the field was actively exploring non-AR generation paradigms
- Relevant to code generation and document editing use cases where iterative refinement is the natural workflow

[Original (arXiv 2210.16886)](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/2210.16886.pdf)
