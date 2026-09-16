---
title: OPT Training Chronicles
date: 2022-05-04
categories:
  - llm
  - machine-learning
  - meta-ai
  - open-source
  - training-transparency
description: Meta's OPT-175B training logbook — a day-by-day record of hardware failures, instabilities, loss spikes, and interventions during a ~2 month distributed training run. Rare public documentation of what large language model training actually looks like at scale.
params:
  source: pinboard
  sourceUrl: https://github.com/facebookresearch/metaseq/tree/main/projects/OPT/chronicles
---

## Summary

The OPT Training Chronicles are a detailed logbook published by Meta AI (facebookresearch) documenting the training run for OPT-175B — the Open Pre-trained Transformer model with 175 billion parameters released in May 2022. Where most large language model papers present the finished artifact and abstract over the messy process, the Chronicles capture the actual day-to-day reality: hardware failures, loss spikes, gradient divergences, manual interventions, and the operational complexity of running distributed training at scale for roughly two months.

The OPT project was explicitly positioned as a response to the closed nature of GPT-3. Meta released the model weights under a research license, along with the code via metaseq, precisely to enable the research community to study and build on frontier-scale language models without needing API access. The Chronicles extend this transparency ethos — rather than just releasing weights, they released the context behind how those weights were obtained.

The logs are instructive at several levels. Practically, they document the failure modes that anyone training at scale will encounter: NaN losses, hardware-induced checkpointing, optimizer state corruption, network topology issues in large clusters. Strategically, they demonstrate that the path from a clean paper description to a working run involves substantial operational engineering that ML papers systematically hide. The Chronicles help normalize this — showing that even well-resourced teams deal with constant interventions.

## Key points

- Day-by-day logbook of the OPT-175B training run — loss curves, hardware failures, interventions, manual checkpointing decisions.
- OPT-175B is Meta AI's 175B parameter large language model, released with open weights in May 2022 to democratize LLM research.
- Rare transparency: most LLM papers don't document the operational chaos of the actual training run.
- Training used metaseq, Meta's large-scale sequence model training framework, on a GPU cluster over ~2 months.
- Context: published around the same time as BLOOM and GLM-130B, part of the 2022 wave of open-weight frontier LLMs.
- The Chronicles sit alongside papers like Chinchilla (compute-optimal scaling) as important documents for understanding the economics and engineering of LLM training.

[Original](https://github.com/facebookresearch/metaseq/tree/main/projects/OPT/chronicles) → GitHub
