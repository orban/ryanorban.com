---
title: "QLoRA Minimal: Fine-tuning Notebook"
date: 2023-11-06
categories:
  - fine-tuning
  - qlora
  - llm
  - notebook
  - python
description: A minimal Jupyter notebook demonstrating QLoRA fine-tuning — strips away framework boilerplate to show the core mechanics of 4-bit quantized LoRA training. Good reference for understanding what QLoRA actually does at the implementation level.
params:
  source: pinboard
  sourceUrl: https://github.com/geronimi73/qlora-minimal/blob/main/qlora-minimal.ipynb
---

![QLoRA Minimal: Fine-tuning Notebook](/images/notes/qlora-minimal-notebook.png)

## Summary

This minimal Jupyter notebook by geronimi73 demonstrates QLoRA fine-tuning stripped to its essentials — deliberately avoiding heavy framework abstractions to show what QLoRA actually does. It's the kind of reference you reach for when a framework's training loop isn't working and you need to understand the underlying mechanics.

QLoRA (Quantized LoRA) works by loading the base model in 4-bit (NF4) precision using bitsandbytes, then attaching small trainable LoRA adapters to the frozen quantized weights. Only the adapter parameters (typically <1% of total parameters) are updated during training — the base model stays at 4-bit, drastically reducing memory requirements while maintaining quality close to full fine-tuning.

The minimal approach here is pedagogically valuable: no trl, no axolotl, no unsloth abstractions. Just transformers, peft, and bitsandbytes wired together directly. Seeing the `BitsAndBytesConfig`, `get_peft_model()`, and the training loop in plain form makes it much easier to debug when higher-level frameworks produce confusing errors.

## Key points

- QLoRA = 4-bit quantized base model (NF4) + trainable LoRA adapters.
- Only adapter weights are updated — ~1% of total parameters, huge memory reduction.
- Uses bitsandbytes for quantization, peft for LoRA adapter management.
- Intentionally minimal — no high-level trainer frameworks, direct control of training loop.
- Good reference alongside Unsloth (which adds speed optimizations on top of the same approach).
- The `prepare_model_for_kbit_training()` call from peft is the key setup step.

[Original](https://github.com/geronimi73/qlora-minimal/blob/main/qlora-minimal.ipynb) → GitHub
