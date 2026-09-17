---
title: "Sol: A Sunny Little Virtual Machine"
date: 2012-10-15
categories:
  - virtual-machines
  - programming-languages
  - compilers
  - systems-programming
  - concurrency
description: Rasmus Andersson's Sol is an educational register-based virtual machine with cooperative multitasking — built to teach VM internals including schedulers, activation records, and coroutines. Small, clean, and unusually readable.
params:
  source: pinboard
  sourceUrl: http://rsms.me/2012/10/14/sol-a-sunny-little-virtual-machine.html
---

![Sol: A Sunny Little Virtual Machine](/images/notes/sol-virtual-machine.png)

## Summary

Rasmus Andersson (creator of the Figma typeface system and various open-source tools) built Sol as an educational process virtual machine designed to run inside an OS process. The name means sun in Swedish. Where most toy VMs are stack-based for simplicity, Sol uses a register machine design — the same approach taken by Lua's VM and CPython's modern bytecode interpreter — on the grounds that registers reduce opcode count and improve execution speed despite slightly larger instruction encoding.

Sol's architecture centers on schedulers and tasks. One scheduler runs per CPU core, managing a run queue of tasks. Each task maintains activation records (its call stack), where each record holds a program counter, a reference to a function prototype, and numbered registers for local storage. Instructions fit into 32-bit words using three encoding formats (ABC, ABx, Bxx), supporting 64 operations and 256 registers — a deliberate constraint that keeps the instruction decoder simple.

The multitasking model is cooperative multitasking: tasks yield voluntarily via a yield operation, and a cost counter forces a yield after a task executes enough instructions, preventing monopolization. Sol also supports coroutines, timer-based scheduling, and I/O event handling — the full set of primitives needed to build a realistic concurrent runtime. The source is MIT-licensed and written to be read and understood.

## Key points

- Register machine design vs. stack machine: register VMs generate fewer opcodes per program, trading instruction encoding complexity for faster execution — the approach used by Lua and modern Python.
- Cooperative multitasking via yield and cost counters: a simpler model than preemptive multitasking but sufficient for understanding scheduler mechanics.
- Activation records per task represent the call stack — each frame holds a program counter, function prototype reference, and local registers.
- Coroutines as first-class primitives allow sequential code in concurrent systems — a 2012 preview of what became central to async/await patterns.
- 32-bit instruction encoding with three formats limits complexity while remaining expressive enough for real programs.

[Original](http://rsms.me/2012/10/14/sol-a-sunny-little-virtual-machine.html)
