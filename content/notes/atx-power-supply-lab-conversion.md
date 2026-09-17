---
title: How to Convert a Computer ATX Power Supply to a Lab Power Supply
date: 2013-01-08
categories:
  - hardware
  - diy
  - electronics
  - maker
  - power-supply
description: WikiHow guide for converting a surplus ATX PC power supply into a benchtop lab power supply — a classic maker hack that gives you multiple regulated DC voltages (3.3V, 5V, 12V) for cheap. Saves $30–$100 over a commercial lab supply and repurposes e-waste.
params:
  source: pinboard
  sourceUrl: http://www.wikihow.com/Convert-a-Computer-ATX-Power-Supply-to-a-Lab-Power-Supply
---

![How to Convert a Computer ATX Power Supply to a Lab Power Supply](/images/notes/atx-power-supply-lab-conversion.png)

## Summary

An ATX power supply from a desktop PC outputs multiple regulated DC voltage rails: 3.3V, 5V, and 12V at substantial current. By pulling the supply out of a case, adding a load resistor to keep it stable, and wiring binding posts to the output leads, you get a serviceable benchtop lab power supply for a fraction of the cost of a commercial unit.

The key trick is the PS_ON pin — ATX supplies require a specific pin to be pulled low before they power on. You short this pin (typically green) to ground (black) to enable the supply outside a motherboard. A small bleeder resistor on the 5V line prevents voltage irregularities when the supply runs under no load.

This is a staple project for electronics prototyping and maker workshops. The resulting supply handles most Arduino, Raspberry Pi, and small motor driver work without needing expensive equipment. The trade-off: no adjustable voltage output, and the current ratings printed on the label are shared across rails in ways that require attention.

## Key points

- ATX power supply rails: 3.3V, 5V, 5Vsb, 12V, -12V — color-coded by the ATX specification
- Requires shorting the PS_ON (green wire) to ground (black wire) to enable standby-free operation
- A bleeder resistor (~10Ω, 10W on 5V) prevents voltage instability under light loads
- Total output current is shared — don't assume each rail can deliver its rated maximum simultaneously
- Great source of recycled supplies: any desktop tower PC; Goodwill and surplus shops sell them cheap

[Original](http://www.wikihow.com/Convert-a-Computer-ATX-Power-Supply-to-a-Lab-Power-Supply)
