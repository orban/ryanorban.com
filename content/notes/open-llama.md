---
title: "OpenLLaMA: Open Reproduction of LLaMA"
date: 2023-05-03
categories:
  - llm
  - open-source
  - llama
  - training
  - research
description: OpenLLaMA is an open-source reproduction of Meta's LLaMA model trained on the RedPajama dataset, released under permissive Apache 2.0 licenses. It was one of the first serious attempts to produce a fully open LLaMA-quality model that anyone could use commercially.
params:
  source: pinboard
  sourceUrl: https://github.com/openlm-research/open_llama
---

![OpenLLaMA: Open Reproduction of LLaMA](/images/notes/open-llama.png)

## Summary

OpenLLaMA is an open-source reproduction of Meta's LLaMA language model from the OpenLM Research group. Rather than using Meta's non-commercially licensed weights, OpenLLaMA is trained from scratch on the RedPajama dataset — a fully open replication of the training data used for LLaMA — and released under the Apache 2.0 license. This makes it freely usable in commercial products, which LLaMA 1 was not.

The project released 3B and 7B parameter models trained on 1 trillion tokens, designed to be drop-in replacements for the original LLaMA weights. Evaluation showed performance competitive with the original models, validating that the RedPajama dataset was a good proxy for LLaMA's training distribution. OpenLLaMA quickly became an important base model for the open-source community — fine-tunable without legal uncertainty.

OpenLLaMA represents a critical moment in the open-source AI trajectory: the gap between open weights with restrictions and fully open weights drove significant community effort to reproduce capabilities independently. It connects to parallel efforts like Falcon (fully open commercial model from TII) and [MPT-7B](/notes/mpt-7b/) from MosaicML, which were all trying to fill the same gap left by LLaMA's non-commercial license in early 2023.

## Key points

- Drop-in replacement for LLaMA weights with Apache 2.0 license — commercially usable, no restrictions.
- Trained on RedPajama dataset (open reproduction of LLaMA training data), 1T tokens.
- 3B and 7B model sizes; performance competitive with original LLaMA models.
- From OpenLM Research; concurrent with [MPT-7B](/notes/mpt-7b/) and Falcon as solutions to the open commercial LLM gap.
- Part of the broader push to make fully open LLM weights the default — not just "open" with strings attached.

[Original](https://github.com/openlm-research/open_llama) → GitHub
