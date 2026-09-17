---
title: "Smart Home Components: A Systems Engineer's Setup"
date: 2022-03-20
categories:
  - smart-home
  - home-automation
  - iot
  - homelab
  - open-source
description: Michael Stapelberg's deep-dive into his home automation setup — a systems engineer's perspective on choosing components for a local-first, open smart home without cloud dependencies. Covers protocols, hubs, and the tradeoffs between ecosystems.
params:
  source: pinboard
  sourceUrl: https://michael.stapelberg.ch/posts/2022-03-19-smart-home-components/
---

![Smart Home Components: A Systems Engineer's Setup](/images/notes/smart-home-components.png)

## Summary

Michael Stapelberg (Go contributor, Google/Debian developer) documents his smart home setup with the same rigor he applies to software systems — protocol choices are reasoned, tradeoffs are explicit, and the design principle is local-first operation that doesn't depend on vendor clouds. This is notably different from the typical smart home article that just lists products; Stapelberg explains why each component was chosen and what would make him replace it.

The protocol layer is the key architectural decision. Zigbee and Z-Wave are the main mesh networking options for smart devices — both operate in the 900MHz/2.4GHz bands, use low-power mesh topology, and work without a cloud dependency. Stapelberg's preference for Zigbee over Wi-Fi devices (like Shelly) is motivated by network pollution and interference avoidance — dozens of Wi-Fi devices on a home network create real congestion and complexity. Zigbee devices talk to a Zigbee coordinator (a USB dongle attached to a home server), which then integrates with Home Assistant or Zigbee2MQTT.

Home Assistant is the integration hub — it runs locally, supports hundreds of device integrations, and has a rule engine for automation. The local-first architecture means: no subscription fees, automations work during internet outages, no risk of vendor shutdown killing your setup, and full control over what data leaves the house. Stapelberg's writeup is valuable not just as a shopping list but as a decision framework: what protocols to use, what hub software, how to think about migration risk, and what trade-offs matter for someone who treats their home as a systems problem to be solved well.

## Key points

- Zigbee preferred over Wi-Fi devices: avoids home network congestion, lower power, purpose-built mesh for IoT.
- Home Assistant: open-source home automation hub — local-first, broad device support, no subscription.
- Zigbee2MQTT: bridges Zigbee devices to MQTT for Home Assistant integration — more control than vendor Zigbee implementations.
- Local-first design: automations work without internet, no vendor lock-in, no subscription risk.
- MQTT as the messaging backbone for device events — lightweight publish-subscribe protocol designed for IoT.
- By Michael Stapelberg — prolific systems engineer; his blog posts are detailed technical references, not lifestyle content.

[Original](https://michael.stapelberg.ch/posts/2022-03-19-smart-home-components/)
