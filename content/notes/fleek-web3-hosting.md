---
title: "Fleek: Web3 Hosting and Deployment"
date: 2022-01-30
categories:
  - web3
  - hosting
  - ipfs
  - decentralized
  - deployment
  - developer-tools
description: Fleek is a Web3 deployment and hosting platform that deploys sites to IPFS, the Internet Computer, and other decentralized networks — positioned as the Netlify/Vercel equivalent for the decentralized web. Eliminates single-point-of-failure hosting by distributing content across the IPFS network.
params:
  source: pinboard
  sourceUrl: https://fleek.co/
---

## Summary

Fleek is a deployment and hosting platform designed for the decentralized web — the Web3 equivalent of Netlify or Vercel. Instead of deploying to centralized cloud infrastructure, Fleek deploys sites and apps to IPFS (the InterPlanetary File System), Internet Computer, and other decentralized networks. The developer experience mirrors familiar CI/CD: connect a Git repository, configure a build command, and Fleek handles the rest.

The value proposition for decentralized hosting: content stored on IPFS is addressed by content hash rather than server location, making it censorship-resistant and not dependent on a single hosting provider's availability. A site hosted on IPFS doesn't go down if the original host's servers do — other IPFS nodes that have pinned the content serve it. Fleek handles the pinning and ENS (Ethereum Name Service) DNS integration to make IPFS sites accessible via human-readable names.

As a product it positions against the concern that Web3 applications are often served from centralized infrastructure despite running smart contracts on decentralized blockchains. Deploying the frontend to IPFS through Fleek is one step toward a more fully decentralized stack. The tradeoff: IPFS content retrieval can be slower than CDN-served content, and the ecosystem tooling is less mature than traditional web hosting.

## Key points

- Deploys to IPFS, Internet Computer, and other decentralized networks — content-addressed, not server-addressed.
- CI/CD workflow similar to Netlify/Vercel: connect Git repo, configure build, automatic deploys.
- ENS integration: IPFS sites accessible via human-readable `.eth` names (with compatible resolvers).
- Censorship-resistance and uptime resilience: content persists as long as any IPFS node has pinned it.
- Positioned as the missing piece for Web3 apps that run on-chain but serve frontends from centralized cloud.

[Original](https://fleek.co/)
