---
title: f.lux, but for your house — Whole-House Circadian Lighting
date: 2022-11-08
categories:
  - home-assistant
  - smart-home
  - circadian-rhythm
  - lighting
  - diy
  - health
description: Tyler Cipriani's guide to implementing whole-house circadian lighting via Home Assistant — warm amber light in the evening, bright cool light in the day, all automated. f.lux for every bulb in your house.
params:
  source: pinboard
  sourceUrl: https://tylercipriani.com/blog/2022/10/17/whole-house-circadian-lighting-with-home-assistant/
---

## Summary

Tyler Cipriani built a whole-house circadian lighting system using Home Assistant — the same idea as f.lux (which shifts your screen toward warm/amber light in the evenings to reduce blue light exposure before sleep), applied to every light in the house. The system adjusts color temperature automatically throughout the day: bright, cool light during the morning and midday to support alertness, transitioning to warm amber light in the evenings to avoid suppressing melatonin production.

The Home Assistant implementation uses the `circadian_lighting` integration (now called `Adaptive Lighting`) which calculates appropriate color temperature and brightness based on solar position — it knows when sunrise and sunset are for your location, and adjusts lighting accordingly. Smart bulbs from Philips Hue, LIFX, or IKEA respond to color temperature commands over the home network.

The health case for this is solid: circadian rhythm disruption from evening blue light exposure is well-documented and linked to sleep quality degradation. Most people know about f.lux for screens but don't realize that ambient lighting has the same effect and is equally correctable. The DIY solution via Home Assistant costs significantly less than commercial circadian lighting systems and is more customizable. Andrew Huberman's popularization of morning bright light exposure also drove interest in deliberate lighting management.

## Key points

- Implements whole-house circadian lighting using Home Assistant's `Adaptive Lighting` integration.
- Mimics f.lux but for ambient lighting: warm amber in evenings, bright cool light during the day.
- Suppresses evening blue light to preserve melatonin production and sleep quality.
- Uses color-temperature-capable smart bulbs (Hue, LIFX, IKEA) controlled via Home Assistant.
- Adaptive Lighting calculates color temperature from solar position for your location automatically.
- More customizable and cheaper than commercial circadian lighting systems.

[Original](https://tylercipriani.com/blog/2022/10/17/whole-house-circadian-lighting-with-home-assistant/)
