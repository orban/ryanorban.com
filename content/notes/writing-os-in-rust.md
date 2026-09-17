---
title: Writing an OS in Rust
date: 2022-02-25
categories:
  - rust
  - operating-systems
  - education
  - systems-programming
  - tutorial
description: Philipp Oppermann's 'Writing an OS in Rust' is a series of detailed blog posts walking through building a minimal OS kernel in Rust from scratch — bootloader, VGA output, interrupts, memory management. The gold standard for learning both Rust and OS internals simultaneously.
params:
  source: pinboard
  sourceUrl: https://os.phil-opp.com/
---

## Summary

Writing an OS in Rust is a series of tutorial blog posts by Philipp Oppermann at `os.phil-opp.com` that walks through building a minimal operating system kernel in Rust from scratch. The series covers the complete journey from a bare-metal environment (no standard library, no runtime) through bootloading, VGA text output, hardware interrupts, keyboard input, memory management (physical and virtual), heap allocation, and async/await in a kernel context.

The project serves two audiences simultaneously: people learning Rust who want to see the language's safety guarantees applied in a context where mistakes genuinely crash the machine, and people learning operating systems who want to implement the concepts rather than just read about them. Rust's ownership system and type system are particularly well-suited to OS development — the same properties that prevent use-after-free bugs in userspace code prevent the equivalent bugs in kernel code.

The series is notable for depth and correctness. Each post explains not just the code but the hardware architecture (x86_64 ISA, APIC interrupt model, paging and virtual memory mechanics, GDT and IDT). The approach is incremental — each post builds directly on the previous one, and the author publishes companion crates (like `bootimage`, `x86_64`) as open-source libraries others can use.

This sits in a tradition of systems programming education that includes OSTEP (Operating Systems: Three Easy Pieces) and xv6, but is distinctive for using Rust rather than C, and for being a live web tutorial rather than a textbook.

## Key points

- Build a full OS kernel from scratch in Rust: bootloader, interrupts, paging, heap allocation, async.
- Rust's ownership model maps well to kernel programming — many OS-level safety invariants are expressible in the type system.
- Covers real x86_64 hardware mechanics: paging, GDT, IDT, APIC, hardware interrupts.
- Companion open-source crates published by the author (`bootimage`, `x86_64`, `uart_16550`).
- Alternative to C-based OS tutorials (xv6, OSDev wiki) — reflects Rust's emergence as a systems language.

[Original](https://os.phil-opp.com/)
