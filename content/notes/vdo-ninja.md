---
title: "VDO.Ninja: Free P2P Live Video via WebRTC"
date: 2023-05-04
categories:
  - video
  - webrtc
  - streaming
  - obs
  - tools
description: VDO.Ninja (formerly OBS.Ninja) is a free, no-account P2P video streaming tool that brings live video from phones, cameras, and remote guests directly into OBS Studio or any browser via WebRTC. The simplest way to pull in a remote camera feed without third-party software or monthly fees.
params:
  source: pinboard
  sourceUrl: https://vdo.ninja/
---

## Summary

VDO.Ninja (formerly OBS.Ninja) is a free, peer-to-peer live video streaming tool built on WebRTC. The core use case: bring a remote camera feed (phone, webcam, another computer) into OBS Studio or any browser as a live video source, without needing additional software, accounts, or subscription fees. The sender opens a link in their browser; the receiver pulls it in as a browser source in OBS.

The system works entirely through the browser using WebRTC's direct peer-to-peer protocol — no server handles the video stream itself, just the signaling to establish the connection. This means latency is very low (typically 150–300ms for local network, 500ms+ for internet) and there's no per-session cloud cost to the service. The free tier is genuine: no watermarks, no time limits, no encoding fees.

VDO.Ninja is particularly popular for podcast production, remote interviews, church streaming, and live event production where pulling in a remote guest's camera feed reliably and cheaply matters. The WebRTC foundation means it works on iOS, Android, and any desktop browser — no app install required for the sender. The creator (Steve Seguin) maintains it actively and has added features like WHIP/WHEP support, NDI output, and multi-guest room management.

## Key points

- WebRTC-based P2P video — no middleman server for the video stream, very low latency.
- Receiver gets a browser source URL for OBS Studio or any video tool — no sender software install.
- Completely free: no watermarks, no time limits, no account required.
- Works on iOS, Android, and all desktop browsers — universal sender compatibility.
- Popular for remote podcast guests, live streaming, remote event production.
- Created and maintained by Steve Seguin; formerly called OBS.Ninja.

[Original](https://vdo.ninja/)
