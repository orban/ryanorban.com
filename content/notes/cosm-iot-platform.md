---
title: "Cosm: Internet of Things Platform"
date: 2012-06-09
categories:
  - iot
  - data-platform
  - sensors
  - api
  - internet-of-things
description: Cosm (formerly Pachube, later renamed Xively) was a cloud platform for connecting and sharing real-time sensor data from physical devices — one of the earliest Internet of Things platforms. It predated AWS IoT by years and pioneered the model of device-to-cloud data streams with public APIs.
params:
  source: pinboard
  sourceUrl: https://cosm.com/
---

## Summary

Cosm was a cloud platform for connecting physical devices and sharing real-time sensor data, founded originally as Pachube by Usman Haque in 2008. By 2012 it had been renamed Cosm and was positioning itself as the central data infrastructure for the emerging Internet of Things. It allowed devices — Arduino microcontrollers, Raspberry Pi boards, commercial sensors — to stream data to the cloud via simple HTTP APIs and expose that data as feeds with REST and WebSocket endpoints.

The model: every device or sensor is a "feed" with one or more datastreams. The platform stored historical data, served it through an API, and allowed public or private sharing of feeds. This enabled mashups where one device's output could be consumed by another device or a web application. You could visualize your home temperature data, share air quality measurements publicly, or trigger actions based on threshold values.

Cosm later became Xively (acquired by LogMeIn in 2013), which pivoted to enterprise IoT and was eventually shut down. The original Pachube/Cosm was a genuinely pioneering service — it predated AWS IoT (2015) by seven years and established the data model that most IoT platforms still follow. The challenge it couldn't overcome was monetization and competition from AWS, Azure, and Google Cloud when they entered the IoT platform space with unlimited infrastructure.

## Key points

- Pachube (2008) → Cosm (2012) → Xively (2013): one of the first cloud platforms for IoT sensor data.
- Usman Haque founded it; architecture was feeds → datastreams → timestamped values, accessible via REST/WebSocket.
- Enabled device-to-cloud streaming for Arduino, Raspberry Pi, and commercial sensors years before AWS IoT.
- Predated AWS IoT (2015) by 7 years — pioneered the feed/datastream IoT data model.
- Acquired by LogMeIn (2013), rebranded as Xively, eventually discontinued as cloud giants offered similar capabilities.

[Original](https://cosm.com/) → REST API
