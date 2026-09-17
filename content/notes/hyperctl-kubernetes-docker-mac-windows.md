---
title: "hyperctl: Kubernetes and Docker on Mac and Windows"
date: 2020-07-11
categories:
  - kubernetes
  - docker
  - developer-tools
  - mac
  - devops
description: hyperctl is a CLI tool for running lightweight Kubernetes and Docker clusters on Mac and Windows using native hypervisors — a faster alternative to Docker Desktop and Minikube for local Kubernetes development.
params:
  source: pinboard
  sourceUrl: https://github.com/youurayy/hyperctl
---

![hyperctl: Kubernetes and Docker on Mac and Windows](/images/notes/hyperctl-kubernetes-docker-mac-windows.png)

## Summary

hyperctl is a command-line tool for running Kubernetes and Docker clusters on macOS and Windows using the native hypervisor (Hyperkit on Mac, Hyper-V on Windows). It's positioned as a faster, lighter alternative to Docker Desktop and Minikube for local Kubernetes development.

The problem it addresses: Minikube and Docker Desktop both run Kubernetes via a virtual machine layer that adds overhead and startup time. hyperctl uses the native OS hypervisor directly, reducing the VM overhead and starting clusters faster. For developers running Kubernetes locally for development or testing, startup time and resource usage are meaningful friction points — a 30-second cluster start vs. 3-minute start significantly affects developer workflow.

By 2020, local Kubernetes development tooling was actively evolving: kind (Kubernetes in Docker), k3s, microk8s, and hyperctl were all competing as alternatives to Minikube. The landscape has since converged somewhat around kind for CI and k3s for lightweight production, but in 2020 hyperctl represented a reasonable approach for Mac/Windows development environments.

## Key points

- hyperctl: lightweight local Kubernetes via native OS hypervisor (Hyperkit/Hyper-V) — faster than Minikube.
- Avoids Docker Desktop overhead by using native hypervisor primitives directly.
- Target: local development and testing of Kubernetes workloads on Mac/Windows.
- 2020 context: competed with kind, k3s, microk8s — the local Kubernetes tooling space was fragmented.
- Relevant to anyone doing local Kubeflow development or testing Kubernetes ML pipelines locally.

[Original](https://github.com/youurayy/hyperctl) → GitHub
