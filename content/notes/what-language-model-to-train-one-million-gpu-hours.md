---
title: What Language Model to Train if You Have One Million GPU Hours?
date: 2022-07-18
categories:
  - llm
  - scaling
  - architecture
  - multilingual
  - bigscience
  - transformers
description: An ablation study by the BigScience group comparing architectural choices and training setups for large multilingual language models targeting 100B+ parameters within a fixed 1M A100 GPU-hour budget. It shows that careful architecture and training setup decisions at the 1.3B scale transfer predictably to larger models, making principled design tractable even at extreme scale.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/what_language_model_to_train_i.pdf
---

## Summary

This paper from the BigScience research group tackles a practical question that every large-scale language model project faces: given a fixed compute budget — in this case one million A100-GPU-hours — which architectural and training choices make the best use of it? Rather than directly training a 100B+ parameter model and hoping for the best, the authors run a systematic ablation study at 1.3B parameters, where each experiment is affordable, then extrapolate conclusions to the larger scale.

The study compares variants along several axes: decoder-only vs. encoder-decoder architectures, different positional embeddings (including ALiBi and rotary embeddings), activation functions, vocabulary sizes, and tokenization strategies for a multilingual corpus. A key finding is that zero-shot generalization is the right proxy metric — models that score well zero-shot at 1.3B tend to retain that advantage as scale increases, which gives the ablations predictive power beyond the experimental regime.

The paper ultimately informed the design of BLOOM, the 176B parameter multilingual model released by BigScience. It demonstrates that a rigorous ablation-first methodology — rather than replicating existing designs like GPT-3 or PaLM — is feasible and yields models that perform surprisingly well on multilingual benchmarks. This is a template for responsible large-scale pretraining when compute is constrained.

## Key points

- Decoder-only architecture with ALiBi positional embeddings outperformed alternatives in zero-shot transfer
- Tokenization vocabulary size has outsized impact on multilingual performance; they tested several multilingual tokenizers
- Training on the ROOTS corpus (a curated multilingual dataset) rather than Common Crawl alone improved downstream tasks
- All experiments done at 1.3B scale; conclusions validated against available 6B and 13B checkpoints before committing the full budget
- This methodology directly shaped BLOOM, one of the largest open-access multilingual LLMs at the time

[Original](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/what_language_model_to_train_i.pdf)
