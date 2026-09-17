---
title: Will Transformers Take Over Artificial Intelligence?
date: 2022-03-10
categories:
  - machine-learning
  - transformers
  - deep-learning
  - research
  - computer-vision
description: Quanta Magazine's 2022 look at whether transformer architectures will dominate all of AI — following their success in NLP and early incursion into image classification. A useful time-capsule of the moment when the transformer paradigm started feeling inevitable.
params:
  source: pinboard
  sourceUrl: https://www.quantamagazine.org/will-transformers-take-over-artificial-intelligence-20220310/
---

## Summary

A Quanta Magazine article from March 2022 asking whether transformers — the architecture behind GPT, BERT, and most large language models at the time — would extend their dominance beyond NLP into other AI domains like computer vision, protein structure prediction, and reinforcement learning.

The transformer architecture, introduced in Attention is All You Need (2017), replaced recurrent neural networks (RNNs and LSTMs) as the dominant approach for sequence modeling. By 2022, the question was whether the same self-attention mechanism would similarly displace convolutional neural networks (CNNs) in vision tasks. Vision Transformer (ViT) had shown that raw transformer architectures could match or beat CNNs on image benchmarks when given sufficient data. AlphaFold 2 had used attention-based models for protein folding with stunning results. Decision Transformer was applying the paradigm to RL.

The key insight was that transformers are generalists: they can process any sequence of tokens — words, image patches, protein residues, game moves — using the same architecture with the same self-attention mechanism. This modularity made them attractive for multi-modal tasks that mix vision and language. The article likely covered debates about whether the transformer's success was due to the attention mechanism specifically, or just scale and data — a question the field hasn't fully settled.

The 2022 context matters: this was before GPT-4 and before the explosion of open-weight models like LLaMA. The dominance of transformers today makes the question feel answered, but at the time it was a live debate about whether domain-specific architectures or general-purpose attention would win.

## Key points

- Transformers had conquered NLP by 2022 and were making inroads into computer vision via Vision Transformer (ViT).
- Self-attention allows the architecture to model long-range dependencies — something convolutional neural networks struggle with without many layers.
- AlphaFold 2 demonstrated that attention-based models generalize well beyond language to protein folding.
- Central debate: is transformer success about the attention mechanism, or just about scale and the ability to train on massive datasets?
- The scaling hypothesis — that simply making models bigger with more data keeps improving results — was gaining credibility in 2022.

[Original](https://www.quantamagazine.org/will-transformers-take-over-artificial-intelligence-20220310/)
