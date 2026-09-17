---
title: "Bitponics: Automated Gardening for Brown-Thumbed Plant Killers"
date: 2012-06-09
categories:
  - iot
  - gardening
  - hydroponics
  - sensors
  - automation
  - startup
description: Bitponics was an Arduino-based automated gardening system that monitored pH, temperature, light, and humidity and sent alerts when plants needed attention. An early consumer IoT product applying sensor networks to home horticulture.
params:
  source: pinboard
  sourceUrl: http://pandodaily.com/2012/06/08/bitponics-automates-gardening-for-brown-thumbed-plant-killers/
---

![Bitponics: Automated Gardening for Brown-Thumbed Plant Killers](/images/notes/bitponics-automated-gardening.png)

## Summary

Bitponics was a hardware/software startup that built a sensor system for hydroponics and indoor gardening. The device monitored key plant health parameters — pH, electrical conductivity (nutrient concentration), temperature, humidity, and light levels — and connected to a cloud platform that stored the data, sent alerts, and provided guidance on when and how to intervene. The pitch was direct: you don't need to know much about plants if you have sensors telling you what they need.

The system was built on Arduino hardware with a custom sensor board. Data streamed to a web platform (likely hosted on something like Cosm / Pachube or a proprietary API). The founders were from the maker/hacker community that had been building Arduino-based home automation systems; Bitponics applied that toolkit specifically to plant care.

Hydroponics is a natural fit for automation because the variables are well-defined and measurable: plants in a hydroponic system live or die based on nutrient concentration, pH, light hours, and temperature — all of which sensors can track continuously. This is harder with soil-based gardening where variables are more distributed and harder to measure.

Bitponics raised funding on Kickstarter and appeared in Y Combinator conversations at the time, but ultimately didn't scale. The market for consumer hydroponics hardware was small in 2012, and the broader IoT consumer market was still pre-Amazon Echo and pre-Nest — before connected home devices had established consumer habits.

## Key points

- Bitponics: Arduino-based sensor system for hydroponic gardening monitoring pH, EC, temperature, humidity, light.
- Cloud-connected: data streams to a platform for historical tracking and alerting.
- Hydroponics suits sensor automation because the variables are measurable and the system is bounded.
- Timing challenge: consumer IoT in 2012 predated the category-establishing devices (Nest, Amazon Echo) that normalized connected hardware.
- Pattern: maker/hacker hardware applied to a specific vertical (plants) with cloud connectivity — a common 2012 IoT startup structure.

[Original](http://pandodaily.com/2012/06/08/bitponics-automates-gardening-for-brown-thumbed-plant-killers/)
