---
title: "Bjorn: Raspberry Pi Network Scanner with e-Paper Display"
date: 2024-11-12
categories:
  - security
  - networking
  - raspberry-pi
  - open-source
  - hardware
  - penetration-testing
description: Bjorn is a network scanning and offensive security tool for Raspberry Pi with a 2.13-inch e-Paper HAT display — discovers targets, identifies open ports and vulnerable services, and shows results on the tiny screen. A self-contained portable pentesting device for the hobbyist security researcher.
params:
  source: pinboard
  sourceUrl: https://github.com/infinition/Bjorn
---

![Bjorn: Raspberry Pi Network Scanner with e-Paper Display](/images/notes/bjorn-raspberry-pi-scanner.png)

## Summary

Bjorn is an open-source network scanning and offensive security tool built specifically for Raspberry Pi with a 2.13-inch e-Paper HAT display. It discovers network targets, identifies open ports, exposed services, and potential vulnerabilities, displaying results on the tiny e-ink screen. The combination of Raspberry Pi portability and e-Paper display makes it a self-contained, power-efficient device for network reconnaissance.

The tool performs host discovery, port scanning, service identification, and basic vulnerability assessment — similar in scope to combining nmap, masscan, and service fingerprinting into a single automated workflow. The e-Paper display is practical for field use: low power consumption, readable in direct sunlight, and no need for an external monitor to check results.

Bjorn targets the hobbyist security researcher and network administrator who wants a portable tool for assessing their own network security without carrying a full laptop. The Raspberry Pi platform is well-suited for this: cheap hardware, runs standard Linux security tools, can be left in place for continuous monitoring or carried for spot assessments.

## Key points

- Network scanner + vulnerability identifier running on Raspberry Pi.
- 2.13-inch e-Paper HAT display shows results without external monitor.
- Performs: host discovery, port scanning, service identification, vulnerability detection.
- Power-efficient e-Paper display enables portable, battery-powered field use.
- Open-source — extend with additional nmap scripts or custom vulnerability checks.

[Original](https://github.com/infinition/Bjorn) → GitHub
