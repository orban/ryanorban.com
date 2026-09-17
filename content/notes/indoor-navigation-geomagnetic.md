---
title: Indoor Navigation Using Disruption of Earth's Geomagnetic Field
date: 2012-07-09
categories:
  - indoor-navigation
  - geomagnetic
  - sensors
  - startup
  - location
description: IndoorAtlas (2012) used disruptions in Earth's magnetic field caused by building steel to create indoor positioning — no GPS, no beacons, no special hardware required. A clever exploitation of a physical property buildings already have.
params:
  source: pinboard
  sourceUrl: http://www.arcticstartup.com/2012/07/09/new-indoor-navigation-startup-uses-disruption-of-geomagnetic-field-from-buildings
---

![Indoor Navigation Using Disruption of Earth's Geomagnetic Field](/images/notes/indoor-navigation-geomagnetic.png)

## Summary

IndoorAtlas, a Finnish startup, built indoor positioning technology around a counterintuitive insight: steel and concrete in buildings distort Earth's magnetic field in unique, fingerprint-like ways at every location. A smartphone magnetometer can detect these micro-variations, and if you pre-map the magnetic field across a building, you can locate a device within that map using only the phone's built-in compass sensor.

The technical appeal is the absence of required infrastructure. GPS doesn't penetrate buildings reliably. WiFi positioning requires access point density and calibration. Bluetooth beacons (iBeacons) require hardware installation and maintenance. Geomagnetic positioning requires only a one-time survey of the building using a smartphone — the building itself is the positioning infrastructure.

What made this compelling in 2012 was the growing market for indoor navigation: large retail spaces (where GPS fails and product location is economically valuable), hospitals, airports, logistics warehouses. Apple had just removed Google Maps from iOS 6 (the Maps debacle) and was actively seeking location alternatives, which put indoor navigation startups in an unusual spotlight. IndoorAtlas was acquired by HERE Technologies (Nokia's mapping unit) in 2018, validating the technology's place in the mapping stack.

## Key points

- Magnetic fingerprinting: steel in building structures creates unique magnetic field distortions at each location — maps these distortions to latitude/longitude coordinates.
- No special hardware beyond the phone's magnetometer, already present in every modern smartphone as of 2012.
- Survey process: walk the building with a smartphone collecting magnetic readings + GPS-calibrated position data → generates the indoor map.
- Accuracy of 1-2 meters in favorable environments (dense steel structure); degrades in wood-frame or mixed construction.
- IndoorAtlas acquired by HERE Technologies (2018) — integrated into Nokia's mapping platform for enterprise indoor navigation use cases.

[Original](http://www.arcticstartup.com/2012/07/09/new-indoor-navigation-startup-uses-disruption-of-geomagnetic-field-from-buildings)
