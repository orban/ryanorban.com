---
title: Hidden Markov Models on Hadoop — Isabel Drost
date: 2012-12-06
categories:
  - machine-learning
  - hmm
  - hadoop
  - nlp
  - probabilistic-models
description: Isabel Drost's slides on Hidden Markov Models and Hadoop — covering how HMMs can be implemented and trained at scale using MapReduce. A 2012-era reference for scaling sequence models before deep learning displaced them.
params:
  source: pinboard
  sourceUrl: http://isabel-drost.de/hadoop/slides/HMM.pdf
---

## Summary

Isabel Drost (Apache Software Foundation member and Apache Mahout contributor) created these slides on implementing Hidden Markov Models (HMMs) using Hadoop and MapReduce. The combination reflects 2012's approach to scaling sequence models: before deep learning and GPUs became the dominant approach, classical probabilistic models like HMMs were the state of the art for speech recognition, part-of-speech tagging, and sequence labeling tasks, and scaling them required distributed computing frameworks.

A Hidden Markov Model is a statistical model for systems that transition between latent (hidden) states, emitting observable outputs at each step. The Viterbi algorithm finds the most likely state sequence; the Baum-Welch algorithm (a special case of expectation-maximization) trains model parameters. Both algorithms have natural parallelization opportunities that MapReduce can exploit for large corpora.

The Apache Mahout project (which Drost contributed to) was the primary machine learning library for Hadoop in this era — implementing collaborative filtering, clustering, and classification algorithms in MapReduce. HMM training on large text corpora fit naturally into this stack. The approach was superseded by Apache Spark's MLlib and eventually by PyTorch/TensorFlow deep learning pipelines, but in 2012 MapReduce-based HMM training was active research.

## Key points

- Hidden Markov Models: probabilistic sequence models with latent states — used for speech recognition, POS tagging, NER
- Viterbi algorithm (decoding) and Baum-Welch (training via EM) are the core HMM algorithms
- MapReduce parallelization: the E-step and M-step of Baum-Welch map to map and reduce phases naturally
- Apache Mahout: the 2012-era ML library for Hadoop — Drost was a key contributor
- Context: pre-deep learning, HMMs were state of the art for sequence tasks that LSTMs and Transformers now dominate

[Original](http://isabel-drost.de/hadoop/slides/HMM.pdf)
