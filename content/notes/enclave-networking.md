---
title: "Enclave: Zero-Trust Overlay Networking"
date: 2022-04-02
categories:
  - networking
  - security
  - zero-trust
  - vpn
  - infrastructure
description: Enclave is a zero-trust overlay networking product that creates software-defined private networks between machines without VPN infrastructure — each machine gets a cryptographic identity and point-to-point encrypted tunnels replace network perimeters.
params:
  source: pinboard
  sourceUrl: https://enclave.io/pricing/
---

## Summary

Enclave is a zero-trust networking product that creates software-defined private networks between hosts — servers, VMs, containers, and developer machines — without requiring traditional VPN infrastructure. The core idea: instead of trusting the network and putting a perimeter around it, each host gets a cryptographic identity and communicates over point-to-point encrypted tunnels that only authorize specific connections. This is the zero-trust model applied to network topology rather than just application access.

Traditional VPNs create a flat network: once you're on the VPN, you can potentially reach any resource the VPN grants access to. Enclave and tools like Tailscale, Nebula, and WireGuard mesh take a different approach — micro-segmentation by default, where each machine only sees the machines it's explicitly authorized to communicate with. The traffic is encrypted end-to-end (not just to a VPN gateway), and authorization is tied to cryptographic identity rather than IP addresses, which change and are easily spoofed.

The use cases are primarily homelab and small-to-medium business: connecting cloud servers to on-premises machines, enabling remote developer access to internal services, securing IoT device communication, and linking multi-cloud deployments. Enclave targets this market with a simpler setup story than WireGuard (which requires manual key management) and a different pricing model than Tailscale (which has a generous free tier but commercial tiers for teams). The pricing page bookmark suggests interest in cost comparisons across this category.

## Key points

- Overlay network: creates a private network layer on top of existing internet infrastructure — no dedicated hardware, no firewall configuration.
- Zero trust by default: each host only communicates with explicitly authorized peers — no flat inside the VPN network.
- Point-to-point encrypted tunnels: WireGuard-based end-to-end encryption between hosts, not just to a gateway.
- Competes with Tailscale, Zerotier, Nebula, and manual WireGuard configurations.
- Cryptographic identity per host: authorization based on certificates, not IP addresses — survives dynamic IP changes.
- Pricing model for small teams: alternative to Tailscale's team tier and the complexity of self-managed WireGuard.

[Original](https://enclave.io/pricing/)
