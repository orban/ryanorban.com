---
title: 7-Colour E-Ink Display for Raspberry Pi (Inky Impression 5.7")
date: 2022-08-22
categories:
  - raspberry-pi
  - e-ink
  - hardware
  - maker
  - pimoroni
description: Tutorial for the Pimoroni Inky Impression 5.7" — a 7-color e-ink display HAT for Raspberry Pi. Covers setup, driving the display with Python, and displaying images. E-ink's low power draw and paper-like quality make it attractive for ambient information displays.
params:
  source: pinboard
  sourceUrl: https://core-electronics.com.au/guides/colour-e-ink-display-raspberry-pi/
---

## Summary

This tutorial covers the Pimoroni Inky Impression 5.7" — a 7-color e-ink display HAT (Hardware Attached on Top) for Raspberry Pi. The Inky Impression supports black, white, red, green, blue, yellow, and orange pixels using electrophoretic display technology, driven via SPI from the Pi. Resolution is 600×448 pixels.

E-ink displays are attractive for maker projects because they consume power only when refreshing (not while holding an image), have a paper-like visual quality that's readable in direct sunlight, and are thin and light. The trade-off is slow refresh rate (seconds, not milliseconds) and limited color gamut compared to LCD or OLED. This makes them well-suited for ambient information displays, digital photo frames, calendar boards, and status indicators that update infrequently.

The Python library provided by Pimoroni handles the SPI communication and image rendering. The tutorial walks through setup (enabling SPI on the Pi, installing the library), displaying images using PIL (Python Imaging Library), and adapting images to the 7-color palette. A project like this sits at the intersection of Raspberry Pi hardware hacking and low-power ambient display design.

## Key points

- Pimoroni Inky Impression 5.7": 7-color e-ink display HAT for Raspberry Pi, 600×448 pixels.
- E-ink advantages: zero power when static, paper-like quality, sunlight-readable.
- Trade-offs: slow refresh rate (seconds), limited color gamut vs. LCD/OLED.
- Best for: ambient displays, digital photo frames, status boards that update infrequently.
- Pimoroni Python library handles SPI communication and image rendering via PIL.
- Connects to Raspberry Pi maker culture and low-power IoT display applications.

[Original](https://core-electronics.com.au/guides/colour-e-ink-display-raspberry-pi/)
