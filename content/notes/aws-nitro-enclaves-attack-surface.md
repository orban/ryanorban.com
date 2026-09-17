---
title: AWS Nitro Enclaves Attack Surface
date: 2024-09-26
categories:
  - security
  - aws
  - cloud
  - trusted-execution
  - research
description: Trail of Bits analysis of AWS Nitro Enclaves' attack surface, covering vsock vulnerabilities, side-channel risks, entropy issues, and the trust model's assumptions. Essential reading before building confidential computing workloads on Nitro.
params:
  source: pinboard
  sourceUrl: https://blog.trailofbits.com/2024/09/24/notes-on-aws-nitro-enclaves-attack-surface/
---

![AWS Nitro Enclaves Attack Surface](/images/notes/aws-nitro-enclaves-attack-surface.png)

## Summary

Trail of Bits published an analysis of the attack surface in AWS Nitro Enclaves, the confidential computing feature that lets you run isolated processes on EC2 instances with cryptographic attestation. The analysis maps practical pitfalls that matter when actually building secure workloads on the platform — not theoretical concerns but issues that appear in real enclave applications.

The most significant findings center on the vsock virtual socket interface, the only communication channel between an enclave and its parent EC2 instance. Enclaves must correctly handle asynchronous connections, implement timeouts, manage state synchronization, and handle edge cases like `EINTR` signals and zero-length reads (which can cause infinite loops). Standard socket programming mistakes become security vulnerabilities in the enclave model because the parent instance is treated as a potentially hostile party.

On side channels: the L3 cache may be shared between the enclave and its parent instance, opening cache-based timing attacks. Applications processing confidential data inside enclaves must use constant-time implementations. For randomness, relying on CPU instructions like `RDRAND` alone is insufficient — enclaves should verify the hardware RNG (`nsm-hwrng`) is actively registered. Time is also tricky: using the TSC without `kvm-clock` yields timestamps defaulting to November 1999, requiring explicit paravirtual clock setup.

## Key points

- vsock is the primary attack surface: handle `EINTR`, timeouts, and zero-length reads correctly.
- Threat model: parent EC2 instance's kernel is considered fully compromised. Hypervisor is trusted.
- L3 cache may be shared between enclave and parent — constant-time implementations required for sensitive ops.
- Verify `nsm-hwrng` is registered as entropy source; don't assume CPU RNG instructions are sufficient.
- Time sync requires `kvm-clock` — TSC alone gives wrong timestamps (November 1999 default).
- All external communications need end-to-end authentication; internal enclave components share a single trust zone.
- Validate attestation nonces and timestamps independently to prevent replay attacks.

[Original](https://blog.trailofbits.com/2024/09/24/notes-on-aws-nitro-enclaves-attack-surface/)
