---
title: "Pathways: Asynchronous Distributed Dataflow for ML"
date: 2022-06-17
categories:
  - distributed-systems
  - ml-infrastructure
  - tpu
  - dataflow
  - google
  - mlsys-2022
description: Google's Pathways is a single-controller orchestration layer for ML accelerators that runs sharded asynchronous dataflow across thousands of TPUs while matching SPMD performance. Designed to break the MPI-style lockstep model so heterogeneous workloads like MoE, pipelining, and foundation-model multiplexing become first-class.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/pathways.pdf
---

## Summary

Pathways is Google's answer to a question that mattered as machine learning systems outgrew the SPMD (Single Program Multiple Data) model inherited from MPI. The authors — Jeff Dean, Sanjay Ghemawat, Michael Isard and team — argue that lockstep all-accelerator collectives like AllReduce are too restrictive for emerging workloads: mixture of experts needs sparse, heterogeneous compute; pipeline parallelism needs MPMD scheduling; and shared foundation models need to multiplex many tasks on the same hardware.

The system uses a sharded dataflow graph of asynchronous operators that produce and consume futures, with a novel design that lets the control plane execute in parallel even when the data plane has dependencies. This is what unlocks the single-controller architecture — usually a bottleneck — and makes complex parallelism patterns expressible in straightforward client code. Gang scheduling coordinates heterogeneous compute across thousands of TPUs while orchestrating data transfers over dedicated ICI (Inter-Chip Interconnect) links.

Performance is the key concession to skeptics: Pathways hits roughly 100% accelerator utilization on SPMD workloads at 2048 TPUs, matching the systems it aims to replace. It also matches that throughput for Transformers pipelined across 16 stages or sharded across two accelerator islands connected via the data center network. The paper sits in the lineage of TensorFlow and JAX runtime work and lays the foundation for what would become PaLM-scale training infrastructure.

## Key points

- SPMD/MPI model is too restrictive for modern ML: pipelining, MoE, and shared foundation models all want MPMD-style heterogeneous scheduling.
- Pathways uses asynchronous dataflow with futures so the control plane runs in parallel even when the data plane has dependencies — eliminating the usual single-controller bottleneck.
- A single-controller design simplifies expressing complex parallelism patterns versus the all-to-all coordination MPI demands.
- Achieves ~100% accelerator utilization at 2048 TPUs on SPMD workloads — proving the abstraction has no performance tax for current workloads.
- Designed so foundation model training, fine-tuning, and inference can multiplex on the same accelerator islands, with shared sub-models batched across tasks.

[Original PDF](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/pathways.pdf)
