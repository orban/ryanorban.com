---
title: "Quaternion: 3D Rotation for Quantified Self Data"
date: 2013-12-06
categories:
  - quaternion
  - rotation
  - quantified-self
  - mathematics
  - sensors
description: Tweet from SFDataScience meetup about quaternions as the right representation for 3D rotation data from phone accelerometers/gyroscopes. Quaternions avoid gimbal lock and enable smooth interpolation — more practical than rotation matrices for sensor fusion.
params:
  source: pinboard
  sourceUrl: https://twitter.com/ryanorban/status/408802733102096384/photo/1
---

## Summary

A tweet from the SFDataScience meetup noting quaternions as the right mathematical representation for 3D rotation data from smartphones and quantified self devices. A quaternion encodes a 3D rotation as a 4-component unit vector (w, x, y, z) — it avoids gimbal lock (a singularity problem with Euler angles) and supports smooth interpolation via SLERP (spherical linear interpolation).

Phone accelerometers and gyroscopes produce orientation data. If you're analyzing activity data — walking gait, gesture recognition, driving behavior — you need to work with 3D rotations. The naive approach (rotation matrices) is a 3×3 representation with 9 parameters for 3 degrees of freedom. Quaternions are a 4-parameter representation that's computationally efficient, numerically stable, and easy to compose.

The note captures the moment (late 2013) when wearable and phone sensor data was becoming a serious data science domain. The quantified self movement was mainstream, Fitbit and early smartwatches were creating sensor data at scale, and practitioners were learning that working with orientation data required understanding the math of 3D rotations.

## Key points

- Quaternion: unit 4-vector (w, x, y, z) encoding a 3D rotation. Avoids gimbal lock, supports SLERP interpolation.
- Why not Euler angles: suffer from gimbal lock (singularity where degrees of freedom collapse) and composition is non-trivial.
- Why not rotation matrices: 9 parameters for 3 DOF, harder to interpolate smoothly.
- Applications in phone/wearable data: gesture recognition, activity classification, step counting, gait analysis.
- Sensor fusion (combining accelerometer + gyroscope + magnetometer) uses quaternion math to track orientation over time.
- Part of the 2013 quantified self / wearables boom where practitioners were figuring out how to analyze motion sensor data.

[Original](https://twitter.com/ryanorban/status/408802733102096384/photo/1)
