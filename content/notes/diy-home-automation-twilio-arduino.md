---
title: DIY Home Automation Using Twilio, PowerSwitch, Arduino, and Pusher
date: 2012-08-21
categories:
  - iot
  - arduino
  - home-automation
  - twilio
  - maker
description: A 2012 Twilio blog post showing how to build DIY home automation using Twilio for SMS control, an Arduino with PowerSwitch Tail relay for electrical switching, and Pusher for real-time status updates. An early blueprint for the hacker home automation pattern.
params:
  source: pinboard
  sourceUrl: http://www.twilio.com/blog/2012/08/diy-home-automation-using-twilio-powerswitch-arduino-and-pusher.html
---

## Summary

A 2012 tutorial from the Twilio blog showing how to build a DIY home automation system by wiring together four components: Twilio for SMS-based remote control, a PowerSwitch Tail relay board for safely switching household electrical devices, an Arduino microcontroller as the local control logic, and Pusher for real-time status updates in a web dashboard.

The architecture was a clean example of early IoT thinking before cloud platforms made this trivial. Twilio received an SMS (turn on lights), sent it to a web server via webhook, the server relayed the command to an Arduino over serial or network, the Arduino triggered the PowerSwitch Tail relay to physically switch the circuit, and Pusher pushed a status update to a browser dashboard via WebSocket. The whole thing could be built for under $100 in hardware.

The PowerSwitch Tail was a key safety component — it let you safely control 120/240V AC loads from the Arduino's 5V logic output without building your own high-voltage switching circuit. This lowered the SKILL barrier for maker home automation significantly. The combination of Twilio + Arduino became a common pattern in 2011–2013 for physical computing projects that needed remote control.

## Key points

- Twilio SMS webhook → web server → Arduino → PowerSwitch Tail relay → physical electrical switching.
- Pusher WebSocket for real-time status updates in a browser dashboard.
- Arduino + PowerSwitch Tail for safe control of household AC electrical circuits.
- Sub-$100 hardware cost for a functional remote control home automation system.
- Demonstrates the IoT duct tape pattern: glue commodity APIs (Twilio, Pusher) to physical hardware (Arduino) with a thin web server layer.

[Original](http://www.twilio.com/blog/2012/08/diy-home-automation-using-twilio-powerswitch-arduino-and-pusher.html)
