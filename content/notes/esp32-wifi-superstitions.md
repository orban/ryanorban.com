---
title: ESP32 WiFi Superstitions
date: 2025-03-16
categories:
  - esp32
  - wifi
  - embedded
  - networking
  - iot
  - troubleshooting
description: "Three practical workarounds for ESP32 WiFi disconnection problems: disable power saving mode, limit 2.4GHz channels to 20MHz width, and pin devices to specific access points. Admitted to be 'superstitions' without rigorous basis, but proven effective in practice."
params:
  source: pinboard
  sourceUrl: https://supakeen.com/weblog/esp32-wifi-superstitions/
---

![ESP32 WiFi Superstitions](/images/notes/esp32-wifi-superstitions.png)

## Summary

This supakeen blog post documents three pragmatic workarounds for a common ESP32 problem: WiFi connections dropping intermittently in production deployments. The author calls them superstitions honestly — they're not backed by rigorous testing, but they eliminated daily disconnections in their IoT deployment. The framing is important: sometimes embedded networking requires cargo-cult solutions because the alternatives (debugging Espressif's WiFi stack) are worse.

The most technically grounded fix is **disabling WiFi power saving mode**. Unlike the ESP8266, the ESP32 has WiFi modem power saving enabled by default. This can interfere with certain access point configurations and cause the module to miss incoming packets or fail to maintain the association. Fix: `esp_wifi_set_ps(WIFI_PS_NONE)` in C, or `power_save_mode: NONE` in ESPHome.

The other two fixes address network topology rather than device firmware: (1) configure your 2.4GHz access point to use 20MHz channel width rather than 40/80MHz automatic, which improves compatibility; (2) manually pin each ESP32 to the closest access point rather than letting the device auto-select — ESP32s don't roam intelligently and will stick to a distant AP even if a better one is available.

## Key points

- Disable power saving: `esp_wifi_set_ps(WIFI_PS_NONE)` — most likely actual fix.
- 20MHz channel width on 2.4GHz AP: improves compatibility with ESP32 radio.
- Manual AP pinning: ESP32s don't roam; assign them to their nearest access point.
- Author's honest framing: anecdotal, no rigorous testing — but worked in practice.
- ESPHome users: `power_save_mode: NONE` in YAML config.
- Common in IoT deployments where reboots are expensive and WiFi reliability is critical.

[Original](https://supakeen.com/weblog/esp32-wifi-superstitions/)
