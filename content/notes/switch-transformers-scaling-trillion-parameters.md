---
title: "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity"
date: 2022-04-28
categories:
  - transformers
  - mixture-of-experts
  - scaling
  - llm
  - google
description: Switch Transformers (Fedus, Zoph, Shazeer 2021) scales language models to 1.6 trillion parameters using a simplified sparse Mixture of Experts architecture that routes each token to exactly one expert. It's the paper that made sparse MoE practical at scale and laid the architecture foundation for models like Mixtral and GPT-4.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2101.03961.pdf
---

## Summary

William Fedus, Barret Zoph, and Noam Shazeer at Google Brain (JMLR 2022, arXiv 2101.03961) introduce Switch Transformers — a massively scaled sparse Mixture of Experts (MoE) architecture that simplifies prior MoE designs into a practical recipe for training trillion-parameter models. The central design choice: each token is routed to exactly one expert (hence "switch"), eliminating the complexity of routing to multiple experts while preserving the core benefit of conditional computation — each input activates only a fraction of total parameters.

The key technical contributions are the Switch Routing algorithm (one expert per token, preserving full capacity when balanced), a capacity factor that controls expert utilization, and expert dropout as regularization. These changes made sparse models more stable to train — earlier mixture of experts work suffered from training instabilities and load imbalance that made large-scale deployment impractical. Switch Transformers demonstrated scaling along a new dimension: more experts with fixed per-expert compute, rather than deeper/wider dense models.

At the scale of 1.6 trillion parameters (Switch-XXL/Switch-C), Switch Transformers achieve up to 7× speedup over dense T5-XXL on pretraining tasks while matching or exceeding the dense baseline on downstream tasks. The results established sparse MoE as a viable path to scaling beyond what dense training budgets allow, directly influencing architectures like GLaM, Mixtral, Gemini Mixture of Experts, and (reportedly) GPT-4.

## Key points

- Switch routing: route each token to exactly one expert, chosen by highest router probability — simplifies Mixture of Experts from multiple-expert to single-expert routing without performance loss
- Scales to 1.6T parameters (Switch-C) with fixed FLOPs per token — achieves 7× speedup over T5-XXL while using same compute budget per forward pass
- Capacity factor: controls how many tokens each expert can process; too low → dropped tokens, too high → wasted capacity; the tradeoff is a key engineering knob
- Training stability fix: expert dropout during fine-tuning + careful initialization prevents the collapse failures that plagued earlier MoE approaches
- Downstream performance: matches dense models on GLUE, SuperGLUE, and other benchmarks when fine-tuned — proving that parameter count from sparsity transfers to task quality

[Original paper →](https://arxiv.org/abs/2101.03961)
