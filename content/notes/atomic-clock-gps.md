---
title: How an Atomic Clock Works, and Its Use in GPS
date: 2012-06-14
categories:
  - physics
  - timekeeping
  - gps
  - engineering
  - explainer
description: An EngineerGuy video explaining how atomic clocks work and why GPS depends on them. A clean demonstration that the entire global positioning system rests on quantum mechanical precision in timekeeping.
params:
  source: pinboard
  sourceUrl: http://www.wimp.com/atomicclock/
---

![How an Atomic Clock Works, and Its Use in GPS](/images/notes/atomic-clock-gps.png)

## Summary

An atomic clock keeps time by exploiting a physical constant that never drifts: the resonant frequency at which cesium-133 atoms oscillate between two hyperfine energy states — exactly 9,192,631,770 cycles per second, which is now the definition of the SI second. Unlike mechanical oscillators or quartz crystals (which drift with temperature and wear), the atom doesn't change. Every cesium atom in the universe ticks at precisely the same rate.

The EngineerGuy (Bill Hammack, professor of chemical engineering at University of Illinois) made this video as part of a series translating engineering principles for general audiences. His explanation walks through the feedback loop that makes an atomic clock work: a microwave signal is tuned until cesium atoms are excited at peak efficiency, and that peak frequency becomes the time reference. The clock doesn't just count a signal — it locks onto the atom's natural resonance and counts that.

GPS (Global Positioning System) depends entirely on atomic clock precision. Each GPS satellite carries multiple atomic clocks and broadcasts its location and timestamp. Your receiver computes its position by measuring the time delay between signals from multiple satellites and trilatulating. The math requires knowing signal travel time to nanosecond precision — because light travels about 30 centimeters in a nanosecond, a 100-nanosecond error translates to 30 meters of position error. Without atomic clock accuracy, GPS as we know it would be impossible.

## Key points

- Cesium-133 resonance at 9,192,631,770 Hz is the SI definition of the second — a physical constant rather than a constructed standard.
- Atomic clock feedback loop: microwave source → cesium atoms → detector → tune microwave frequency to peak excitation → lock.
- GPS satellite accuracy requires nanosecond-level timing; 1 nanosecond error = ~30 cm position error.
- Consumer quartz watches drift seconds per day; cesium atomic clocks drift less than 1 second per 300 million years.
- Modern atomic clocks use laser cooling to slow cesium atoms, increasing precision further (optical lattice clocks are even more precise).

[Original](http://www.wimp.com/atomicclock/)
