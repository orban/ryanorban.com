---
title: Near-Linear Scaling of Gigantic Model Training on AWS
date: 2022-07-03
categories:
  - machine-learning
  - distributed-training
  - aws
  - large-language-models
  - infrastructure
description: Amazon Science's post on achieving near-linear scaling when training gigantic language models across thousands of GPUs on AWS infrastructure. Covers parallelism strategies (tensor, pipeline, data) that make training 100B+ parameter models economically feasible.
params:
  source: pinboard
  sourceUrl: https://www.amazon.science/blog/near-linear-scaling-of-gigantic-model-training-on-aws
---

## Summary

This Amazon Science blog post describes the infrastructure and parallelism techniques AWS used to achieve near-linear scaling when training very large language models across thousands of GPUs. At the scale of 100B+ parameter models, the engineering challenge isn't just model architecture — it's making distributed training efficient enough that adding more hardware actually reduces wall-clock time proportionally.

The key techniques: tensor parallelism splits individual layer computations across multiple GPUs (necessary when a single layer doesn't fit in memory); pipeline parallelism splits the model by depth, with different GPUs handling different layers; data parallelism runs the same model on different data batches and synchronizes gradients. Combining these three dimensions (3D parallelism) is the standard approach for training at this scale, popularized by Megatron-LM from NVIDIA and implemented in frameworks like DeepSpeed from Microsoft.

The near-linear claim in the title is the important result: doubling the number of GPUs should roughly halve training time. In practice, communication overhead, memory bandwidth constraints, and load imbalance cause sublinear scaling. Getting close to linear requires careful tuning of all-reduce operations, overlapping computation and communication, and matching parallelism dimensions to the specific hardware topology. This kind of systems work is less glamorous than model architecture research but is what makes training feasible within reasonable time and cost budgets.

## Key points

- 3D parallelism (tensor + pipeline + data) is the standard approach for 100B+ parameter model training
- Tensor parallelism (splitting layer computations) requires high-bandwidth interconnects — efficient on NVLink but expensive across nodes
- Pipeline parallelism introduces micro-batching overhead; naive implementations have significant pipeline bubbles of idle GPU time
- AWS SageMaker distributed training library implements these strategies for EC2 clusters; DeepSpeed and Megatron-LM are the research equivalents
- Scaling efficiency typically degrades at very large cluster sizes; this work pushed practical limits for transformer training in 2022

[Original](https://www.amazon.science/blog/near-linear-scaling-of-gigantic-model-training-on-aws)
