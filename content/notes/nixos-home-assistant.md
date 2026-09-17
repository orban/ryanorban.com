---
title: "NixOS: Headless Home Assistant VM"
date: 2022-02-25
categories:
  - nixos
  - home-assistant
  - self-hosting
  - smart-home
  - linux
description: A tutorial on running Home Assistant as a headless VM on NixOS — covering NixOS configuration, declarative VM setup, and integrating Home Assistant into a reproducible infrastructure-as-code home lab. Good example of the NixOS approach applied to home automation.
params:
  source: pinboard
  sourceUrl: https://myme.no/posts/2021-11-25-nixos-home-assistant.html
---

## Summary

A post by myme.no covering how to run Home Assistant as a headless virtual machine on NixOS. Home Assistant is the leading open-source home automation platform; running it in a VM on NixOS rather than as a dedicated hardware device (like a Home Assistant OS install on a Pi) allows it to coexist with other services on the same machine while benefiting from NixOS's declarative configuration model.

The NixOS approach to configuration is the key differentiator here. In NixOS, system state is described in a `configuration.nix` file — including the VM definition, its resources, its network configuration, and its services. This means the entire Home Assistant setup is reproducible: you can destroy and recreate the VM from the config, commit it to git, and diff changes. This is in stark contrast to the typical home lab approach where configuration drift accumulates over years of ad-hoc changes.

The post likely covers: defining a NixOS VM using the `nixpkgs.lib.nixosSystem` configuration or using QEMU modules, configuring the VM for Home Assistant OS image, setting up networking (bridged or NAT), persistent storage for Home Assistant data, and autostart on boot. The headless in the title means the VM runs without a GUI — managed entirely through Home Assistant's web interface.

NixOS is the kind of system where the setup cost is higher than alternatives (compared to just flashing Home Assistant OS to a Pi), but the operational benefits compound over time. This post represents a specific philosophy: treat home infrastructure with the same reproducibility standards as production infrastructure.

## Key points

- Declarative NixOS configuration for a Home Assistant VM — reproducible, version-controllable, diffable.
- NixOS `configuration.nix` describes both the host and the VM, so the full setup is captured in git.
- QEMU virtualization enables running multiple services on one machine instead of dedicated hardware.
- The tradeoff: higher setup complexity than Home Assistant OS on dedicated hardware, but operational reproducibility long-term.
- Part of the self-hosting and NixOS home lab pattern — treating personal infrastructure as code.

[Original](https://myme.no/posts/2021-11-25-nixos-home-assistant.html)
