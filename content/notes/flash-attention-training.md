---
title: "Flash Attention: Training Examples"
date: 2022-11-29
categories:
  - flash-attention
  - transformer
  - gpu
  - efficiency
  - research
description: Flash Attention's training examples from Hazy Research — demonstrating how to use the memory-efficient attention implementation for training large transformers. Flash Attention became one of the most impactful algorithmic contributions to LLM training efficiency.
params:
  source: pinboard
  sourceUrl: https://github.com/HazyResearch/flash-attention/tree/main/training
---

![Flash Attention: Training Examples](/images/notes/flash-attention-training.png)

## Summary

Flash Attention is a memory-efficient attention algorithm by Tri Dao and colleagues at Hazy Research (Stanford) that computes exact self-attention while using O(N) memory rather than O(N²) — the quadratic memory cost that made long context windows impractical. This GitHub link points to the training examples in the repository, showing how to use Flash Attention in practice for training transformer models.

The algorithmic insight: standard self-attention materializes the full N×N attention matrix in GPU HBM (high-bandwidth memory), which is slow due to memory bandwidth. Flash Attention avoids materializing the full matrix by tiling the computation into blocks that fit in fast SRAM, computing attention incrementally. The result: exact same outputs as standard attention, but with IO complexity reduced from O(N²) to O(N), enabling 2-4x speedups and much longer sequence lengths for the same GPU memory.

The practical impact of Flash Attention has been enormous. It enabled training with longer context windows that were previously impossible at reasonable cost — Llama 2's 4096-token context, Claude's long context, GPT-4's 32K context all depend on efficient attention implementations like Flash Attention. It also reduced training costs significantly. Flash Attention 2 and Flash Attention 3 improved on the original further. The algorithm is now a standard component in PyTorch (via `torch.nn.functional.scaled_dot_product_attention`), xFormers, and most major training frameworks.

## Key points

- Memory-efficient exact self-attention algorithm: O(N) memory vs. O(N²) for standard attention.
- Tiles computation into blocks that fit in fast SRAM, avoiding slow HBM reads/writes.
- Same mathematical output as standard attention — not an approximation.
- 2-4x training speedup; enables much longer context windows for the same GPU memory.
- Foundation for long-context models (Llama 2 4K, GPT-4 32K, Claude long context).
- Now standard in PyTorch (`scaled_dot_product_attention`), xFormers, and major frameworks.

[Original](https://github.com/HazyResearch/flash-attention/tree/main/training) → GitHub
