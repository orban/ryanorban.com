---
title: "Safe Yolo Mode: running LLM agents in isolated VMs"
date: 2026-02-15
categories:
  - ai-agents
  - security
  - sandboxing
  - virtualization
  - developer-tools
description: A guide to running LLM agents with full auto-approval permissions inside libvirt/virsh VMs, so risky operations are contained without restricting what the agent can do. The sandbox is the safety rail, not permission restrictions.
params:
  source: pinboard
  sourceUrl: https://www.metachris.dev/2026/02/safe-yolo-mode-running-llm-agents-in-vms-with-libvirt-and-virsh/
---

![Safe Yolo Mode: running LLM agents in isolated VMs](/images/notes/safe-yolo-mode-llm-vms.png)

## Summary

\Safe Yolo Mode\ is the idea that you can grant AI agents broad auto-approval permissions — letting them execute tools without confirmation prompts — while still protecting your system by running them inside isolated virtual machines. Instead of restricting what agents can do, you restrict what they can reach. The agent can destroy its environment; it can't destroy yours.

The implementation uses libvirt and virsh, Linux's standard virtualization management layer, with Ubuntu cloud images for rapid VM provisioning. Cloud-init handles automated setup. The workflow: download a cloud image, resize the disk, use `virt-install` to create the VM with specified resources, configure SSH access (optionally via Tailscale). Development tools and LLM providers are installed inside the VM, and tmux keeps sessions persistent and remotely accessible.

This is the infrastructure answer to the agent safety question. The complementary approaches are permission-based (Claude Code's permission system, [matchlock](/notes/matchlock/), [Destructive Command Guard](/notes/destructive-command-guard/)) — you constrain what tools the agent can call. The VM approach is different: give the agent full permissions, but put it in a box. Both have their place. VM isolation makes sense for long, complex, autonomous tasks where you want maximum agent capability. Permission systems make sense for interactive development where you want oversight.

## Key points

- VM isolation as the safety primitive: full agent permissions inside a contained environment, not restricted permissions on the host.
- Built on libvirt/virsh + Ubuntu cloud images + cloud-init — standard Linux virtualization stack.
- Tailscale VPN for remote VM access without port forwarding — useful for cloud-hosted VMs.
- tmux keeps agent sessions persistent across SSH reconnections.
- Snapshot and clone capabilities enable rapid environment reset and testing.
- Contrasts with permission-based approaches: the isolation is at the infrastructure layer, not the tool call layer.

[Original](https://www.metachris.dev/2026/02/safe-yolo-mode-running-llm-agents-in-vms-with-libvirt-and-virsh/)
