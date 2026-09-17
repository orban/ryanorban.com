---
title: "Radicle: Peer-to-Peer Code Collaboration"
date: 2022-01-20
categories:
  - git
  - p2p
  - decentralized
  - open-source
  - code-collaboration
  - crypto
description: Radicle is a peer-to-peer code collaboration stack built on Git — no central server, no platform dependency, repositories hosted on a distributed network. The decentralized alternative to GitHub for sovereign code hosting.
params:
  source: pinboard
  sourceUrl: https://radicle.xyz/
---

## Summary

Radicle is a decentralized code collaboration platform built on Git that eliminates the dependency on centralized hosting services like GitHub or GitLab. Instead of repositories living on a company's servers, Radicle stores them in a peer-to-peer network where each node holds copies of the repos it cares about. The protocol is built on top of Git objects and cryptographic identities — repositories are addressed by their content hash, not a URL path on someone else's server.

The motivation is digital sovereignty for code: GitHub can suspend accounts, governments can compel data access, companies can shut down services. Radicle makes repositories resistant to these failure modes because there's no single point of control. The trade-off is losing the network effects that make GitHub a social platform — stars, profiles, discoverability, the pull request workflow as currently understood.

The technical design uses libp2p for networking and cryptographic keypairs for identity. Radicle has gone through several iterations — early versions used Ethereum for identity anchoring, later versions moved to a simpler crypto-key-based identity model. It's still a relatively small ecosystem and requires that collaborators also run Radicle nodes, which limits adoption compared to GitHub's universal reach.

## Key points

- Repositories addressed by content hash, not platform URLs — no central hosting dependency.
- Peer-to-peer network using libp2p; cryptographic keypairs for identity — no accounts at a centralized service.
- Built on standard Git objects — existing Git tooling and workflows are compatible.
- Digital sovereignty use case: repositories can't be taken down by a platform, government order, or business decision.
- Tradeoff: loses GitHub's network effects, discoverability, and collaborative workflow tooling.

[Original](https://radicle.xyz/)
