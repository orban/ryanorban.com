---
title: "BLOOM: A 176B-Parameter Open-Access Multilingual Language Model"
date: 2022-11-23
categories:
  - large-language-models
  - nlp
  - open-source
  - multilingual
description: The BLOOM paper introducing a 176-billion parameter open-access multilingual language model trained by the BigScience collaborative on 46 natural languages and 13 programming languages. It demonstrated that a community-organized research effort could produce a frontier-scale LLM without proprietary infrastructure.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2211.07636.pdf
---

## Summary

BLOOM (BigScience Large Open-science Open-access Multilingual Language Model) is a 176-billion parameter large language model developed through the BigScience research workshop, a collaborative effort involving over 1,000 researchers from 70+ countries. Published on arxiv in November 2022 (arXiv:2211.07636), it was trained on the ROOTS corpus — a carefully curated dataset of 341 billion tokens spanning 46 natural languages and 13 programming languages — using Jean Zay, a French national supercomputer operated by IDRIS. It represents one of the first serious attempts to produce a frontier-scale LLM as a fully open-access artifact.

The model architecture is a causal language model based on GPT-style decoder-only Transformer with some modifications including ALiBi positional encodings (which allow generalization to longer sequences than seen during training) and an extra embedding layer normalization. Training used a variant of Megatron-LM for tensor parallelism and DeepSpeed for ZeRO-3 sharded optimizer states. The paper is notable not just for its model but for the extensive documentation of the data governance process: language communities were actively involved in curating sources, and the BLOOM License (a variant of the Responsible AI License) restricted commercial use for early releases while keeping weights publicly downloadable.

BLOOM's multilingual performance is competitive with GPT-3 on English benchmarks and stronger on non-English languages, particularly those well-represented in ROOTS. The paper is significant as a proof-of-concept that open, community-organized AI development can match proprietary labs on scale — a challenge to the then-dominant assumption that only closed organizations like OpenAI could build frontier models.

## Key points

- 176B parameters, trained on 341B tokens from 46 languages — genuinely multilingual unlike most large models that pay lip service to non-English while being predominantly English-trained
- ALiBi positional encodings replace standard rotary position embeddings, enabling extrapolation to longer contexts without performance degradation
- Training infrastructure: Megatron-LM tensor parallelism + DeepSpeed ZeRO optimizer sharding on 384 A100 80GB GPUs — required careful engineering of the multi-node communication topology
- BigScience License / RAIL License approach: weights are open but specific harmful use cases are contractually restricted — an early attempt at responsible release of frontier models
- Benchmark performance shows that scale + data quality can compensate for architecture differences: BLOOM competes with GPT-3 despite being trained on a more diverse, smaller-vocabulary corpus

[Original](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2211.07636.pdf)
