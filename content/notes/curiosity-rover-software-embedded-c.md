---
title: "Mars Curiosity Rover: 2.5 Million Lines of Embedded C"
date: 2012-08-07
categories:
  - embedded-systems
  - c
  - nasa
  - space
  - software-engineering
description: Stack Exchange answer explaining that the Mars Curiosity rover runs on 2.5 million lines of embedded C, using a real-time operating system called VxWorks. An eye-opening look at mission-critical embedded software at its most demanding.
params:
  source: pinboard
  sourceUrl: http://programmers.stackexchange.com/questions/159637/what-is-the-mars-curiosity-rovers-software-built-in/159638#159638
---

## Summary

A Stack Exchange answer explaining the software stack powering the Mars Curiosity rover, which landed on Mars on August 6, 2012. The rover runs approximately 2.5 million lines of C code on a VxWorks real-time operating system (RTOS), running on a radiation-hardened PowerPC processor. The choice of C and VxWorks reflected the constraints of mission-critical embedded systems: determinism, reliability, and a proven track record in space hardware.

VxWorks is Wind River's commercial RTOS, and it appears in an extraordinary range of mission-critical systems — spacecraft, medical devices, aviation autopilots, and industrial control systems. The key property of an RTOS is deterministic timing: tasks execute within guaranteed time bounds, which is essential when missing a deadline means crashing a rover or losing a spacecraft. C is the natural language for this environment — it gives the programmer direct control over memory and timing with no runtime overhead from garbage collection or virtual dispatch.

The scale — 2.5 million lines of C — was striking to the programming community in 2012. It underscored something important: even the most spectacular engineering achievements rest on software that looks unremarkable by Silicon Valley standards. No Python, no JavaScript, no fancy frameworks. Just disciplined, carefully tested C, run on an RTOS, with extensive ground testing and simulation before deployment. The software had to work correctly the first time, without the possibility of a quick patch — the 14-minute round-trip communication delay to Mars made real-time human intervention impossible.

## Key points

- Mars Curiosity rover runs ~2.5 million lines of C on VxWorks RTOS.
- Hardware: radiation-hardened PowerPC processor (BAE Systems RAD750), designed to survive Mars's radiation environment.
- VxWorks provides deterministic timing — tasks execute within guaranteed bounds, essential for mission-critical hardware.
- 14-minute round-trip communication delay to Mars means the software must handle failures autonomously.
- No garbage collection, no runtime overhead — C's manual memory control is a feature here, not a limitation.
- 2.5M lines of C landed a rover on Mars — a reminder that mission-critical software is unglamorous by design.

[Original](http://programmers.stackexchange.com/questions/159637/what-is-the-mars-curiosity-rovers-software-built-in/159638#159638)
