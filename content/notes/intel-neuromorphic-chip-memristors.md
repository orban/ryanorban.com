---
title: Intel Reveals Neuromorphic Chip Design
date: 2012-06-18
categories:
  - neuromorphic-computing
  - hardware
  - brain
  - chips
  - intel
description: MIT Technology Review's coverage of Intel's 2012 neuromorphic chip design using memristors and lateral spin valves — an attempt to build silicon that computes like neurons rather than logic gates. Early work in a research direction that would eventually produce Intel's Loihi chip.
params:
  source: pinboard
  sourceUrl: http://www.technologyreview.com/view/428235/intel-reveals-neuromorphic-chip-design/
---

![Intel Reveals Neuromorphic Chip Design](/images/notes/intel-neuromorphic-chip-memristors.png)

## Summary

In 2012, Intel revealed research into neuromorphic computing — silicon chip architectures designed to mimic the computational principles of biological neurons rather than implementing traditional von Neumann architecture. The specific approach used memristors and lateral spin valves as the key novel components. Memristors (memory + resistors) are circuit elements whose resistance changes based on the history of current flowing through them — a property that makes them natural candidates for implementing synaptic weights in hardware. Lateral spin valves use electron spin to represent state.

Neuromorphic computing is motivated by a fundamental inefficiency in conventional computing: the von Neumann bottleneck. Standard CPUs process information by shuttling data between separate memory and compute units — expensive in both energy and latency. Biological brains process information locally in massively parallel networks of neurons, where the "memory" (synaptic weights) is physically co-located with the computation (neuron activation). Neuromorphic chips try to replicate this architecture: sparse, event-driven computation (neurons fire only when activated), local memory in synaptic weights, massive parallelism.

The 2012 Intel work was early-stage research, not a commercial product. The challenge was reliability and density: memristors were promising in theory but difficult to manufacture consistently at scale. Intel's later work produced Loihi (2017) and Loihi 2 (2021) — actual neuromorphic processors that demonstrated real spiking neural network computation. The broader neuromorphic computing landscape also includes IBM TrueNorth, SpiNNaker (Manchester), and academic projects. The field remains niche as of 2026 — useful for specific edge inference tasks but hasn't displaced GPU-based deep learning for training.

## Key points

- Neuromorphic computing: silicon architectures that mimic biological neural computation — event-driven, sparse, local memory co-located with compute.
- Memristors: resistance changes with current history — natural hardware implementation of synaptic weights.
- Addresses the von Neumann bottleneck: separating memory from compute is energy-expensive; neuromorphic chips collocate both.
- Intel 2012 work was early research; commercial descendants include Intel Loihi (2017) and Loihi 2 (2021).
- Competing approaches: IBM TrueNorth, SpiNNaker, BrainScaleS — all exploring different hardware substrates for spiking neural networks.
- Field still niche as of 2026: useful for edge inference and spike-timing dependent plasticity experiments, but hasn't displaced GPU-based deep learning.

[Original](http://www.technologyreview.com/view/428235/intel-reveals-neuromorphic-chip-design/)
