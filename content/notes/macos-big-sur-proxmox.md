---
title: Installing macOS Big Sur on Proxmox
date: 2021-07-18
categories:
  - proxmox
  - macos
  - virtualization
  - homelab
  - sysadmin
description: Nicholas Sherlock's guide for running macOS Big Sur as a virtual machine inside Proxmox VE — the canonical resource for macOS virtualization on open-source hypervisors. Makes it possible to run macOS without dedicated Apple hardware.
params:
  source: pinboard
  sourceUrl: https://www.nicksherlock.com/2020/06/installing-macos-big-sur-on-proxmox/
---

## Summary

Nicholas Sherlock's guide is the canonical reference for running macOS as a virtual machine inside Proxmox VE, the open-source hypervisor platform. Proxmox is based on KVM/QEMU on Linux, and running macOS on non-Apple hardware requires patching the bootloader and carefully configuring hardware IDs to pass Apple's platform checks — the guide walks through all of this.

The setup involves: creating a VM with specific hardware configurations that macOS accepts (correct CPU type, SMBIOS values that identify the VM as a supported Mac model), using OpenCore as the bootloader (which handles the platform spoofing), downloading the macOS installer from Apple's servers, and working through macOS's normal installation flow once booted.

The use cases for macOS on Proxmox are specific but real: developers who want a macOS environment without purchasing another Mac, CI/CD environments where macOS builds are needed (though licensing is murky here), and homelab enthusiasts who want a macOS VM alongside Linux and Windows VMs on a single Proxmox host. Apple's EULA technically prohibits running macOS on non-Apple hardware, so this is a gray-area use.

## Key points

- OpenCore bootloader handles the platform spoofing needed to convince macOS it's running on real Apple hardware.
- Requires specific KVM CPU configuration and SMBIOS values matching a real Mac model.
- GPU passthrough is possible for full graphics acceleration — adds significant complexity.
- Licensing note: Apple's EULA restricts macOS to Apple-branded hardware; this is technically a terms violation.
- Nicholas Sherlock's site also covers later macOS versions (Monterey, Ventura) with updated guides.

[Original](https://www.nicksherlock.com/2020/06/installing-macos-big-sur-on-proxmox/)
