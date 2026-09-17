---
title: "virtual-builders: VM Environment Builder Scripts"
date: 2021-11-17
categories:
  - virtualization
  - dev-environment
  - tools
  - linux
  - open-source
description: virtual-builders is a collection of scripts for building various virtual machine environments — QEMU/KVM-based VMs for development and testing. Useful for quickly spinning up reproducible Linux environments without Docker.
params:
  source: pinboard
  sourceUrl: https://github.com/kstenerud/virtual-builders
---

## Summary

[virtual-builders](/notes/virtual-builders/) is a GitHub repository by Karl Stenerud containing scripts for building various virtual environments using QEMU/KVM. The project targets developers who need reproducible, isolated Linux environments for testing and development — cases where Docker containers aren't appropriate (e.g., testing kernel behavior, running different Linux distros, or needing a full OS rather than a container).

The scripts automate the tedious parts of VM creation: downloading base images, configuring networking, setting up disk images, and launching the VM with reasonable defaults. The emphasis is on repeatability — run the build script, get the same VM every time.

In 2021, before tools like Lima, OrbStack, or UTM became widely adopted on macOS, this kind of scripted QEMU approach was one of the cleaner ways to run full Linux VMs on macOS without heavy commercial tools. The niche it occupies has since gotten more competitive as native virtualization tooling on Apple Silicon and Linux has matured.

## Key points

- Shell scripts for building QEMU-based VMs — more flexible than Docker for full-OS testing needs.
- Reproducible environment creation: run the same script, get the same VM.
- Targets Linux development/testing use cases: kernel work, cross-distro testing, system-level isolation.
- Since 2021, the space has gotten competition from Lima, OrbStack, and UTM on macOS.
- Karl Stenerud is also known for the libkern and concise-encoding projects.

[Original](https://github.com/kstenerud/virtual-builders)
