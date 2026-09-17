---
title: "Rancher K3s: Kubernetes on Proxmox Containers"
date: 2022-07-15
categories:
  - kubernetes
  - k3s
  - proxmox
  - homelab
  - infrastructure
description: A guide to running K3s (lightweight Kubernetes) inside Proxmox LXC containers — a popular homelab setup that gives you a real Kubernetes cluster on commodity hardware without the overhead of full VMs. Good reference for homelabbers who want production-grade container orchestration locally.
params:
  source: pinboard
  sourceUrl: https://betterprogramming.pub/rancher-k3s-kubernetes-on-proxmox-containers-2228100e2d13
---

## Summary

This Better Programming guide walks through deploying K3s — Rancher Labs' lightweight Kubernetes distribution — inside Proxmox LXC containers rather than full virtual machines. The setup is popular in homelab communities because Proxmox provides efficient container virtualization (LXC is lower overhead than KVM VMs), and K3s is a single-binary Kubernetes distribution that runs on resource-constrained hardware.

K3s strips Kubernetes down to what's needed for most workloads: it bundles containerd, CoreDNS, Traefik, and a local-path provisioner, removing the optional components and distributing the control plane as a lightweight process. The result is a Kubernetes cluster that runs on hardware that would struggle with full kubeadm deployments — Raspberry Pis, small VPSes, and homelab nodes with 1-2GB RAM.

Running K3s inside Proxmox LXC requires some privileged container configuration — LXC containers share the host kernel, so running a container runtime (containerd) inside one requires specific cgroup and capabilities settings. The guide covers the exact Proxmox configuration: creating the LXC container with the right features enabled, installing K3s, and joining additional agent nodes. The result is a multi-node cluster running efficiently on a single Proxmox host.

## Key points

- K3s is a minimal Kubernetes distribution — single binary, bundled dependencies, minimal RAM requirement (~512MB for control plane)
- Proxmox LXC containers are more efficient than KVM VMs for this use case: containers share host kernel, reducing overhead
- Privileged LXC containers required: containerd needs specific cgroup and capability settings to run inside LXC
- Common homelab pattern: single Proxmox host running multiple LXC containers as K3s nodes, giving a real multi-node cluster
- Rancher (the company behind K3s) also offers RKE2 for production deployments; K3s is the dev/homelab variant

[Original](https://betterprogramming.pub/rancher-k3s-kubernetes-on-proxmox-containers-2228100e2d13) → AI agent
