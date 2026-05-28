---
title: "f.lux: adaptive screen color temperature"
date: 2009-02-21
categories:
  - software
  - health
  - display
  - productivity
description: f.lux adjusts monitor color temperature throughout the day — warmer at night to reduce blue light exposure. One of the earliest widely-adopted tools for circadian-aware display calibration, predating OS-level Night Mode by years.
params:
  source: pinboard
  sourceUrl: http://stereopsis.com/flux/
---

![f.lux: adaptive screen color temperature](/images/notes/flux-screen-color-temperature.png)

## Summary

f.lux is a utility that automatically adjusts the color temperature of your monitor based on time of day and geographic location. During daylight hours, the display stays calibrated for sunlight (around 6500K, cool/blue). After sunset, it shifts warmer (toward 2700K, incandescent-range) to reduce blue light emission, which interferes with melatonin production and sleep quality.

The science it draws on: circadian rhythm disruption from evening blue light exposure delays sleep onset. Before f.lux (and later iOS Night Shift, macOS Night Mode, Android Blue Light Filter), late-night computer use was uniformly harsh on the eyes. f.lux made this adjustment automatic based on your latitude/longitude and local sunset time.

f.lux was early — released around 2009 — and became a genuine staple for people who worked late on computers. It predated mainstream OS-level equivalents by about 7 years. The concept is now built into essentially every major OS and display, which is itself an interesting technology diffusion story.

## Key points

- Adjusts monitor color temperature from ~6500K (daylight) to ~2700K (evening) automatically.
- Uses your location to calculate sunset time; gradual transition over ~60 minutes.
- Targets circadian rhythm preservation — reducing blue light to allow natural melatonin production.
- Preceded Apple's Night Shift (2016) and Android's Night Mode by ~7 years.
- Free software; available for Windows, Mac, Linux.

[Original](http://stereopsis.com/flux/)
