---
title: "AVRQueue: Task Scheduler and Watchdog for Arduino"
date: 2012-07-22
categories:
  - arduino
  - embedded-systems
  - scheduling
  - avr
  - open-source
description: AVRQueue is a cooperative task scheduler and watchdog for Arduino/AVR microcontrollers — lets you run multiple pseudo-concurrent tasks without an RTOS. Useful when polling multiple sensors or peripherals in a loop without blocking.
params:
  source: pinboard
  sourceUrl: https://github.com/Zuph/AVRQueue
---

## Summary

AVRQueue is a lightweight cooperative task scheduler for Arduino and AVR microcontrollers — it lets you define multiple tasks that run at specified intervals without blocking the main loop. The core problem it solves: Arduino projects often need to handle multiple sensors, actuators, and peripherals simultaneously. The naive approach (sequential `delay()` calls) blocks everything else during each wait. AVRQueue implements a round-robin cooperative multitasking model where tasks yield control between executions.

The design is appropriate for the hardware constraints. AVR microcontrollers (ATmega328 in the classic Arduino Uno) don't have an MMU or the resources to run a full RTOS — even lightweight options like FreeRTOS add significant overhead. AVRQueue's model is simpler: each task is a function with a scheduled interval; the scheduler tracks timestamps and calls each task when its time comes. No preemption, no thread-safety concerns — just explicit cooperative yielding through the scheduler loop.

The watchdog integration is the other useful piece: a hardware watchdog timer that resets the microcontroller if the main loop stops executing (e.g., due to a bug or lockup). Arduino projects running unattended need this — without a watchdog, a frozen program requires physical intervention. The combination of task scheduling and watchdog gives a simple foundation for reliable embedded projects that need to do multiple things periodically.

## Key points

- Cooperative multitasking on AVR: task functions registered with intervals, scheduler calls each when due — no preemption, no stack-switching overhead.
- Avoids `delay()` blocking: the main loop stays responsive to all registered tasks while waiting for each individual task's interval.
- Watchdog timer integration: hardware reset if main loop freezes — essential for unattended Arduino deployments.
- Appropriate for ATmega328 resource constraints: much lighter than FreeRTOS, sufficient for projects with 5-10 concurrent periodic tasks.
- Pattern used in Arduino libraries like TaskScheduler (later, more featured) — cooperative scheduling remains standard for embedded projects that don't justify RTOS complexity.

[Original](https://github.com/Zuph/AVRQueue) → GitHub
