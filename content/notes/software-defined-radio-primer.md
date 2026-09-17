---
title: A Primer on Cheap Software Defined Radios
date: 2012-12-03
categories:
  - radio
  - hardware
  - sdr
  - signal-processing
  - maker
description: Yuval Adam's 2012 primer on cheap software-defined radios using the RTL-SDR USB dongle — a $20 TV tuner repurposed as a 24MHz–1766MHz radio receiver. Triggered an explosion of hobbyist RF experimentation that continues today.
params:
  source: pinboard
  sourceUrl: http://blog.y3xz.com/blog/2012/12/02/a-primer-on-cheap-software-defined-radios/
---

## Summary

Software-defined radio (SDR) moves radio signal processing from fixed analog hardware into software running on a general-purpose computer. In 2012, the discovery that cheap RTL2832U-based USB TV tuner dongles could be repurposed as wideband receivers — for around $20 — democratized RF experimentation in a way that dedicated ham radio gear never could.

The RTL-SDR dongle covers roughly 24 MHz to 1766 MHz depending on the chipset, giving access to FM broadcast, aircraft transponders (ADS-B), weather satellites (NOAA APT), trunked police radio, and much more. The GNU Radio framework and tools like SDR# (Windows) and Gqrx (Linux/macOS) provide the software layer — spectrum analyzers, demodulators, and signal processing pipelines that previously required professional hardware.

By 2012 this was a very new discovery and Yuval Adam's primer was among the early how-to guides walking through setup and use cases. The key insight: RF spectrum that was previously invisible to hobbyists became audible with a $20 dongle and open-source software. The subsequent years saw ADS-B aircraft tracking, trunking police scanner communities, and LoRa and 433MHz IoT signal decoding all become routine hobbyist activities.

## Key points

- RTL-SDR uses cheap RTL2832U + R820T TV tuner chips repurposed as wideband radio receivers
- Frequency coverage: ~24 MHz to 1.7 GHz — FM radio, aircraft ADS-B (1090 MHz), weather satellites, 433MHz IoT
- GNU Radio is the standard open-source framework for signal processing pipelines on SDR hardware
- Bandwidth: ~2.4 MHz real-time — can record IQ samples to disk for later processing
- Key applications in 2012: FM reception, ADS-B plane tracking, NOAA weather satellite image decoding

[Original](http://blog.y3xz.com/blog/2012/12/02/a-primer-on-cheap-software-defined-radios/)
