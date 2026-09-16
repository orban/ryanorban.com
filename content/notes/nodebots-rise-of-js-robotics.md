---
title: "NodeBots: The Rise of JS Robotics"
date: 2012-10-30
categories:
  - javascript
  - robotics
  - nodejs
  - hardware
  - iot
description: Chris Williams argues that Node.js and JavaScript's event-driven model make it a surprisingly natural fit for physical computing and robotics. A 2012 manifesto for what became the Johnny-Five ecosystem.
params:
  source: pinboard
  sourceUrl: http://www.voodootikigod.com/nodebots-the-rise-of-js-robotics
---

![NodeBots: The Rise of JS Robotics](/images/notes/nodebots-rise-of-js-robotics.png)

## Summary

In 2012, Chris Williams ([@voodootikigod](https://twitter.com/voodootikigod)) made the case that JavaScript and [Node.js](/notes/nodejs/) weren't just for web servers — they were a natural fit for hardware and physical computing. The post introduced the concept of NodeBots: robots and hardware devices controlled through [Node.js](/notes/nodejs/) using libraries like Johnny-Five and node-serialport.

The core argument is structural: JavaScript's event-driven programming model mirrors how physical devices actually work. A servo waiting for a signal, a sensor polling for input, an accelerometer emitting readings — these are inherently event-based interactions. The async/await patterns that make [Node.js](/notes/nodejs/) effective for I/O also work cleanly for hardware I/O. Where languages like Python or C were traditionally used for this work, JavaScript lowered the barrier for the much larger pool of web developers who already knew the language.

The technical proof was Johnny-Five, which let developers control Arduino microcontrollers with remarkably little code — ten lines to read an accelerometer, a handful more to drive a servo. The v1.0.0 release discussed in the post added Windows support, broadening the platform reach further. The binding to hardware happened through node-serialport, a C++ module that handled low-level serial port communication while exposing a clean JavaScript interface.

## Key points

- JavaScript's event-driven programming model naturally matches how physical hardware operates — waiting for sensor input and responding accordingly.
- Johnny-Five demonstrated that meaningful Arduino control requires very little code in [Node.js](/notes/nodejs/) — the abstraction layer is genuinely thin.
- The developer audience advantage: many more people know JavaScript than C or Python, so [Node.js](/notes/nodejs/) hardware bindings have a large accessible user base.
- node-serialport bridges native C++ serial communication with JavaScript, showing the composability of [Node.js](/notes/nodejs/)'s native addon system.
- Windows support in v1.0.0 made cross-platform hardware development practical for the first time in this ecosystem.

[Original](http://www.voodootikigod.com/nodebots-the-rise-of-js-robotics)
