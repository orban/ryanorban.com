---
title: Teensy USB Development Board
date: 2012-04-15
categories:
  - maker
  - arduino
  - microcontroller
  - hardware
  - electronics
description: "The Teensy USB development board by PJRC — a compact Arduino-compatible microcontroller with native USB. Bookmarked while seeking cheaper Arduino alternatives, it represents the early 2010s maker movement's economics problem: capable hardware at accessible price points."
params:
  source: pinboard
  sourceUrl: http://www.pjrc.com/teensy/
---

![Teensy USB Development Board](/images/notes/teensy-usb-development-board.png)

## Summary

The Teensy is a compact, USB-enabled microcontroller development board by PJRC (Paul Stoffregen's company). At $16 in 2012, it was cheaper than a full Arduino Uno but more capable in some ways: native USB device support meant it could appear to a computer as a keyboard, mouse, MIDI controller, or serial port without additional hardware. The bookmarker's question ("Anyone know of a cheaper Arduino clone that doesn't need USB?") suggests they were comparing options for a project using FTDI for serial communication.

The Teensy occupied an interesting niche in the 2012 maker ecosystem. The Arduino platform had democratized microcontroller programming with easy-to-use tooling, but the Arduino Uno was bulkier and more expensive than many projects needed. Alternatives included the Arduino Nano (~$30), bare ATmega328 chips ($3), and boards like the Teensy that added capabilities like native USB.

The native USB feature was what made the Teensy distinctive. A standard Arduino needs an FTDI chip to communicate over USB (bridging UART to USB). The Teensy's microcontroller (originally an Atmel AT90USB, later ARM Cortex-M) speaks USB directly, enabling it to implement any USB device class — which opened up custom MIDI controllers, HID devices, and complex USB setups without additional hardware.

## Key points

- Teensy provides native USB device support, not just serial-over-USB — can emulate keyboards, MIDI controllers, HID devices.
- PJRC's Teensyduino add-on made Teensy compatible with the Arduino IDE, lowering the learning curve.
- The 2012 maker ecosystem had a real cost problem: capable hardware was either expensive or required deep electronics knowledge.
- Teensy 3.x (2012-era) moved to ARM Cortex-M processors — significantly more powerful than AVR-based Arduinos.
- Price/capability tradeoffs drove DIY maker hardware: ATmega328 chips were cheapest, Arduino Nano was balanced, Teensy added USB at modest cost.

[Original](http://www.pjrc.com/teensy/)
