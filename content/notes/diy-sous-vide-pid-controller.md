---
title: DIY PID Controlled Sous Vide Using a Crockpot
date: 2012-04-16
categories:
  - maker
  - hardware
  - cooking
  - electronics
  - pid-control
description: A DIY build of a PID-controlled sous vide cooker using a crockpot, a triac, and zero-cross detection — the kind of over-engineered kitchen hack that defined the early 2010s maker movement. A document of when software engineers started applying control theory to cooking.
params:
  source: pinboard
  sourceUrl: http://www.over-engineered.com/projects/sous-vide-pid-controller/
---

## Summary

This project builds a sous vide temperature controller using a crockpot as the water bath, controlled by a PID controller built from scratch. Sous vide cooking requires holding water at a precise temperature (often within 0.1°C) for hours — the opposite of what a crockpot's on/off thermostat provides. The solution is to bypass the crockpot's control circuitry and drive the heating element directly with a triac switched at the zero-crossing of the AC waveform.

The zero-cross detection is a key detail that the bookmark author called out (fancy!). Switching a triac at the zero-crossing point of the AC sine wave — rather than at a random phase — eliminates the electromagnetic interference (EMI) spike that would otherwise occur and reduces stress on the triac itself. It's the difference between a properly engineered power control circuit and one that causes radio interference and premature component failure.

The PID controller math (proportional-integral-derivative) is what keeps the temperature stable without overshooting. A naive bang-bang controller (heater fully on or off) would cause temperature oscillations; PID control adjusts the power level continuously based on the error, the accumulated error over time, and the rate of change. Applied to cooking, this means the water temperature converges smoothly on the target and holds there.

## Key points

- Triac + zero-cross detection is the standard technique for smooth, RFI-free AC power control in DIY heating controllers.
- PID control vs. bang-bang: bang-bang oscillates, PID converges — critical when a 1°C error changes a recipe outcome.
- The project represents early-2010s maker movement sensibility: applying engineering rigor to domestic objects.
- Sous vide as a hobby cooking technique was spreading from professional kitchens to enthusiasts around 2012, partly driven by DIY controllers like this.
- Commercial sous vide controllers (Anova, etc.) followed within 2-3 years — this kind of DIY build often precedes a product category.

[Original](http://www.over-engineered.com/projects/sous-vide-pid-controller/)
