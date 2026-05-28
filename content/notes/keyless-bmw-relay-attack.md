---
title: Keyless BMW Cars Prove to Be Very Easy to Steal
date: 2012-07-09
categories:
  - security
  - rfid
  - relay-attack
  - automotive
  - hardware-hacking
description: "Hackaday's 2012 coverage of the relay attack on BMW keyless entry: two cheap radios extend the key fob's short-range signal across a parking lot, fooling the car into thinking the key is nearby. Still the standard theft method for passive-entry luxury cars today."
params:
  source: pinboard
  sourceUrl: http://hackaday.com/2012/07/07/keyless-bmw-cars-prove-to-be-very-easy-to-steal/
---

![Keyless BMW Cars Prove to Be Very Easy to Steal](/images/notes/keyless-bmw-relay-attack.png)

## Summary

Hackaday's 2012 coverage detailed the relay attack against BMW's keyless entry system — and by extension, nearly all passive entry systems from that era. The attack is simple: two people each carry a radio amplifier. One stands near the car, one stands near the house where the key fob is sitting. The amplifiers relay the car's query signal to the key and the key's response back to the car, across a distance the system was designed to treat as impossible. The car unlocks and starts. No cloning, no cryptography broken — just physics exploited.

The attack exposed a fundamental design flaw in passive keyless entry (PKE) systems. PKE works by having the car constantly emit a low-power challenge signal; when a valid key responds within range (~1 meter), the car unlocks. The designers assumed physical proximity was an unfakeable authentication factor — if the key is responding, it must be nearby. The relay attack breaks that assumption with commodity hardware. In 2012, the equipment cost a few hundred dollars; by 2020 it was available on Amazon.

The fix — measuring signal time-of-flight to verify the key is actually nearby — was known at the time but not implemented because it required hardware changes manufacturers were reluctant to make. Ultra-wideband (UWB) chips that enable precise ranging (< 10cm) became the solution, rolled out in iPhone 11 (2019) and BMW models starting around 2021. The relay attack window: roughly 2007-2022, affecting tens of millions of vehicles.

## Key points

- Relay attack mechanism: two amplifiers extend the car's PKE challenge/response across distance, fooling the authentication without breaking any cryptography.
- Attack requires ~$200 of hardware (2012) and two people — a low barrier for professional car thieves; now ubiquitous theft method for passive-entry vehicles.
- Root cause: passive keyless entry systems used signal strength as a proxy for physical proximity, a fakeable metric.
- The fix (UWB ranging) was technically available but required hardware redesign — delayed by manufacturer inertia until theft rates became PR problems.
- Industry adopted ultra-wideband (UWB) for precise ranging starting ~2019-2021, closing the vulnerability for new vehicles.

[Original](http://hackaday.com/2012/07/07/keyless-bmw-cars-prove-to-be-very-easy-to-steal/)
