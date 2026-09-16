---
title: Cross Compiling Node.js v0.8.x
date: 2012-12-18
categories:
  - nodejs
  - embedded-systems
  - cross-compilation
  - arm
  - raspberry-pi
description: Nathan Rajlich's guide to cross-compiling Node.js v0.8.x for ARM targets — a prerequisite for running Node.js on Raspberry Pi and similar ARM boards in 2012, before pre-built ARM binaries were widely distributed.
params:
  source: pinboard
  sourceUrl: http://n8.io/cross-compiling-nodejs-v0.8/
---

![Cross Compiling Node.js v0.8.x](/images/notes/cross-compiling-nodejs.png)

## Summary

Nathan Rajlich (n8.io) documented the process of cross-compiling [Node.js](/notes/nodejs/) v0.8.x for ARM architecture targets — specifically to run Node on embedded systems like the Raspberry Pi, which couldn't compile it natively in reasonable time. In 2012, pre-built ARM binaries for Node.js weren't reliably distributed, so running Node on the Pi required either compiling it natively (which could take hours on the Pi's 700MHz ARM CPU) or cross-compiling on a faster host machine.

Cross-compilation means building software on one architecture (x86 host) targeting another architecture (ARM target). This requires a cross-compilation toolchain — a gcc variant configured to generate ARM machine code. The process was non-trivial in 2012: finding the right toolchain, configuring the build system, and handling v8's native code dependencies (since v8 has architecture-specific components) all required careful steps.

Nathan Rajlich was a prolific Node.js contributor — author of several core modules and active in the early Node community. His guide reflects the era when deploying Node.js to non-standard platforms required deep knowledge of build systems. By 2014-2015, the Node.js Foundation and distributions like nvm had made ARM binaries much more accessible, and the Raspberry Pi itself had official Node.js support.

## Key points

- Cross-compilation: building for ARM on an x86 host to avoid slow native compilation on the Pi
- [Node.js](/notes/nodejs/) v0.8.x (2012) had no official ARM binary distribution — this was a gap the community filled
- v8 engine has architecture-specific code generation — adds complexity to cross-compilation vs. pure interpreted runtimes
- Nathan Rajlich was a key early [Node.js](/notes/nodejs/) community contributor — his documentation was trusted
- By 2015, official Node.js ARM builds made this guide obsolete — but it filled a real gap in 2012

[Original](http://n8.io/cross-compiling-nodejs-v0.8/)
