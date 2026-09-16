---
title: My Smart Home 2021
date: 2022-02-17
categories:
  - smart-home
  - home-assistant
  - self-hosting
  - iot
  - automation
description: A detailed writeup of a production Home Assistant smart home setup in 2021 — covering hardware choices, integrations, automations, and lessons learned. A useful reference for anyone building a serious self-hosted home automation system.
params:
  source: pinboard
  sourceUrl: https://jorisroovers.com/posts/my-smart-home-2021
---

## Summary

Joris Roovers documents his complete Home Assistant smart home setup as of 2021 — one of the more thorough annual state of my smart home posts that the self-hosting community produces. The post covers the full stack: hardware (dedicated server vs. Raspberry Pi, network infrastructure), integrations (Zigbee devices, z-wave, Wi-Fi sensors), automation patterns, and the operational side of maintaining a self-hosted home automation system.

The subtitle "A Home Assistant Love Story" captures the tone — this is someone who has invested real time in making it work well and documents both what works and what's frustratingly complex. Home Assistant serves as the hub integrating devices from many vendors (Philips Hue, Sonos, IKEA Tradfri, etc.) that wouldn't otherwise talk to each other, without routing data through vendor clouds.

What makes it useful as a reference: the depth covers things that aren't in official docs, like how to handle device reliability issues, battery management for Zigbee sensors, and the architecture of multi-room audio. The self-hosted smart home pattern in 2022 was growing — concern about vendor lock-in (after devices like Revolv were bricked by Google) and cloud dependency was pushing enthusiasts toward local-first solutions.

## Key points

- Home Assistant as a local hub: no cloud dependency, works when internet is down.
- Zigbee and Z-Wave over Wi-Fi devices: more reliable, lower power, less network congestion.
- Automation patterns: presence detection, time-based triggers, scene management, conditional logic.
- Self-hosted home automation requires more setup but pays off in reliability and longevity.
- The complexity: Home Assistant YAML configs grow large; good organization and version control (git) matter.

[Original](https://jorisroovers.com/posts/my-smart-home-2021)
