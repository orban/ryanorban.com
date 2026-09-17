---
title: Google's Self-Driving Car Generates ~1GB Per Second
date: 2013-05-02
categories:
  - autonomous-vehicles
  - sensor-data
  - lidar
  - google
  - big-data
description: Bill Gross's 2013 tweet with an infographic showing Google's self-driving car generating ~1GB of sensor data per second — a striking illustration of the gap between human-scale perception and machine-scale data requirements for autonomous driving.
params:
  source: pinboard
  sourceUrl: https://twitter.com/Bill_Gross/status/329069954911580160/photo/1
---

![Google's Self-Driving Car Generates ~1GB Per Second](/images/notes/google-self-driving-car-1gb-per-second.png)

## Summary

Bill Gross (founder of Idealab) shared an infographic in May 2013 illustrating the sensor data rate of Google's self-driving car project (what became Waymo): approximately 1GB per second of raw sensor data during operation. This figure became widely cited in big data and autonomous vehicles discussions as a visceral illustration of machine-perception data volumes.

The breakdown: LIDAR (the rotating sensor producing a 3D point cloud) was the primary contributor, generating hundreds of megabytes per second. Radar, cameras (multiple HD cameras at high frame rates), and GPS/IMU added to the total. The critical engineering challenge wasn't storing this data — it was processing it fast enough to make real-time driving decisions. The onboard compute had to consume, process, and act on the sensor stream with latency in the tens of milliseconds.

This data rate revealed why self-driving cars were fundamentally a machine learning and real-time computing problem rather than a simple robotics problem. The data volume also explained why Google's fleet was initially limited to logged test drives rather than continuous autonomous operation — the storage and processing requirements were enormous even by 2013 standards. It also previewed the data flywheel argument: more miles driven → more edge cases encountered → better models, which is why Waymo and Tesla have competed so intensely on miles-driven metrics.

## Key points

- ~1GB/sec from a combination of LIDAR, cameras, radar, and GPS — the exact mix varied by vehicle generation
- Real-time constraint: processing must complete in <100ms for driving decisions — raw throughput alone doesn't matter without latency guarantees
- Data flywheel: the data advantage compounds — more miles → more edge cases → better models → safer cars → public acceptance → more miles
- LIDAR cost was $75,000+ in 2013 (the Velodyne HDL-64E unit) — Waymo would spend years designing cheaper solid-state alternatives
- The 1GB/sec figure resonated in 2013 because it was the same order as high-speed network links — putting autonomous driving data rates in infrastructure terms
- This period (2013-2014) was when serious deep learning applied to computer vision was beginning — the sensor data volumes were accumulating precisely as the ML tools to analyze them were arriving

[Original](https://twitter.com/Bill_Gross/status/329069954911580160/photo/1)
