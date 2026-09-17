---
title: "Universal Radio Hacker (URH): Wireless Protocol Analysis"
date: 2025-04-23
categories:
  - sdr
  - radio
  - security
  - reverse-engineering
  - hardware
description: Universal Radio Hacker (URH) is a comprehensive SDR suite for investigating wireless protocols — demodulation, protocol inference, fuzzing, and simulation in one tool. The go-to tool for reverse-engineering radio signals from weather stations to IoT devices.
params:
  source: pinboard
  sourceUrl: https://github.com/jopohl/urh
---

![Universal Radio Hacker (URH): Wireless Protocol Analysis](/images/notes/urh-universal-radio-hacker.png)

## Summary

Universal Radio Hacker (URH) is a software suite for investigating wireless protocols using Software Defined Radio (SDR) devices. It covers the full workflow of wireless security research: signal demodulation with automatic parameter detection, protocol structure inference from captured signals, fuzzing for stateless protocols, and simulation environments for stateful attack scenarios.

The automatic modulation parameter detection is the key usability feature. Wireless signals use a variety of modulations (ASK, FSK, PSK, etc.) with varying parameters; URH tries to detect these automatically rather than requiring the user to specify them manually. The rule-based protocol field inference adds another layer: it attempts to identify which bytes are headers, payloads, checksums, etc., without manual annotation.

URH supports the major SDR hardware: HackRF, RTL-SDR, LimeSDR, USRP, and others. The tool has been used to analyze everything from weather stations and car remote controls to IoT devices with weak or absent security. The repository is now archived (read-only) but remains available for use. Runs on Windows, Linux, and macOS.

## Key points

- Demodulation with automatic modulation parameter detection — ASK, FSK, PSK, and more.
- Rule-based protocol field inference: headers, payloads, checksums without manual labeling.
- Fuzzing for stateless protocols; simulation environment for stateful attack scenarios.
- Supports HackRF, RTL-SDR, LimeSDR, USRP, and other common SDR hardware.
- Used for IoT security research, car remotes, weather stations, industrial protocols.
- Repository is archived but fully functional — cross-platform (Windows/Linux/macOS).

[Original](https://github.com/jopohl/urh) → GitHub
