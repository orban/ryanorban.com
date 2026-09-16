---
title: "Internet of Food: Arduino-Based Urban Aquaponics in Oakland"
date: 2022-01-11
categories:
  - arduino
  - aquaponics
  - hardware
  - urban-farming
  - iot
description: YouTube video documenting an Arduino-based urban aquaponics system in Oakland — combining IoT sensor monitoring with a closed-loop fish-and-plant growing system. Sits at the intersection of hardware hacking and urban food production.
params:
  source: pinboard
  sourceUrl: https://m.youtube.com/watch?v=3IryIOyPfTE
---

## Summary

This YouTube video documents an urban aquaponics system in Oakland, California, monitored and controlled with Arduino microcontrollers. Aquaponics is a closed-loop food production system combining aquaculture (fish farming) and hydroponics (soilless plant growing) — fish waste provides nutrients for plants, plants filter the water for fish. The internet of food framing connects this to IoT (Internet of Things) infrastructure for agricultural monitoring.

The Arduino component handles environmental sensing and automation: water pH, temperature, dissolved oxygen, ammonia and nitrite levels, grow light scheduling, pump control, and potentially alerting when parameters drift. These are exactly the kind of low-cost, low-power sensing tasks Arduino is well-suited for — each sensor costs a few dollars, the microcontroller costs $10-20, and the whole system can run continuously on minimal power.

Urban aquaponics in Oakland specifically connects to food sovereignty and urban agriculture movements in the Bay Area — communities building local food production capacity independent of industrial supply chains. The system is part of a YouTube playlist suggesting a broader series documenting the setup and operation over time.

The technical appeal for makers: aquaponics requires tight parameter control to keep fish healthy and plants productive. PID controllers, data logging (local or cloud), sensor fusion, and notification systems make it a rich real-world project for learning embedded systems and IoT patterns.

## Key points

- Aquaponics: closed-loop fish + plant system — fish waste → plant nutrients → filtered water → fish
- Arduino handles: water chemistry sensing (pH, dissolved O2, ammonia), pump control, grow light scheduling
- Urban agriculture meets IoT: low-cost sensors make continuous monitoring viable for small-scale food production
- Oakland context: urban farming as food sovereignty / local resilience, not just hobbyist project
- Entry point into IoT skills: real-world parameter control, sensor integration, data logging, alerting

[Original](https://m.youtube.com/watch?v=3IryIOyPfTE)
