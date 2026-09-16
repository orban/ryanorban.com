---
title: "Homelab: Fully Automated Self-Hosting Infrastructure"
date: 2022-01-22
categories:
  - homelab
  - gitops
  - kubernetes
  - infrastructure-as-code
  - self-hosting
  - ansible
description: "Khue's homelab is a fully automated self-hosting infrastructure project: from empty disk to running services with a single command, using Ansible for bare-metal provisioning, K3s for Kubernetes, and ArgoCD for GitOps deployment. A reference architecture for serious homelab automation."
params:
  source: pinboard
  sourceUrl: https://github.com/khuedoan/homelab
---

## Summary

khuedoan/homelab is a reference implementation of fully automated homelab infrastructure — the goal being a reproducible path from empty disk to running services with a single command. It applies production-grade GitOps and Infrastructure as Code (IaC) practices to a personal home server setup, which is as much a learning exercise as a practical deployment.

The stack is layered: Ansible provisions bare metal over PXE boot, setting up the base OS and networking. K3s (a lightweight Kubernetes distribution) provides container orchestration. ArgoCD handles GitOps continuous deployment — any change pushed to the Git repository is automatically applied to the cluster. Cilium provides eBPF-based networking. Rook Ceph provides distributed storage. Cloudflare tunnels handle DNS and external access without exposing your home IP. Prometheus, Grafana, and Loki cover observability.

This is more infrastructure than most homelabs need, and that's the point: it's a vehicle for learning the full stack of modern cloud-native tooling in an environment you control completely. The same patterns (GitOps, Kubernetes, Ansible) appear in production at companies operating at scale — a homelab like this is one of the better ways to build genuine hands-on expertise with them.

## Key points

- PXE boot + Ansible handles bare-metal provisioning — fully automated from empty disk.
- K3s (lightweight Kubernetes) + ArgoCD (GitOps) = changes to the Git repo automatically apply to the cluster.
- Cilium for eBPF networking; Rook Ceph for distributed storage; Prometheus/Grafana/Loki for observability.
- Cloudflare tunnels enable external access without port-forwarding or exposing your home IP.
- Related: Proxmox homelab setup (different approach: VMs instead of Kubernetes containers).

[Original](https://github.com/khuedoan/homelab) → GitHub
