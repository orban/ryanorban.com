---
title: Android Fragmentation Visualized
date: 2012-05-16
categories:
  - android
  - mobile
  - fragmentation
  - data-visualization
  - developer-experience
description: OpenSignalMaps visualized the Android device ecosystem by collecting data from 681 distinct Android devices in their user base, showing the extreme hardware and OS version fragmentation developers faced. The visualization became a reference point in iOS-vs-Android developer experience debates.
params:
  source: pinboard
  sourceUrl: http://opensignal.com/reports/fragmentation.php
---

## Summary

OpenSignalMaps (a crowd-sourced cell signal mapping service) published a visualization of the Android device ecosystem as seen through their app's user base. The data covered 681 distinct Android device models, ranging across different screen sizes, hardware capabilities, Android OS versions (from 1.6 Donut through 4.0 Ice Cream Sandwich), and chipset architectures. The visual output — hundreds of device icons arranged by manufacturer and version — became a widely circulated demonstration of what "Android fragmentation" actually looked like in practice.

The fragmentation problem was real for Android developers at the time. Writing an app that worked well across Android 2.2 (still on many devices) through 4.0 required handling different APIs, different screen densities, different hardware buttons (physical vs. soft), different camera hardware, and different performance profiles. The same app that ran fine on a Samsung Galaxy S3 might be unusable on a low-end 2.2 device. This was a genuine development cost that made Android harder to target than iOS, where Apple controlled hardware and OS version distribution was faster.

The OpenSignalMaps report became a go-to citation in discussions about the developer experience tradeoffs between iOS and Android. It was part of a larger conversation about whether fragmentation would cause developers to prioritize iOS — which some did, particularly for paid apps where iOS users spent more. The situation has somewhat improved with Google Play Services abstracting key APIs across versions, but device and OS fragmentation never fully resolved.

## Key points

- 681 distinct Android device models in a single app's user base — from major manufacturers to no-name OEMs.
- OS version fragmentation: Android 2.2, 2.3, 3.x, and 4.0 all active simultaneously, with incompatible APIs.
- Contrasted sharply with iOS update adoption rates, where Apple's ecosystem pushed users to new versions faster.
- Google Play Services later partially addressed this by providing a consistent API layer independent of OS version.
- Fragmentation drove iOS-first development strategies for many startups and indie developers through ~2015.

[Original](http://opensignal.com/reports/fragmentation.php)
