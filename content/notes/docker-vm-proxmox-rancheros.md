---
title: Docker VM on Proxmox with RancherOS and Portainer
date: 2022-01-29
categories:
  - docker
  - proxmox
  - homelab
  - self-hosting
  - virtualization
description: A walkthrough for running Docker on Proxmox using RancherOS as a minimal container-focused VM OS, with Portainer for container management UI. RancherOS is now unmaintained, but the pattern of a dedicated Docker VM inside Proxmox remains common.
params:
  source: pinboard
  sourceUrl: https://joshspicer.com/docker-proxmox
---

## Summary

This post by Josh Spicer covers setting up a dedicated Docker VM inside Proxmox using RancherOS — a minimal Linux OS designed around running containers. The idea is sensible: Proxmox is a hypervisor for running VMs, and rather than installing Docker on bare metal or on a general-purpose Linux VM, you use an OS that's purpose-built for containers.

RancherOS was appealing because it ran Docker as PID 1 and eliminated the typical Linux overhead for container-centric workloads. Setup involves creating a VM in Proxmox, booting from the RancherOS ISO, and installing to disk with a cloud-config YAML file specifying SSH keys, networking, and hostname. QEMU Guest Agent is enabled for proper Proxmox integration. Portainer is then deployed as a container for a visual management interface.

The important caveat: RancherOS is unmaintained as of ~2020. The successor in this space is k3OS (also now deprecated) or simply using a minimal Alpine Linux or Ubuntu Server with Docker installed. The Proxmox pattern — run a dedicated container host VM alongside other VMs — is still common and sensible for homelabs where you want workload separation without full Kubernetes.

## Key points

- Pattern: dedicated Docker VM inside Proxmox for workload isolation — keeps containers separate from other VMs.
- RancherOS was purpose-built for Docker (PID 1) but is now unmaintained — use Alpine Linux or Ubuntu Server instead.
- cloud-config YAML configures SSH keys, networking, and hostname during OS install — same approach works for any cloud-init VM.
- Portainer provides a visual container management interface as a Docker container on the same host.
- QEMU Guest Agent enables Proxmox to see the VM's IP and manage it properly.

[Original](https://joshspicer.com/docker-proxmox) → AI agent
